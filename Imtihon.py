#1-masala
import psycopg2
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE Product (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price NUMERIC NOT NULL,
        color VARCHAR(50),
        image BYTEA
    );
""")
conn.commit()
cur.close()
conn.close()
print("Table 'Product' muvaffaqiyatli qo'shildi.")
#2-masala
import psycopg2
def insert_product(name, price, color, image):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()   
    cur.execute("INSERT INTO Product (name, price, color, image) VALUES (%s, %s, %s, %s)", (name, price, color, image))  
    conn.commit()    
    cur.close()
    conn.close()
    print("Product muvafaqiyatli insert qilindi.")
import psycopg2
def select_all_products():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM Product")
    products = cur.fetchall()
    cur.close()
    conn.close()
    return products
import psycopg2
def update_product(product_id, name, price, color, image):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1",
        host="loczlhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("UPDATE Product SET name=%s, price=%s, color=%s, image=%s WHERE id=%s", (name, price, color, image, product_id))
    conn.commit()
    cur.close()
    conn.close()
    print("Product muvafiqiyatli yangilandi.")
import psycopg2
def delete_product(product_id):
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM Product WHERE id=%s", (product_id,))
    conn.commit()
    cur.close()
    conn.close()
    print("Product muvaffiqiyatli o'chirildi.")
#3-masala
class Alfabit:
    def __init__(self):
        self.indeksi = 0
        self.alfabit = "abcdefghijklmnopqrstuvwxyz"
    def __iter__(self):
        return self
    def __next__(self):
        if self.indeksi < len(self.alfabit):
            letter = self.alfabit[self.indeksi]
            self.indeksi += 1
            return letter
        else:
            raise StopIteration
alfabit_iter = Alfabit()
for letter in alfabit_iter:
    print(letter)
#4-masala
import threading
import time
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)
def print_letters():
    for letter in 'ABCDE':
        print(letter)
        time.sleep(1)
if __name__ == "__main__":
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
#5-masala    
import psycopg2
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Product (id SERIAL PRIMARY KEY, name VARCHAR, price NUMERIC, color VARCHAR, image VARCHAR);")
conn.commit()
class Product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image
    def save(self):
        cur.execute("INSERT INTO Product (name, price, color, image) VALUES (%s, %s, %s, %s);", (self.name, self.price, self.color, self.image))
        conn.commit()
        print("Product databazaga saqlandi")
product1 = Product("Mushuk", 100, "sariq", "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg")
product1.save()
cur.close()
conn.close()
#6-masala
import psycopg2
class DbConnect:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cur = self.conn.cursor()
        return self.conn, self.cur
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
dbname = "postgres"
user = "postgres"
password = "1"
host = "localhost"
port = "5432"
with DbConnect(dbname, user, password, host, port) as (conn, cur):
    cur.execute("SELECT * FROM your_table")
    rows = cur.fetchall()
    for row in rows:
        print(row)
