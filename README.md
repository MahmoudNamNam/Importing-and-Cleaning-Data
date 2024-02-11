# Course-1: Introduction to Importing Data in Python

## Reading a Text File using Python

```python
filename = 'huck_finn.txt'

# Open the file in 'r' mode
file = open(filename, mode='r')  # 'r' is for reading

# Read the content of the file
text = file.read()

# Close the file
file.close()
```

#### Another way by with

## Reading a Text File using Python

```python
filename = 'huck_finn.txt'

# Open the file in 'r' mode using a 'with' statement
with open(filename, mode='r') as file:
    text = file.read()

# The file is automatically closed when the 'with' block is exited
```

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

## By using the `with` statement, you ensure that the file is closed properly, and it simplifies the code compared to manually managing the opening and closing of the file.

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

- #### Reading CSV File:

```python
import csv

filename = 'data.csv'

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

- #### Writing CSV File:

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

## Understanding the Power of NumPy for Data Import

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

```

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

---

## Importing flat files using pandas

Pandas is a popular data manipulation library in Python, and it provides a convenient way to import and manipulate flat files, such as CSV files. The `pandas.read_csv()` function is commonly used for this purpose. Here's an example of how to import a flat file using pandas:

```python
import pandas as pd

# Specify the file path
filename = 'data.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(filename)

# Display the DataFrame
print(df)

# View the head of the DataFrame
print(df.head())
```

```python
# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array =data.values

```

In this example, `pd.read_csv()` reads the CSV file and creates a DataFrame, which is a two-dimensional labeled data structure with columns that can be of different data types. The resulting DataFrame (`df`) can be easily manipulated using various pandas functions.

If your flat file has a different delimiter or uses a different encoding, you can specify these options using additional parameters. For example:

```python
# Specify a different delimiter (e.g., tab-separated values)
df = pd.read_csv('data.tsv', delimiter='\t')

# Specify a different encoding (e.g., UTF-8)
df = pd.read_csv('data.csv', encoding='utf-8')
```

Pandas also provides functions for reading Excel files (`pd.read_excel()`), JSON files (`pd.read_json()`), and many other data formats.

Remember to install pandas before running the code if you haven't already:

```bash
pip install pandas
```

Pandas simplifies the process of working with tabular data and is widely used in data analysis and manipulation tasks.

Example:

```python
# Import pandas library
import pandas as pd

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
# Use sep='\t' for tab-separated values, comment='#' for lines starting with '#', and na_values='Nothing' for recognizing 'Nothing' as NA/NaN
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
```

In this code:

- `sep='\t'` specifies that the values in the file are tab-separated.
- `comment='#'` indicates that lines starting with '#' should be treated as comments and ignored.
- `na_values='Nothing'` specifies that the string 'Nothing' should be recognized as NA/NaN values.

This code reads the data from 'titanic_corrupt.txt' into a DataFrame, prints the first few rows of the DataFrame using `head()`, and then plots a histogram of the 'Age' variable using `matplotlib.pyplot`.

### Let's explore some additional aspects and functionalities related to importing flat files using Pandas:

### Handling Missing Values:

Sometimes, your flat file might contain missing or undefined values. Pandas provides options to handle such cases:

```python
# Specify custom missing values during import
missing_values = ['NA', 'None', '-']
df = pd.read_csv('data_with_missing.csv', na_values=missing_values)
```

### Skipping Rows:

You can skip a specific number of rows at the beginning of the file using the `skiprows` parameter:

```python
# Skip the first two rows
df = pd.read_csv('data.csv', skiprows=2)
```

### Specifying Column Names:

If your file doesn't have header information, or you want to provide custom column names, you can use the `names` parameter:

```python
# Specify custom column names
column_names = ['ID', 'Name', 'Age', 'Salary']
df = pd.read_csv('data_no_header.csv', names=column_names)
```

### Reading Specific Columns:

You can read only specific columns from the file by passing the `usecols` parameter:

```python
# Read only 'Name' and 'Salary' columns
df = pd.read_csv('data.csv', usecols=['Name', 'Salary'])
```

### Skipping Footer:

If your file has metadata or footer information that you want to skip, you can use the `skipfooter` parameter:

