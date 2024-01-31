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


### section-2


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
   Example: Database files, images, audio files, etc.

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

These are basic examples, and there are more advanced libraries and methods for working with flat files, such as using `pandas` for more complex data manipulation.


