print("hello world")
#this is a commment 
print('hello')
 
 #VARIABLES
 #variables are containers for storing data values
 #we can assign different data types to variables
name='JOHN SMITH'
age=20
is_new=True

#input function
#input function allows us to take user input
name=input('what is your name? ')
print('hi ' + name)
colour=input('what is your favourte colour?')
print(name +  'likes'  + colour)

#type converstion
birth_year=input('what is your birth year? ')
#age=2026-birth_year this will give error as int-string cannot be subtracted
age=2026-int(birth_year)
print(age)
print(type(age))
print(type(birth_year))
