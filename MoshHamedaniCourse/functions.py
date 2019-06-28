#Setting parameters
def greet_user(first_name, last_name):
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
#Postitional Arguments
greet_user("Owain", "Williams")

#keyword argument
greet_user(last_name="Smith", first_name="Toby")

#postional arguments should come first if using both positional and keyword
#e.g. greet_user("Toby", last_name="Smith")

print("Finish")