import os
import slack
from scraper import do
from database import initialise_db_connection, insert_record, check_record_exists

INIT_TABLE = False  # Will delete existing records and create a new table if True
QUIET_MODE = True

def parse_listing(listing):
	parsed_listing = "*{name}* \n _{location}_ \n ${price} \n {url} \n (Beds: {beds}/Area:{area})".format(name=listing["name"],
										   price=listing["price"],
										   location=listing["where"],
										   beds=listing["bedrooms"],
										   area=listing["area"],
										   url=listing["url"])
	return parsed_listing

def initialise_slack_client():
	client = slack.WebClient(token=os.environ["SLACK_API_TOKEN"])
	return client

def post_to_slack(client, listing):
	response = client.chat_postMessage(channel="#housing", text=listing)

if __name__ == "__main__":
	if INIT_TABLE == True:
		print("Warning: INIT_TABLE==True will delete existing records.")
		answer = input("Continue? (y/n)")
		if answer.strip() == 'n':
			print("Quitting.")
			quit()

	client = initialise_slack_client()
	cursor, connection = initialise_db_connection(init_table=INIT_TABLE)

	print("Starting scrape...")
	results = do()

	new_listing_count = 0
	for listing in results:
		print(listing)
		record_exists = check_record_exists(cursor, listing)
		insert_record(cursor, listing)
		if not record_exists:
			new_listing_count += 1
			post_to_slack(client, parse_listing(listing))
	connection.commit()
	connection.close()

	total_listings = len(results)
	
	print("Scraping Complete. {total} total listings. {new} new listings.".format(total=total_listings, new=new_listing_count))