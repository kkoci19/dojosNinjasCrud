from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    db_name='dojoandninja'
    def __init__(self,data):
        self.id = data['id'],
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def getAllDojos(cls):
        query= 'SELECT * FROM dojos;'
        results =  connectToMySQL(cls.db_name).query_db(query)
        dojos= []
        for row in results:
            dojos.append(row)
        return dojos
    @classmethod
    def get_dojo_by_id(cls, data):
        query= 'SELECT * FROM dojos WHERE dojos.id = %(dojo_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]

    @classmethod
    def create_dojo(cls,data):
        query = 'INSERT INTO dojos(name) VALUES (%(name)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete_Dojo(cls,data):
        query = 'DELETE FROM dojos WHERE id = %(dojos_id)s;'
        return connectToMySQL(cls.db_name).query_db(query,data)

    

