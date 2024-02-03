from sqlalchemy import create_engine, MetaData, text
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')

with engine.connect() as con:
    metadata = MetaData()
    metadata.reflect(bind=engine)

    tables_names = metadata.tables.keys()
    print(tables_names)

    # Using pandas to fetch data
    query = text("SELECT * FROM Employee")
    employees = pd.read_sql(query, con)

print(employees.head())
