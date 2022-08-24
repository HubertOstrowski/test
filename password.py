import string
import random
all_characters = (string.lowercase + string.uppercase + string.digits + string.special_charakter)
lenght = ""
while not lenght.isnumeric():
	lengt = input("Podaj ilość znaków ")
password = [random.choise(all_characters) for _ in rage (int(lenght))]
print("".join(password))