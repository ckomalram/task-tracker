import sys
import json
from datetime import datetime

TASK_FILE = "tasks.json"
COMMANDS = ["add" , "update", "delete", "mark-in-progress", "mark-done", "list"]

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)    
    except FileNotFoundError:
        print("FileNotFoundError ==>")
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def print_tasks(tasks):
        print("\n List Of Tasks:")
        for task in tasks:
            print(f"ID: {task['id']} | DESCRIPTION: {task['description']} | STATUS: {task['status']} ")                

def update_task(id, newDescription):
    tasks = load_tasks()
    task_id = int(id)

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = newDescription
            task["updatedAt"] = datetime.now().isoformat()
            break
    else: # only executed if not throw break action  during execution
        print(f"Task with ID {task_id} not found.")
        return
    
    save_tasks(tasks)
    print(f"Task with ID {task_id} updated sucessfully.")

def delete_task(id):
    tasks = load_tasks()
    task_id = int(id)
    tasks = [task for task in tasks if task["id"] != task_id]

    save_tasks(tasks)
    print(f"Task with ID {task_id} deleted sucessfully.")

def mark_in_progress_task(task_id):
    tasks = load_tasks()
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress" # "in-progress" "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task with ID {task_id} mark sucessfully.")
            return
    else:
        print(f"Task with ID {task_id} not found.")

def mark_done_task(task_id):
    tasks = load_tasks()
    task_id = int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done" 
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task with ID {task_id} mark sucessfully.")
            break
    else:
        print(f"Task with ID {task_id} not found.")
        return
 
def main():
    if len(sys.argv) < 2:
        print("usage : main.py <command> [options]")
        return
    
    command = sys.argv[1]

    if command not in COMMANDS:
        print(f"Unknown command: {command}")
        print("Available commands: add, update, delete, mark-in-progress, mark-done, list")
        return

    if command == "add":
        if len(sys.argv) < 3:
            print("usage: main.py add <description>")
            return
        
        description = sys.argv[2]
        tasks = load_tasks()
        task_id = len(tasks) + 1
        task = {
            "id": task_id,
            "description": description,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }
        tasks.append(task)
        save_tasks(tasks)
        print(tasks)
        print(f"Task Added successfully (ID: {task_id})")
    elif command == "list":
        tasks = load_tasks()
        # print(len(sys.argv))
        if len(sys.argv) == 2:
            if not tasks:
                print(" Not Tasks found")
            else:
                print_tasks(tasks)
        elif len(sys.argv)==3:
            status = sys.argv[2]
            filtered_tasks = [task for task in tasks if task["status"] == status]
            if not filtered_tasks:
                print(" Not Filtered Tasks  found")
            else:
                print_tasks(filtered_tasks)
        else:
            print("usage: main.py list [done|todo|in-progress]")
    elif command == "update":
        if len(sys.argv) < 4:
            print("Please, write id and new description")
        else:
            id = sys.argv[2]
            newDesc = sys.argv[3]
            update_task(id, newDesc)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please, write id")
        else:
            delete_task(sys.argv[2])
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Please, write id")
        else:
            id = sys.argv[2]
            mark_in_progress_task(id)   
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Please, write id")
        else:
            id = sys.argv[2]
            mark_done_task(id)                        
    else:
        print("Command no recognize! please try again")

        


if __name__ == "__main__":
    main()
