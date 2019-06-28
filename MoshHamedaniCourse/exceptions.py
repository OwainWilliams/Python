try:
    age = int(input('Age: '))
    income = 200000
    risk = income / age
    print(age)
except ValueError:
    print('Oops!')
except ZeroDivisionError:
    print('Age cannot be 0')

