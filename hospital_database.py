#-----------------------------------------------------------
# Here is a brief example how you create a hospital database
# using python & the sqlite library.
#------------------------------------------------------------

import sqlite3


# Connect tot the database
connection = sqlite3.connect('hospital.db')

# Create a cursor object 
cursor = connection.cursor()

# Create the patients table
# cursor.execute('''CREATE TABLE patients(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Commit the transaction
connection.commit()

# Insert some data
cursor.execute("INSERT INTO patients(name, age) VALUES(?,?)", ('Lebo', 40))
cursor.execute("INSERT INTO patients(name, age) VALUES(?,?)", ('Kagiso', 35))

# Commit the transaction
connection.commit()

# Close the connection
connection.close()


