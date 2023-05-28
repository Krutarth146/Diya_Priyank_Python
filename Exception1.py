print(3+2)  # 5

try:
    print(4//1)  # gives error

except Exception as e:   # Base class
    print("This is Exception Base class which includes all types of error")

except ValueError:
    print("This is Value Error")

except NameError:
    print("This is Name error")

except ZeroDivisionError:
    print("Zero division error")

except ArithmeticError:
    print("THis is Arithmetic error")




else:
    print("This is else block")

finally:
    print("This block is always executed")



print("Hello Diya and Priyank")


# Try 10 Examples of exception classes