from abc import ABC, abstractmethod
from users.user import Cashier, Customer
from products.product import Hamburger, Soda, Drink, HappyMeal

class Converter(ABC):
  """Abstract base class to convert a DataFrame to a list of objects."""
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      """Convert DataFrame rows to a list of objects."""
      pass  
  
  def print(self, objects):
    """Print the description of each object in the list."""
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  """Convert DataFrame rows into Cashier objects."""
  def convert(self,dataFrame) -> list:    
    cashiers = []
    for _, row in dataFrame.iterrows():
        cashier = Cashier(
            dni=row['dni'],
            name=row['name'],
            age=int(row['age']),
            timeTable=row['timetable'],
            salary=float(row['salary'])
        )
        cashiers.append(cashier)
    return cashiers      

class CustomerConverter(Converter):
  """Convert DataFrame rows into Customer objects."""
  def convert(self, dataFrame) -> list:
      customers = []
      for _, row in dataFrame.iterrows():
          customer = Customer(
              dni=row['dni'],
              name=row['name'],
              age=int(row['age']),
              email=row['email'],
              postalCode=row['postalCode']
          )
          customers.append(customer)
      return customers

class ProductConverter(Converter):
  """Convert DataFrame rows into Product objects (Hamburger, Soda, Drink, HappyMeal)."""
  def convert(self, dataFrame, product_type) -> list:
      products = []
      for _, row in dataFrame.iterrows():
          # Determine product class based on product_type
          if product_type == 'Hamburger':
              product = Hamburger(id=row['id'], name=row['name'], price=float(row['price']))
          elif product_type == 'Soda':
              product = Soda(id=row['id'], name=row['name'], price=float(row['price']))
          elif product_type == 'Drink':
              product = Drink(id=row['id'], name=row['name'], price=float(row['price']))
          elif product_type == 'HappyMeal':
              product = HappyMeal(id=row['id'], name=row['name'], price=float(row['price']))
          else:
              continue
          products.append(product)
      return products