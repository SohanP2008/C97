introduction = input("Enter your introduction: ")
print(introduction)
word_count = 1
character_count = 0
for character in introduction:
    character_count = character_count + 1
    if(character == " "):
        word_count = word_count + 1
print(character_count)
print(word_count)