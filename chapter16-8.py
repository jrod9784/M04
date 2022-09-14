import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
conn.execute(
    '''CREATE TABLE books(title VARCHAR(30), author VARCHAR(20), year INT)''')
ins = 'INSERT INTO books (title, author, year) VALUES (?, ?, ?)'
conn.execute(ins, 'A Song of Ice and Fire', 'George R. R. Martin', 1996)
conn.execute(ins, 'The Winds of Winter', 'George R. R. Martin', 2025)
titles = conn.execute('SELECT TITLE FROM books')
years = conn.execute('SELECT YEAR FROM books')

for title in titles:
    print(title)

for year in years:
    print(year)
