
import csv
import os
from datetime import datetime



SYLLABUS_FILE = 'syllabus_tracker_nopandas.csv'

FIELDNAMES = ['Module', 'Topic', 'Due Date', 'Status', 'Notes']



def load_syllabus():
    """Loads the syllabus from the CSV file into a list of dictionaries."""
    syllabus_data = []
    
    
    if not os.path.exists(SYLLABUS_FILE):
        print(f"Creating new syllabus file: {SYLLABUS_FILE}")
        with open(SYLLABUS_FILE, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
        return syllabus_data

   
    try:
        with open(SYLLABUS_FILE, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                syllabus_data.append(row)
        print(f"Loading existing syllabus from: {SYLLABUS_FILE}")
    except Exception as e:
        print(f"Error loading syllabus: {e}")
        
    return syllabus_data

def save_syllabus(syllabus_data):
    """Saves the syllabus (list of dicts) back to the CSV file."""
    try:
        with open(SYLLABUS_FILE, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(syllabus_data)
        print("\n✅ Syllabus saved successfully.")
    except Exception as e:
        print(f"Error saving syllabus: {e}")


def display_syllabus(syllabus_data):
    """Prints the current syllabus, sorted by Due Date."""
    if not syllabus_data:
        print("\n▶️ Syllabus is currently empty.")
        return

    
    try:
    
        sorted_data = sorted(
            syllabus_data, 
            key=lambda item: datetime.strptime(item['Due Date'], '%Y-%m-%d')
        )
    except ValueError:
        print("\n⚠️ Date format error in data! Displaying unsorted. Please ensure all dates are YYYY-MM-DD.")
        sorted_data = syllabus_data

    print("\n--- Current Syllabus Tracker ---")
    
    # Print header
    header_format = "{:<5} | {:<20} | {:<20} | {:<12} | {:<15} | {}"
    print(header_format.format("Index", "Module", "Topic", "Due Date", "Status", "Notes"))
    print("-" * 90)

    # Print data rows
    for i, entry in enumerate(sorted_data):
       
        is_overdue = False
        if entry['Status'].lower() != 'completed':
            try:
                due_date = datetime.strptime(entry['Due Date'], '%Y-%m-%d').date()
                if due_date < datetime.now().date():
                    is_overdue = True
            except ValueError:
                pass 

        row_str = header_format.format(
            i, 
            entry['Module'][:20], 
            entry['Topic'][:20], 
            entry['Due Date'], 
            entry['Status'][:15], 
            entry['Notes']
        )
        
        if is_overdue:
            
            print(f"\033[91m{row_str} <--- OVERDUE!\033[0m") # ANSI escape code for red
        else:
            print(row_str)
            
    print("-" * 90)

def add_entry(syllabus_data):
    """Adds a new entry (dictionary) to the syllabus list."""
    print("\n--- Add New Entry ---")
    module = input("Enter Module Name (e.g., 'Chapter 1'): ")
    topic = input("Enter Topic/Lesson: ")
    
    
    while True:
        due_date_str = input("Enter Due Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(due_date_str, '%Y-%m-%d')
            break
        except ValueError:
            print("❌ Invalid date format. Please enter date as YYYY-MM-DD.")
            
    status = input("Enter Status (e.g., 'Planned', 'In Progress', 'Completed'): ")
    notes = input("Enter Notes (optional): ")

    new_entry = {
        'Module': module,
        'Topic': topic,
        'Due Date': due_date_str,
        'Status': status,
        'Notes': notes
    }
    
    syllabus_data.append(new_entry)
    print(f"\n➕ Added: {topic} ({module})")
    return syllabus_data

def update_entry(syllabus_data):
    """Updates the details of an existing entry."""
    if not syllabus_data:
        print("\n⚠️ Syllabus is empty. Nothing to update.")
        return syllabus_data
        
    display_syllabus(syllabus_data)
    
    
    try:
        index_to_update = int(input("Enter the Index number of the entry to update: "))
        
    
        sorted_data = sorted(
            syllabus_data, 
            key=lambda item: datetime.strptime(item['Due Date'], '%Y-%m-%d')
        )
        
        if 0 <= index_to_update < len(sorted_data):
            # Get the actual item (dictionary) from the sorted list
            entry_to_update = sorted_data[index_to_update] 
            
            print(f"\nEditing entry:\n{entry_to_update}")
            
            field = input("Which field do you want to update (Module, Topic, Status, Due Date, Notes)? ").strip()
            
            if field in FIELDNAMES:
                new_value = input(f"Enter new value for **{field}**: ")
                
                # Update the value in the actual dictionary object
                entry_to_update[field] = new_value 
                
                print(f"☑️ Updated **{entry_to_update['Topic']}** | {field} to: **{new_value}**")
            else:
                print("⚠️ Invalid field name.")
        else:
            print("❌ Invalid index number.")
            
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return syllabus_data

def delete_entry(syllabus_data):
    """Deletes an existing entry from the syllabus."""
    if not syllabus_data:
        print("\n⚠️ Syllabus is empty. Nothing to delete.")
        return syllabus_data

    display_syllabus(syllabus_data)

    try:
        index_to_delete = int(input("Enter the Index number of the entry to **DELETE**: "))
        
        # Re-sort to get the correct item based on the displayed index
        sorted_data = sorted(
            syllabus_data, 
            key=lambda item: datetime.strptime(item['Due Date'], '%Y-%m-%d')
        )

        if 0 <= index_to_delete < len(sorted_data):
            # Get the actual dictionary object to remove
            entry_to_remove = sorted_data[index_to_delete]
            topic_to_delete = entry_to_remove['Topic']
            
            confirm = input(f"Are you sure you want to delete '{topic_to_delete}'? (yes/no): ").strip().lower()

            if confirm == 'yes':
                # Remove the dictionary object from the main list
                syllabus_data.remove(entry_to_remove)
                print(f"🗑️ Successfully deleted entry: **{topic_to_delete}**.")
            else:
                print("Deletion cancelled.")
        else:
            print("❌ Invalid index number.")
            
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return syllabus_data

# --- Main Program Logic ---

def main():
    """The main loop for the Syllabus Tracker."""
    # Load the syllabus data when the program starts
    syllabus_data = load_syllabus()

    while True:
        print("\n\n--- Syllabus Tracker Menu ---")
        print("1: **View** Syllabus (Sorted by Date)")
        print("2: **Add** New Entry")
        print("3: **Update** Entry Details")
        print("4: **Delete** an Entry")
        print("5: **Exit** and Save")
        print("-" * 35)

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_syllabus(syllabus_data)
        elif choice == '2':
            syllabus_data = add_entry(syllabus_data)
        elif choice == '3':
            syllabus_data = update_entry(syllabus_data)
        elif choice == '4':
            syllabus_data = delete_entry(syllabus_data)
        elif choice == '5':
            save_syllabus(syllabus_data)
            print("\n👋 Exiting Syllabus Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
    

