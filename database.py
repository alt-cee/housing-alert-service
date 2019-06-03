import sqlite3
from datetime import datetime, timezone

SCHEMA = {
	"id": "integer",
	"name": "text",
	"url": "text",
	"price": "integer",
	"area": "text",
	"bedrooms": "integer",
	"location": "text",
	"timestamp": "real"
}

def initialise_db_connection(init_table=False):
	conn = sqlite3.connect('records.db')
	cursor = conn.cursor()
	if init_table:
		cursor.execute('''drop table listings''')
		cursor.execute("""create table listings ({})""".format(", ".join(map(lambda x: " ".join(x), [(key, value) for key, value in SCHEMA.items()]))))
	return cursor, conn 

def format_record(record, schema):
	for key, value in record.items():
		if key in schema.keys() and schema[key] == "integer":
			record[key] = int(record[key].strip('$'))
	record["location"] = record["where"]
	return record

def insert_record(c, record):
	timestamp = datetime.now()
	timestamp = timestamp.replace(tzinfo=timezone.utc).timestamp()
	formatted_record = format_record(record, SCHEMA)
	c.execute('''insert into listings values ({id}, '{name}', '{url}', {price}, '{area}', {bedrooms}, '{location}', {timestamp})'''.format(**formatted_record, timestamp=timestamp))

def check_record_exists(c, listing):
	flag = False
	result = c.execute('''select count(id) from listings where id={listing_id}'''.format(listing_id=listing["id"]))
	count = result.fetchone()[0]
	if count > 0:
		flag = True
	return flag
