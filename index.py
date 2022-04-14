import sqlite3
import os
import matplotlib.pyplot as plt 
import matplotlib.ticker as plticker
import numpy as np
import unittest
import json
from numpy.core.fromnumeric import size
import requests
import pandas as pd

## Team Name: The Yelpers 
## Team Members: Tarush Nandrajog, Jenya Patel

# Incomplete need to scrape data
def readDataFromFile(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)
    return json_data

# Create project database
def setUpDatabase(db_name):
    # Takes in database name (string) as input. Returns database cursor and connection as outputs.
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def setUpYelpTable(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Types (Restaurant TEXT UNIQUE PRIMARY KEY, Month_2019 TEXT, Rating_2019 INTEGER, Month_2021 TEXT, Rating_2021 INTEGER, Zip_Code INTEGER)")
    for i in range(len(type_list)):
        cur.execute("INSERT OR IGNORE INTO Types (id,type) VALUES (?,?)",(i,type_list[i]))
    conn.commit()

def setUpCovidTable(data, cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS Types (Month_2021 TEXT, Cases INTEGER, Zip_Code INTEGER")
    for i in range(len(type_list)):
        cur.execute("INSERT OR IGNORE INTO Types (id,type) VALUES (?,?)",(i,type_list[i]))
    conn.commit()