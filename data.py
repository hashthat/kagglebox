#!/usr/bin/env python3
import csv
import random
import os

# ==============================
# Step 1: Generate a Large Dataset (CSV File)
# ==============================

def generate_large_dataset(filename="students.csv", num_records=10000):
    """Generate a CSV file with random student data."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["ID", "Name", "Grade", "Attendance"])

        # Generate random student data
        for i in range(1, num_records + 1):
            student_id = i
            student_name = f"Student_{i}"
            grade = random.randint(50, 100)  # Grades between 50 and 100
            attendance = random.choice(["Present", "Absent"])
            writer.writerow([student_id, student_name, grade, attendance])

    print(f"Dataset '{filename}' with {num_records} records generated successfully.")

# ==============================
# Step 2: Read and Parse the CSV File
# ==============================

def read_dataset(filename="students.csv"):
    """Read the dataset from the CSV file."""
    if not os.path.exists(filename):
        print(f"Error: '{filename}' does not exist.")
        return []

    data = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            student_id = int(row[0])
            student_name = row[1]
            grade = int(row[2])
            attendance = row[3]
            data.append({
                "ID": student_id,
                "Name": student_name,
                "Grade": grade,
                "Attendance": attendance
            })
    return data

# ==============================
# Step 3: Format and Display the Data
# ==============================

def display_summary(data):
    """Display a summary of the dataset."""
    total_students = len(data)
    top_students = [student for student in data if student["Grade"] > 85]
    present_students = [student for student in data if student["Attendance"] == "Present"]

    print("\n--- Student Records Summary ---")
    print(f"Total Students: {total_students}")
    print(f"Top Performers (Grade > 85): {len(top_students)}")
    print(f"Students Present Today: {len(present_students)}")
    print("\nSample Data:")
    print(f"{'ID':<5} {'Name':<20} {'Grade':<10} {'Attendance':<10}")
    print("-" * 50)
    for student in data[:10]:  # Display only the first 10 records
        print(f"{student['ID']:<5} {student['Name']:<20} {student['Grade']:<10} {student['Attendance']:<10}")

def filter_top_students(data):
    """Display students with grades above a certain threshold."""
    top_students = [student for student in data if student["Grade"] > 85]
    print("\n--- Top Performers (Grade > 85) ---")
    print(f"{'ID':<5} {'Name':<20} {'Grade':<10} {'Attendance':<10}")
    print("-" * 50)
    for student in top_students:
        print(f"{student['ID']:<5} {student['Name']:<20} {student['Grade']:<10} {student['Attendance']:<10}")

# ==============================
# Step 4: User Interaction
# ==============================

def main():
    filename = "students.csv"

    print("Welcome to the Student Records Manager!")
    print("1. Generate Large Dataset")
    print("2. Load and Display Dataset")
    print("3. Display Top Performers")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice: ")
        if choice == '1':
            num_records = int(input("Enter the number of records to generate: "))
            generate_large_dataset(filename, num_records)
        elif choice == '2':
            data = read_dataset(filename)
            if data:
                display_summary(data)
        elif choice == '3':
            data = read_dataset(filename)
            if data:
                filter_top_students(data)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

