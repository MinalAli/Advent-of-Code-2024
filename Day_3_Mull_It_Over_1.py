import re

def calculate_sum_from_memory(memory):
    # Regex to find valid mul(X,Y) instructions
    pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    
    # Find all matches
    matches = re.findall(pattern, memory)
    
    # Compute the sum of results from valid mul instructions
    total = sum(int(x) * int(y) for x, y in matches)
    
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
        result = calculate_sum_from_memory(memory)
        
        # Print the result
        print(f"Sum of valid mul instructions: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
