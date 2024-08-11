def hello(to="world"):
    print("hello", to)


name = input("What's your name? ")
hello(name)

"""   to is a parameter in the hello() function 
definition. It acts as a placeholder for the value t
hat will be passed to the function.
name is an argument when calling hello(name). 
It is the actual value provided to the function.

So, when hello(name) is called, t
he value of name is passed to the hello() function 
and is used where to appears in the function. 
Thus, to and name refer to the same data in this context. """

