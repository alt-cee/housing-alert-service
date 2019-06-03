# craigslist site
SITE = 'sfbay'
AREA = 'sfc'

# housing type
CATEGORY = 'apa' # apts/housing for rent

# price
MIN_PRICE = 3000
MAX_PRICE = 5000

# size
MIN_BEDROOMS = 1
MAX_BEDROOMS = 2
MIN_FT2 = 700
MAX_FT2 = 1200
MIN_BATHROOMS = 1
MAX_BATHROOMS = None

# other
IS_FURNISHED = False
HOUSING_TYPE = [
	'apartment',
	'condo',
	'duplex',
	'flat',
	'house',
	'loft',
	'townhouse']
LAUNDRY = ['w/d in unit']
PARKING = [
	'carport',
	'attached garage',
	'detached garage',
	'off-street parking',
	'street parking']

# location
AREAS = {
	'Mission District': [
		[37.748861, -122.422523], # lower left corner
		[37.764604, -122.407460]], # upper right corner
	'Noe Valley': [
		[37.751371, -122.434078],
		[37.756732, -122.423306]],
	'Dolores': [
		[37.756122, -122.434592],
		[37.768013, -122.424379]]
}

site_parameters = {
	'site': SITE,
	'category': CATEGORY,
	'area': AREA
}

search_parameters = {
	'max_price': MAX_PRICE,
	'min_price': MIN_PRICE,
	'min_bedrooms': MIN_BEDROOMS,
	'max_bedrooms': MAX_BEDROOMS,
	'min_ft2': MIN_FT2,
	'max_ft2': MAX_FT2,
	'min_bathrooms': MIN_BATHROOMS,
	'max_bathrooms': MAX_BATHROOMS,
	'is_furnished': IS_FURNISHED,
	'housing_type': HOUSING_TYPE,
	'laundry': LAUNDRY,
	'parking': PARKING
}