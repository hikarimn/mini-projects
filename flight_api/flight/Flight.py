# -*- coding: utf-8 -*-

import json
import requests
import psycopg2

URL = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsedates/v1.0/US/USD/en-US/ORD-sky/LGA-sky/2020-07"

QUERYSTRING = {"inboundpartialdate":""}
HEADERS = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "de0a24e1c1msh6ab9b8d6bcf0861p149e6ejsn257c882fc44c"
    }
DB_USERNAME =  'postgres'
DB_PASSWORD = 'password'
DB_HOST =  "127.0.0.1"
DB_PORT = "5432"

class Flight:
    def __init__(self):
        # self.parsed_data = json.loads(self.get_raw_data())
        self.parsed_data = None
        self.connection = None
        self.cursor = None
        self.record = None
    
    def create_tables_and_fill_with_data(self):
        
        self.create_db('flight')
        self.open_db_connection('flight')
        self.create_tables()
        self.insert_data_to_db()
        self.close_db_connection()

    def open_db_connection(self, db_name = None):
        try:
            if db_name:
                self.connection = psycopg2.connect(
                    user = DB_USERNAME,
                    password = DB_PASSWORD,
                    host = DB_HOST,
                    port = DB_PORT,
                    database = db_name
                )
            else:
                self.connection = psycopg2.connect(
                    user = DB_USERNAME,
                    password = DB_PASSWORD,
                    host = DB_HOST,
                    port = DB_PORT
                )
            self.connection.autocommit = True

            self.cursor = self.connection.cursor()
            print ( self.connection.get_dsn_parameters(),"\n")

            self.cursor.execute("SELECT version();")
            self.record = self.cursor.fetchone()
            print("You are connected to - ", self.record,"\n")
        except (Exception, psycopg2.DatabaseError) as error:
            print('failed to open the database connection')
            print(error)
    
    def close_db_connection(self):
        try:
            if(self.connection):
                self.cursor.close()
                self.connection.commit()
                self.connection.close()
                print("PostgreSQL connection is closed")
        except (Exception, psycopg2.DatabaseError) as error:
            print('failed to close the database connection')
            print(error)

    def create_db(self, db_name):
        self.open_db_connection()
        query = 'CREATE database ' + db_name;
        self.cursor.execute(query)
        print("Database created successfully..")
        self.close_db_connection()
    
    def create_tables(self):
        """ create tables in the PostgreSQL database"""
        commands = (
            """
            CREATE TABLE quotes (
                quote_id INTEGER PRIMARY KEY,
                min_price INTEGER NOT NULL,
                direct_flight BOOL NOT NULL,
                carrier_id INTEGER NOT NULL,
                origin_id INTEGER NOT NULL,
                destination_id INTEGER NOT NULL,
                departure_date VARCHAR(255) NOT NULL
            )
            """,
            """
            CREATE TABLE places (
                place_id INTEGER PRIMARY KEY,
                itata_code VARCHAR(8) NOT NULL,
                place_name VARCHAR(255) NOT NULL,
                city_name VARCHAR(255) NOT NULL,
                country_name VARCHAR(255) NOT NULL   
            )
            """,
            """
            CREATE TABLE carriers (
                carrier_id INTEGER PRIMARY KEY,
                carrier_name VARCHAR(255) NOT NULL
            )
            """
        )
        try:
            for command in commands:
                self.cursor.execute(command)
            # self.connection.commit()
        except Exception as error:
            print(error)

    def get_raw_data(self):
        ''' get data using SkyScanner API and returns in an original format'''
        try:
            # print('got raw data')
            return requests.request("GET", URL, headers=HEADERS, params=QUERYSTRING).text
        except Exception as error:
            print(error)
            exit()
    
    def insert_data_to_db(self):
        # print('insert_data_to_db')
        if not self.parsed_data:
            self.parsed_data = json.loads(self.get_raw_data())
        # print(json.dumps(self.parsed_data, indent = 4))
        self.insert_quotes_to_db()
        self.insert_places_to_db()
        self.insert_carriers_to_db()

    def insert_quotes_to_db(self):
        try:
            for quote_data in self.parsed_data['Quotes']:
                # print(json.dumps(quote_data, indent = 4))
                quote_id = quote_data['QuoteId']
                min_price = quote_data['MinPrice']
                direct_flight = quote_data['Direct']
                carrier_id = quote_data['OutboundLeg']['CarrierIds'][0]
                origin_id = quote_data['OutboundLeg']['OriginId']
                destination_id = quote_data['OutboundLeg']['DestinationId']
                departure_date = quote_data['OutboundLeg']['DepartureDate'].split('T')[0]
                insert_query = "INSERT INTO quotes VALUES {}".format(
                    "(" + str(quote_id) 
                    + ", " + str(min_price) 
                    + ", " +  str(direct_flight) 
                    + ", " + str(carrier_id) 
                    + ", " + str(origin_id) 
                    + ", " + str(destination_id)
                    + ", '" + str(departure_date) + "')"
                    )
                # print(insert_query)
                self.cursor.execute(insert_query)
                # self.connection.commit()
        except Exception as error:
            print(error)

    def insert_places_to_db(self):
        try:
            for place_data in self.parsed_data['Places']:
                place_id = place_data['PlaceId']
                itata_code = place_data['IataCode']
                place_name = place_data['Name'].replace("'", "")
                city_name = place_data['CityName']
                country_name = place_data['CountryName']
                # print(place_id)
                insert_query = "INSERT INTO places VALUES {}".format(
                    "(" + str(place_id) 
                    + ", '" + str(itata_code) 
                    + "', '" +  str(place_name) 
                    + "', '" + str(city_name) 
                    + "', '" + str(country_name) 
                    + "')"
                    )
                # print(insert_query)
                self.cursor.execute(insert_query)
                # self.connection.commit()
        except Exception as error:
            print(error)
        
    def insert_carriers_to_db(self):
        try:
            for carrier_data in self.parsed_data['Carriers']:
                carrier_id = carrier_data['CarrierId']
                carrier_name = carrier_data['Name']
                insert_query = "INSERT INTO carriers VALUES {}".format(
                    "(" + str(carrier_id) 
                    + ", '" + str(carrier_name)  
                    + "')"
                    )
                # print(insert_query)
                self.cursor.execute(insert_query)
                # self.connection.commit()
        except Exception as error:
            print(error)

    def get_data_from_db_by_tablename(self, tablename):
        try:
            self.open_db_connection('flight')
            insert_query = "SELECT * FROM " + tablename + " ORDER BY " + tablename[:-1] + "_id"
            self.cursor.execute(insert_query)
            rows = self.cursor.fetchall()
            # print("The number of parts: ", self.cursor.rowcount)
            # for row in rows:
                # print(row)
            self.close_db_connection()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_summary_from_db(self):
        try:
            summary = {}
            self.open_db_connection('flight')
            avg_query = "SELECT AVG(min_price) FROM quotes"
            min_query = "SELECT * FROM quotes WHERE min_price = ( SELECT MIN(min_price) FROM quotes)"
            
            self.cursor.execute(avg_query)
            avg_min_price = self.cursor.fetchone()
            summary['avg_min_price'] = int(avg_min_price[0])

            self.cursor.execute(min_query)
            flight_with_min_price = list(self.cursor.fetchone())
            flight_with_min_price[3] = self._get_carrier_by_id_from_db(flight_with_min_price[3])
            flight_with_min_price[4] = self._get_place_by_id_from_db(flight_with_min_price[4])
            flight_with_min_price[5] = self._get_place_by_id_from_db(flight_with_min_price[5])
            summary['flight_with_min_price'] = flight_with_min_price
            
            print(summary)
            self.close_db_connection()
            return summary
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_quote_by_id_from_db(self, quote_id):
        try:
            self.open_db_connection('flight')
            quote_query = "SELECT * FROM quotes WHERE quote_id =" + str(quote_id)
            self.cursor.execute(quote_query)
            quote = self.cursor.fetchone()
            self.close_db_connection()
            
            return quote 
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def _get_carrier_by_id_from_db(self, carrier_id):
        try:
            # self.open_db_connection('flight')
            carrier_query = "SELECT * FROM carriers WHERE carrier_id =" + str(carrier_id)
            self.cursor.execute(carrier_query)
            carrier = self.cursor.fetchone()
            return carrier 
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def _get_place_by_id_from_db(self, place_id):
        try:
            # self.open_db_connection('flight')
            place_query = "SELECT * FROM places WHERE place_id =" + str(place_id)
            self.cursor.execute(place_query)
            place = self.cursor.fetchone()
            return place 
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_min_price_by_quote_id(self, quote_id, new_price):
        try:
            self.open_db_connection('flight')
            update_query = "UPDATE quotes SET min_price = " + str(new_price) + " WHERE quote_id =" + str(quote_id)
            self.cursor.execute(update_query)
            self.close_db_connection()
            return
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)