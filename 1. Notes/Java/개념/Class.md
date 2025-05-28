# 1. Class 란?
자바(Java)에서 **클래스(class)** 는 객체 지향 프로그래밍의 기본 단위로, **객체(object)** 를 생성하기 위한 설계도(템플릿) 역할을 합니다. 클래스는 상태(state)와 동작(behavior)을 한 곳에 묶어 정의합니다.

# **2. 클래스의 구성 요소**

1. **필드(fields) (속성, 상태)**
    
    - 클래스가 가지는 데이터 멤버
        
    - 예: int age;, String name;
        
    
2. **메서드(methods) (행동, 기능)**
    
    - 클래스가 수행할 수 있는 동작
        
    - 예: void eat() { … }, String toString() { … }
        
    
3. **생성자(constructor)**
    
    - 객체를 생성하면서 초기 상태를 설정하는 특별한 메서드
        
    - 클래스 이름과 동일하며 반환 타입이 없음
        
    - 기본 생성자(Default Constructor)는 작성하지 않으면 컴파일러가 자동 생성
        
    
4. **초기화 블록(initializer block)** (선택적)
    
    - 필드 초기화를 수행하는 블록
        
    - 인스턴스 초기화 블록, 정적(static) 초기화 블록으로 구분
        
    
5. **중첩 타입(nested types)** (선택적)
    
    - 클래스 안에 정의된 또 다른 클래스, 인터페이스, enum 등
        
    

---자바(Java)에서 **클래스(class)** 는 객체 지향 프로그래밍의 기본 단위로, **객체(object)** 를 생성하기 위한 설계도(템플릿) 역할을 합니다. 클래스는 상태(state)와 동작(behavior)을 한 곳에 묶어 정의합니다.자바(Java)에서 **클래스(class)** 는 객체 지향 프로그래밍의 기본 단위로, **객체(object)** 를 생성하기 위한 설계도(템플릿) 역할을 합니다. 클래스는 상태(state)와 동작(behavior)을 한 곳에 묶어 정의합니다.

# 3. Example
#### 2.1 Class 선언
```java
// 클래스 선언
public class Person {
    // 1) 필드
    private String name;
    private int age;

    // 2) 생성자
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // 3) 메서드
    public void introduce() {
        System.out.println("안녕하세요, 저는 " + name + "이고, 나이는 " + age + "살입니다.");
    }

    // 4) getter / setter (캡슐화)
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        }
    }
}
```
#### 2.2 클래스 인스턴스/객체 생성
```Java
public class Main {
    public static void main(String[] args) {
        // Person 클래스의 인스턴스 생성
        Person p = new Person("철수", 25);
        p.introduce();  // 출력: 안녕하세요, 저는 철수이고, 나이는 25살입니다.
        
        // 필드 값 변경
        p.setAge(26);
        System.out.println(p.getName() + "님의 새로운 나이: " + p.getAge());
    }
}
```

# 4. 메인 클래스
## main class
Java는 **클래스 기반 언어**이기 때문에, ==모든 실행 가능한 코드는 반드시 클래스 안에 정의==되어야 합니다. 그중에서도 프로그램의 시작 지점을 담당하는 main 메서드는 다음과 같은 이유로 **Main(또는 아무 이름이나 가능하지만 관습적으로 Main)** 이라는 클래스로 감싸서 만듭니다:
- **public 클래스**는 소스 파일 이름과 **반드시 일치**
- JVM은 프로그램을 실행할 때 **public static void main(String[] args)** 메서드를 찾아 실행합니다.
- 이 메서드는 **클래스** 안에 반드시 있어야 하며, 클래스 이름을 통해 어떤 파일을 로드할지 판단합니다

#### JVM 과 클래스
Java 프로그램을 실행하려면 **JVM**(Java Virtual Machine)에게 “어디서부터 시작해야 할지” 알려줘야 합니다. 그 역할이 바로 public static void main(String[] args) 메서드와 이를 담고 있는 클래스입니다. 차례대로 살펴보면: