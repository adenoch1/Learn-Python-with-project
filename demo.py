import math_utils

# print("demo __name__:", __name__)

result = math_utils.add(10, 5)
print(result)
"""
__name__ is a shortcut for the name of the module.
It helps flask to know where this app is 
and relatively use it to locate templates and static files in the project folder.

__name__ is a special built-in variable (a "dunder" attribute) that stores 
the name of the current module. Its value is automatically set by the Python 
interpreter to determine whether the script is being run as the main program or 
imported as a module into another script. 
How __name__ Works?
The value of the __name__ variable changes depending on how the Python file is executed: 
When the script is run directly, the interpreter sets the __name__ 
variable to the string "__main__". This signifies that the file is the entry 
point of the program.
When the script is imported as a module into another file, 
the interpreter sets the __name__ variable to the module's actual name 
(which is usually the filename without the .py extension

when you run python demo.py, python import math_utils
Inside math_utils, __name__ == "math_utils", not __main__
add() works
"Running math_utils directly" does NOT print
Condition is False.
Code inside if __name__ == "__main__": is skipped.

Importing a module gives you its functions; 
running a file executes its entry-point logic. 
__name__ == "__main__" separates those two worlds.

A library is something which you call upon to do something specific.
But a Framework something that you have to abide by their rules,
you have to use their architecture
and when it comes to triggering some form of functionality,
it's the framework that calls upon your code.
"""