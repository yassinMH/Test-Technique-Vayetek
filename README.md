# Test-Technique-Vayetek
Test Technique Vayetek Pour Yassine Mahfoudh
# Extract and Combine Numbers from Text File

This Python script reads a text file, extracts the first digit of the first number and the last digit from each line, combines them into a single number, and then calculates the sum of these combined numbers.

## Requirements

- Python 3.x
- No additional Python libraries are required, other than the built-in `re` module.

## Functions

### `extract_first_number(text)`
This function extracts the **first digit** from the first number found in a given string.

#### Parameters:
- `text` (str): The string from which the first digit will be extracted.

#### Returns:
- The first digit as a string if found, otherwise `'0'`.

### `extract_last_number(text)`
This function extracts the **last digit** from the given string.

#### Parameters:
- `text` (str): The string from which the last digit will be extracted.

#### Returns:
- The last digit as a string if found, otherwise `'0'`.

### `extract_lines_to_list(file_path)`
This function reads a file and returns all its lines as a list of strings.

#### Parameters:
- `file_path` (str): The path to the text file.

#### Returns:
- A list of strings, where each string is a line from the file.

## Script Workflow

1. **Read the file**: The script reads the file located at `'document.txt'` and splits its contents into lines.
2. **Extract and combine digits**: For each line:
   - The script extracts the **first digit** of the first number (`extract_first_number`).
   - It also extracts the **last digit** of the line (`extract_last_number`).
   - It then combines these two digits into a single number.
3. **Sum the combined numbers**: The combined numbers from all lines are added together.
4. **Display the result**: The total sum is displayed as `Combined_number: <result>`.



