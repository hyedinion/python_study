import re
strin = "aaa1234, ^&*2233pp"
numbers = re.sub(r'[^0-9]', '', strin)
print(numbers)