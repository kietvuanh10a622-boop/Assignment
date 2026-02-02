def make_acronym(phrase):
    
    words = phrase.split()
    
    acronym = ""
    
    
    for word in words:
       
        acronym = acronym + word[0]
    
    
    return acronym.upper()


user_input = input('Input: ')
print(f"Output: {make_acronym(user_input)}")