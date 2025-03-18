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

    def save_sorted_data(self, sorted_df, filename="test_sorted_diabetes.csv"):
        sorted_df.to_csv(filename, index=False)
        print(f"Sorted data saved to \"{filename}\".")

class DiabetesData(SearchSortBase):
    def linear_search(self, column, target):
        for index, value in enumerate(self.df[column]):
            if value == float(target):
                return index
        return -1

    def binary_search(self, column, target):
        values = self.df[column].tolist()
        # sariling quicksort in binary search
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)

        sorted_values = quicksort(values)

        # Binary Search on sorted list
        low, high = 0, len(sorted_values) - 1
        # Attempt to convert target to the correct data type
        try:
            if pd.api.types.is_numeric_dtype(self.df[column]):
                target = float(target)
        except ValueError:
            print("Invalid target value. Please enter a valid number or string.")
            return -1

        while low <= high:
            mid = (low + high) // 2
            if sorted_values[mid] == target:
                for idx, val in enumerate(self.df[column]):
                    if val == target:
                        return idx
            elif sorted_values[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
#----Bubble-smallest & swaps, Selection-swaps adjacent, Insertion Sort-inserts in correct pos, and Quick Sort-recursively divides list---- 
    def bubble_sort(self, column): #like a bubble
        sorted_data = self.df.copy() #Make a copy of the dataset
        values = sorted_data[column].tolist() # Convert the column to a list
        start_time = time.time()

        n = len(values) # of elements length of list, outer loop runs n times
        for i in range(n):
            for j in range(0, n - i - 1): #largest unsorted number moves to the end & to ensure in-range index
                if values[j] > values[j + 1]: 
                    values[j], values[j + 1] = values[j + 1], values[j] #assigns the value of j+1 to values j 
        sorted_data[column] = values
        end_time = time.time()
        return sorted_data, end_time - start_time

    def selection_sort(self, column): #choose smallest and swap w/ first element, move 
        sorted_data = self.df.copy()
        values = sorted_data[column].tolist() #extract values from specified column 
        start_time = time.time()

        n = len(values) #tells how many numbers need to be sorted
        for i in range(n):
            min_idx = i #assumes first element is smallest
            for j in range(i + 1, n): #index 0 + 1, moved to n (end of list)
                if values[j] < values[min_idx]:
                    min_idx = j
            values[i], values[min_idx] = values[min_idx], values[i]     #Swaps the smallest value with the first unsorted element (i).
        sorted_data[column] = values     #updates the sorted values back into DF
        end_time = time.time()
        return sorted_data, end_time - start_time

    def insertion_sort(self, column):     #1st element-sorted section, pick next element and compare with sorted part, shift to right(largest)
        sorted_data = self.df.copy()
        values = sorted_data[column].tolist()
        start_time = time.time()

        for i in range(1, len(values)):  #Starts looping from the second element
            key = values[i]     #Stores the current value that needs to be inserted in the sorted section
            j = i - 1         #j is the index of the last sorted element before key.
            while j >= 0 and key < values[j]:     #Checks if key is smaller than the previous element (values[j])
                values[j + 1] = values[j]  
                j -= 1 #Moves to the left, continues checking til key is in position
            values[j + 1] = key     #places key in its correct position inside the sorted section.
        sorted_data[column] = values
        end_time = time.time()
        return sorted_data, end_time - start_time

    def quick_sort(self, column):
        sorted_data = self.df.copy()
        values = sorted_data[column].tolist()
        start_time = time.time()

        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quicksort(left) + middle + quicksort(right)

        sorted_values = quicksort(values)
        sorted_data[column] = sorted_values
        end_time = time.time()
        return sorted_data, end_time - start_time
        
#----Bubble, Selection, Insertion Sort, and Quick Sort---- 

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
        print(f"Linear Search: {'Found at row index ' + str(result) if result != -1 else 'Not Found'}")
        print(f"Time taken: {end_time - start_time:.6f}s")
    elif search_method == "2":
        print(f"\nSorting \"{column}\" column before Binary Search...")
        sorted_df, _ = diabetes.quick_sort(column)
        start_time = time.time()
        result = diabetes.binary_search(column, target)
        end_time = time.time()
        print(f"Binary Search: {'Found at row index ' + str(result) if result != -1 else 'Not Found'}")
        print(f"Time taken: {end_time - start_time:.6f}s")
    else:
        print("Invalid choice for search method.\n")
        return

    # User input fo the sorting part
    sort_column = input("\nChoose a column to sort (Glucose, Age, BMI, etc.): ")
    sort_algorithm = input("Choose sorting algorithm:\n1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Quick Sort\nEnter choice: \n")

    if sort_algorithm == "1":
        print(f"\nSorting by \"{sort_column}\" using Bubble Sort...")
        sorted_df, time_taken = diabetes.bubble_sort(sort_column)
    elif sort_algorithm == "2":
        print(f"\nSorting By \"{sort_column}\" using Selection Sort...")
        sorted_df, time_taken = diabetes.selection_sort(sort_column)
    elif sort_algorithm == "3":
        print(f"\nSorting by \"{sort_column}\" using Insertion Sort...")
        sorted_df, time_taken = diabetes.insertion_sort(sort_column)
    elif sort_algorithm == "4":
        print(f"\nSorting by \"{sort_column}\" using Quick Sort...")
        sorted_df, time_taken = diabetes.quick_sort(sort_column)
    else:
        print("Invalid choice.....")
        return

    print("Sorting completed...")
    diabetes.save_sorted_data(sorted_df)
    print(f"Time taken: {time_taken:.6f}s")

if __name__ == "__main__":
    main()
