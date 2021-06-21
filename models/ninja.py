from config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data ['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def save(cls, data):
    query = "INSERT INTO ninjas ( first_name, last_name, dojo_id, crated_at, updated_at ) VALUES (%(firt_name)s,%(last_name)s,%(dojo_id)s,NOW(),NOW());"
    
    ninja_id = connectToMySQL('dojos_and_ninjas').query_db(query,data)

    return ninja_id