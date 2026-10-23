class Employee:
    
    def __init__(self,name, salary) -> None:
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            print("Error: Salary cannot be negative!")
        else:
            self.__salary = new_salary

    @salary.deleter
    def salary(self):
        print("Salary deleted. ")
        del self.__salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


    def get_info(self):
        print(f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}")


mgr = Manager("Nika", 3500, "IT")
mgr.get_info()

try:
    print(mgr.__salary)
except AttributeError as e:
    print("\n Verification successful: Direct access to __salary raises an AttributError")