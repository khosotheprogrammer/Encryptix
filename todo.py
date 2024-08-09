import sqlite3
con = sqlite3.connect("todo.db")
cursor = con.cursor()
try:
    cursor.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
except sqlite3.OperationalError:
    pass
while True:
    print("TO DO LIST")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Task")
    print("4. Update Task")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        status = input("Enter status (done/pending): ")
        while status not in ['done', 'pending']:
            print("Invalid status. Please enter 'done' or 'pending'.")
            status = input("Enter status (done/pending): ")
        cursor.execute("INSERT INTO todo (task, status) VALUES (?, ?)", (task, status))
        con.commit()
        print("Task added successfully")

    elif choice == 2:
        task = input("Enter task: ")
        cursor.execute("DELETE FROM todo WHERE task=?", (task,))
        con.commit()
        print("Task deleted successfully")

    elif choice == 3:
        cursor.execute("SELECT * FROM todo")
    
        rows = cursor.fetchall()
        for row in rows:
                if row[2] == 'done':
                    print(f"[DONE] {row[1]}")
                else:
                    print(f"[PENDING] {row[1]}")

    elif choice == 4:
        task = input("Enter task: ")
        status = input("Enter status (done/pending): ")
        while status not in ['done', 'pending']:
            print("Invalid status. Please enter 'done' or 'pending'.")
            status = input("Enter status (done/pending): ")
        cursor.execute("UPDATE todo SET status=? WHERE task=?", (status, task))
        con.commit()
        print("Task updated successfully")

    elif choice == 5:
        cursor.close()
        con.close()
        print("Exiting...")
        exit()

    input("Press Enter to continue...")
    # Clear the screen
    print("\033c")
