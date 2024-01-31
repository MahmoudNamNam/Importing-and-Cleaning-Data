# Importing-and-Cleaning-Data
---




## Course-1: Introduction to Importing Data in Python


#### This is a common way to read the contents of a file in Python.
![image](https://github.com/MahmoudNamNam/Importing-and-Cleaning-Data/assets/148398760/31006863-79f1-455e-9616-30d780c659eb)

#### Another way by with
![image](https://github.com/MahmoudNamNam/Importing-and-Cleaning-Data/assets/148398760/c70673d2-f1f6-4bf8-8724-fa9c3ad93fec)


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
