from craigslist import CraigslistHousing
from filters import site_parameters, search_parameters, AREAS

def check_area(coords, area):
	lat, lon = coords
	if area[0][0] < lat < area[1][0] and area[0][1] < lon < area[1][1]:  #TODO: more robust to negative lat, lon
		return True
	return False


def do():
	# get listings from craigslist
	# applies craiglist filters
	housing = CraigslistHousing(
		**site_parameters,
		filters=search_parameters)
	results = list(housing.get_results(sort_by='newest', geotagged=True))
	# apply area filter
	filtered_results = []

	for result in results:  # loop through listings
		if result["geotag"]:
			for area, coords in AREAS.items():  # loop through areas of interest
				if check_area(result["geotag"], coords):
					filtered_results.append(result)
	return filtered_results
