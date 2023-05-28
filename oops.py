# Oops - > Object Oriented Programming 
# Class , Object, Inheritance, PolyMorphism, Abstraction, Encapsulation, getattr, setaattr

# class Student
# {
#     int id;
#     char name[10];
#     float marks;


    # void studentscan()
    # {

    # }

    # void studentdisplay()
    # {

    # }   
# };

# void main()
# {
#     int a,b;
#     Student a1,a2;

#     a1.id = 900;
#     a2.marks = 70.90;

# }   In C Programming


# Student s1;  
# Student s2;

# Object -> Object is Instance of Class.
# class -> Defination of Particular Object


# Class and Object in Python

class Student:
    # Member Variables
    id = 0   # Int 
    name = ""  # str 
    marks = 0.0  # Float


diya = Student() # diya is object, Student() is class

print(type(diya.id))
print(diya.id)
diya.id = 50
print(diya.id)  # 50

diya.name = "Diya Gandhi"
diya.marks = 92
print(diya.name, diya.marks, sep='->')  # Diya Gandhi->92
