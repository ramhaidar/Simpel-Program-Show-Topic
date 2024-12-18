# main program
# The value of the 'Activities' key is a list containing id_activity
list_topic = [
    {
        "Title": "Dummy Topic 1",
        "Description": "This is the description for topic 1",
        "Activities": [0, 1],
    },
    {
        "Title": "Dummy Topic 2",
        "Description": "This is the description for topic 2",
        "Activities": [2],
    },
]

# The key in dict_activity is id_activity
dict_activity = {
    0: {
        "Title": "Dummy Assignment 1",
        "Type": "assignment",
        "Description": "Create a Game program",
    },
    1: {
        "Title": "Dummy Material",
        "Type": "material",
        "Description": "This week's slides",
    },
    2: {
        "Title": "Dummy Assignment 2",
        "Type": "assignment",
        "Description": "Create an LMS program",
    },
}

# function
def show_topic(list_topic, dict_activity):
    """
    Display each topic along with the details of its activities
    """
    print('----Function "show_topic" is running----')
    print("")
    for topic in list_topic:  # Access each dictionary in the list of topics
        print("Title\t\t:", topic["Title"])  # Access the value of the 'Title' key
        print("Description\t:", topic["Description"])  # Access the value of the 'Description' key
        print("List of Activities\t:")
        print("ID\t| Title\t\t\t| Type\t\t| Description\t\t")  # Table header
        print("-" * 70)
        for activity_id in topic["Activities"]:
            activity = dict_activity[activity_id]
            print(
                activity_id,
                "\t|",
                activity["Title"],
                "\t|",
                activity["Type"],
                "\t|",
                activity["Description"],
            )
        print("")

    input("Press Enter to return to the main menu...")

def main():
    """
    Main function to run the program
    """
    show_topic(list_topic, dict_activity)

if __name__ == "__main__":
    main()
