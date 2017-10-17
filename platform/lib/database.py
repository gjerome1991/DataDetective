"""
Wrapper for PostgreSQL

Requires environmental variables be set:
    - DB_HOST
    - DB_USER
    - DB_PASSWORD
    - DB_NAME

"""
from sqlalchemy import create_engine
import psycopg2
import os


def cursor():
    """
    Returns a connection/cursor to the database
    """
    con = psycopg2.connect(host=os.environ['DB_HOST'],
                           user=os.environ['DB_USER'],
                           password=os.environ['DB_PASSWORD'],
                           database=os.environ['DB_NAME'])

    return con.cursor()

def query(sql):
    """
    Returns the results of the sql query
    """
    return cursor().execute(sql)

def get_measure_data(measure, year, month):
    """
    Returns the data for a given measure
    """
    # TODO:
    data = query("SELECT .... FROM data_points")
    ...
    return data
