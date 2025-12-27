import pandas as pd
class CSVFileManager:
  """Class to manage reading and writing CSV files."""
  def __init__(self,path: str):
    """Initialize with the path to the CSV file."""
    self.path = path

  def read(self) -> pd.DataFrame:
    """Read CSV file and return as a pandas DataFrame."""
    return pd.read_csv(self.path) 
   
  def write(self,dataFrame: pd.DataFrame):
    """Write a pandas DataFrame to the CSV file."""
    dataFrame.to_csv(self.path, index=False)