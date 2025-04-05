import sqlite3




def get_person_and_pets(person_id):
    conn = sqlite3.connect('pets.db')
    cur = conn.cursor()

    #Gets person's info
    cur.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = cur.fetchone()

    if not person:
        conn.close()
        return None, None

    #Gets person's pets
    cur.execute('''
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
    ''', (person_id,))
    pets = cur.fetchall()

    conn.close()
    return person, pets

def main():
    while True:
        try:
            person_id = int(input("Please enter person ID or -1 to exit: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if person_id == -1:
            print("Exiting now, goodbye!")
            break

        person, pets = get_person_and_pets(person_id)

        if not person:
            print("Person not found.\n")
            continue

        first, last, age = person
        print(f"\n{first} {last}, {age} years old")

        for pet in pets:
            name, breed, pet_age, dead = pet
            ownership = "owned" if dead else "own" #If the pet is alive, use "own", else "owned"
            tense = "was" if dead else "is" #If the pet is alive, use "is", else use "was"
            status = "and is no longer alive." if dead else "and is still living."
            
            print(f"  They {ownership} {name}, a {breed}, that {tense} {pet_age} years old, {status}")


if __name__ == "__main__":
    main()