class Employee:
    
    def __init__(self, salary: int) -> None:
        self.salary = salary
        
    def give_raise(self, amount=None) -> int:
        if amount:
            new_salary = self.salary + amount
            
        else:
            new_salary = self.salary + 5000
            
        return new_salary