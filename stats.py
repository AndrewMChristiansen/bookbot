def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    num_characters = {}
    lower_case = text.lower()
    for i in lower_case:
        if i in num_characters:
            num_characters[i] += 1
        else: 
            num_characters[i] = 1
    return num_characters

def sort_on(d):
    return d["num"]

def sort_characters(num_characters):
    character_list = []
    for char in num_characters:
        num = num_characters[char]
        character = {"char" : char, "num" : num}   
        if char.isalpha():
            character_list.append(character)
    character_list.sort(reverse=True, key=sort_on)
    return character_list