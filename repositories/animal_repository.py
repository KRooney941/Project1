from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet
import repositories.vet_repository as vet_repository


def save(animal):
    sql = "INSERT INTO animals (name, type, dob, age, notes, owner, owner_tel, owner_email, vet_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) RETURNING * "
    values = [animal.name, animal.type, animal.dob, animal.age, animal.notes,
              animal.owner, animal.owner_tel, animal.owner_email, animal.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal


def select_all():
    animals = []

    sql = 'SELECT * FROM animals'
    results = run_sql(sql)

    for row in results:
        animal = Animal(row['name'], row['dob'], row['age'], row['owner'],
                        row['owner_tel'], row['owner_email'], row['notes'], row['vet'], row['id'])
        animals.append(animal)
    return animals


def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select(result['vet_id'])
        animal = Animal(result['name'], result['dob'], result['age'], result['owner'],result['owner_tel'], result['owner_email'], result['notes'], vet, result['id'])
    return animal


def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM animals WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(animal):
    sql = "UPDATE animals SET (name, type, dob, age, owner, owner_tel, owner_email, notes, vet_id) = (?, ?, ?, ?, ?, ?, ?, ?, ?) WHERE id = ?"
    values = [animal.name, animal.type, animal.dob, animal.age, animal.owner, animal.owner_tel, animal.owner_email, animal.notes, animal.vet.id]
    run_sql(sql, values)
