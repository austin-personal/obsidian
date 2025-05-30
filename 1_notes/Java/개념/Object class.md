## **1.** 

## **Object**

## **란 무엇인가?**

- **최상위 클래스 (Root Class)**
    
    JVM 내에서 모든 참조형 타입의 공통 조상으로, 어떠한 클래스라도 extends Object를 기본으로 가집니다.
    
- **주요 메서드**
    
    - public String toString()
        
    - public boolean equals(Object obj)
        
    - public int hashCode()
        
    - protected Object clone() throws CloneNotSupportedException
        
    - public final ClassgetClass()
        
    - protected void finalize() throws Throwable
        
    

  

이 덕분에, 자바의 모든 객체는 최소한 위 메서드들을 사용할 수 있습니다.
Java에서 모든 클래스는 Object를 최상위 클래스로 갖습니다. 즉:public class MyService { … }는 암묵적으로
public class MyService extends Object { … } 와 같고, Object가 가진 표준 메서드(toString(), equals(), hashCode() 등)를 사용할 수 있게 됩니다.