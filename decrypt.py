import pyfiglet

# list all the charscters
characters = "*&#+!"
key = "aeiou"
# ask user's encrypted text
text = input("\033[34mEnter your encrypted text: ")
# * changed to a, & changed to e, # changed to i, + changed to o, ! changed to u,
decrypt_text = ""
for letter in text:
    if letter.lower() in characters:
        decrypt_text += key[characters.find(letter.lower())]
    else:
        decrypt_text += letter
# print ouptput
print(f"\033[91mDecrypted text: ")
print("*" * 70)
print(pyfiglet.figlet_format(decrypt_text))
print("*" * 70)

