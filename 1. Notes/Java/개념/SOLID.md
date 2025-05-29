다음은 객체지향 설계의 5가지 기본 원칙인 **SOLID** 원칙입니다. 각 원칙마다 개념 설명과 간단한 예시(Java 코드) 를 들어 이해를 돕겠습니다.

---

## **1. Single Responsibility Principle (SRP)**

**단일 책임 원칙**

- **정의**: 클래스는 단 하나의 책임(변경 이유)만 가져야 한다.
    
- **취지**: 한 클래스가 여러 기능을 가지면, 기능 변경 시 영향을 받는 부분이 많아져 유지보수가 어려워진다.
### **예시**
```java
// 잘못된 예: User 클래스가 사용자 정보 저장과 이메일 발송을 함께 담당
public class User {
    private String name;
    private String email;
    // … getter/setter …

    public void save() {
        // DB에 사용자 정보 저장
    }

    public void sendWelcomeEmail() {
        // 이메일 발송 로직
    }
}

// 개선된 예: 두 개의 클래스로 분리
public class User {
    private String name;
    private String email;
    // … getter/setter …
    public void save() {
        // DB에 사용자 정보 저장
    }
}

public class EmailService {
    public void sendWelcomeEmail(User user) {
        // 이메일 발송 로직
    }
}
```

---

## **2. Open/Closed Principle (OCP)**
**개방-폐쇄 원칙**

- **정의**: 소프트웨어 요소(class, module, function 등)는 **확장에는 열려(Open)** 있어야 하고, **수정에는 닫혀(Closed)** 있어야 한다.
    
- **취지**: 기존 코드를 수정하지 않고 기능을 추가할 수 있어야 안정성이 높아진다.
### **예시**

```java
// 잘못된 예: 새로운 할인 정책을 추가할 때마다 Order 클래스 수정 필요
public class Order {
    public double calculatePrice(double basePrice, String discountType) {
        if (discountType.equals("NONE")) {
            return basePrice;
        } else if (discountType.equals("SEASONAL")) {
            return basePrice * 0.9;
        }
        // 새로운 할인 정책 추가 시 if-else 계속 늘어남
        return basePrice;
    }
}

// 개선된 예: 할인 정책을 인터페이스로 분리하고, Strategy 패턴 적용
public interface DiscountStrategy {
    double apply(double basePrice);
}

public class NoDiscount implements DiscountStrategy {
    public double apply(double basePrice) {
        return basePrice;
    }
}

public class SeasonalDiscount implements DiscountStrategy {
    public double apply(double basePrice) {
        return basePrice * 0.9;
    }
}

public class Order {
    private DiscountStrategy discountStrategy;

    public Order(DiscountStrategy ds) {
        this.discountStrategy = ds;
    }

    public double calculatePrice(double basePrice) {
        return discountStrategy.apply(basePrice);
    }
}
// 해당 인터페이스의 구현체 주입은 Main.java에서 해주면 된다. 
```

---

## **3. Liskov Substitution Principle (LSP)**

**리스코프 치환 원칙**

- **정의**: 자식 클래스는 언제나 부모 클래스로 교체해도 시스템의 정확성이 깨지지 않아야 한다.
    
- **취지**: 상속 관계에서 “is-a” 관계가 올바르게 지켜져야 예측 가능한 동작이 가능하다.
    

  

### **예시**

```
// 잘못된 예: 사각형과 정사각형 관계에서 LSP 위반
public class Rectangle {
    protected int width, height;
    public void setWidth(int w) { width = w; }
    public void setHeight(int h) { height = h; }
    public int getArea() { return width * height; }
}

public class Square extends Rectangle {
    @Override
    public void setWidth(int w) {
        width = w;
        height = w;   // 정사각형이므로 높이도 동일하게 설정
    }
    @Override
    public void setHeight(int h) {
        width = h;
        height = h;
    }
}

// 클라이언트 코드에서 Rectangle을 기대하지만 Square를 전달하면 의도치 않은 동작 발생
```

**개선**: 상속 대신 구성(composition) 또는 별도 인터페이스 사용

```
public interface Shape {
    int getArea();
}

public class Rectangle implements Shape {
    private int width, height;
    // … 생성자, getter/setter …
    public int getArea() { return width * height; }
}

public class Square implements Shape {
    private int side;
    // … 생성자, getter/setter …
    public int getArea() { return side * side; }
}
// Shape 인터페이스만 사용하므로 치환해도 안전하다.
```

---

## **4. Interface Segregation Principle (ISP)**

  

**인터페이스 분리 원칙**

- **정의**: 클라이언트는 자신이 사용하지 않는 메서드에 의존하지 않아야 한다.
    
- **취지**: 거대한 인터페이스 하나 대신, 역할별로 세분화된 인터페이스를 제공하여 불필요한 구현 부담을 줄인다.
    

  

### **예시**

```
// 잘못된 예: 멀티 기능 인터페이스
public interface MultiFunctionDevice {
    void print(Document d);
    void scan(Document d);
    void fax(Document d);
}

// 간단한 프린터 클래스도 scan(), fax() 메서드를 구현해야만 한다.
public class SimplePrinter implements MultiFunctionDevice {
    public void print(Document d) { /*…*/ }
    public void scan(Document d) { throw new UnsupportedOperationException(); }
    public void fax(Document d) { throw new UnsupportedOperationException(); }
}

// 개선된 예: 기능별로 인터페이스 분리
public interface Printer {
    void print(Document d);
}
public interface Scanner {
    void scan(Document d);
}
public interface Fax {
    void fax(Document d);
}

public class SimplePrinter implements Printer {
    public void print(Document d) { /*…*/ }
}

public class MultiFunctionMachine implements Printer, Scanner, Fax {
    private Printer printer;
    private Scanner scanner;
    private Fax fax;
    // 생성자 주입
    // print/scan/fax 구현
}
```

---

## **5. Dependency Inversion Principle (DIP)**

  

**의존 역전 원칙**

- **정의**:
    
    1. 상위 모듈(비즈니스 로직)은 하위 모듈(구현 세부 사항)에 의존해서는 안 된다.
        
    2. 둘 다 추상화(인터페이스)에 의존해야 한다.
        
    
- **취지**: 구체 클래스 대신 인터페이스나 추상 클래스에 의존함으로써 결합도를 낮추고 유연성을 높인다.
    

  

### **예시**

```
// 잘못된 예: 구체 구현에 직접 의존
public class MySQLConnection {
    public void connect() { /*…*/ }
}

public class UserRepository {
    private MySQLConnection connection;

    public UserRepository() {
        connection = new MySQLConnection(); // 구체 클래스 직접 생성
    }
    // CRUD 메서드…
}

// 개선된 예: 추상화 의존
public interface DBConnection {
    void connect();
}

public class MySQLConnection implements DBConnection {
    public void connect() { /*…*/ }
}

public class OracleConnection implements DBConnection {
    public void connect() { /*…*/ }
}

public class UserRepository {
    private DBConnection connection;

    // 생성자 주입으로 의존성 역전
    public UserRepository(DBConnection connection) {
        this.connection = connection;
    }
    // CRUD 메서드…
}

// 활용
DBConnection conn = new MySQLConnection();
UserRepository repo = new UserRepository(conn);
```

---

이상으로 SOLID 다섯 원칙을 간단한 예시와 함께 정리했습니다.

각 원칙을 적용하면 코드의 유지보수성과 확장성을 크게 향상시킬 수 있습니다.