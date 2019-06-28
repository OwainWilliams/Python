numbers = [5,3,2,3,4,5]

numbers2 = numbers.copy()

numbers.append(20)
numbers.insert(0, 22)
numbers.remove(3)
numbers.pop() #remove last item in list

print(numbers.index(2))

print(3 in numbers)
print(numbers.count(3))

numbers.sort()
print(numbers)
print(numbers2)

# Write a program to remove the duplicates in a list
numbers = [1,2,3,4,5,5,6,6,7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)