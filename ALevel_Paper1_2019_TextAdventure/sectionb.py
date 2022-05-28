word1 = input("Enter first word...").upper()
word2 = input("Enter second word...").upper()
word2_characters = []
for char in word2:
    word2_characters.append(char)
success = True
for char in word1:
    if char in word2_characters:
        word2_characters.remove(char)
    else:
        success = False
print(f"The first word can{'' if success else 'not'} be made from the second")