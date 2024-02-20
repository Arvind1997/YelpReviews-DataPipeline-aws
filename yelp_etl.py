import requests
import pandas as pd
        
def etl_airflow_run():
            
    url = 'https://api.yelp.com/v3/businesses/search'
    key = 'P-rv2JVRSFz6qcX8tmZctCHkwtrMFVhJE5FsA1pXg60xp03x4V8epDVLWSbdNbzwElukaMEstSvd6Abj25Wx5kKRWNROk5dxTROsVDNKR6JpD-AgMW3ZAT8JYnvNZXYx'
                
    headers = {
                    'Authorization': 'Bearer %s' % key
    }
            
    location = ['Sacramento, CA', 'Southern California, CA', 'New York City, NY', 'Los Angeles, CA', 'San Francisco, CA', 'Seattle, WA', 'Portland, OR',
               'Las Vegas, LA', 'boise, ID', 'Helena, MT', 'Cheyenne, WY', 'Austin, TX', 'Honolulu, HI', 'Tallahassee, FL', 'Montgomery, AL', 'Lansing, MI',
               'Detroit, MI', 'Juneau, AK', 'Columbus, OH', 'Harrisburg, PA', 'Denver, CO', 'Saint Paul, MN', 'Nashville, TN', 'Des Moines, IA', 
               'Raileigh, NC', 'Augusta, ME', 'Boston, MA', 'Phoenix, AZ', 'Concord, NH', 'Salem, OR', 'Columbia, SC', 'Jefferson City, MO', 'Hartford, CT',
               'Salt Lake City, UT', 'Annapolis, MD', 'Madison, WI', 'Richmond, VA', 'Frankfurt, KY', 'Louisville, KY', 'Baton Rouge, LA', 
               'Oklahoma City, OK', 'Jackson, MS', 'Mont pelier, VT', 'Little Rock, AR', 'Santa Fe, NM', 'Providence, RI', 'Indianapolis, IN',
               'Bloomington, IN', 'Topeka, KS', 'Lincoln, NE', 'Carson City, NV', 'Olympia, WA', 'Dover, DE', 'Charleston, WV', 'Bismarck, ND', 'Albany, NY',
               'Pierre, SD', 'Jersey City, NJ', 'Miami, FL', 'Orlando, FL', 'Tulsa, OK', 'Tampa, FL', 'Key West, FL', 'Chicago, IL', 'Springfield, IL', 
               'San Diego, CA', 'Philadelphia, PA', 'Cincinnati, OH', 'Charlotte, NC', 'Pittsburgh, PA', 'Ann Arbor, MI', 'Fort Wayne, IN', 'Cleveland, OH',
               'Dallas, TX', 'Houston, TX', 'Fort Worth, TX', 'San Antonio, TX', 'New Orleans, LA', 'Jacksonville, FL', 'Fort Lauderdale, FL',
               'West Palm Beach, FL', 'Knoxville, TN', 'Washington D.C', 'Memphis, TN']

    restaurant_info = { '_id': [], 'Name': [], 'Type': [], 'Review-Count': [], 'Categories': [], 'Ratings': [], 'Latitude': [], 'Longitude': [], 'Transactions': [], 
                   'Address': [], 'City': [], 'Zipcode': [], 'State': [], 'Phone': [], 'Distance': [] }

    types = ['restaurants', 'bars']

    for j in types:
                    
        for i in location:
                        parameters = {
                            'location': i,
                            'term': 'Bars',
                            'radius': 40000
        }
        response = requests.get(url, headers = headers, params=parameters)
        query = response.json()['businesses']
        for q in query:
                            restaurant_info['_id'].append(q['id'])
                            restaurant_info['Name'].append(q['name'])
                            restaurant_info['Type'].append(j)
                            restaurant_info['Review-Count'].append(q['review_count'])
                            restaurant_info['Categories'].append(q['categories'])
                            restaurant_info['Ratings'].append(q['rating'])
                            restaurant_info['Latitude'].append(q['coordinates']['latitude'])
                            restaurant_info['Longitude'].append(q['coordinates']['longitude'])
                            restaurant_info['Transactions'].append(q['transactions'])
                            restaurant_info['Address'].append(q['location']['address1'])
                            restaurant_info['City'].append(q['location']['city'])
                            restaurant_info['Zipcode'].append(q['location']['zip_code'])
                            restaurant_info['State'].append(q['location']['state'])
                            restaurant_info['Phone'].append(q['phone'])
                            restaurant_info['Distance'].append(q['distance'])
    restaurants_info_dfs = pd.DataFrame(restaurant_info)
    restaurants_info_dfs.to_csv("s3://yelp-ec2-airflow/yelp_reviews.csv")