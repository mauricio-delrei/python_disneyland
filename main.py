from tui import display_title, main_menu, view_data_submenu, visualize_data_submenu, get_user_input
from process import (
    read_csv_file, view_reviews_by_park, number_of_reviews_by_park_and_location,
    average_score_per_year_by_park, average_score_per_park_by_reviewer_location
)
from visual import visualize_most_reviewed_parks, visualize_average_scores, park_ranking_by_nationality, most_popular_month_by_park

def handle_view_data_choice(sub_choice, data):
    if sub_choice == 'A':
        view_reviews_by_park(data)
    elif sub_choice == 'B':
        number_of_reviews_by_park_and_location(data)
    elif sub_choice == 'C':
        average_score_per_year_by_park(data)
    elif sub_choice == 'D':
        average_score_per_park_by_reviewer_location(data)
    else:
        print("Invalid choice.")

def handle_visualize_data_choice(sub_choice, data):
    if sub_choice == 'A':
        visualize_most_reviewed_parks(data)
    elif sub_choice == 'B':
        visualize_average_scores(data)
    elif sub_choice == 'C':
        park_ranking_by_nationality(data)
    elif sub_choice == 'D':
        most_popular_month_by_park(data)
    else:
        print("Invalid choice.")

def main():
    display_title("Disneyland review analyzer")
    data = read_csv_file("data/disneyland_reviews.csv")

    while True:
        main_menu()
        choice = get_user_input()
        print(f"You have chosen option {choice}\n")

        if choice == 'X':
            print("Exiting the program.")
            break
        elif choice == 'A':
            view_data_submenu()
            sub_choice = get_user_input()
            print(f"You have chosen option {sub_choice}")
            handle_view_data_choice(sub_choice, data)
        elif choice == 'B':
            visualize_data_submenu()
            sub_choice = get_user_input()
            handle_visualize_data_choice(sub_choice, data)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
