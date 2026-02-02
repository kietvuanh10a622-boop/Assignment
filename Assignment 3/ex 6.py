def get_middle_characters(text):
    length = len(text)
    middle = length // 2

    if length % 2 == 0:
        
        return text[middle - 1 : middle + 1]
    else:
        
        return text[middle]


print(f"Middle of 'Tuyen': {get_middle_characters('Tuyen')}") 
print(f"Middle of 'Quang': {get_middle_characters('Quang')}")   