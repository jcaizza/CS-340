from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables (Apporto preset values)
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34058
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data) :
        if data is not None:
            try:
                insert_result = self.database.animals.insert_one(data)  # data should be dictionary
                return insert_result.acknowledged
            except Exception as e:
                print(f"[CREATE ERROR]: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            try:
                documents = self.database.animals.find(query)
                return list(documents)
            except Exception as e:
                print(f"[READ ERROR]: {e}")
                return []
        else:
            raise Exception("Nothing to query, because query parameter is empty")
    # Create method to implement the U in CRUD
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            try:
                update_result = self.database.animals.update_many(query, {"$set": new_values})
                return update_result.modified_count
            except Exception as e:
                print(f"[UPDATE ERROR]: {e}")
                return 0
        else:
            raise Exception("query and new_values parameters cannot be empty")
    # Create method to implement the D in CRUD
    def delete(self, query):
        if query is not None:
            try:
                delete_result = self.database.animals.delete_many(query)
                return delete_result.deleted_count
            except Exception as e:
                print(f"[DELETE ERROR]: {e}")
                return 0
        else:
            raise Exception("query parameter cannot be empty")
            
    # ===== Project Two: Rescue-type query helpers =====
    # These live INSIDE the AnimalShelter class

    # Spec taken from the Dashboard Specifications doc
    FILTER_DEFS = {
        "water": {
            "breeds": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"],
            "sex": "Intact Female",
            "age": (26, 156),  # weeks
        },
        "mountain": {
            "breeds": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"],
            "sex": "Intact Male",
            "age": (26, 156),  # weeks
        },
        "disaster": {
            "breeds": ["Doberman Pinscher", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"],
            "sex": "Intact Male",
            "age": (20, 300),  # weeks
        },
    }

    def _build_rescue_query(self, filter_type: str) -> dict:
        """
        Translate a rescue filter ('water'|'mountain'|'disaster'|'reset')
        into a MongoDB query dict.
        """
        if not filter_type or filter_type == "reset":
            return {}

        spec = self.FILTER_DEFS.get(filter_type, {})
        query = {"animal_type": "Dog"}

        # Breeds list
        breeds = spec.get("breeds")
        if breeds:
            query["breed"] = {"$in": breeds}

        # Sex field
        sex = spec.get("sex")
        if sex:
            query["sex_upon_outcome"] = sex

        # Age range (in weeks)
        age = spec.get("age")
        if age:
            query["age_upon_outcome_in_weeks"] = {"$gte": age[0], "$lte": age[1]}

        return query

    def find_by_rescue_type(self, filter_type: str):
        """
        Return documents from MongoDB filtered by rescue profile.
        filter_type: 'water' | 'mountain' | 'disaster' | 'reset'
        """
        return self.read(self._build_rescue_query(filter_type))