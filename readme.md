# sysllbus tracker

# Overview of the project
This python application serves as a SYLLABUS TRACKER. It allows the users :- 
1)To view the subjects
2)To edit syllabus
3)	To calculate the completed syllabus
4)	To update the progress
5)	To add compliment
It’s primary features are presented through a simple, interactive timetable  Users can select: 
•	 Data Management: It uses Python's built-in csv module to save and load syllabus items (Modules, Topics, Due Dates, Statuses) as a list of dictionaries.
•	Tracking Features: It displays the syllabus sorted by date and highlights any items that are overdue in red.
•	User Interaction: It provides a main menu allowing users to View, Add, Update, or Delete entries.

PROBLEM STATEMENT 
 
The core problem addressed by this system is the need for a simple, reliable and user-friendly digital system to manage the fundamental operations of syllabus and portion
The fundamental problem this system seeks to solve is the operational inefficiency and potential for error inherent in manual or legacy systems used by students  and instructor  to manage their syllabus functions. 
The goal is to provide a reliable, modular and easy-touse digital solution that enhances accuracy and student experience. 
 	 
 
# Features 
 1. Data Management (Persistence)
•	FR1.1: Load Syllabus Data: The system must be able to read existing syllabus entries from the designated CSV file (syllabus_tracker_nopandas.csv) upon startup.
•	FR1.2: Create New File: If the CSV file does not exist, the system must create a new file and write the header row.
•	FR1.3: Save Syllabus Data: The system must be able to write the current in-memory syllabus data (list of dictionaries) back to the CSV file when the user selects the "Exit and Save" option.

2. Syllabus Manipulation (CRUD Operations)

•	FR2.1: Add Entry (Create): The system must allow the user to input details (Module, Topic, Due Date, Status, Notes) and add a new entry to the syllabus list.<br>
o	Sub-Requirement: The system must validate that the Due Date is entered in the YYYY-MM-DD format.<br>
•	FR3.2: Indicate Overdue Items: The system must check the current date against the Due Date and, if the entry's Status is not 'Completed' and the Due Date is in the past, it must visually mark the item as OVERDUE (using red text/ANSI codes).<br>

4.. User Interface and Control<br>

•	FR4.1: Display Menu: The system must present a clear, numbered menu of available actions (View, Add, Update, Delete, Exit/Save) to the user in a loop until the user chooses to exit<br>

•	FR4.2: Handle Invalid Input: The system must detect and handle invalid menu choices or non
numeric index inputs gracefully by notifying the user and returning to the menu<br>


# Technologies/tools used 
1.	Unit Testing 
Each isolated function should be tested to ensure it performs its specific task correctly. Since this is a console application, unit testing will often involve setting up expected input and checking the function's output or side effects (like file content).
Integration tests confirm that the functions work correctly together as part of a full user workflow. This mimics how a real user would interact with the main() loop.
 2. Integration Testing (Workflow Verification)
1.	Full CRUD Cycle: Start the program, Add a new entry, Update its status, View the syllabus, Delete the entry, and then Exit and Save. Rerun the program to verify the deleted entry is gone.
2.	Date Sorting and Overdue Check: Add entries with dates: one completed and past, one incomplete and past (overdue), one incomplete and future. View the syllabus to ensure the sort order is correct and the overdue item is flagged.
3.	Update on Sorted Index: View the sorted syllabus. Note the index of a specific entry (e.g., index 0). Use the Update option with that index. Verify that the correct item in the original unsorted list of dictionaries was modified.

3. Error and Robustness Testing (Negative Testing)
This focuses on intentionally causing problems to ensure the program handles exceptions gracefully without crashing.

4. Regression Testing
After any change or feature addition (e.g., adding a search feature), run the critical test cases from steps 1 and 2 to ensure the new code has not broken any existing functionality (like loading or saving data correctly


 



# Steps to install & run the project
enter the number and get the selected menu
# Instructions for testing 
1. Indexing Confusion in Sorted View
This is the most significant challenge in your current design.
•	The Problem: The display_syllabus() function sorts the data by date before displaying it and assigns an index (0, 1, 2...). However, the actual in-memory list (syllabus_data) remains in its original (unsorted) order. When the user selects an index to Update or Delete, the code must re-sort the list to find the correct dictionary object to modify or remove.
•	The Risk: If the sorting logic in display_syllabus(), update_entry(), and delete_entry() ever becomes inconsistent, the user could inadvertently update or delete the wrong item, leading to data corruption.
2. Date Format Strictness
•	The Problem: Your code relies strictly on the YYYY-MM-DD format (e.g., 2025-11-24) for sorting and overdue checks. If a user manually edits the CSV file or enters a date in a slightly different but valid format (e.g., 2025/11/24), the datetime.strptime() function will raise a ValueError, causing issues with sorting and the overdue check.
3. Lack of Unique ID
•	The Problem: The current system uses the displayed row index as the key identifier for updates and deletions. This index is volatile, changing every time the list is sorted or a new item is added/removed.
•	The Solution/Challenge: Without a unique, immutable identifier (like an auto-generated UUID or timestamp) stored in the CSV for each entry, operations rely entirely on the positional index, which is prone to the indexing confusion noted above.
4. Limited Input Validation
•	The Problem: Only the Due Date has robust input validation. Users can enter any text for Status (e.g., Comleted, InPrgress), which leads to inconsistent data that cannot be reliably filtered later. They can also enter very long strings for Module or Topic, which could break the formatting in the display_syllabus() output.
5. Repetitive Update Process
•	The Problem: To simply mark a task as "Completed," the user must: 1) View the syllabus, 2) Choose the Update option, 3) Enter the index, 4) Enter the field name (Status), and 5) Enter the new value (Completed).
•	The Improvement: This multi-step process is cumbersome for frequent status changes.
6. Command-Line Limitations
•	The Problem: It's a command-line interface (CLI). Users cannot click, scroll easily, or use the mouse. Managing a large syllabus (20+ items) in a CLI environment can quickly become visually overwhelming, despite your good formatting.
7. Global Variable Dependence
•	The Problem: Constants like SYLLABUS_FILE and FIELDNAMES are defined globally. While simple for this script, in larger applications, this tight coupling makes it harder to reuse functions or change configurations without modifying the core file.
8. Handling File Conflicts
•	The Problem: If two programs (or two processes) tried to write to syllabus_tracker_nopandas.csv at the same time, the save_syllabus function could result in a race condition, potentially corrupting or losing data. Since the file is only saved upon exit, any crash will result in the loss of all changes made during that session.

 input their thoughts. This facilitates data-driven quality assurance. 
 

 



# Screenshots (optional but recommended)
