from flask import Flask, render_template, request, redirect
from pony.orm import db_session, select
from models import Pet, CareRecord

app = Flask(__name__)

@app.route("/")
@db_session
def home():
    pets = Pet.select()[:]
    records = CareRecord.select()[:]

    total_pets = len(pets)
    total_records = len(records)

    vaccinations = len([r for r in records if r.record_type == "Cijepljenje"])
    parasite_treatments = len([r for r in records if r.record_type == "Tretman protiv parazita"])
    vet_visits = len([r for r in records if r.record_type == "Veterinarski pregled"])
    weight_measurements = len([r for r in records if r.record_type == "Mjerenje težine"])

    parasite_treatments = len([
        r for r in records
        if r.record_type == "Tretman protiv parazita"
    ])

    weight_measurements = len([
     r for r in records
        if r.record_type == "Mjerenje težine"
    ])
    return render_template(
        "index.html",
        pets=pets,
        records=records,
        total_pets=total_pets,
        total_records=total_records,
        vaccinations=vaccinations,
        parasite_treatments=parasite_treatments,
        vet_visits=vet_visits,
        weight_measurements=weight_measurements
    )

@app.route("/add-pet", methods=["POST"])
@db_session
def add_pet():
    Pet(
        name=request.form["name"],
        species=request.form["species"],
        breed=request.form["breed"],
        weight=float(request.form["weight"]) if request.form["weight"] else None,
        notes=request.form.get("notes")
    )
    return redirect("/")

@app.route("/add-record", methods=["POST"])
@db_session
def add_record():
    pet = Pet[int(request.form["pet_id"])]

    CareRecord(
        pet=pet,
        record_type=request.form["record_type"],
        description=request.form.get("description"),
        date=request.form["date"],
        next_due_date=request.form.get("next_due_date")
    )

    return redirect("/")

@app.route("/delete-pet/<int:pet_id>")
@db_session
def delete_pet(pet_id):
    pet = Pet[pet_id]
    pet.delete()

    return redirect("/")

@app.route("/edit-pet/<int:pet_id>")
@db_session
def edit_pet_form(pet_id):
    pet = Pet[pet_id]
    return render_template("edit_pet.html", pet=pet)

@app.route("/update-pet/<int:pet_id>", methods=["POST"])
@db_session
def update_pet(pet_id):
    pet = Pet[pet_id]

    pet.name = request.form["name"]
    pet.species = request.form["species"]
    pet.breed = request.form.get("breed")
    pet.weight = float(request.form["weight"]) if request.form["weight"] else None
    pet.notes = request.form.get("notes")

    return redirect("/")

@app.route("/edit-record/<int:record_id>")
@db_session
def edit_record_form(record_id):
    record = CareRecord[record_id]
    pets = Pet.select()[:]
    return render_template("edit_record.html", record=record, pets=pets)


@app.route("/update-record/<int:record_id>", methods=["POST"])
@db_session
def update_record(record_id):
    record = CareRecord[record_id]

    record.pet = Pet[int(request.form["pet_id"])]
    record.record_type = request.form["record_type"]
    record.description = request.form.get("description")
    record.date = request.form["date"]
    record.next_due_date = request.form.get("next_due_date")

    return redirect("/")

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
    
