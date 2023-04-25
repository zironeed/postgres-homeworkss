"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from utils.open_csv import get_csv
from utils.insert_data import insert_data


def main():
    employees_data = get_csv("north_data/employees_data.csv")
    customers_data = get_csv("north_data/customers_data.csv")
    orders_data = get_csv("north_data/orders_data.csv")

    insert_data('employees', employees_data)
    insert_data('customers', customers_data)
    insert_data('orders', orders_data)


main()
