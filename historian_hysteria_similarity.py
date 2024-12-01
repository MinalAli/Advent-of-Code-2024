from collections import Counter

def calculate_similarity_score(left, right):
    # Count occurrences of each number in the right list
    right_counts = Counter(right)
    
    # Calculate the similarity score
    similarity_score = sum(num * right_counts[num] for num in left)
    
    return similarity_score

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
    # Specify the input file path
    file_path = r"C:\Users\microsoft\Downloads\input.txt"  # Update this path if needed
    
    try:
        # Read the lists from the input file
        left, right = read_input(file_path)
        
        # Calculate the similarity score
        similarity_score = calculate_similarity_score(left, right)
        
        # Print the result
        print(f"Similarity Score: {similarity_score}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
