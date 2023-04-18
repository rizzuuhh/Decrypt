# list all the charscters
characters = "*&#+!"
key = "aeiou"
# ask user's encrypted text
text = input("Enter your encrypted text: ")
# * changed to a, & changed to e, # changed to i, + changed to o, ! changed to u,
decrypt_text = ""
for letter in text:
    if letter.lower() in characters:
        decrypt_text += key[characters.find(letter.lower())]
    else:
        decrypt_text += letter
# print ouptput

