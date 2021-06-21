from config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def show_all_dojos(cls):
        query = "SELECT * FROM dojos_and_ninjas.dojos;"

        results = connectToMySQL("dojos_and_ninjas").query_db(query)

        dojos = []

        for row in results:
            dojos.append(Dojo(row))

        return dojos