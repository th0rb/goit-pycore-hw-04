def total_salary(path: str):
    total_salary = 0
    average_salary = 0
    num_developers = 0
    try:
        with open(path, "r", encoding="UTF-8") as file_data:
            for line in file_data:
                _ , salary = line.strip().split(",")
                #we don't need developer name, so 1st argumend is trashed
                total_salary += int(salary)
                #convert to int to fix possible error in file
                num_developers += 1
                average_salary = total_salary / num_developers
                #recalculate average on the fly in case of exception
  
    except FileNotFoundError:
        print(f"File '{path}' not found!")

    except Exception as ex:
        print(f"An error occurred: {ex}")
    
    finally:
        return total_salary, average_salary
    

total, average = total_salary("data/salaries.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")   
