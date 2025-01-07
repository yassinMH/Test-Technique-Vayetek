import re
def extract_first_number(text):
    match = re.search(r'(\d)', text)
    return match.group(1) if match else '0'

def extract_last_number(text):
    match = re.search(r'(\d)', text[::-1])
    return match.group(1) if match else '0'

def extract_lines_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()  
    return lines


file_path = 'document.txt'  
lines = extract_lines_to_list(file_path)
Number_list=[]

for  line in lines:
    combined_number = int(extract_first_number(line) + extract_last_number(line))
    Number_list.append(combined_number)
    

Result = sum(Number_list)
print(f"Combined_number: {Result}")
