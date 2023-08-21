import pandas as pd
import re

# Sample data
data = {
    'id': [666, 666, 455, 666, 666, 545],
    'transaction': [865, 1295, 995, 54554, '45ty4566', '45y'],
    'comments': ['wrwrw dfgfg', 'wefwefk 55455 sfffwerf', 'fwfwe #64534', 'rgwergwv etete', 'fwrtw34rt34 ertrter erger et45t64', '454554'],
    'uc id': ['', '55455', '64534', 'etete', 'et45t64', '54rtrt']
}

# Read data from CSV file
input_file = 'input_data.csv'
df = pd.read_csv(input_file)
# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to extract 5-digit numbers from a string
def extract_5_digit_numbers(text):
    numbers = re.findall(r'\b(\d{5})\b', text)
    return numbers

# Find the unique IDs with 5-digit numbers in comments or uc id
unique_ids = df['id'].unique()
result_data = []

for id_ in unique_ids:
    comments = df[df['id'] == id_]['comments'].apply(extract_5_digit_numbers)
    uc_ids = df[df['id'] == id_]['uc id'].apply(extract_5_digit_numbers)
    
    found_status = 'Not found'
    uc_result = ''
    
    for comment_numbers in comments:
        if has_5_digit_number(comment_numbers):
            found_status = 'Found'
            uc_result = comment_numbers[0]
            break
    
    if found_status == 'Not found':
        for uc_numbers in uc_ids:
            if has_5_digit_number(uc_numbers):
                found_status = 'Found'
                uc_result = uc_numbers[0]
                break
    
    result_data.append({'id': id_, 'uc': uc_result, 'Result': found_status})

result_df = pd.DataFrame(result_data)

print(result_df)
