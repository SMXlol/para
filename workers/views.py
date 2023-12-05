from records import joke
name = str(input("Введите имя сотрудника: "))
surname = str(input("Введите фамилию сотрудника: "))
job_title = str(input("Введите должность сотрудника: "))
salary = str(input("Введите зарплату сотрудника: "))
age = str(input("Введите возраст сотрудника: "))
height = str(input("Введите рост сотрудника: "))
print(joke(name))