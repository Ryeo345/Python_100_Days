"""
Global Scope is outside of a function

variables work inside a function and outside a function

Local Scope is inside of a function

variable declared inside of a function only works within the function

python does not have block scope

variable defined with a value in an if statement will effect the variable in a function,

if the code is not enclosed, the variable will have global scope

if the variable is in a function, and we want to modify the variable, that is already defined in the global scope

we need

"global" keyword variable

which is fallible and prone to causing errors

its better to return the modification in the function and assign the new value to the variable outside of local scope

- Python constants are variables that we don't ever want to change i.e. pi

the naming convetion is all uppercase

PI = 3.14159
"""
