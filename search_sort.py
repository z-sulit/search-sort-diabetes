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

  def selection_sort(self, column):
    sorted_data = self.df.copy()
    values = sorted_data[column].tolist()
    start_time = time.time()

    n = len(values_
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
          if values[j] < values[min_idx]:
            min_idx = j 
        values[i], values[min_idx] = values[min_idx], values[i]
    sorted_data[column] = values
    end_time = time.time()
    return sorted_data, end_time - start_time

  def insertion_sort(self, column):
    sorted_data = self.df.copy()
    values = sorted_data[column].tolist()
    start_time = time.time()

    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
          values[j + 1] = values[j]
          j -= 1
        values[j + 1] = key
    sorted_data[column] = values
    end_time = time.time()
    return sorted_data, end_time - start_time

  def quick_sort(self, column):
    sorted_data = self.df.copy()
    values = sorted_data[column].tolist()
    start_time = time.time()

    def quicksort(arr):
      if len(arr) <=1:
        return arr
      pivot = arr[len(arr) // 2]
      left = [x for x in arr if x < pivot]
      middle = [x for x in arr if x == pivot]
      right = [x for x in arr if x > pivot]
      return quicksort(left) + middle + quicksort(right)

    sorted_vallues = quicksort(values)
    sorted_data[column] = sorted_values
    end_timme = time.time()
    return sorted_data, end_time - start_time

def main():
  diabetes = DiabetesData()

  # Display available columns
  print("Available columns:")
  print(diabetes.df.columns.tolist())

  # User input for column and target
  column = input("Choose a column to search (Glucose, Age. BMI, etc.): ")
  target = input("Enter a value to search for: ")

  # Choose search method
  search_method = input("\nChoose search method:\n1. Linear Search\n2. Binary Search\nEnter choice: ")
  if search_method == "1":
    start_time = time.time()
    result = diabetes.linear_search(column, target)
    end_time = time.time()
    print(f"Linear Search: {'Found at row index' + str(result) if result != -1 else 'Not Found'}")
    print(f"Time taken: {end-time - start_time:.6f}s")
  elif search_method == "2":
    print(f"\nSorting \"{column}\" column before Binary Search...")
    sorted_df, _ = diabetes.quick_sort(column)
    start_time = time.time()
    result = diabetes.binary_search(column, target)
    end_time = time.time()
    print(f"Binary Search: {'Found at row index' + srt(result if result != -1 else 'Not Found'}")
    print(f"Time taken: {end_time - start_time:.6f}s")
  else:
    print("Invalid choice for search method.\n")

  # User input fo the sorting part
  sort_column = input("\nChoose a column to sort (Glucose, Age, BMI, etc.): ")
  sort_algorithm = input("Choose sorting algorithm:\n1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Quick Sort\nEnter choice: \n")

  if sort_algorithm == "1":
    print(f"\nSorting by \"{sort_column}\" using Bubble Sort...")
    sorted_df, time_taken = diabetes.bubble_sort(sort_column)
  elif sort_algorithm == "2":
    print(f"\\Sorting By \"{sort_column}\" using Selection Sort...")
    sorted_df, time_taken = diabetes.selection_sort(sort_column)
  elif sort_algorithm == "3":
    print(f"\nSorting by \"{sort_column}\" using Insertion Sort...")
    sorted_df, time_taken = diabetes.insertion_sort(sort_column)
  elif  sort_algorithm == "4":
    print(f"\nSorting by \"{sort_column}\" using Quick Sort...")
    sorted_df, time_taken = diabetes.quick_sort(sort_column)

  else:
    print("Invalid choice.....")
    return

  pritn("Sorting completed...")
  diabetes.save_sorted_data(sorted_df)
  print(f"Time taken: {time_taken:.6f}s")

if __name__ == "__main__":
  main()
  
