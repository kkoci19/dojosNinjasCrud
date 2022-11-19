from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db_name='dojoandninja'
    def __init__(self,data):
        self.id = data['id'],
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.age = data['age'],
        self.dojo_id = data['dojo_id'],
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def getAllNinjas(cls):
        query= 'SELECT * FROM ninjas;'
        results =  connectToMySQL(cls.db_name).query_db(query)
        ninjas= []
        for row in results:
            ninjas.append(row)
        return ninjas
    @classmethod
    def getAllNinjasOfDojo(cls,data):
        query= 'SELECT * FROM ninjas WHERE ninjas.dojo_id = %(dojo_id)s;'
        results =  connectToMySQL(cls.db_name).query_db(query,data)
        ninjas= []
        if results:
            for row in results:
                ninjas.append(row)
            return ninjas
        return ninjas
    @classmethod 
    def create_ninja(cls,data):
        query = 'INSERT INTO ninjas ( dojo_id , first_name, last_name , age ) VALUES( %(dojo_id)s ,%(first_name)s, %(last_name)s, %(age)s);'
        return connectToMySQL(cls.db_name).query_db(query,data)
