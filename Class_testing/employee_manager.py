class Person():    
    def __init__(self, fN, lN, age = 0):
        self.firstName = fN
        self.lastName = lN
        self.age = age


    def getFullName(self):
        return f"{self.firstName} {self.lastName}"


    def getEmail(self):
        return f"{self.firstName.lower()}.{self.lastName.lower()}@email.com"


    def alterAge(self, age) -> int:
        self.age = age


    def alterEmail(self, email) -> str:
        self.email = email


class Employee(Person):
    def __init__(self, fN, lN, age, wage):
        super().__init__(fN, lN, age)
        self.wage = wage


class Manager(Employee):
    def __init__(self, fN, lN, age, wage, emp = None):
        super().__init__(fN, lN, age, wage)
        if not emp: self.employees = []
        else: self.employees = emp


    def add_employee(self, emp):
        if emp not in self.employees: self.employees.append(emp)        


    def remove_employee(self, emp):
        if emp in self.employees: self.employees.remove(emp)


    def list_employees(self):
        for emp in self.employees: print(emp.getFullName())
        

emp1 = Employee("Employee","number1",16,1500)
emp2 = Employee("Employee","number2",18,1700)
mng1 = Manager("Manager","number1",30,3000)

# Adding employees to test the method: add_employee()
mng1.add_employee(emp1)
mng1.add_employee(emp2)

# Removing employees to test the method: remove_employee()
mng1.remove_employee(emp1)
mng1.remove_employee(emp2)

mng1.list_employees()
