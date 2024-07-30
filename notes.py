#here ae some notes about functions i learnt about.
#You can give a parameter a default value
def my_function(parameter_1, parameter_2, parameter_3:True):
    '''this functions holds parameters'''
    '''Parameter_1: The first parameter
       Parameter_2: The second parameter
       Parameter_3: This is a third parameter which has a default value of True.
       So because of the default value set to it, it's optional to give it a value to the third 
       parameter when the function is called.
    '''
    main_parameter=parameter_1,parameter_2,parameter_3
    return main_parameter


#this is an example when i call he function above.
my_function('adam','eve')
#so here i gave the first and second parameters values of adam and eve but i didnt give the third
#parameter a value because it already has a value set for it names True.
#But tho it has a vaue set to be True, i can also assign a new value to it if i want when i call the function.

#another thing i can do is named notations or names parameters.
#named notations is me calling the function and writing the same parameter names in the parrentheses and assigning them
#to new values.But this time it doesnt need to be i order like when there are no assigned values already. example 

my_function(parameter_3='adam',parameter_1='eve',parameter_2='abel')


# Handling exceptions. There are ways to handle exceptions in python. Exceptions are errors and events or situations in
# a python code that sometimes occurs when a program is running. Exceptions can be raised by the program due to 
# a user wrong input, servers being down and other stuffs. As programmers, we need to write codes to handle those 
# exceptions that will come up. To write exceptions, we need to use a built in 'try' and 'except' keywords to handle
# exceptions that may arise whiles the program is running.
