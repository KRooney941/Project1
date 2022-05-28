from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet


def save(vet):
    sql = "INSERT INTO vets (name) VALUES (?) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet


def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['name'], row['id'])
        vets.append(vet)
    return vets


def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(result['name'], result['id'])
    return vet


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM vets where id = ?"
    values = [id]
    run_sql(sql, values)


def update(vet):
    sql = "UPDATE vets SET (name) = (?) WHERE id = ?"
    values = [vet.name, vet.id]
    run_sql(sql, values)


def animal(vet):
    animals = []

    sql = "SELECT * FROM animals WHERE vet_id = ?"
    values = [vet.id]
    results = run_sql(sql, values)

    for row in results:
        animal = Animal(row['name'], row['dob'], row['age'], row['owner'],
                        row['owner_tel'], row['owner_email'], row['notes'], row['vet'], row['id'])
        animals.append(animal)
    return animals