```python
# Skip the last three rows
df = pd.read_csv('data_with_footer.csv', skipfooter=3, engine='python')
```

### Reading Excel Files:

Pandas can also read Excel files using `pd.read_excel()`:

```python
# Read Excel file
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```

### Handling Date Formats:

If your flat file contains date columns, you can specify the date format for proper parsing:

```python
# Specify date format
df = pd.read_csv('data_with_dates.csv', parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
```

These additional features showcase the flexibility of Pandas in handling various scenarios while importing flat files. Depending on your specific requirements, you can customize the import process accordingly.

## Introduction to Other File Types

### Other file types

- Pickled files
- Excel spreadsheets
- MATLAB files
- SAS files
- Stata files
- HDF5 files

### Pickled Files in Python

#### What are Pickled Files?

Pickled files are a type of serialized data format native to Python. Serialization refers to the process of converting a Python object into a byte stream. Pickling is the term used for this process in Python.

#### Motivation for Pickled Files:

Pickling becomes particularly useful when dealing with complex data structures or objects that don't have an obvious and straightforward way to be stored in a text-based format like CSV or JSON. It allows you to serialize and store Python objects for later use.

#### Introduction to Importing Pickled Files:

To import pickled files in Python, you can use the `pickle` module. Here's a simple example:

```python
import pickle

# Open the pickled file for reading in binary mode ('rb')
with open('pickled_fruit.pkl', 'rb') as file:
    # Load the pickled data
    data = pickle.load(file)

# Print the loaded data
print(data)
```

In this example, the `open` function is used to open the pickled file in binary mode (`'rb'`), and `pickle.load()` is used to deserialize the data.

#### Example Pickled File Content:

Assuming the pickled file contains information about fruit quantities, the loaded data might look like this:

```python
{'peaches': 13, 'apples': 4, 'oranges': 11}
```

This represents a Python dictionary with fruit names as keys and corresponding quantities as values.

---

#### In addition to the commonly used flat files and pickled files, there are various other file types that you might encounter in data analysis and manipulation. Here's a brief introduction to some of them:

#### 1. Excel Spreadsheets:

Excel files are widely used for storing tabular data. Pandas provides a function `pd.read_excel()` to read data from Excel files. Similarly, you can use `pd.to_excel()` to write Pandas DataFrames to Excel.

```python
# Read Excel file
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Write DataFrame to Excel
df.to_excel('output.xlsx', index=False)
```

#### 2. MATLAB Files:

MATLAB files often have a `.mat` extension and can store matrices, arrays, and other MATLAB-specific data types. You can use the `scipy.io` module to read MATLAB files.

```python
from scipy.io import loadmat

# Load MATLAB file
mat_data = loadmat('data.mat')
```

#### 3. SAS Files:

SAS files are associated with the Statistical Analysis System. The `pandas` library provides a `read_sas()` function for reading SAS files.

```python
# Read SAS file
df_sas = pd.read_sas('data.sas7bdat')
```

#### 4. Stata Files:

Stata files have extensions like `.dta` and are common in the field of statistics. The `pandas` library supports Stata file reading with `read_stata()`.

```python
# Read Stata file
df_stata = pd.read_stata('data.dta')
```

#### 5. HDF5 Files:

HDF5 (Hierarchical Data Format version 5) files are designed to store and organize large amounts of data. The `h5py` library is commonly used to work with HDF5 files.

```python
import h5py

# Open HDF5 file
with h5py.File('data.h5', 'r') as file:
    # Access datasets
    dataset = file['dataset_name']
    # Do something with the dataset
```

---

## Introduction to Relational Databases

Relational databases are a structured way to organize and store data, and Python provides several libraries to interact with them. One of the most commonly used libraries is **SQLite**, which is a lightweight, serverless, and self-contained relational database engine. Additionally, the **SQLAlchemy** library is popular for working with various relational databases in a more abstracted and flexible manner.

#### **1. SQLite - A Simple Relational Database:**

**SQLite** is a C library that provides a lightweight disk-based database. Python comes with built-in support for SQLite through the `sqlite3` module. Here's a simple example of working with SQLite in Python:

