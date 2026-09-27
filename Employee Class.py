class Employee:  # created class 
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.salary = Employee._base_salaries[level]

    def __str__(self):
        return f'{self.name}: {self.level}'

    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    @property  # getter created for name 
    def name(self):
        return self._name

    @name.setter # setter created for name 
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    @property  # getter created for level 
    def level(self):
        return self._level

    @level.setter  # setter created for level 
    def level(self, new_level):
        if not isinstance(new_level, str):   # raised TypeError as new_level must be string
            raise TypeError("'level' must be a string.")
        if new_level not in Employee._base_salaries:   # raise ValueError as new_level doesn't exist in employee base salary
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if hasattr(self, '_level') and new_level == self.level:  # raised ValueError if the new level already exists in the current level and period
            raise ValueError(f"'{self.level}' is already the selected level.")
        if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:  # raised VlaueError if the new base salary is less than current level means can't change to lower level
            raise ValueError("Cannot change to lower level.")
        print(f"'{self.name}' promoted to '{new_level}'.")
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level

    @property  # created getter for salary by using property decorator 
    def salary(self):
        return self._salary

    @salary.setter  #  created setter for salary 
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):  # raised TypeError if the new_salary isn't a number 
            raise TypeError("'salary' must be a number.")
        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:   # raised ValueError when the new salary less than minimum base salary
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')

charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.level = 'junior'
