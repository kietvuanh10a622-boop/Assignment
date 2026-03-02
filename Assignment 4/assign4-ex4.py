import re

def protect_privacy(document):

    phone_pattern = r'\+84\d+|\d{10}'
    
    redacted_doc = re.sub(phone_pattern, "[REDACTED]", document)
    
    return redacted_doc

report = "Contact Kiet at +84898506589 or call the office at 0123456789."
protected_report = protect_privacy(report)

print(f"Original: {report}")
print(f"Protected: {protected_report}")