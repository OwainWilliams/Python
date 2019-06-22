course = "Python's course for newbies"
courses = 'Python for "Beginners"'

triple_quote = '''
Hi Owain,

Here is our first email to you. 

Thanks, 
Owain.

'''

indexing = "A sentences to index"
another = indexing[:] # clones entire string

name = 'Owain'


print (course)
print (courses)
print (triple_quote)

print(indexing[0]) # A
print(indexing[-1]) # x
print(indexing[0:5]) # A sen
print(indexing[1:]) # exclude first character and start at location 1, string starts with 0
print(indexing[:5]) # 0 is assumed as start index then display next 5 chars

print(another)