class Person():
    def __init__(self, fN, lN, age):
        self.firstName = fN
        self.lastName = lN
        self.age = age
        self.email = f"{fN.lower()}.{lN.lower()}@email.com"


    def fullName(self):
        return f"{self.firstName} {self.lastName}"


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
        else: return


    def remove_employee(self, emp):
        if emp in self.employees: self.employees.remove(emp)
        


emp1 = Employee("Employee","number1",16,1500)
mng1 = Manager("Manager","number1",18,1600,emp1)
