import matplotlib.pyplot as plt
from collections import defaultdict

# "Setting BRANCH_NAMES here to be used in the visualization functions."
BRANCH_NAMES = {
    "disneyland_california": "Disneyland_California",
    "disneyland_paris": "Disneyland_Paris",
    "disneyland_hongkong": "Disneyland_HongKong",
    "paris": "Disneyland_Paris",
    "hong_kong": "Disneyland_HongKong",
    "hongkong": "Disneyland_HongKong",
    "california": "Disneyland_California",
}

def visualize_most_reviewed_parks(data):
    park_reviews_count = defaultdict(int)
    for review in data:
        park_reviews_count[review[4]] += 1

    labels = park_reviews_count.keys()
    sizes = park_reviews_count.values()

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Number of Reviews for Each Park')
    plt.show()

def visualize_average_scores(data):
    park_average_scores = defaultdict(list)
    for review in data:
        park_average_scores[review[4]].append(int(review[1]))

    park_names = list(park_average_scores.keys())
    average_scores = [sum(scores) / len(scores) for scores in park_average_scores.values()]

    plt.bar(park_names, average_scores)
    plt.xlabel('Park')
    plt.ylabel('Average Score')
    plt.title('Average Scores for Each Park')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def park_ranking_by_nationality(data):
    park = input("Enter the park name: ").lower()
    reviews_by_park = [review for review in data if review[4].replace(' ', '_').lower() == BRANCH_NAMES.get(park, park).lower()]

    nationality_ratings = defaultdict(list)
    for review in reviews_by_park:
        nationality = review[3]
        rating = int(review[1])
        nationality_ratings[nationality].append(rating)

    top_nationalities = sorted(nationality_ratings.items(), key=lambda x: sum(x[1]) / len(x[1]), reverse=True)[:10]

    nationalities = [nationality[0] for nationality in top_nationalities]
    average_ratings = [sum(nationality[1]) / len(nationality[1]) for nationality in top_nationalities]

    plt.bar(nationalities, average_ratings)
    plt.xlabel('Nationality')
    plt.ylabel('Average Rating')
    plt.title(f'Top 10 Nationalities with Highest Average Rating for {BRANCH_NAMES.get(park, park)}')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def most_popular_month_by_park(data):
    park = input("Enter the park name: ").lower()
    reviews_by_park = [review for review in data if review[4].replace(' ', '_').lower() == BRANCH_NAMES.get(park, park).lower()]

    month_count = defaultdict(int)
    for review in reviews_by_park:
        if len(review) > 2:  # "Check if the 'review' list has at least 3 elements."
            year_month = review[2]
            if '-' in year_month:  # "Check if the string 'year_month' contains the character '-'." '-'
                month = year_month.split('-')[1]
                month_count[month] += 1

    months = list(month_count.keys())
    counts = list(month_count.values())

    plt.bar(months, counts)
    plt.xlabel('Month')
    plt.ylabel('Number of Reviews')
    plt.title(f'Most Popular Months for {BRANCH_NAMES.get(park, park)}')
    plt.xticks(rotation=45, ha='right')
    plt.show()

