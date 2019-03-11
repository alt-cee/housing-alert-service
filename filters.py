# craigslist site
SITE = 'sfbay'

# housing type
CATEGORY = 'apa' # apts/housing for rent

# price
MIN_PRICE = 3000
MAX_PRICE = 5000

# size
MIN_BEDROOMS = 6
MAX_BEDROOMS = None
MIN_FT2 = None
MAX_FT2 = None
MIN_BATHROOMS = None
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
LAUNDRY = 'w/d in unit'
PARKING = [
	'carport',
	'attached garage',
	'detached garage',
	'off-street parking']

# location

site_parameters = {
	'site': SITE,
	'category': CATEGORY
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