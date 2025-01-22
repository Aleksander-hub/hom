import sqlite3


connection = sqlite3.connect("initiate.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT NOT NULL,
price INTEGER
);
''')

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT NOT NULL,
price INTEGER
);
''')

#def get_all_products(title, description, price):
#    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f"{title}", f"{description}", f"{price}"))
#k = 100
#for i in range(1, 5):
#    get_all_products(f'Продукт{i}', f'Описание{i}', f'{k}')
#    k += 100

def set_product(title,description,price,img_name):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (title,description,price, img_name) VALUES (?,?,?,?)",
                   (f'{title}', f'{description}', f'{price}',f'{img_name}'))
    connection.commit()
    connection.close()




def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    total = cursor.fetchall()
    connection.close()
    return total


connection.commit()
connection.close()



'''
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс {user[3]}")


def get_buying_list():
    products = cursor.execute("SELECT title, description, price FROM Products")
    a = []
    for i in products:
        a += {f'Название: {i[0]} | Описание: {i[1]} | Цена: {i[2]}'}
    connection.commit()
    return a
'''