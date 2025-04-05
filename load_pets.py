

import sqlite3




conn = sqlite3.connect('pets.db')
cur = conn.cursor()





cur.execute("DROP TABLE IF EXISTS person;")
cur.execute("DROP TABLE IF EXISTS pet;")
cur.execute("DROP TABLE IF EXISTS person_pet;")




#Creates tables
cur.execute('''
CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
);
''')

cur.execute('''
CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
);
''')

cur.execute('''
CREATE TABLE person_pet (
    person_id INTEGER,
    pet_id INTEGER
);
''')





#Inserts people data into person table
people = [(1, 'James', 'Smith', 41),
          (2, 'Diana', 'Greene', 23),
          (3, 'Sara', 'White', 27),
          (4, 'William', 'Gibson', 23)]
cur.executemany('INSERT INTO person VALUES (?, ?, ?, ?)', people)

#Inserts pets data into pet table
pets = [(1, 'Rusty', 'Dalmation', 4, 1),
          (2, 'Bella', 'Alaskan Malamute', 3, 0),
          (3, 'Max', 'Cocker Spaniel', 1, 0),
          (4, 'Rocky', 'Beagle', 7, 0), 
          (5, 'Rufus', 'Cocker Spaniel', 1, 0),
          (6, 'Spot', 'Bloodhound', 2, 1)]
cur.executemany('INSERT INTO pet VALUES (?, ?, ?, ?, ?)', pets)





#Inserts pets and their relationships to people in the person_pet table
person_pet = [(1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6)]
cur.executemany('INSERT INTO person_pet VALUES (?, ?)', person_pet)





#Selects all from person table to verify that data is there
res = cur.execute("SELECT * FROM person;")
res.fetchall()





#Selects all from pet table to verify that data is there
res = cur.execute("SELECT * FROM pet;")
res.fetchall()





#Selects all from person_pet table to verify that data is there
res = cur.execute("SELECT * FROM person_pet;")
res.fetchall()




conn.commit()
conn.close()





'''2. What is the purpose of the person_pet table? Person_pet is a join table that represents a many-to-many relationship between people and pets. A person can have many pets, and a pet can be owned by many people (though in this data, it’s one-to-one).'''