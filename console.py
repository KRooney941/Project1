import pdb
from models.animal import Animal
from models.vet import Vet

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository


animal_repository.delete_all()
vet_repository.delete_all()

vet_1 = Vet("Dr Frank")
vet_repository.save(vet_1)

vet_2 = Vet("Dr Teddy")
vet_repository.save(vet_2)

animal_1 = Animal("Sunny", "cockatiel", "02/05/2020", "2", "James Smith",
                  "07700184669", "james_smith12@gmail.com", "broken beak", vet_1)
animal_repository.save(animal_1)

animal_2 = Animal("George", "budgie", "21/07/2018", "3", "Samantha Jones",
                  "07706182162", "SamJones@live.co.uk", "sore foot", vet_2)
animal_repository.save(animal_2)
