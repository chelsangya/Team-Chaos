import requests
import csv

API_KEY = "AIzaSyBjFCTyNQnHFpRjg7gLmH6op_R_Meimg3M"

def get_restaurants(location, radius=900, keyword="restaurants"):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key": API_KEY,
        "location": location,
        "radius": radius,
        "keyword": keyword
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data.get("results", [])

def save_to_csv(restaurants, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Latitude", "Longitude", "Rating", "Reviews"])
        for restaurant in restaurants:
            name = restaurant.get("name", "N/A")
            lat = restaurant.get("geometry", {}).get("location", {}).get("lat", "N/A")
            lng = restaurant.get("geometry", {}).get("location", {}).get("lng", "N/A")
            rating = restaurant.get("rating", "N/A")
            reviews = restaurant.get("user_ratings_total", "N/A")

            writer.writerow([name, lat, lng, rating, reviews])

def main():
    # Define the location (latitude and longitude) for the search
    location = "27.705795, 85.322714"

    # Fetch restaurant data
    restaurants = get_restaurants(location)

    if not restaurants:
        print("No restaurants found.")
        return

    # Save restaurant data to CSV file
    save_to_csv(restaurants, "restaurant_data15.csv")
    print("Restaurant data exported to restaurant_data.csv")

if __name__ == "__main__":
    main()
