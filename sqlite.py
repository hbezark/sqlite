import sqlite3

conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR, age INTEGER)')

cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Noor', 39))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Ioanna', 16))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Hibah', 38))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Jasveer', 34))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)', ('Eljon', 22))

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

conn.commit()
for row in cur:
	print(row)
	break

cur.close()

conn.close()
