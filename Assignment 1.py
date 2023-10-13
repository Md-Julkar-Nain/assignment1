mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Russia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'UK'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 107.25
}

for item in mobile_data["data"]:
    usd = float(item['price'].split()[0])
    price_bdt = (usd * mobile_data['exchange_rate'])

    print(
        f"{item['name']} is made in {item['made']}. The price is {item['price']} which is almost equal to {price_bdt} BDT.")
