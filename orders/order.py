from users.user import User, Cashier, Customer
from products.product import Product, Hamburger, Soda, Drink, HappyMeal

class Order:
  """Class representing a customer's order."""
  def __init__(self, cashier:Cashier, customer:Customer):
    """Initialize order with a cashier, a customer, and an empty product list."""
    self.cashier = cashier
    self.customer = customer
    self.products = []

  def add(self, product : Product):
    """Add a product to the order."""
    self.products.append(product)

  def calculateTotal(self) -> float:
    """Calculate and return the total price of all products in the order."""
    return sum(product.price for product in self.products)
  
  def show(self):    
    """Print the details of the order, including customer, cashier, products and total."""
    print("Hello : "+self.customer.describe())
    print("Was attended by : "+self.cashier.describe())
    for product in self.products:
      print(product.describe())
    print(f"Total price : {self.calculateTotal()}")
