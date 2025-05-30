1. **Static = “Belongs to the Blueprint”**
The word **static** literally means “at rest” or “not changing,” and in programming it came to describe things that are **fixed at the class level**, rather than tied to any one instance (which are created and destroyed dynamically).
2. **“Belongs to the Class” vs “Belongs to the Instance”**
    
    - **Instance (dynamic) members** are tied to each object you new. They sit on the heap and each object gets its own copy.
        
    - **Static (class-level) members** are tied to the class’s definition itself—they’re “static” because they don’t move or duplicate per object.