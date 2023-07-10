import mysql.connector
import sys

uname = sys.argv[1]
upass = sys.argv[2]
email = sys.argv[3]

def add_data_to_database(data):
    try:
        # Establish a connection to the MySQL server
        cnx = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='login_system'
        )
        
        # Create a cursor object to execute SQL queries
        cursor = cnx.cursor()

        # Insert data into the database
        query = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"
        values = (data['value1'], data['value2'], data['value3'])
        cursor.execute(query, values)

        # Commit the changes to the database
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        print("Success")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

# Example data to add to the database
data_to_insert = {
    'value1': uname,
    'value2': upass,
    'value3': email
}

# Call the function to add data to the database
add_data_to_database(data_to_insert)
