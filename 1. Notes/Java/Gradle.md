# 정의
Gradle은 자바(Java) 생태계를 비롯해 다양한 언어와 플랫폼에서 쓰이는 **빌드 자동화 도구(build automation tool)**입니다. 주된 특징과 역할을 간단히 정리하면 다음과 같습니다.

## **1. Gradle의 주요 역할**

1. **컴파일**
    - 소스 코드(.java, .kt 등) → 바이트코드(.class)로 컴파일
        
2. **테스트 실행**
    - 단위 테스트(JUnit, TestNG 등) 자동 실행
        
3. **의존성 관리**
    - 외부 라이브러리(예: Apache Commons, Spring 등) 의존성 선언 및 다운로드
    
4. **패키징**
    - JAR/WAR/ZIP 등 형태로 결과물(artifact) 생성
    
5. **배포**
    - 생성된 결과물을 사내/외부 저장소(Maven Central, Artifactory 등)에 업로드