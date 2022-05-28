from logging import NOTSET


class Animal:
    def __init__(self, name, type, dob, age, owner, owner_tel, owner_email, notes, vet, id=None):
        self.name = name
        self.type = type
        self.dob = dob
        self.age = age
        self.owner = owner
        self.owner_tel = owner_tel
        self.owner_email = owner_email
        self.notes = notes
        self.vet = vet
        self.id = id
