# Steps
### 1. Set up env
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
- **uv** 는 Astral 사(예: ruff Lint로 유명)가 Rust로 만든 **초고속 Python 패키지·프로젝트 관리 도구**

```bash
# Create a new directory for our project 
uv init weather 
cd weather 
# Create virtual environment and activate it 
uv venv 
source .venv/bin/activate 
# Install dependencies 
uv add "mcp[cli]" httpx 
# Create our server file 
touch weather.py
```
- uv로 파이선 프로젝트 초기화
- mcp`[cli]`: `**Model Context Protocol Python SDK + CLI**`: **LLM과 대화할 API 서버를 Rust 아닌 Python으로, 그리고 CLI 한 줄로 띄우는**
- **httpx** :  차세대 HTTP 클라이언트**
	- 동기/비동기 모두 지원
	- http/2 지원 
	- 기본 보안 안정성 수치 내장
	- 테스트 용이
--- 
#### *이 프로젝트에서 MCP + httpx로 사용하는 이유:*
##### **1.** **당신이 작성할 MCP 툴(서버 로직)에서 외부 HTTP 호출을 해야 한다
- 빠른 시작 문서가 권장한 _weather_ 서버처럼, MCP 툴 안에서 기상청·GitHub·사내 REST API 등을 비동기로 불러와야 하는 경우가 흔합니다.
- 예제 코드에서도 httpx.AsyncClient()로 NWS(미국 기상청) API를 호출하고 있어요.
- httpx는 **동기·비동기 공용 API + HTTP/2 + 스트리밍(SSE)** 까지 지원해, MCP 툴 구현에 필요한 네트워크 기능을 한 방에 해결합니다.
> 즉, _서버 코드 안에서 “인터넷에 나갔다 오겠다”_ → requests 대신 httpx 권장 → 따라서 프로젝트 의존성에 명시.
##### **2.** **MCP Python SDK / CLI 내부에서도 httpx를 사용한다**
- MCP CLI가 **Streamable HTTP** (HTTP POST + 선택적 SSE) 전송을 쓸 때, 내부 클라이언트 트랜스포트 구현이 httpx.AsyncClient를 그대로 사용합니다.
    - import httpx 구문이 SDK의 mcp/client/streamable_http.py에 바로 들어가 있습니다.   
- mcp dev …, mcp inspect …, 원격 서버 접속, OAuth 토큰 교환 등 **CLI 레벨의 네트워킹**이 모두 httpx 기반이라서, 패키지가 없다면 CLI 기능 일부가 ImportError로 깨집니다.
#####  **3.** **왜 mcp[cli] 자체 종속성에 묶어 두지 않았을까?**
- MCP SDK는 **“필요한 전송(transport)만 골라 쓰라”**는 철학이라, HTTP 계층을 _강제_로 끼워 넣지 않습니다.
    - 로컬 stdio 전송만 쓸 사람에게까지 HTTP 스택을 설치하게 하면 과해서요.
- 그래서 **“CLI + HTTP 전송 or 외부 API 호출을 할 예정”**인 튜토리얼에서 따로 httpx를 추가하도록 안내한 것입니다.
---- 
## 2. Building your server
```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"
```

| **코드**                                   | **무슨 일?**                                                                                         | **왜 필요한가?**                                                                 |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| from typing import Any                   | **Any** 타입 힌트를 쓰기 위해 typing 모듈을 불러옵니다. 예: def get_temp() -> Any: 처럼 반환 값이 다양할 때                   | FastMCP의 자동 스키마 생성(프롬프트·파라미터 설명서)에 타입 힌트가 활용됩니다.                            |
| import httpx                             | 동기·비동기 모두 지원하는 **HTTPX** 클라이언트.                                                                   | 기상청(NWS) REST API를 호출할 때 사용합니다. HTTP/2·스트리밍 등 현대 기능을 갖춰 FastMCP 툴과 잘 어울립니다. |
| from mcp.server.fastmcp import FastMCP   | Astral MCP SDK의 **FastMCP** 클래스를 가져옵니다.                                                           | Flask/FastAPI처럼 “서버 뼈대” + “도구 스키마 자동화”를 동시에 제공하는 MCP 전용 프레임워크입니다.           |
| mcp = FastMCP("weather")                 | **FastMCP 인스턴스 생성**. 툴 이름을 "weather" 로 지정하면 나중에 MCP-IDE나 LLM 프롬프트에서 weather.<toolName> 식으로 노출됩니다. | 인스턴스를 전역에 두면, 아래쪽 함수들을 **데코레이터**(@mcp.tool 등)로 간편하게 등록할 수 있습니다.             |
| NWS_API_BASE = "https://api.weather.gov" | **미국 기상청( National Weather Service ) API** 기본 엔드포인트를 상수로 정의합니다.                                   | httpx 호출을 구성할 때 실수 없이 재사용 가능.                                               |
| USER_AGENT = "weather-app/1.0"           | 모든 HTTP 요청 헤더에 넣을 **User-Agent** 식별자.                                                             | NWS 측은 UA 없이 요청하면 403을 줄 수 있으므로 관례상 명시합니다.                                  |
##### **MCP 서버를 만들 때 선택할 수 있는 대표적 프레임워크들**

