# -*- coding: utf-8 -*-

# region Application Example Scripts

def test_application():
    from flight import Flight
    flight = Flight()
    flight.create_tables_and_fill_with_data()
    print('quotes!')
    print(flight.get_data_from_db_by_tablename('quotes'))
    print('carriers!')
    print(flight.get_data_from_db_by_tablename('carriers'))
    print('places!')
    print(flight.get_data_from_db_by_tablename('places'))

# endregion Application Example Scripts

# region Main Script
if __name__ == "__main__":
    test_application()

# endregion Main Script