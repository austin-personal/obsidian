The **Singleton Pattern** is a creational design pattern that ensures a class has only **one** instance throughout the application’s lifecycle and provides a **global point of access** to it. It’s commonly used for shared resources like configuration managers, connection pools, or logging facilities.

---

## **1. Key Characteristics**

1. **Single Instance**
    
    The class controls its own instantiation and prevents more than one object from being created.
    
2. **Global Access Point**
    
    Provides a static method (often named getInstance()) to retrieve the sole instance.
    
3. **Lazy vs. Eager Initialization**
    
    - **Eager**: Instance is created when the class is loaded.
        
    - **Lazy**: Instance is created on first request, saving resources if it’s never used.
        
    
4. **Thread Safety**
    
    In multithreaded environments, you must guard against race conditions when initializing the singleton.
    

---

## **2. Typical Java Implementations**

  

### **2.1 Eager Initialization**

```
public class EagerSingleton {
    private static final EagerSingleton INSTANCE = new EagerSingleton();
    private EagerSingleton() { /* prevent external instantiation */ }
    public static EagerSingleton getInstance() {
        return INSTANCE;
    }
}
```

- **Pros**: Simple, thread-safe by default (class loading is thread-safe).
    
- **Cons**: Instance created even if never used.
    

  

### **2.2 Lazy Initialization (Non-Thread-Safe)**

```
public class LazySingleton {
    private static LazySingleton instance;
    private LazySingleton() {}
    public static LazySingleton getInstance() {
        if (instance == null) {
            instance = new LazySingleton();
        }
        return instance;
    }
}
```

- **Pros**: Instance created only when needed.
    
- **Cons**: Not safe under multithreading — two threads could create two instances simultaneously.
    

  

### **2.3 Thread-Safe (Synchronized Access)**

```
public class ThreadSafeSingleton {
    private static ThreadSafeSingleton instance;
    private ThreadSafeSingleton() {}
    public static synchronized ThreadSafeSingleton getInstance() {
        if (instance == null) {
            instance = new ThreadSafeSingleton();
        }
        return instance;
    }
}
```

- **Pros**: Thread-safe.
    
- **Cons**: synchronized on every call can hurt performance.
    

  

### **2.4 Double-Checked Locking**

```
public class DCLSingleton {
    private static volatile DCLSingleton instance;
    private DCLSingleton() {}
    public static DCLSingleton getInstance() {
        if (instance == null) {
            synchronized (DCLSingleton.class) {
                if (instance == null) {
                    instance = new DCLSingleton();
                }
            }
        }
        return instance;
    }
}
```

- **Pros**: Lazily initialized, minimizes synchronization overhead.
    
- **Cons**: Slightly more complex; requires the volatile keyword to work correctly.
    

  

### **2.5 Initialization-On-Demand Holder**

```
public class HolderSingleton {
    private HolderSingleton() {}
    private static class Holder {
        static final HolderSingleton INSTANCE = new HolderSingleton();
    }
    public static HolderSingleton getInstance() {
        return Holder.INSTANCE;
    }
}
```

- **Pros**: Thread-safe, lazy, no synchronization overhead.
    
- **Cons**: May be less obvious to beginners.
    

---

## **3. When to Use**

- **Shared, expensive-to-create resources** (e.g., database connections, thread pools).
    
- **Centralized configuration** or **logging** services.
    
- **Caching** objects where duplicate instances would be wasteful.
    

---

## **4. Pitfalls & Alternatives**

1. **Hidden Dependencies**
    
    Singletons act like global variables—overuse can lead to tightly coupled code.
    
2. **Testing Difficulty**
    
    Harder to mock or replace in unit tests. Consider dependency injection frameworks (e.g., Spring) that manage lifecycle for you.
    
3. **Enum-Based Singleton (Joshua Bloch’s Recommendation)**
    

```
public enum EnumSingleton {
    INSTANCE;
    public void someMethod() { … }
}
```

3. - Simplest, handles serialization and reflection attacks automatically.
        
    

---

### **Summary**

  

The Singleton Pattern ensures **one-and-only-one** instance of a class and a **global access point**. In modern applications, it’s often preferable to let an IoC container (like Spring) manage singleton-scoped beans rather than hand-rolling singletons.