def word_frequency(text):
    words = text.lower().split()
    frequency_dict = {}

    for word in words:
        word = word.strip(".,!?;:\"()")
        if word:
            frequency_dict[word] = frequency_dict.get(word, 0) + 1
            
    return frequency_dict

sample_text = "Data is the new oil. Data is valuable, but data needs processing."
result = word_frequency(sample_text)
print(result)