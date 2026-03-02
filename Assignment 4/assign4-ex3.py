import re

def calculate_paragraph_sum(paragraph):
    number_strings = re.findall(r'\d+', paragraph)
    
    total_sum = 0
    
    for num_str in number_strings:
        total_sum += int(num_str)
        
    return total_sum

input_data = "Today is March 02, 2026. The temperature is 30 degrees Celsius."
output = calculate_paragraph_sum(input_data)

print(f"Numbers found: {re.findall(r'\d+', input_data)}")
print(f"Final Sum: {output}")