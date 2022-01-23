from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name, last_name , age, created_at, updated_at, dojo_id ) VALUES ( %(first_name)s , %(last_name)s ,%(age)s , NOW() , NOW(),%(dojo_id)s  );"
        return connectToMySQL('schema_dojos_and_ninjas').query_db( query, data )
    
    @classmethod
    def get_ninjas_by_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.dojo_id = %(id)s;"
        results = connectToMySQL('schema_dojos_and_ninjas').query_db(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append( cls( ninja ) )
        return ninjas