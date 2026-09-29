import add_data
import file_read_write
import show_graphs
# importing datetime to get current time
from datetime import datetime

def run_program():
    while True:
        print("\n=== SCREEN TIME TRACKER MENU ===")
        print("1. Log new app usage")
        print("2. Show my report card")
        print("3. Show bar chart graph")
        print("4. Reset all data")
        print("5. Exit program")
        
        user_choice = input("Enter your choice (1-5): ")
        
        if user_choice == '1':
            app = input("Which app did you use? (eg. YouTube, VS Code): ")
            print("Categories: Productive, Education, Entertainment, Social Media, Gaming")
            cat = input("Type category from above: ")
            time_input = input("How many minutes? ")
            
            # basic check if user entered a number
            if time_input.isdigit() == True:
                mins = int(time_input)
                now = datetime.now().strftime("%Y-%m-%d %H:%M")
                
                # create object and save
                s = add_data.ScreenSession(app, cat, mins, now)
                file_read_write.save_new_record(s.make_list())
                print("--> Data saved successfully!")
            else:
                print("Error! Please enter a valid number for minutes.")
                
        elif user_choice == '2':
            data = file_read_write.get_all_data()
            if len(data) == 0:
                print("No data found! Please add some first.")
            else:
                show_graphs.print_report(data)
                
        elif user_choice == '3':
            data = file_read_write.get_all_data()
            show_graphs.print_bar_chart(data)
                
        elif user_choice == '4':
            ans = input("Are you sure you want to delete all? (yes/no): ")
            if ans == "yes":
                file_read_write.delete_everything()
                print("All data cleared!")
                
        elif user_choice == '5':
            print("Exiting... Have a good day!")
            break
            
        else:
            print("Wrong input. Try again.")

# Run the project
if __name__ == "__main__":
    run_program()