# Importing-and-Cleaning-Data
---




## Course-1: Introduction to Importing Data in Python


#### This is a common way to read the contents of a file in Python.
# Reading a Text File using Python

```python
filename = 'huck_finn.txt'

# Open the file in 'r' mode
file = open(filename, mode='r')  # 'r' is for reading

# Read the content of the file
text = file.read()

# Close the file
file.close()


#### Another way by with
# Reading a Text File using Python

```python
filename = 'huck_finn.txt'

# Open the file in 'r' mode using a 'with' statement
with open(filename, mode='r') as file:
    text = file.read()

# The file is automatically closed when the 'with' block is exited



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
