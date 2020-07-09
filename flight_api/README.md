### How to run this 

#### Running PostgreSQL server

```docker run --name postgres-0 -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine ```

Alternatively, 
``` docker-compose up ```

then, 
```docker exec -it postgres-0 bash```

then, ```psql -U postgres``` (for manually managing the database later)

#### Running Flask

Create a virtual environment with
```python3 -m venv vacayhome```<br>
and activate it with 
```source vacayhome/bin/activate```<br>
Then, install packages ```pip install -r requirements.txt```<br>
```export FLASK_APP=server```<br>
```flask run```

#### Running the application multiple times
This application creates a new database every time it starts. To avoid ```psycopg2.errors.DuplicateDatabase: database "flight" already exists```,  after the first run, you can either delete the database by ```drop database flight;``` on posgreSQL CLI or comment out ```flight.create_tables_and_fill_with_data()``` in server/__ init __.py

#### Requests
- Posting a new minimum flight price <min_price> for a flight with an ID <quote_id> <br>
```curl -X POST http://localhost:5000/api/v1/quotes?quote_id=<quote id>&min_price=<new minimum price>``` <br>
For example, ```curl -X POST http://localhost:5000/api/v1/quotes?quote_id=12&min_price=50```
- Getting all the quotes for July <br>
Returning 1 or 2 cheapest flights/day from ORD to LGA in July 2020 <br>
```curl -X GET http://localhost:5000/api/v1/quotes```
```[<quote_id>,<minimum price>,<direct flight or not>,<carrier id>,<departure airport id>,<arrival airport id>,<date>]```
- Showing the summary of the quotes for July <br>
```curl -X GET http://localhost:5000/api/v1/summary```

<!-- - Getting all the carriers for the flights <br>
```curl -X GET http://localhost:5000/api/v1/carriers``` -->
