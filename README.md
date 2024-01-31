# Importing-and-Cleaning-Data
---




## Course-1: Introduction to Importing Data in Python
---


### Section-1



#### This is a common way to read the contents of a file in Python.
## Reading a Text File using Python

```python
filename = 'huck_finn.txt'

# Open the file in 'r' mode
file = open(filename, mode='r')  # 'r' is for reading

# Read the content of the file
text = file.read()

# Close the file
file.close()
````

#### Another way by with
## Reading a Text File using Python

```python
filename = 'huck_finn.txt'

# Open the file in 'r' mode using a 'with' statement
with open(filename, mode='r') as file:
    text = file.read()

# The file is automatically closed when the 'with' block is exited
````


1. **`with` statement:**
   - The `with` statement in Python is used to ensure that a block of code is executed with a particular context, and when the block is exited, a cleanup or resource release is performed.
   - In the case of working with files, the `with` statement is commonly used to open a file. It automatically takes care of closing the file when you are done with it.

2. **Opening a file using `with` statement:**
   - `with open(filename, mode='r') as file:`: This line opens the file specified by the `filename` in read mode (`'r'`). The file is assigned to the variable `file`.
   - The `with` statement ensures that the file is properly closed when the code block inside it is exited.

3. **Reading the file:**
   - `text = file.read()`: This line reads the entire content of the file and stores it in the variable `text`. The `read()` method is used for this purpose.

4. **Automatic closing of the file:**
   - As soon as the code block indented under the `with` statement is executed, the file is automatically closed. You don't need to explicitly call `file.close()`.

By using the `with` statement, you ensure that the file is closed properly, and it simplifies the code compared to manually managing the opening and closing of the file.
---


### section-2 The importance of flat files in data science

## Flat File:
Flat files refer to files that contain records with no structured relationships between the records and no structure for indexing, unlike a relational database. These files typically contain plain text and are used to store tabular data.

There are two common types of flat files:

1. **Text Files:**
   - **CSV (Comma-Separated Values):** In CSV files, each record is a separate line, and fields within the record are separated by commas. It's a widely used format for storing tabular data.
   Example:
   ```
   Name, Age, Occupation
   John, 25, Engineer
   Jane, 30, Scientist
   ```

   - **TSV (Tab-Separated Values):** Similar to CSV, but fields are separated by tabs.
   Example:
   ```
   Name    Age    Occupation
   John    25     Engineer
   Jane    30     Scientist
   ```

   - **Fixed-width Files:** In these files, each field has a fixed width, and data is aligned accordingly.
   Example:
   ```
   John 25 Engineer
   Jane 30 Scientist
   ```

2. **Binary Files:**
   - Binary flat files store data in a format that is not human-readable. They are more efficient for storing and retrieving data quickly, but they lack human readability.
   Examples: Database files, images, audio files, etc.

### Reading and Writing Flat Files in Python:

#### Reading CSV File:
```python
import csv

filename = 'data.csv'

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

#### Writing CSV File:
```python
import csv

filename = 'output.csv'

data = [
    ['Name', 'Age', 'Occupation'],
    ['John', 25, 'Engineer'],
    ['Jane', 30, 'Scientist']
]

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```
---


### Section-3 Importing flat files using NumPy


# Understanding the Power of NumPy for Data Import

## 1. Why NumPy?

NumPy, short for Numerical Python, is a powerful library in the Python ecosystem that provides support for large, multi-dimensional arrays and matrices, along with a variety of high-level mathematical functions to operate on these arrays. It is an essential tool for data manipulation and analysis, particularly in the fields of machine learning, data science, and scientific computing.

Key features of NumPy include:
- Efficient and fast array operations
- Broadcasting capabilities for element-wise operations
- Tools for integrating C/C++ and Fortran code
- Linear algebra and mathematical functions

## 2. Importing Flat Files using NumPy

When working with data stored in flat files (such as CSV files), NumPy provides convenient functions to import the data into arrays. One of the commonly used functions is `numpy.loadtxt()`. Let's take a look at a basic example:

```python
import numpy as np

# Specify the file path
filename = 'data.csv'

# Load data from the CSV file using NumPy
data = np.loadtxt(filename, delimiter=',')

# Print the loaded data
print(data)
This code snippet demonstrates how to import data from a CSV file using NumPy. The `delimiter=','` parameter specifies that the values in the file are separated by commas.

````
## 3. Customizing Your NumPy Import

NumPy provides additional parameters to customize the import process based on the specifics of your data. Let's explore some customization options:

```python
import numpy as np

# Specify the file path
filename = 'MNIST_header.txt'

# Load data from the CSV file using NumPy
# Skip the first row (header) and select only columns 0 and 2
data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0, 2], dtype=str)

# Print the loaded data
print(data)
```

In this example:
- `skiprows=1` skips the first row (header) of the file.
- `usecols=[0, 2]` specifies that only columns 0 and 2 will be loaded into the NumPy array.
- `dtype=str` ensures that the data is loaded as strings, which can be crucial when dealing with mixed data types in a column.

Customizing your NumPy import allows you to tailor the loading process to your specific needs, making it a versatile tool for handling diverse datasets.

In conclusion, NumPy plays a crucial role in efficiently importing and manipulating data, providing a solid foundation for various data-related tasks in the Python programming language.

### Import file using `np.recfromcsv()`



The `np.recfromcsv()` function in NumPy is specifically designed for structured or record arrays, where fields have names and data types. It is useful when dealing with CSV files containing heterogeneous data types and named columns. Here's an example of how you can use `np.recfromcsv()` to import data from a CSV file:

```python
import numpy as np

# Specify the file path
filename = 'data.csv'

# Load data from the CSV file using np.recfromcsv()
data = np.recfromcsv(filename, delimiter=',')

# Print the loaded data
print(data)
```

In this example:
- `np.recfromcsv()` reads the CSV file and automatically interprets the header to create a structured array with named fields.
- The `delimiter=','` parameter specifies that the values in the file are separated by commas.

If the CSV file has a header row, the function will use the header to name the fields. You can access the data using field names like you would with a dictionary:

```python
# Accessing data by field name
print(data['Name'])
print(data['Age'])
print(data['Occupation'])
```

This approach is particularly helpful when dealing with CSV files that contain different data types in different columns and when you want to work with named fields rather than numerical indices.
