import csv
from collections import defaultdict

REVIEW_ID_INDEX = 0
RATING_INDEX = 1
YEAR_MONTH_INDEX = 2
REVIEWER_LOCATION_INDEX = 3
BRANCH_INDEX = 4

BRANCH_NAMES = {
    "disneyland_california": "Disneyland_California",
    "disneyland_paris": "Disneyland_Paris",
    "disneyland_hongkong": "Disneyland_HongKong",
    "paris": "Disneyland_Paris",
    "hong_kong": "Disneyland_HongKong",
    "hongkong": "Disneyland_HongKong",
    "california": "Disneyland_California",
}

def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    print("\nDataset loaded. Total rows:", len(data))
    return data

def find_reviews_by_park(reviews, park):
    park = park.lower()
    mapped_park = BRANCH_NAMES.get(park, park)
    return [review for review in reviews if review[BRANCH_INDEX].replace(' ', '_').lower() == mapped_park.lower()]

def find_reviews_by_location(reviews, location):
    location = location.lower()
    return [review for review in reviews if review[REVIEWER_LOCATION_INDEX].lower() == location]

def find_reviews_by_year(reviews, year):
    return [review for review in reviews if review[YEAR_MONTH_INDEX].startswith(str(year))]

def calculate_rating_average_to_reviews(reviews):
    total = sum(int(review[RATING_INDEX]) for review in reviews)
    return total / len(reviews) if reviews else 0

def view_reviews_by_park(data):
    park = input("Enter the park name: ").lower()
    reviews = find_reviews_by_park(data, park)
    if reviews:
        for review in reviews:
            print(review)
    else:
        print("Park not found or no reviews found for the specified park.")        

def number_of_reviews_by_park_and_location(data):
    park = input("Enter the park name: ").lower()
    reviews_by_park = find_reviews_by_park(data, park)
    location = input("Enter the reviewer's location: ").lower()
    reviews_by_park_and_location = find_reviews_by_location(reviews_by_park, location)
    if reviews_by_park_and_location:
        print(f"Number of reviews for {park} from {location}: {len(reviews_by_park_and_location)}")
    else:
        print(f"No reviews found for {park} from {location}.")

def average_score_per_year_by_park(data):
    park = input("Enter the park name: ").lower()
    reviews_by_park = find_reviews_by_park(data, park)
    year = int(input("Enter the year: "))
    reviews_by_year = find_reviews_by_year(reviews_by_park, year)
    if reviews_by_year:
        average_score = calculate_rating_average_to_reviews(reviews_by_year)
        print(f"Average score for {park} in {year}: {average_score:.2f}")
    else:
        print(f"No reviews found for {park} in {year}.")

def average_score_per_park_by_reviewer_location(data):
    reviews_by_park_location = defaultdict(list)
    for review in data:
        park = review[BRANCH_INDEX].replace(' ', '_').lower()
        location = review[REVIEWER_LOCATION_INDEX].lower()
        reviews_by_park_location[(park, location)].append(int(review[RATING_INDEX]))

    for (park, location), ratings in reviews_by_park_location.items():
        average_score = sum(ratings) / len(ratings)
        print(f"Average score for {park} from {location}: {average_score:.2f}")
