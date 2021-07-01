import json
from jobs_info_scraper import get_jobs, get_matching_jobs

def main():
    print("JOBS SEARCHING TOOL")
    print("-----------------------")
    menu = {
        "1": "Scrape the Internet for Jobs or update list of existing jobs.",
        "2": "Get jobs that match your skills.",
        "3": "Exit."
    }
    while True:
        options = menu.keys()
        for option in options:
            print(f"{option}. {menu[option]}")
        print("-----------------------")
        user_input = input("Please select an option: ")
        if user_input == "1":
            get_jobs()
        elif user_input == "2":
            get_matching_jobs()
        elif user_input == "3":
            break
        else:
            print("Unknown instruction. Try again.\n")

if __name__ == "__main__":
    main()
