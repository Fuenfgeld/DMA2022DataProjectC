import sqlite3
from sqlite3 import Error
import csv
import os

def connect_to_db(logger, db_file):
    if os.path.isfile(db_file):
        os.remove(db_file)

    sqlite3_conn = None

    try:
        sqlite3_conn = sqlite3.connect(db_file)

    except Error as err:
        logger.logError("Could not open db", err)
        if sqlite3_conn is not None:
            sqlite3_conn.close()
    
    cursor = sqlite3_conn.cursor()
    cursor.executescript('''DROP TABLE IF EXISTS patients;
                            DROP TABLE IF EXISTS conditions;
                            DROP TABLE IF EXISTS observations;''')
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS patients (
        Id STRING PRIMARY KEY,
        BIRTHDATE DATE,
        DEATHDATE DATE,
        SSN STRING,
        DRIVERS STRING,
        PASSPORT STRING,
        PREFIX STRING,
        FIRST STRING,
        LAST STRING,
        SUFFIX STRING,
        MAIDEN STRING,
        MARITAL STRING,
        RACE STRING,
        ETHNICITY STRING,
        GENDER STRING,
        BIRTHPLACE STRING,
        ADDRESS STRING,
        CITY STRING,
        STATE STRING,
        COUNTRY STRING,
        ZIP STRING,
        LAT INTEGER,
        LON INTEGER,
        HEALTHCARE_EXPENSES INTEGER,
        HEALTHCARE_COVERAGE INTEGER
    );
    CREATE TABLE IF NOT EXISTS conditions (
        START DATE,
        STOP DATE,
        PATIENT STRING,
        ENCOUNTER STRING,
        CODE STRING,
        DESCRIPTION STRING,
        FOREIGN KEY (PATIENT)
            REFERENCES patients (Id) 
        FOREIGN KEY (Encounter)
            REFERENCES encounters (Id) 

    );
    CREATE TABLE IF NOT EXISTS observations (
        DATE DATE,
        PATIENT STRING,
        ENCOUNTER STRING,
        OBSERVATION_TYPE STRING,
        CODE STRING,
        DESCRIPTION STRING,
        VALUE STRING,
        UNITS STRING,
        TYPE STRING,
        FOREIGN KEY (PATIENT)
            REFERENCES patients (Id) 
        FOREIGN KEY (Encounter)
            REFERENCES encounters (Id) 

    )
    ''')
    sqlite3_conn.commit()

    return sqlite3_conn

def insert_values_to_table(logger, cursor, table_name, csv_file_path):

    """
    Open a csv file, store its content in a list excluding header and insert the data from the list to db table
    :param table_name: table name in the database to insert the data into
    :param csv_file_path: path of the csv file to process
    :return: None
    """

    logger.log("???? Extracting data from " + csv_file_path)
    #cursor.execute("DELETE FROM " + table_name)

    # Read CSV file content
    values_to_insert = open_csv_file(csv_file_path)

    # Insert to table
    if len(values_to_insert) > 0:
        column_names, column_numbers = get_column_names_from_db_table(cursor, table_name)

        values_str = '?,' * column_numbers
        values_str = values_str[:-1]

        sql_query = 'INSERT INTO {}({}) VALUES ({})'.format(
            table_name,
            column_names,
            values_str
        )

        cursor.executemany(sql_query, values_to_insert)
    else:
        logger.log('Nothing to insert')


def open_csv_file(csv_file_path):
    """
    Open and read data from a csv file without headers (skipping the first row)
    :param csv_file_path: path of the csv file to process
    :return: a list with the csv content
    """
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        data = list()
        for row in reader:
            data.append(row)

        return data

def get_column_names_from_db_table(sql_cursor, table_name):
    """
    Scrape the column names from a database table to a list and convert to a comma separated string, count the number
    of columns in a database table
    :param sql_cursor: sqlite cursor
    :param table_name: table name to get the column names from
    :return: a comma separated string with column names, an integer with number of columns
    """

    table_column_names = 'PRAGMA table_info(' + table_name + ');'
    sql_cursor.execute(table_column_names)
    table_column_names = sql_cursor.fetchall()

    column_count = len(table_column_names)

    column_names = list()

    for name in table_column_names:
        column_names.append(name[1])

    return ', '.join(column_names), column_count
