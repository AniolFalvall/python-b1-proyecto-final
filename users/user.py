from abc import ABC, abstractmethod

class User(ABC):
  """Abstract base class for all users (Cashier and Customer)."""
  def __init__(self,dni:str,name:str,age:int):
    """Initialize a user with DNI, name, and age."""
    self.dni = dni
    self.name = name
    self.age = age    
   
  @abstractmethod
  def describe(self):
      """Return a string describing the user."""
      pass

class Cashier(User):
  """Cashier user with timetable and salary."""
  def __init__(self,dni:str,name:str,age:int,timeTable:str,salary:float):
    """Initialize cashier with timetable and salary."""
    super().__init__(dni, name, age)
    self.timeTable = timeTable
    self.salary = salary

  def describe(self):
        """Return a descriptive string for the cashier."""
        return f"Cashier - Name: {self.name}, DNI: {self.dni} , Timetable: {self.timeTable}, Salary: {self.salary}."

class Customer(User):
  """Customer user with email and postal code."""
  def __init__(self,dni:str,name:str,age:int,email:str,postalCode:str):
    """Initialize customer with email and postal code."""
    super().__init__(dni, name, age)
    self.email = email
    self.postalCode = postalCode

  def describe(self):
        """Return a descriptive string for the customer."""
        return f"Customer - Name: {self.name}, DNI: {self.dni} , Age: {self.age}, Email: {self.email}, Postal Code: {self.postalCode}"