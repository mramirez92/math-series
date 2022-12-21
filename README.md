# LAB - Class 02 - Modules and Testing

## Author: Monica Ramirez 

## Links and Resources

[Python Tutor](https://pythontutor.com/)

[Fibonacci Series](http://en.wikipedia.org/wiki/Fibbonaci_Series)

[Lucas Series](http://en.wikipedia.org/wiki/Lucas_number)

[Generate the Fibonacci Sequence With Python](https://www.youtube.com/watch?v=I_Giq4-2Pn8&ab_channel=RealPython)



# Setup
.venv requirements:
    - pywatch 

# How to initialize/run your application (where applicable)

start virtual environment to test package modules: `.venv` , run  `pythontest tests/test_series.py` or python testing libray of your choosing. 


# Tests

test_series.py tested in our virtual environment.  tests were conducted using python-watch library.
First two sets of tests expect outcome based on [Fibonacci Series](http://en.wikipedia.org/wiki/Fibbonaci_Series), [Lucas Series](http://en.wikipedia.org/wiki/Lucas_number) respectively. Where `n` is the required input. 
The last set of tests will run either Fibonacci or the Lucas function based off of one required parameter (n) and two optional parameters (a,b).
    - if optional parameters a = 0 and b = 1 run fibonacci function
    - if optional parameters a = 2 and b = 1 run lucas function 