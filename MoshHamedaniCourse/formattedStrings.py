firstname = "Owain"
lastname = "Williams"
message = f'{firstname} [{lastname}] is a coder' #formatted string

print(message)


# String Methods

course = 'Python for Beginners'

#display string length with len
print (len(course))
print (course.upper())
print (course.lower())
print (course.find('o'))
print (course.find('for'))
print (course.replace('Beginners', 'Absolute Beginners'))

# in Operator
print('Python' in course)