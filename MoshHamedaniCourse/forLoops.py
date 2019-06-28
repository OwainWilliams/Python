# print each letter on a new line
for item in 'Python':
    print(item)

# print list, taking a new line for each name
for item in ['Owain', 'Amanda', 'Tony', 'Bruce']:
    print(item)

# print numbers 0 - 9
for item in range(10):
    print(item)

# Print a range of numbers starting at 5 
# Stops when it hits 10, doesn't print 10
for item in range(5, 10):
    print(item)

# Print a range of numbers, starting at 2 and incrementing by 2
# until you hit the end of range (10)  
for item in range(2, 10, 2):
    print(item)



# Calculate the value of a list
prices = [10, 20, 30]
total = 0

for price in prices:
    total += price
print (f"Total: £{total}")