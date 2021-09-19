import sqlite3

conn = sqlite3.connect('Movies_db.db')
c = conn.cursor()

c.execute("""CREATE TABLE Movies(
                Name text,
                Actor text,
                Actress text,
                Director text,
                Year_of_Release interger
                                )
            """)
many_movies = [
    ('Avengers', 'Robert Downy Jr', 'Scarlett Johanssen', 'Joss Whedon', 2012),
    ('The Matrix', 'Keanu Reavus', 'Carrie A Moss', 'Lana Wahoshki', 1989),
    ('BayWatch', 'Dwyane John', 'Alexandra Deddario', 'Seth Gordon', 2017),
    ('Speed', 'Keanu Reavus', 'Sandra Bullock', 'Jan de Bont', 1994),
    ('Iron Man', 'Robert Downy Jr', 'Gwyeth Paltrow', 'Jon Faveaus', 2008),
    ('Quiet Place', 'John Krasinski', 'Emily Blunt', 'John Krasinski', 2018),
    ('Sherlock Holmes', 'Robert Downy Jr', 'Rachel McAdams', 'Guy Ritchie', 2010)
                ]
c.executemany("INSERT INTO Movies VALUES (?, ?, ?, ?, ?)", many_movies)
c.execute("SELECT * FROM Movies")
items = c.fetchall()
for i in items:
    print(i)
print("\nSelecting Movies by Actor.")
print("Actor List:"
      "\nRobert Downy Jr"
      "\nKeanu Reavus"
      "\nJohn Krasinski"
      "\nDwyane John"
      "\nEnter name of the Actor:")
mydata = str(input())
query = "SELECT Name FROM Movies WHERE Actor='" + mydata +"'"
c.execute(query)
item_para = c.fetchall()
for i in item_para:
    print(i)

conn.commit()
conn.close()