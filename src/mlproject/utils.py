import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
import psycopg2
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get database credentials from environment variables
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")




def read_sql_data():
    logging.info("Reading sql data started...")
    try:
        # Establish a database connectioncle
        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )
        logging.info("Connection established",connection)
        
        cursor = connection.cursor()
        sql_query = 'select * from students;'
        # Execute the query
        cursor.execute(sql_query)
        df = pd.read_sql_query(sql_query,connection)
        return df
        # Execute SQL queries or other database operations here

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)

    finally:
        if connection:
            connection.commit()
            cursor.close()
            connection.close()
    