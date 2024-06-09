def display_title(title):
    num_dashes = len(title)
    print("-" * num_dashes)
    print(title)
    print("-" * num_dashes)

def main_menu():
    print("\nPlease enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit\n")

def view_data_submenu():
    print("Please Enter One of the Following Options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviews Location")
    print("[C] Average Score per Year by Park")
    print("[D] Average Score per Park by Reviewer Location\n")

def visualize_data_submenu():
    print("Please Enter One of the Following Options:")
    print("[A] Most Reviewed Parks")
    print("[B] Average Scores")
    print("[C] Park Ranking by Nationality")
    print("[D] Most Popular Month by Park")

def get_user_input():
    return input("Enter your choice: ").upper()
