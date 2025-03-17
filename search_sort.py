import pandas as pd

#----Bubble, Selection, and Insertion Sort----

def bubble_sort(self, column):
  sorted_data = self.df.copy()
  values = sorted_data[column].tolist()
  start_time = time.time()

n = len(alues)
for i in range (n):
  for j in range(0, n - i - 1):
    if values[j] > valurd[j + 1]:
      values[j], values[j+1] = values[j + 1], values[j]
sorted_data[column] = values
end_time = time.time()
return sorted_data, end_time - start_time
