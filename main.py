import sys
import os
import json
import pprint

def createSchema(doc):
	'''
	Loop through keys and create a dctionary that will represent the schema for the document.
	'''
	## create object schema
	schema = {}

	## loop through keys
	for key in doc:
		## get key type
		key_type = type(doc[key])

		## change key from unicode to string
		key = str(key)

		# in case the type is not accounted for
		key_type_string = "UNKNOWN TYPE"

		## Check which type this is
		if key_type is int or key_type is int or key_type is float:
			key_type_string = "INTEGER"
		elif key_type is bool:
			key_type_string = "BOOLEAN"
		elif key_type is str or key_type is str:
			key_type_string = "STRING"
		elif key_type is list:
			key_type_string = "ENUM"
		elif key_type is dict:
			key_type_string = "ARRAY"

		## Entry for schema key
		schema_entry = {}

		## Set key type
		schema_entry["type"] = key_type_string

		## Pad schema with required keys
		schema_entry["tag"] = ""
		schema_entry["description"] = ""
		schema_entry["required"] = False

		# insert values in schema
		schema[key] = schema_entry

	## return fnished schema
	return schema


def getSchema(path):
	'''
	Open file and pass the json document to createSchema
	'''
	with open(path) as data_file:    
		doc = json.loads(data_file.read())
		get_only_message = doc["message"]
		return createSchema(get_only_message)

if __name__ == "__main__":
	path = ""

	## test if file name given in command line
	if len(sys.argv) == 2:
		## grab from command line
		path = sys.argv[1]
	else:
		## Get file from user
		path = input("Please enter data file path: ")
	# get schema
	schema = json.dumps(getSchema(path))
	pprint.pprint(schema)
	# save schema to file
	data_file_name = os.path.basename(path)
	schema_file_name = data_file_name.replace("data", "schema")
	with open(f'schema/{schema_file_name}', 'w+') as schema_file:
		schema_file.write(schema)
