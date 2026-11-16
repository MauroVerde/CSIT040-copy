import csv
import os
from datetime import datetime, date

pri_order = {"High": 1, "Medium": 2, "Low": 3}

def save_tasks(tasks):
    with open("sample.csv", "w", newline="") as file:
      writer = csv.DictWriter(file, fieldnames=["name", "course", "deadline", "priority", "completed"])
      writer.writeheader()
      writer.writerows(tasks)
tasks = []
if os.path.exists("sample.csv"):
    with open("sample.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["completed"] = (row["completed"] == "True")
            tasks.append(row)


for task in tasks:
    print(task["name"], "-", task["course"], "- due", task["deadline"])


def add_task(tasks):
   name = input("Task name: ")
   course = input("Course name: ")
   while True:
      deadline = input("Deadline (YYYY-MM-DD)")
      try:
         datetime.strptime(deadline, "%Y-%m-%d")
         break
      except ValueError:
         print("Incorrect format, try again! (YYYY-MM-DD)")
   while True:
      priority = input("Priority (High-Medium-Low): ").capitalize()
      if priority not in pri_order:
         print("Enter a valid priority order (High-Medium-Low): ")
      else:
         break
   task = {
       "name": name,
       "course": course,
       "deadline": deadline,
       "priority": priority,
       "completed": False
    }  
   tasks.append(task)
   save_tasks(tasks)
   print("Task added!")


def view_task(tasks):
   for task in tasks:
      print(task["name"], " - ", task["course"], "- ", task["deadline"])

def complete_task(tasks):
   name = input("Enter task name: ")
   for task in tasks:
      if task["name"] == name:
         task["completed"] = True
         save_tasks(tasks)
         print("Task completed! ")
         return
   print("Task not found!")
    
def overdue_task(tasks):
   found = False
   for task in tasks:
      if task["completed"]:
         continue
      deadline = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
      days = (deadline - date.today()).days
      if days < 0:
         print("Overdue: ", task["name"], "- was due", -days, "days ago")
         return

   print("No tasks found!")

def check_deadline(tasks):
   name = input("Enter task name: ")
   for task in tasks: 
      if task["name"] == name:
         deadline = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
         days = (deadline - date.today()).days
         if days < 0:
             print("Overdue: ", task["name"], "- was due", -days, "days ago")
         else: 
             print(task["name"], "- ", days, "days until deadline")
         return
   print("Task not found")

def summary(tasks):

   done = 0
   total = len(tasks)
   overdue = 0
   for task in tasks:
      deadline = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
      if deadline < date.today() and not task["completed"]:
         overdue += 1 
   for task in tasks:
      if task["completed"]:
         done += 1
   print("\n--- Summary ---")
   print("Total:     ", total)
   print("Completed:     ", done)
   print("Pending:     ", total - done)
   print("Overdue:     ", overdue)

def delete_task(tasks):
   name = input("Enter task name to delete: ")
   for task in tasks:
      if task["name"] == name:
         tasks.remove(task)
         save_tasks(tasks)
         print("Task deleted!")
         return
   print("Task not found!")

def completed_task(tasks):
   found = False
   for task in tasks:
      if task["completed"]:
         print(task["name"], "-", task["deadline"])
         found = True
   if not found:
      print("No tasks found!")

while True:
    print("\n1. Add tasks")
    print("2. View tasks")
    print("3. Remove tasks")
    print("4. Mark as completed")
    print("5. Check overdue tasks")
    print("6. Show Summary")
    print("7. Check completed tasks")
    print("8. Check task deadline")
    print("9. Quit")
    choice = input("Enter a choice: ")

    if choice == "1":
       add_task(tasks)
    elif choice == "2":
       view_task(tasks)
    elif choice == "3":
       delete_task(tasks)
    elif choice == "4":
       complete_task(tasks)
    elif choice == "5":
       overdue_task(tasks)
    elif choice == "6":
       summary(tasks)
    elif choice == "7":
       completed_task(tasks)
    elif choice == "8":
       check_deadline(tasks)
    elif choice == "9":
        break
    else:
        print("Invalid Option")