```python
import sqlite3

# Connect to the SQLite database (creates a new one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SQL query to create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Insert data into the table
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('user-1', 'UserEmail@example.com'))

# Commit the changes and close the connection
conn.commit()
conn.close()
```

#### **2. SQLAlchemy - An ORM for Relational Databases:**

**SQLAlchemy** is a powerful and flexible Object-Relational Mapping (ORM) library that abstracts the interaction with relational databases. It provides a high-level, Pythonic interface for working with databases, allowing you to work with objects in a more intuitive way. Here's a basic example:

```python
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

# Create an SQLite database engine
engine = create_engine('sqlite:///example.db', echo=True)

# Define a Table and metadata
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, nullable=False),
    Column('email', String, nullable=False)
)

# Create the table in the database
metadata.create_all(engine)

# Insert data into the table
with engine.connect() as conn:
    conn.execute(users.insert().values(username='User', email='UserEmail@example.com'))
```

#### **3. Reading Data:**

After creating tables and inserting data, you can retrieve data using SQL queries or ORM queries, depending on the approach you choose:

- **SQLite (with `sqlite3`):**

  ```python
  conn = sqlite3.connect('example.db')
  cursor = conn.cursor()

  # Execute a SELECT query
  cursor.execute("SELECT * FROM users")
  rows = cursor.fetchall()

  for row in rows:
      print(row)

  conn.close()
  ```

#### another Example

```python
from sqlalchemy import create_engine, MetaData, text
import pandas as pd

# Create an SQLite database engine
engine = create_engine('sqlite:///DB/Chinook.sqlite')

# Connect to the database using a context manager
with engine.connect() as con:
    # Reflect metadata from the database
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Get the names of all tables in the database
    tables_names = metadata.tables.keys()
    print(tables_names)

    # Using pandas to fetch data from the 'Album' table
    query = text("SELECT * FROM Album")
    Album = pd.read_sql(query, con)

    # Using pandas to fetch data from the 'Artist' table
    query = text("SELECT * FROM Artist")
    Artist = pd.read_sql(query, con)

# Print the first few rows of the 'Album' table
print(Album.head())
print("\n")
# Print the first few rows of the 'Artist' table
print(Artist.head())
```

- **SQLAlchemy:**

  ```python
  from sqlalchemy import select

  # Use the select statement to retrieve data
  with engine.connect() as conn:
      result = conn.execute(select([users]))
      rows = result.fetchall()

  for row in rows:
      print(row)
  ```

# Course-2: Importing flat files from the web

## Importing Flat Files from the Web in Python

In Python, you can import and locally save datasets from the web using various libraries. Two commonly used libraries for this purpose are **urllib** and **requests**. Additionally, you can load datasets into Pandas DataFrames for easy manipulation and analysis.

#### 1. **Using `urllib` for HTTP Requests:**

The `urllib` module in Python provides functionality to make HTTP requests. Here's a simple example of downloading a file from the web:

```python
from urllib.request import urlretrieve

# URL of the dataset
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

# Local filename to save the data and Download the file
urlretrieve(url, 'winequality-white.csv')
```

#### how to make a simple GET request using the `urllib` library to retrieve the HTML content from the Wikipedia homepage. Here's a breakdown of the code:

```python
from urllib.request import urlopen, Request

# URL to make a GET request to
url = "https://www.wikipedia.org/"

# Create a Request object with the specified URL
request = Request(url)

# Open the URL using urlopen to get the response
response = urlopen(request)

# Read the HTML content from the response
html = response.read()

# Close the response object
response.close()
```

#### 2. **Using `requests` for HTTP Requests:**

The `requests` library is a popular and more user-friendly alternative for making HTTP requests:

```python
import requests

# URL of the dataset
url = "https://www.wikipedia.org/"

# Make a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a local file
    with open('local_data.csv', 'wb') as file:
        file.write(response.content)
```

#### 3. **Loading Datasets into Pandas DataFrames:**

Once the data is saved locally, you can use Pandas to load it into a DataFrame:

