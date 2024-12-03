import re

def calculate_sum_with_enable_disable(memory):
    # Regex patterns
    mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    control_pattern = r"(do\(\)|don't\(\))"

    # Initialize variables
    mul_enabled = True  # By default, mul instructions are enabled
    total = 0

    # Split memory into chunks to process sequentially
    tokens = re.findall(f"{mul_pattern}|{control_pattern}", memory)

    # Process each token
    for token in tokens:
        if token[0]:  # Match for mul(X,Y)
            if mul_enabled:
                x, y = int(token[0]), int(token[1])
                total += x * y
        elif token[2] == "do()":  # Enable future mul instructions
            mul_enabled = True
        elif token[2] == "don't()":  # Disable future mul instructions
            mul_enabled = False

    return total

def read_input(file_path):
    # Read the corrupted memory from the input file
    with open(file_path, 'r') as file:
        return file.read().strip()

def main():
    # Input file path
    file_path = r"C:\Users\microsoft\Downloads\input.txt"  # Adjust path if needed
    
    try:
        # Read the corrupted memory
        memory = read_input(file_path)
        
        # Calculate the total sum of valid mul instructions
        result = calculate_sum_with_enable_disable(memory)
        
        # Print the result
        print(f"Sum of enabled mul instructions: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