|**계열**|**프레임워크/SDK**|**주 사용 언어**|**특징 (장점 & 포지션)**|
|---|---|---|---|
|**공식 저수준 SDK**|**MCP Python SDK**modelcontextprotocol/python-sdk|Python|규격 100 % 준수, 모든 메시지·라이프사이클을 직접 다룰 수 있음. 세밀한 제어가 필요할 때 적합.|
|**MCP TypeScript SDK** @modelcontextprotocol/sdk|TypeScript / Node|같은 기능을 JS/TS 생태계에서 제공. STDIO·Streamable HTTP 전송 내장, 서버·클라이언트 모두 구현 가능.|
|MCP Java SDK, .NET (Semantic Kernel MCP) 등|Java, C#|JVM·.NET 기반 백엔드/엔터프라이즈 환경을 노린 공식 포트.|
|**고수준 Python 래퍼**|**FastMCP** ( mcp.server.fastmcp.FastMCP )|Python|_타입 힌트 + docstring_만으로 툴/리소스를 자동 스키마화, 데코레이터 베이스 API, STDIO·HTTP·SSE 전송 지원, CLI 핫리로드·테스트·배포 툴까지 올인원.|
|**FastAPI-MCP**|Python|기존 FastAPI 앱을 “MCP 도구”로 자동 변환·노출. 기존 REST 코드를 재사용할 때 유리.|
|**에이전트/RAG 특화**|**LlamaIndex MCP**|Python|강력한 문서 인덱싱·검색 + MCP 서버/클라이언트 어댑터 제공. RAG 워크로드에 최적.|
|**LangChain MCP**|Python / JS|풍부한 에이전트·워크플로 그래프와 결합. 툴 체인이 복잡한 에이전트형 서비스에 적합.|
|**Haystack MCP**|Python|검색·평가·프로덕션 지향 기능 탑재. 검색 품질·모니터링이 중요한 환경.|
##### FASTmcp
|**영역**|**세부 기능**|
|---|---|
|**1. 초저보일러플레이트**|함수에 @mcp.tool, @mcp.resource 같은 데코레이터만 붙이면 파라미터 타입·docstring을 읽어 **Tool Manifest**를 자동 생성. Swagger 따로 쓸 필요 X.|
|**2. 멀티 트랜스포트**|mcp.run() 한 줄로 STDIO ↔ Streamable HTTP ↔ SSE 전송 방식 선택. 로컬 툴~웹 서비스까지 동일 코드 재사용 가능.|
|**3. 생산성 지원**|fastmcp dev ― 자동 리로드, 실시간 인스펙터·테스트 UIfastmcp generate ― REST 스펙/OpenAPI를 MCP 툴로 변환|
|**4. 서버 컴포지션**|mcp.mount() 로 여러 서버를 하나로 합치거나, Tag 필터링으로 뷰를 분할 가능.|
|**5. 배포·운영 도구**|내장 Auth(OAuth 2/OIDC), 로깅·메트릭, Prefect 기반 워크플로, Docker / Serverless 탬플릿 제공.|
|**6. IDE·에이전트 연동**|Claude Desktop, ChatGPT, Cursor 등 주요 LLM-IDE가 FastMCP 2.0을 1급 지원 – 로컬에서 바로 “도구 호출” 테스트 가능.|
>**보일러플레이트(boilerplate)**는 “실제로 문제를 해결하거나 비즈니스 로직을 수행하지는 않지만, 코드가 실행되기 위해 반드시 매번 써 넣어야 하는 **반복적‧상투적 코드**”를 가리키는 프로그래밍 용어예요. - 19세기 미국에서 신문사가 **증기보일러 제작소(boiler works)**에서 찍어낸 얇은 철판 위 광고 글자를 그대로 가져와 인쇄했다는 이야기가 기원입니다.


>**고수준 Python 래퍼**는
> “복잡한 저수준 API를 파이썬 개발자가 **쉽고 안전하게** 다룰 수 있도록,
> **추상화·자동화·보일러플레이트 제거**를 제공하는 라이브러리/프레임워크”
> 를 뜻합니다.