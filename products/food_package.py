from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    """Abstract base class for all types of food packaging."""
    @abstractmethod
    def pack(self) -> str:
        """Return the type of packaging."""
        pass

    @abstractmethod
    def material(self) -> str:
        """Return the material of the packaging."""
        pass

    def describe(self):
        """Return a descriptive string for the packaging."""
        return f"Packaging: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(FoodPackage):  
  """Food wrapped in paper (e.g., hamburger)."""
  def pack(self) -> str:
      return "Food Wrap Paper"
  
  def material(self) -> str:
      return "Aluminium"

class Bottle(FoodPackage): 
  """Beverage packaged in a bottle.""" 
  def pack(self) -> str:
      return "Bottle"
  
  def material(self) -> str:
      return "Plastic"
      
class Glass(FoodPackage):  
  """Beverage packaged in a glass."""
  def pack(self) -> str:
      return "Glass"
  
  def material(self) -> str:
      return "Carton"

class Box(FoodPackage): 
  """Meal packaged in a box (e.g., HappyMeal).""" 
  def pack(self) -> str:
      return "Box"
  
  def material(self) -> str:
      return "Cardboard"