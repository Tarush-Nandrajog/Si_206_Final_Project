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

# Create project database
def setUpDatabase(db_name):
    # Takes in database name (string) as input. Returns database cursor and connection as outputs.
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn