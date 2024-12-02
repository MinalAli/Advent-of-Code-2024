def is_safe_report(report):
    """
    Check if a report is safe under the original rules.
    """
    # Calculate the differences between adjacent levels
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if differences are all positive (increasing) or all negative (decreasing)
    increasing = all(1 <= diff <= 3 for diff in differences)
    decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    # A report is safe if it's either all increasing or all decreasing
    return increasing or decreasing

def is_safe_with_dampener(report):
    """
    Check if a report can become safe by removing a single level.
    """
    n = len(report)
    for i in range(n):
        # Create a new report by skipping the i-th level
        modified_report = report[:i] + report[i+1:]
        # Check if the modified report is safe
        if is_safe_report(modified_report):
            return True
    return False

def count_safe_reports_with_dampener(file_path):
    """
    Count the number of safe reports considering the Problem Dampener.
    """
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Parse the report into a list of integers
            report = list(map(int, line.strip().split()))
            # Check if the report is safe directly or with the Problem Dampener
            if is_safe_report(report) or is_safe_with_dampener(report):
                safe_count += 1
    return safe_count

def main():
    # Input file path
    file_path = r"C:\Users\microsoft\Downloads\input.txt"  # Adjust path if needed
    
    try:
        # Count safe reports with the Problem Dampener
        safe_reports = count_safe_reports_with_dampener(file_path)
        print(f"Number of Safe Reports (with Dampener): {safe_reports}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
