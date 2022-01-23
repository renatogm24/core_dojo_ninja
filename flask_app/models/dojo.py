from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('schema_dojos_and_ninjas').query_db( query, data )
    
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('schema_dojos_and_ninjas').query_db(query, data)
        dojo = cls(results[0])
        for ninjas in results:
            # ahora parseamos los datos de hamburguesa para crear instancias de hamburguesa y agregarlas a nuestra lista
            ninja_data = {
                "id" : ninjas["ninjas.id"],
                "first_name" : ninjas["first_name"],
                "last_name" : ninjas["last_name"],
                "age" : ninjas["age"],
                "created_at" : ninjas["ninjas.created_at"],
                "updated_at" : ninjas["ninjas.updated_at"],
                "dojo_id" : ninjas["dojo_id"]
            }
            dojo.ninjas.append( Ninja( ninja_data ) )
        return dojo
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('schema_dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos