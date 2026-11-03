import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class DB:

    def __init__(self):
        try:
            self.conn = None
            self.mycursor = None
            self.conn = mysql.connector.connect(
                host = os.getenv("DB_Host"),
                user = os.getenv("DB_User"),
                password = os.getenv("DB_PASSWORD"),
                database = os.getenv("DB_NAME")
            )
            self.mycursor = self.conn.cursor()
            print('Connection Succesful')
        except mysql.connector.Error as e:
            print(e)

    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
        SELECT DISTINCT Destination FROM flights
        UNION
        SELECT DISTINCT Source FROM flights
        """)

        data = self.mycursor.fetchall()

        for i in data:
            city.append(i[0])

        return city

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
        SELECT Airline, Route, Dep_Time, Duration, Price
        FROM flights
        WHERE Source = %s and Destination = %s
        """, (source,destination))

        return self.mycursor.fetchall()

    def fetch_airline_frequency(self):
        self.mycursor.execute("""
        SELECT Airline, COUNT(*) AS count FROM flights
        GROUP BY Airline
        """)
        return self.mycursor.fetchall()

    def fetch_airline_fare(self):
        self.mycursor.execute("""
        SELECT Airline, AVG(Price) AS avg_price 
        FROM flights 
        GROUP BY Airline
        """)
        return self.mycursor.fetchall()

    def fetch_city_frequencey(self):
        self.mycursor.execute("""SELECT Source, COUNT(*) AS count 
        FROM flights 
        GROUP BY Source
        """)
        return self.mycursor.fetchall()