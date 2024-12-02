def is_safe_report(report):
    # Calculate the differences between adjacent levels
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if differences are all positive (increasing) or all negative (decreasing)
    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    # A report is safe if it's either all increasing or all decreasing
    return increasing or decreasing

def count_safe_reports(file_path):
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Parse the report into a list of integers
            report = list(map(int, line.strip().split()))
            # Check if the report is safe and count it
            if is_safe_report(report):
                safe_count += 1
    return safe_count

def main():
    # Input file path
    file_path = r"C:\Users\microsoft\Downloads\input.txt"  # Adjust path if needed
    try:
        safe_reports = count_safe_reports(file_path)
        print(f"Number of Safe Reports: {safe_reports}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
