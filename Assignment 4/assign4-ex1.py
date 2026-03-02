
def course_code(code):
 if len(code) !=6:
     return False
 letter = code[:3]
 number = code[3:]
 if letter.isupper() and number.isdigit():
     return True
 else:
     return False

print(course_code("TEC001"))

