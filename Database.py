# Using the database diagram below...write a query that will display the results below (Some columns mighjt be renamed but use the column names given)...
# it should only display 2020 data and order by driver points

import sqlite3

def get_driver_points(db_path):

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # sql query
    query = """
    SELECT *
    FROM races
    WHERE year = 2020
    ORDER BY driver_points;
    """
    
    try:
        # Execute the query
        cursor.execute(query)
        
        results = cursor.fetchall()
        
        for row in results:
            print(row)
    
    except sqlite3.Error as e:
        print("Error executing query:", e)
    
    finally:
        # Close the database connection
        conn.close()

get_driver_points('./drivers.db')

