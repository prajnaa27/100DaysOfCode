import random
from email.utils import parsedate_to_datetime

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#EASY VERSION
# mixed_list=[letters,numbers,symbols]
# print(mixed_list)
# new_list=[]
# print(mixed_list[0])
# for i in range(nr_letters):
#     random_letter=random.choice(mixed_list[0])
#     print(type(random_letter))
#     new_list.insert(i,random_letter)
# print(new_list)
#
# for i in range(nr_numbers):
#     random_number=random.choice(mixed_list[1])
#     print(type(random_number))
#     new_list.append(random_number)
# print(new_list)
#
# for i in range(nr_symbols):
#     random_symbol=random.choice(mixed_list[2])
#     print(type(random_symbol))
#     new_list.append(random_symbol)
# print(new_list)
#
# final_password=''.join(new_list)
# print(f"Generated password is ...{final_password}")


total_characters=nr_symbols+nr_numbers+nr_letters
print(total_characters)
new_list=[]
for i in range(nr_letters):
    random_index = random.randint(0, total_characters)
    print(random_index)
    random_letter= random.choice(letters)
    print(random_letter)
    new_list.insert(random_index,random_letter)
for i in range(nr_symbols):
    random_index = random.randint(0, total_characters)
    print(random_index)
    random_symbol = random.choice(symbols)
    print(random_symbol)
    new_list.insert(random_index, random_symbol)
for i in range(nr_numbers):
    random_index = random.randint(0, total_characters)
    print(random_index)
    random_number = random.choice(numbers)
    print(random_number)
    new_list.insert(random_index, random_number)
print(new_list)

password=''.join(new_list)
print(f"Generated password is \n{password}")


#Key notes is using random.shuffle method to just mix the items in a list