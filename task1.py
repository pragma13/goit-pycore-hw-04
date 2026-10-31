#returns total and average salaries calculated from file data
def total_salary(path):

    try:
        with open(path, "r", encoding="utf-8") as f:
            line_count = 0
            total_salary_amount = 0
            current_line_number = 0

            for line in f:
                current_line_number += 1

                if not line.strip():
                    continue
                
                try:
                    _, salary = line.split(",")
                    total_salary_amount += int(salary)
                    line_count += 1
                except ValueError:
                    print(f"line {current_line_number} is corrupted, not included in calculation")

            if line_count == 0:
                print("file is either empty or data is corrupted")
                return 0, 0

            return total_salary_amount, total_salary_amount / line_count

    except FileNotFoundError:
        print(f"file {path} is not found")
        return 0, 0
    except PermissionError:
        print(f"no permission to read the file {path}")
        return 0, 0
    except UnicodeDecodeError:
        print("file couldn't be read in utf8")
        return 0, 0
    except IsADirectoryError:
        print(f"{path} is a directory")
        return 0, 0


   
   


total, average = total_salary("salaries.txt")
print(f"Total salary amount: {total}, average salary: {average}")
