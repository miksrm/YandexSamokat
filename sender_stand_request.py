import configuration
import requests
import data

# Создание заказ
def create_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

response = create_orders(data.orders_body)
track_orders = response.json()['track']

# Поиск заказа по треку
def search_orders():
    return requests.get(configuration.URL_SERVICE + configuration.SEARCH_ORDERS,
                        params={'t': track_orders})

