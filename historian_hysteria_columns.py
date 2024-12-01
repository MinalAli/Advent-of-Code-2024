# historian_hysteria_columns.py
def calculate_total_distance(left, right):
    # Sort both lists
    left.sort()
    right.sort()
    
    # Calculate the total distance by pairing sorted values
    total_distance = sum(abs(a - b) for a, b in zip(left, right))
    return total_distance

def read_input(file_path):
    # Read the input file and parse the two columns
    left = []
    right = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into two numbers (left and right columns)
            values = line.strip().split()
            if len(values) == 2:
                left.append(int(values[0]))
                right.append(int(values[1]))
    
    return left, right

def main():
    # Specify the input file
    file_path = "C:\\Users\\microsoft\\Downloads\\input.txt"  # Update the file path to your uploaded file
    
    try:
        # Read the lists from the input file
        left, right = read_input(file_path)
        
        # Calculate the total distance
        total_distance = calculate_total_distance(left, right)
        
        # Print the result
        print(f"Total Distance: {total_distance}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
