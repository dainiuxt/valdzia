#~ import MySQLdb
from skylark import Database, Model, Field
#~ database connection
Database.config(db='valdzia', user='valdzia_py', passwd='123456')

class employees(Model):
	name = Field()
	position = Field()

employees.create(name='Valdas Adamkus', position='Lietuvos Respublikos Prezidentas')
