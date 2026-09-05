import random
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "!", "@", "#", "$", "%", "^", "&", "*", "/", "<", ">", "(", ")",
              ";", ":", "+", "-", "=", "`", "~", "?", "1", "2", "3", "4", "5",
              "6", "7", "8", "9", "0", "|", ".", ","]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "/", "<", ">", "(", ")",
           ";", ":", "+", "-", "=", "`", "~", "?", "|", ".", ","]

password = ""
print("=========PASSWORD GENERATOR========")
print("Which password would you like?")
print("1. Everything (letters, numbers, symbols)")
print("2. Letters only")
print("3. Numbers only")
print("4. Symbols only")
ans = input("")
print("What length would you like?")
length = int(input(""))
if ans == "1":
    for x in range(length):
        passwordg = random.choice(characters)
        password += passwordg
    print(password)
elif ans == "2":
    for x in range(length):
        passwordg = random.choice(letters)
        password += passwordg
    print(password)
elif ans == "3":
    for x in range(length):
        passwordg = random.choice(numbers)
        password += passwordg
    print(password)
elif ans == "4":
    for x in range(length):
        passwordg = random.choice(symbols)
        password += passwordg
    print(password)
    