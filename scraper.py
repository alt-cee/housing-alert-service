from craigslist import CraigslistHousing
from filters import site_parameters, search_parameters

def do():
	# get listings from craigslist
	housing = CraigslistHousing(
		**site_parameters,
		filters=search_parameters)
	results = housing.get_results()
	return results