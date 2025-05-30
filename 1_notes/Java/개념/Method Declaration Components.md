Method Declaration은 말 그대로 Method를 Declare할때 필요한 요소들이다. 

이 요소들은 자바에서 **메서드 선언(method declaration)** 을 구성하는 **구성 요소(components)** 들입니다. 각 요소의 명칭은 다음과 같습니다:

1. **수정자(Modifiers)**
    
    - public, static 같이 메서드의 접근 범위와 속성을 지정하는 키워드
        
    
2. **반환 타입(Return Type)**
    
    - void 처럼 메서드가 돌려주는 값의 타입
        
    
3. **메서드 이름(Method Name)**
    
    - main 처럼 메서드 고유의 이름
        
    
4. **매개변수 목록(Parameter List)**
    
    - (String[] args) 처럼 외부에서 넘겨받는 값을 정의하는 부분
        
    
5. **메서드 본문(Method Body)**
    
    - { … } 안에 실제 실행될 코드를 작성하는 블록
        
    
### Example 
> public static void main(String[] args) { 
>  본문 }
  

이 중 앞의 네 가지(수정자+반환 타입+메서드 이름+매개변수 목록)를 **메서드 시그니처(method signature)** 라 부르며, 그 뒤에 따라오는 { … } 를 **메서드 본문(method body)** 또는 **메서드 구현부(implementation block)** 라고 합니다.