import pandas as pd
import time

class SearchSortBase:
  def __init__(self, file_path="diabetes.csv"):
    self.file_path = file_path
    self.df = self.load_csv()

  def load_csv(self):
    try:
      df = pd.read_csv(self.file_path)
      print("Dataset loaded!!")
      return df
    except FileNotFoundError:
      print("Error: File not found.....")
      return None

  def save_sorted_data(self, sorted_df, filename="sorted_diabetes.csv"):
    sorted_df.to_csv(filename, index=False)
    print(f"Sorted data saved to \"{filename}\".")
      

#----Bubble, Selection, and Insertion Sort----
class DiabetesData(SearchSortBase):
  def bubble_sort(self, column):
    sorted_data = self.df.copy()
    values = sorted_data[column].tolist()
    start_time = time.time()

  n = len(values)
  for i in range (n):
    for j in range(0, n - i - 1):
      if values[j] > valurd[j + 1]:
        values[j], values[j+1] = values[j + 1], values[j]
  sorted_data[column] = values
  end_time = time.time()
  return sorted_data, end_time - start_time
