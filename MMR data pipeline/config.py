import os
from urllib.parse import quote_plus

"""
add the PASSWORD of database and UID to path.
e.g export PASSWORD=pass123
    export USERID=awesomeuser101
"""

USERID = os.environ.get('USERID')        # Retrieve the UID from system variables
PASSWORD = os.environ.get('PASSWORD')    # Retrieve the PASSWORD from the system variables
CONN_STR = r"Driver={ODBC Driver 17 for SQL Server};Server=tcp:mmrdata.database.windows.net," \
           "1433;Database=mmr;Uid=" + USERID + r";Pwd={" + PASSWORD + r"};Encrypt=yes;TrustServerCertificate=no" \
                                                                      ";Connection Timeout=30; "

PARAMS = quote_plus(CONN_STR)

# Azure MySQL
DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(PARAMS)    # Construct as database uri

# Local Postgresql
# DATABASE_URI = 'postgres+psycopg2://postgres:postgres@localhost:5432/data'
