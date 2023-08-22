import pandas as pd
import re

# Sample data
data = {
    'Ticket Number': [666, 666, 455, 666, 666, 545, 77765566],
    'transaction': [865, 1295, 995, 54554, '45ty4566', '45y',''],
    'comments': ['','wrwrw dfgfg', 'wefwefk #53435 sfffwerf', 'fwfwe #64534', 'rgwergwv etete', 'fwrtw34rt34 ertrter erger et45t64', '454554'],
    'DUC ID': ['', '55455', '64534', '43439#', 'ducid42942', '443443442','']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to extract 5-digit numbers from a string
def extract_5_digit_numbers(text):
    return re.findall(r'(?<![0-9])\d{5}(?![0-9])', text)

# Find unique ticket numbers and validate 5-digit numbers in comments and DUC ID
unique_ticket_numbers = df['Ticket Number'].unique()
result_data = []

for ticket_number in unique_ticket_numbers:
    # Get comments and DUC IDs for the current ticket number
    comments = ' '.join(df[df['Ticket Number'] == ticket_number]['comments'])
    duc_ids = ' '.join(df[df['Ticket Number'] == ticket_number]['DUC ID'])
    
    # Extract valid 5-digit numbers from comments and DUC IDs
    valid_comments = set(extract_5_digit_numbers(comments))
    valid_duc_ids = set(extract_5_digit_numbers(duc_ids))
    
    # Combine valid 5-digit numbers from both sources
    valid_5_digit_numbers = valid_comments.union(valid_duc_ids)
    
    # Determine the result status and valid 5-digit numbers if found
    if valid_5_digit_numbers:
        found_status = 'Found'
        duc_results = ', '.join(valid_5_digit_numbers)
    else:
        found_status = 'Not found'
        duc_results = ''
    
    # Add result entry to the result data list
    result_data.append({'Ticket Number': ticket_number, '5-Digit Numbers': duc_results, 'Result': found_status})

# Create a DataFrame from the result data
result_df = pd.DataFrame(result_data)

# Print the input data and the result DataFrame
print("Input Data:")
print(df)
print("\nResult:")
print(result_df)
