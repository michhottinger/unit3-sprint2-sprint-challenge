"""
question one of sprint challenge, making database
Consider the following data:

| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `demo_data.sqlite3`
- Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
  the above data (name the table `demo`)
- Write and execute appropriate `INSERT INTO` statements to add the data (as
  shown above) to the database

Make sure to `commit()` so your data is saved! The file size should be non-zero.

Then write the following queries (also with `sqlite3`) to test:

- Count how many rows you have - it should be 3!
- How many rows are there where both `x` and `y` are at least 5?
- How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
  `DISTINCT`)?
"""

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

def q_all(query):
    curs = conn.cursor()
    curs.execute(query)
    rows = curs.fetchall()
    curs.close()
    return rows

def q_one(query):
    row = q_all(query)
    return row[0][0]

q_all('DROP TABLE IF EXISTS demo')
q_all('CREATE TABLE demo (s varchar(30), x int, y int);')
# conn.commit()

q_all("""
    INSERT INTO demo
    (s, x, y)
    VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
    """)
#conn.commit()

print('Numb Rows:', q_one("SELECT COUNT(s) FROM demo"))
print('Numb Rows >=5:', q_one("SELECT COUNT(*) FROM demo WHERE x>=5 AND y>=5"))
print('Unique y Values:', q_one("SELECT COUNT(DISTINCT y) FROM demo"))
