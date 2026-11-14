import csv

def main():
    input_file = 'attendance.txt'
    output_file = 'attendance_clean.csv'
    
    try:
        # Read student names from the input file
        with open(input_file, mode='r') as file:
            raw_names = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found. Please create it first.")
        return

    original_count = len(raw_names)
    
    # Clean names using strip() and title()
    cleaned_names = [name.strip().title() for name in raw_names if name.strip()]
    
    # remove duplicates
    unique_names_set = set(cleaned_names)
    unique_count = len(unique_names_set)
    
    # sort alphabetically
    sorted_attendance = sorted(list(unique_names_set))
    
    # made csv or save to csv file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Student Name"])  # Header
        for name in sorted_attendance:
            writer.writerow([name])
            
    print("--- Attendance Cleaner Report ---")
    print(f"Original Records Count: {original_count}")
    print(f"Unique Students Count: {unique_count}")
    print(f"\n--- Cleaned & Sorted Attendance List ---")
    
    for name in sorted_attendance:
        print(name)
        
    print(f"\nData successfully saved to '{output_file}'.")

if __name__ == "__main__":
    main()
