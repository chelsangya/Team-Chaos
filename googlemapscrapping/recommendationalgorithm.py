import numpy as np
import pandas as pd
import googlemaps
import requests

data_file = 'D:/HACKATHON/Team-Chaos/googlemapscrapping/restaurant_data.csv'
df = pd.read_csv(data_file)

user_latitude = 27.705161 
user_longitude = 85.314003 



def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    d_lat = lat2 - lat1
    d_lon = lon2 - lon1
    a = np.sin(d_lat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(d_lon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    earth_radius_km = 6371.0  # Earth radius in kilometers
    distance = earth_radius_km * c
    print(distance)
    return distance


def distance_between_locations(lat1, lon1, lat2, lon2):
    origin = '{},{}'.format(lat1, lon1)
    destination = '{},{}'.format(lat2, lon2)
    get_walking_directions(origin, destination)

df['Distance'] = haversine_distance(user_latitude, user_longitude, df['Latitude'], df['Longitude'])


ratings = df["Rating"]
num_reviews = df["Reviews"]
percentile_ratings = np.percentile(ratings, (num_reviews / np.sum(num_reviews)) * 100)

df = df.sort_values(by='Distance')

df['Percentile_Rating'] = percentile_ratings

num_top_restaurants = 15
df_top_15 = df.head(num_top_restaurants)

df_top_15 = df_top_15.sort_values(by='Percentile_Rating', ascending=False)

print("Top restaurant recommendations:")
for i, recommendation in enumerate(df_top_15.iterrows(), 1):
    print(f"{i}. {recommendation[1]['Name']} (Rating: {recommendation[1]['Rating']}, Distance: {recommendation[1]['Distance']} km, Percentile Rating: {recommendation[1]['Percentile_Rating']}%)")
