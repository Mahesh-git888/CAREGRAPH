# test_location_tool.py

import requests
from config import FOURSQUARE_API_KEY, FOURSQUARE_API_VERSION

BASE_URL = "https://places-api.foursquare.com/places"

HEADERS = {
    "accept": "application/json",
    "authorization": f"Bearer {FOURSQUARE_API_KEY}",
    "X-Places-Api-Version": FOURSQUARE_API_VERSION
}


def search_therapists(lat: float, lng: float, limit: int = 5):
    url = f"{BASE_URL}/search"
    params = {
        "ll": f"{lat},{lng}",
        "radius": 5000,
        "query": "therapist psychologist psychotherapist counselor",
        "limit": limit
    }

    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()["results"]


def get_place_details(fsq_place_id: str):
    url = f"{BASE_URL}/{fsq_place_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()


def find_nearby_therapists(lat: float, lng: float) -> str:
    places = search_therapists(lat, lng)

    if not places:
        return "No therapists found."

    output = [f"Therapists near ({lat}, {lng}):"]

    for place in places:
        fsq_id = place["fsq_place_id"]
        details = get_place_details(fsq_id)

        name = details.get("name", "Unknown")
        address = details.get("location", {}).get(
            "formatted_address", "Address not available"
        )
        phone = details.get("tel", "Phone not available")
        website = details.get("website", "Website not available")

        output.append(
            f"- {name} | {address} | {phone} | {website}"
        )

    return "\n".join(output)


if __name__ == "__main__":
    # New York coordinates
    LAT = 40.7128
    LNG = -74.0060

    print(find_nearby_therapists(LAT, LNG))
