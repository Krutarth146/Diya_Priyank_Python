# Inheritance : Take property access from another class to own class


# Parent Class (Base class, Super class)
# Child class (Derived Class, Subclass)

# Inheritance : 5 Types
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# 1. Single Inheritance

class Birds:
    def __init__(self):
        self.wings = 2   # constructor ->  TO initializa data memeber variables
    
    def fly(self):
        print("All birds can fly.")

    def eat(self):
        print("All Birds can Eat.")


# class Sparrow : public Birds (in cpp)
class sparrow(Birds):                  
    def sp_wings(self):
        print("Sparrow has 2 wings")

    def size(self):
        print("Sparrow'size is smaller than peacock.")


s1 = sparrow()   # wings = 2
print(s1.wings)
s1.size()  # Sparrow'size is smaller than peacock.
s1.sp_wings()  # Sparrow has 2 wings
s1.eat()   # All Birds can Eat.
s1.fly()   # All birds can fly.


