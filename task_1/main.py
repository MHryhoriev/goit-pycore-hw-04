from processing_salary import total_salary

def main():
    total, average = total_salary("salary_file.txt")
    print(f"Total salary: {total}, Average salary: {average}")

if __name__ == "__main__":
    main()