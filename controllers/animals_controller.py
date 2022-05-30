from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)


@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", all_animals=animals)


@animals_blueprint.route("/animals/new", methods=['GET'])
def new_animal():
    vets = vet_repository.select_all()
    return render_template("/animals/new.html", all_vets=vets)


@animals_blueprint.route("/animals", methods=["POST"])
def add_animal():
    name = request.form["name"]
    type = request.form["type"]
    dob = request.form["dob"]
    age = request.form["age"]
    owner = request.form["owner"]
    owner_tel = request.form["owner_tel"]
    owner_email = request.form["owner_email"]
    notes = request.form["notes"]
    vet = vet_repository.select(request.form['vet_id'])
    animal = Animal(name, type, dob, age, notes,
                    owner, owner_email, owner_tel, vet)
    animal_repository.save(animal)
    return redirect("/animals")


@animals_blueprint.route("/animals/<id>/edit", methods=['GET'])
def edit_animal(id):
    animal = animal_repository.select(id)
    vet = vet_repository.select_all()
    return render_template('/animals/edit.html', animal=animal, vet=vet)


@animals_blueprint.route("/animals/<id>", methods=['POST'])
def update_animal(id):
    name = request.form["name"]
    type = request.form["type"]
    dob = request.form["dob"]
    age = request.form["age"]
    notes = request.form["notes"]
    owner = request.form["owner"]
    owner_tel = request.form["owner_tel"]
    owner_email = request.form["owner_email"]
    vet = vet_repository.select(request.form['vet_id'])
    animal = Animal(name, type, dob, age, owner,
                    owner_email, owner_tel, notes, vet)
    animal_repository.update(animal)
    # return redirect('/animals')

    return render_template("/animals/show.html", animal=animal, vets=vet)


@animals_blueprint.route("/animals/<id>")
def show_animal(id):
    animal = animal_repository.select(id)
    return render_template("/animals/show.html", animal=animal)


@animals_blueprint.route("/animals/<id>/delete", methods=['POST'])
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('/animals')