```python
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('local_data.csv')

# Now 'df' contains the data from the web in a DataFrame
print(df.head())
```
```python
# Import package
import pandas as pd
from urllib.request import urlretrieve

# Assign url of file: url
url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Download the file using urlretrieve
urlretrieve(url, 'latitude.xls')

# Read in all sheets of Excel file: xls
xls = pd.read_excel('latitude.xls', sheet_name=None)

# Print the sheet names to the shell
print("Sheet names:", list(xls.keys()))

# Print the head of the first sheet (using its name, NOT its index)
first_sheet_name = '1700'
print(f"\nHead of the sheet '{first_sheet_name}':")
print(xls[first_sheet_name].head())

```


#### 4. **Web Scraping with BeautifulSoup:**

If the data is embedded in HTML and not available as a downloadable file, you can use the `requests` library along with `BeautifulSoup` for web scraping:

```python
from bs4 import BeautifulSoup
import requests

# URL of the web page
url = 'https://www.crummy.com/software/BeautifulSoup/'

# Make a GET request
response = requests.get(url)

# Parse the HTML content
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

# Prettified Soup
print(soup.prettify())

# Extracting title
print("Title:", soup.title)

# Extracting text
print("Text:", soup.get_text())

# Extracting links
for link in soup.find_all('a'):
    print("Link:", link.get('href'))

```

#### 5. **Handling Authentication:**

If the web server requires authentication, you can provide credentials with `requests`:

```python
import requests
from requests.auth import HTTPBasicAuth

# URL of the dataset requiring authentication
url = 'https://example.com/data.csv'

# Provide authentication credentials
auth = HTTPBasicAuth('username', 'password')

# Make a GET request with authentication
response = requests.get(url, auth=auth)
```

## Introduction to APIs and JSONs

#### **APIs (Application Programming Interfaces):**

APIs define a set of rules and protocols that allow different software applications to communicate with each other. In the context of web development, APIs often enable interaction with external services or data sources. Python provides libraries such as `requests` to work with APIs.

#### **1. Making HTTP Requests:**

The `requests` library simplifies the process of making HTTP requests to APIs. Here's a simple example:

```python
import requests

# URL of the API endpoint
api_url = 'http://www.omdbapi.com/?t=hackers'

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()
    for key, value in json_data.items():
        print(f"{key}: {value}")
else:
    print(f"Error: {response.status_code}")
```

```python
import requests

# Assign the URL with query parameters
url = 'http://www.omdbapi.com/?apikey=72bc447a&'

# Send a GET request to the URL
response = requests.get(url)

# Print the text of the response
print(response.text)

# Import package
import requests

# Assign URL to variable: url
url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza"

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data

json_data = r.json()
# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

```

#### **2. Working with JSON Data:**

APIs often return data in JSON (JavaScript Object Notation) format. Python has a built-in module called `json` for working with JSON data:

```python
import json

# Sample JSON data
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string to Python dictionary
python_data = json.loads(json_data)

# Convert Python dictionary to JSON string
new_json_data = json.dumps(python_data, indent=2)

print(python_data)
print(new_json_data)
```

```python
import json

# Open the JSON file for reading
with open('snakes.json', 'r') as json_file:
    # Load the JSON data from the file
    json_data = json.load(json_file)

# Iterate through the key-value pairs in the JSON data
for key, value in json_data.items():
    # Print the key and its corresponding value
    print(key + ':', value)


```

#### **3. Handling Authentication:**

If an API requires authentication, you can include credentials in the request headers:

```python
import requests

api_url = 'https://api.example.com/data'
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

#### **4. Making POST Requests:**

In addition to GET requests, you might need to make POST requests to send data to the API:

```python
import requests

api_url = 'https://api.example.com/data'
data_to_send = {'key1': 'value1', 'key2': 'value2'}

response = requests.post(api_url, data=data_to_send)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

#### **5. Using APIs with Python Libraries:**

Certain Python libraries provide convenient ways to work with specific APIs. For example, the `Tweepy` library simplifies interactions with the Twitter API, and the `praw` library is designed for the Reddit API.

```python
import tweepy
import json

# Replace the placeholders with your Twitter API credentials
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"

# Create an OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Set the access token and access token secret
auth.set_access_token(access_token, access_token_secret)
```
