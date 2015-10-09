# ZomatoData

A Scrapy project to scrape restaurant information from [Zomato](www.zomato.com).
Currently only restaurant information from New Delhi, Kolkata, Mumbai,
Hyderabad, Chennai, Bangalore, Mysore have been scraped. 

## Data
The scraped data can be found in `\data` and it contains three files `restaurants.csv`, `cuisines.csv`, `collections.csv`. Each restaurant in the dataset is uniquely identified by its `r_id`. `restaurants` contains the following variables:

- `r_type`: Whether the listing is a casual dining restaurant, a fine-dining restaurant, a cafe etc.
- `r_name`
- `area`
- `bookmarks`: # bookmarks of the restaurant made using the bookmark feature in the website
- `checkins`: Check-ins using the "been here" feature
- `city`
- `cost`: Cost for two in rupees
- `r_address`
- `link`
- `photos`: No. of photos of the restaurant uploaded to the service
- `r_id`
- `r_latitude`: Latitude coordinate of the restaurant's location
- `r_longitude`: Longitude coordinate of the restaurant's location
- `rating`: Average rating out of 5
- `rating_votes`: Number of ratings
- `reviews`: Number of reviews
