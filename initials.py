#this function gets the names of users and returns the first letters are their initials

def get_initial(names):
   name_initial=names[0].upper()
   return name_initial  

first_name=input('please enter your first name: ')
last_name=input('please enter your last name: ')
print(f'your initials are {get_initial(first_name) + get_initial(last_name)}')

#with this kind of code, i have called the functions and applied the parameter values in the format string

#here is another way


first_name=input('please enter your first name: ')
last_name=input('please enter your last name: ')
first_name_initial=get_initial(first_name)
last_name_initials=get_initial(last_name)
print(f'your initials are {first_name_initial + last_name_initials}')

#also with this second approach, the functions were called outside the format string