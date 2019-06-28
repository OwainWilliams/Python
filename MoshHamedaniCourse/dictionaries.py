customer = {
    "name": "Tony Stark",
    "age": 30,
    "is_verified": True
}
print(customer["name"])

print(customer.get("Name", "No name available")) # If Name doesn't exist, show default value


phone = input("Phone: ")
digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for char in phone:
    output += digits_mapping.get(char, "!") + " "
print(output)