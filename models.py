from pony.orm import *

db = Database()

class Pet(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    species = Required(str)
    breed = Optional(str)
    weight = Optional(float)
    notes = Optional(str)
    
    records = Set("CareRecord")
    
class CareRecord(db.Entity):
    id = PrimaryKey(int, auto=True)
    pet = Required(Pet)
    
    record_type = Required(str)
    description = Optional(str)
    date = Required(str)
    next_due_date = Optional(str)
    
db.bind(
    provider="sqlite",
    filename="pets.sqlite",
    create_db=True
)

db.generate_mapping(create_tables=True)