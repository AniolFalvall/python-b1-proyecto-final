from abc import ABC, abstractmethod
from .food_package import FoodPackage, Wrapping, Bottle, Glass, Box

class Product(ABC):
    """Abstract base class for all products."""
    def __init__(self,id:str,name:str,price:float):
      """Initialize product with id, name, and price."""
      self.id = id
      self.name = name
      self.price = price     
    
    def describe(self):
        """Return a string describing the product and its packaging."""
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self) -> str:
        """Return the product type."""
        pass
    
    @abstractmethod
    def foodPackage(self)-> FoodPackage:
        """Return the packaging associated with the product."""
        pass  

class Hamburger(Product):
    """Hamburger product, packaged with Wrapping."""
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)

    def type(self) -> str:
        return "Hamburger"
    
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
class Soda(Product):
    """Soda product, packaged in a Bottle."""
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)

    def type(self) -> str:
        return "Soda"
    
    def foodPackage(self) -> FoodPackage:
        return Bottle()

class Drink(Product):
    """Drink product, packaged in a Glass."""
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)

    def type(self) -> str:
        return "Drink"
    
    def foodPackage(self) -> FoodPackage:
        return Glass()

class HappyMeal(Product):
    """Drink product, packaged in a Glass."""
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)

    def type(self) -> str:
        return "HappyMeal"
    
    def foodPackage(self) -> FoodPackage:
        return Box()