import re

# Define the input string
input_string = "meed to 34534230 43456,erte 95459"

# Define a regular expression pattern to match continuous, exact five-digit numbers
pattern = r'\b\d{5}\b'

# Use re.findall to extract all matching five-digit numbers
result = re.findall(pattern, input_string)

# Convert the list of matches to a comma-separated string
output_string = ','.join(result)

# Print the result
print(output_string)
