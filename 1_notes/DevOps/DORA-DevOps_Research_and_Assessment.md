# 0. Who is Dora
DORA(DevOps Research and Assessment)란 소프트웨어 조직의 **개발·배포 성능**을 계량화해주는 대표적인 생산성·품질 지표 모형입니다. Google Cloud의 DevOps 연구팀과 Nicole Forsgren 박사, Jez Humble, Gene Kim 등이 주도한 연구를 바탕으로 만들어졌어요.


# 1. Executive summary
- **연구 개요**: 전 세계 39,000명 이상의 개발·운영 전문가 대상 설문·심층 인터뷰를 통해 지난 10년간의 DevOps/DORA 연구 성과를 집대성
    
- **핵심 성과 지표**: 팀과 조직의 성과(수익성·시장점유율·고객만족 등), 번아웃, 플로(flow), 직무만족, 제품 퍼포먼스, 생산성, 팀 퍼포먼스
    
- **AI·플랫폼 등 주요 트렌드**:    
    - AI 도입은 생산성·플로·직무만족 향상에 긍정적이지만, 소프트웨어 딜리버리 성능에는 일부 부정적 영향
    - 플랫폼 엔지니어링은 생산성과 조직 성과를 높이지만 딜리버리 성능에는 경고 신호
    
- **개선 로드맵**: 현재 상태 진단 → 목표 설정 → 가설 수립 → 개선 실행 → 재측정 → 반복


# 2. Software delivery performance
요약:
> 핵심 메시지: **측정 → 학습 → 개선**의 선순환을 문화로 정착시키면, 어느 팀이든 엘리트 수준에 도달할 수 있습니다. 자주 빠르게 배포 -> 더욱 적은 배포 실패 혹은 짧은 recovery time

![[스크린샷 2025-06-17 오후 8.53.32.png]]
- **DORA의 네 가지 핵심 지표**:
    1. Change lead time: 
	    1. time taken to be successfully deployed to production.
    2. Deployment frequency: 
	    1. how often application changes are deployed to production.
    3. Change failure rate (+ Rework rate): 
	    1. the percentage of deployments that cause failures in production
		    1. “변경 실패율 지표가 사실상 **팀에 추가로 요구되는 재작업(rework)의 양**을 대리 측정하고 있는 것 아닐까? -> 재작업 비중 질문 추가함
    4. Failed deployment recovery time
	    1. the time it takes to recover from a failed deployment
	결국 얼마나 자주 성공적으로 배포하냐, 실패시 얼마나 빠르게 복구하냐. 
- **재작업 비율(rework rate)**과 **변경 실패율(change failure rate)**이 밀접하게 연관되어 있음을 확인했습니다. 이 두 지표를 합치면 “소프트웨어 딜리버리 안정성(software delivery stability)”이라는 하나의 **신뢰도 높은 요인(factor)**을 구성할 수 있게 되었습니다.
- **성능 클러스터**: 응답자 기반 군집 분석으로 ‘Elite, High, Medium, Low’ 네 레벨 제시
    
- Throughput ↔ Stability 상관, 그리고 트레이드오프
	•	네 클러스터 모두에서 속도와 안정성은 양(+)의 상관을 유지. 즉 더 자주·빨리 배포하는 팀이 오히려 실패율도 낮은 사례가 많음.  ￼
	•	단, Medium 클러스터는 안정성은 높지만 속도가 낮아 ‘더 자주 배포’가 개선 포인트로 지목.
	•	“속도가 좋을까, 안정성이 좋을까?” → 정답은 팀·도메인·사용자 기대치에 따라 달라지며, **“지속적 개선”**이 궁극 관건이라 경고합니다.  ￼
    
- **벤치마크 활용법**: DORA Quick Check 및 밸류 스트림 매핑으로 현재 상태를 파악하고 개선 영역 설정

Artificial intelligence:

Adoption and attitudes 17

Exploring the downstream

impact of AI 27

Platform engineering 47
- TFS팀이 하는 일인것같다. 물론 DORA에서는 더욱 큰 개념으로 설명하지만, 플랫폼엔지니어는 개발자 경험을 개선하는 데 많은 에너지를 쏟는 것이라는 틀안에서 같다. 
- 변경 불안정성 모니터링, 지속적인 학습 및 실험 문화 조성, 협업 및 피드백, 개발자 독립성 및 셀프 서비스 기능 우선순위 지정 등등을 주요 성과로 삼는데 이건 잭과 내가 하는 작업과 상당히 유사하다. 

Developer experience 57
- 개발자 경험은 단순히 개발자의 편의를 넘어 조직의 성공과 제품 품질에 직접적인 영향을 미치는 핵심 요소이며, 특히 사용자 중심적 접근 방식과 안정적인 우선순위 관리가
	- (paradox)불안정한 우선순위의 위험: 조직의 우선순위가 끊임없이 바뀌면 생산성이 의미 있게 감소하고 번아웃이 크게 증가합니다
	- (paradox)안정된 우선순위가 소프트웨어 제공에 미치는 영향: DORA 연구는 우선순위가 안정될 때 소프트웨어 제공 성능이 저하되는
	- 의미 있는 작업 및 교차 기능 협업: 개발자들은 자신의 작업이 다른 사람들에게 미치는 영향에서 의미를 찾습니다
		- 의미가 있으려면 우선순위가 있어야함 그건 궁극적 목표가 있어야함

Leading transformations 69

A decade with DORA 77

Final thoughts 83

Acknowledgements 85

Authors 87

Demographics and

firmographics 91

Methodology 99

Models 113

Recommended reading 117



후기:

결국 리더가 가장 중요하다. DORA의 4개 지표들이 생산성을 대변한다. 하지만 리더가 상황에 따라, 각 구성원의 기분 상태에 따라 등등 유연하게 잘 대처해야하면서 여러가지를 챙겨서 생산성이 높을 확율이 있는 상황을 만들어야한다. 근데 이건 회사마다, 시간마다 다르다. 그렇다면 이런 것까지 전부 포함해서 생산성 측정으로 넣으면 아무것도 측정할 수 없으니 DORA같은 지표로 해보자. 

DORA의 4개 지표는 생산성의 원리인 인풋 대비 아웃풋을 얼마나 자주 성공적으로 이루는지라고 생각한다. 

