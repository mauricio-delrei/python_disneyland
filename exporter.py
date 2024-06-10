import json
import csv

class Exporter:
    def __init__(self, data):
        self.data = data

    def export_to_txt(self, output_file):
        with open(output_file, 'w') as file:
            for park, info in self._aggregate_park_data().items():
                file.write(f"{park}\n")
                file.write(f"Number of reviews: {info['num_reviews']}\n")
                file.write(f"Number of positive reviews: {info['num_positive_reviews']}\n")
                file.write(f"Average review score: {info['average_score']}\n")
                file.write(f"Number of countries reviewed: {info['num_countries']}\n\n")

    def export_to_csv(self, output_file):
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Park", "Number of reviews", "Number of positive reviews", "Average review score", "Number of countries reviewed"])
            for park, info in self._aggregate_park_data().items():
                writer.writerow([park, info['num_reviews'], info['num_positive_reviews'], info['average_score'], info['num_countries']])

    def export_to_json(self, output_file):
        with open(output_file, 'w') as file:
            json.dump(self._aggregate_park_data(), file, indent=4)

    def _aggregate_park_data(self):
        park_data = {}
        for review in self.data:
            park = review[4]
            if park not in park_data:
                park_data[park] = {'num_reviews': 0, 'num_positive_reviews': 0, 'total_score': 0, 'num_countries': set()}
            park_data[park]['num_reviews'] += 1
            park_data[park]['total_score'] += int(review[1])
            if int(review[1]) > 3:  # Assuming a positive review has a score greater than 3
                park_data[park]['num_positive_reviews'] += 1
            park_data[park]['num_countries'].add(review[3])  # Reviewer location
        for park, info in park_data.items():
            info['average_score'] = info['total_score'] / info['num_reviews']
            info['num_countries'] = len(info['num_countries'])
        return park_data
