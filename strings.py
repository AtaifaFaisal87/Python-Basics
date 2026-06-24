#STRINGS
#'' and "" are used for short strings
#''' and """ are used for long strings

course="""
respectful teacher,
I am writing to express my sincere gratitude for your dedication and support throughout the course. Your passion for teaching and commitment to our learning have made a significant impact on my educational journey.
Your ability to explain complex concepts in a clear and engaging manner has greatly enhanced my understanding of the
subject matter. I appreciate the time and effort you have invested in creating a positive and inclusive learning environment, where students feel comfortable asking questions and sharing their ideas.
Thank you for your patience, encouragement, and willingness to go the extra mile to ensure our success. Your guidance and mentorship have been invaluable, and I am truly grateful for the knowledge and skills I have gained under your instruction.
I look forward to applying what I have learned in future endeavors and continuing to grow as a student. Once again, thank you for being an exceptional teacher and for making a lasting impact on my education.
Sincerely,  
Ataifa
"""
print(course)

 #strings by indexes
name="ataifa"
# 012345

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

print(name[0:3]) #this will print the first three characters of the string
print(name[3:]) #this will print the characters from index 3 to the end
print(name[:3]) #this will print the first three characters of the string
print(name[:]) #this will print the entire string   
print(name[-1]) #this will print the last character of the string
print(name[1:-1]) #this will print the characters from index 1 to the second last character
 
 #formatted strings

 #concatination
first_name='Ataifa'
last_name='faisal'
#ataifa faisal is a coder
message=first_name + '[' + last_name + ']'+ 'is a coder'
print(message)
msg=f'{first_name} [{last_name}] is a coder' #this is a formatted string using f-string
#f-string is a way to format strings in python by using curly braces {} to insert variables or expressions into the string
print(msg)

#string methods
course='python for beginners'

#functions are reusable pieces of code that perform a specific task and can be called by their name
#len() function returns the length of the string
print(len(course))

#methods are functions that are associated with a particular data type and can be called on an instance of that data type
#upper() method converts the string to uppercase
print(course.upper())
#lower() method converts the string to lowercase
print(course.lower())
#find() method returns the index of the first occurrence of the specified value
#case-sensitive, so it will return -1 if the value is not found
print(course.find('y')) #this will return the index of the first occurrence of 'y' in the string
print(course.find('for')) #this will return the index of the first occurrence of 'for' in the string
print(course.replace('for', '4')) #this will replace 'for' with '4' in the string
print(course.title()) #this will convert the first character of each word to uppercase and the rest to lowercase
#. operator is used to access the methods of the string

#in operator is used to check if a substring is present in the string returning a boolean value (True or False)
print('python' in course) #this will return True if 'python' is present in the string, otherwise it will return False
print('java' in course) #this will return False as 'java' is not present in the string
