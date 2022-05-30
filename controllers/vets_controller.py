from flask import Flask, render_template, Blueprint, redirect, request

from models.vet import Vet

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)


@vets_blueprint.route("/vets/")
def vets():
    vets = vet_repository.select_all()
    return render_template("/vets/index.html", vets=vets)


@vets_blueprint.route("/vets/<id>")
def show(id):
    vet = vet_repository.select(id)
    return render_template("vets/edit.html", vet=vet)


@vets_blueprint.route("/vets/<id>", methods=['GET'])
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets', vet=vet)


@vets_blueprint.route("/vets/<id>/edit", methods=["POST"])
def update_vet(id):
    name = request.form['name']
    vet = Vet(name, id)
    vet_repository.update(vet)
    return redirect('/vets')


@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template("/vets/new.html")


@vets_blueprint.route("/vets", methods=["POST"])
def add_vet():
    name = request.form["name"]
    vet = Vet(name)
    vet_repository.save(vet)
    return redirect("/vets")


@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect("/vets")
