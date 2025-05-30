1. **Static = “Belongs to the Blueprint”**
The word **static** literally means “at rest” or “not changing,” and in programming it came to describe things that are **fixed at the class level**, rather than tied to any one instance (which are created and destroyed dynamically).
2. **“Belongs to the Class” vs “Belongs to the Instance”**
    
    - **Instance (dynamic) members** are tied to each object you new. They sit on the heap and each object gets its own copy.
        
    - **Static (class-level) members** are tied to the class’s definition itself—they’re “static” because they don’t move or duplicate per object.

네, 거의 “글로벌 변수”와 비슷한 개념이라고 볼 수 있어요. 다만 몇 가지 차이가 있습니다:

1. **클래스 범위(Class Scope)**
    
    - 전통적인 C/C++ 의 글로벌 변수는 보통 파일 단위로 선언해서 프로그램 전체에서 접근 가능한 반면,
        
    - 자바의 static 변수는 **반드시 클래스 안**에 선언돼야 하고, 클래스이름.변수명 으로 접근합니다.
2. **네임스페이스 보호**
    
    - 클래스 단위로 네임스페이스가 분리되기 때문에, 같은 이름의 static 변수를 여러 클래스에서 각각 가질 수 있어 충돌 위험이 줄어듭니다.
        
    - C의 전역 변수는 파일 간 이름 충돌을 방지하려면 static(파일 스코프) 또는 extern(외부 선언)을 섞어 써야 했죠.
        
    
3. **생명 주기**
    
    - JVM에서 해당 클래스를 로드할 때 한 번 메모리에 올라가고, 언로드될 때(또는 앱 종료 시)까지 살아 있습니다.
        
    - 진짜 전역 변수처럼 프로그램 시작부터 끝까지 존재한다고 보면 됩니다.
        
    
4. **캡슐화 & 접근 제어**
    
    - private static 으로 선언해 외부에서 직접 접근을 막고, public static 메서드(예: getInstance())를 통해 제어된 접근만 허용할 수도 있습니다.