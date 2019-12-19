
import psycopg2
from faker import Faker

connection = psycopg2.connect(host='localhost',database='demo',user='demo',password='demo')

cursor = connection.cursor()
fake = Faker()

for i in range(1, 100):
    name = fake.name()
    dob = fake.date()
    updated = fake.date_time()
    cursor.execute("""INSERT INTO customers ("name","dob","updated_at") VALUES (%s,%s,%s)""", (name, dob,updated))
    connection.commit()