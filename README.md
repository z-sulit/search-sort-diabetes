**Project Title:**
Search & Sort Algorithm Implementation (Diabetes Dataset)

**Description:** 
This Python program loads a diabetes dataset and allows the user to interactively search and sort data using classical algorithms. It includes Linear Search, Binary Search with Quick Sort, and three sorting algorithms: Bubble Sort, Selection Sort, Insertion Sort, and Quick Sort. The program compares the performance of each algorithm and saves the sorted results into a CSV file.


**Installation:**
You don't need to install time as time is already part of Python's built-in library.
To install Pandas, you need to go to your python command line and type

pip install pandas

**Usage:**
Go to your repository on GitHub.

Click the green Code button and select:

Open with Codespaces → New codespaces

GitHub will launch a VS Code-like environment in your browser.
In the left panel (Explorer), open your .ipynb file.
It will automatically open in Notebook mode (just like Jupyter).
At the top of the notebook, click “Run All” or run individual cells with ▶️.


**Sample Output:**

----> run the program via codespaces

Dataset loaded!!
Available columns:
['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
Choose a column to search (Glucose, Age, BMI, etc.): Age
Enter a value to search for: 30

Choose search method:
1. Linear Search
2. Binary Search
Enter choice: 2

Sorting "Age" column before Binary Search...
Binary Search: Found at row index 5
Time taken: 0.000361s

Choose a column to sort (Glucose, Age, BMI, etc.): BMI
Choose sorting algorithm:
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Quick Sort
Enter choice: 4

Sorting by "BMI" using Quick Sort...
Sorting completed.
Sorted data saved to "sorted_diabetes.csv".
Time taken: 0.001561s
