import pypyodbc
import tkinter as tk

# Establishing a connection to the database
connection_string = 'DRIVER={SQL Server};SERVER=ABD-ELRAHMAN;DATABASE=TrainStation'
conn = pypyodbc.connect(connection_string)

def addingTrainGui():
    # Create the main application window
    root = tk.Tk()
    root.title("Train Station System")
    root.geometry("400x300")

    # Admin Data
    user_name = 'admin'
    password = 'admin'

    # Adding a train (by admin)
    # Adding a train (by admin)
    # Adding a train (by admin)
    def add_train(train_id, train_name, source_station, destination_station, total_seats):
        cursor = conn.cursor()
        query = f"SELECT train_id FROM Train WHERE train_id = '{train_id}'"
        cursor.execute(query)
        existing_train = cursor.fetchone()

        if existing_train:
            error_label.config(text="Train ID already exists in the database.")
        else:
            insert_query = f"INSERT INTO Train (train_id, train_name, source_station, destination_station, total_seats) VALUES ('{train_id}', '{train_name}', '{source_station}', '{destination_station}', '{total_seats}')"
            cursor.execute(insert_query)
            conn.commit()
            error_label.config(text="Train added successfully!")



    # Function to handle the form submission
    # Function to handle the form submission
    def submit_form():
        error_label.config(text="")
        train_id = int(train_id_entry.get())
        train_name = train_name_entry.get()
        source_station = source_station_entry.get()
        destination_station = destination_station_entry.get()
        total_seats = int(total_seats_entry.get())
        add_train(train_id, train_name, source_station, destination_station, total_seats)
        get_all_trains()

    # Function to retrieve and display all trains
    def get_all_trains():
        cursor = conn.cursor()
        query = "SELECT * FROM Train"
        cursor.execute(query)
        trains = cursor.fetchall()
        for train in trains:
            train_info = f"Train ID: {train[0]}\nTrain Name: {train[1]}\nSource Station: {train[2]}\nDestination Station: {train[3]}\nTotal Seats: {train[4]}\n"
            print(train_info)

    # Function to open a new window and display all trains in a table
    def open_trains_window():
        trains_window = tk.Toplevel(root)
        trains_window.title("All Trains")
        trains_window.geometry("600x400")

        # Create a text widget to display the train information
        text_widget = tk.Text(trains_window)
        text_widget.pack()

        # Retrieve all trains and insert the information into the text widget
        cursor = conn.cursor()
        query = "SELECT * FROM Train"
        cursor.execute(query)
        trains = cursor.fetchall()
        for train in trains:
            train_info = f"Train ID: {train[0]}\nTrain Name: {train[1]}\nSource Station: {train[2]}\nDestination Station: {train[3]}\nTotal Seats: {train[4]}\n"
            text_widget.insert(tk.END, train_info + "\n")

    # Create labels and entry fields for the form
    train_id_label = tk.Label(root, text="Train ID:")
    train_id_label.pack()
    train_id_entry = tk.Entry(root)
    train_id_entry.pack()

    train_name_label = tk.Label(root, text="Train Name:")
    train_name_label.pack()
    train_name_entry = tk.Entry(root)
    train_name_entry.pack()

    source_station_label = tk.Label(root, text="Source Station:")
    source_station_label.pack()
    source_station_entry = tk.Entry(root)
    source_station_entry.pack()

    destination_station_label = tk.Label(root, text="Destination Station:")
    destination_station_label.pack()
    destination_station_entry = tk.Entry(root)
    destination_station_entry.pack()

    total_seats_label = tk.Label(root, text="Total Seats:")
    total_seats_label.pack()
    total_seats_entry = tk.Entry(root)
    total_seats_entry.pack()

    error_label = tk.Label(root, text="", fg="red")
    error_label.pack()


    submit_button = tk.Button(root, text="Submit", command=submit_form)
    submit_button.pack()

    # Add a button to open a new window and display all trains
    show_trains_button = tk.Button(root, text="Show All Trains", command=open_trains_window)
    show_trains_button.pack()

    # Run the Tkinter main loop
    root.mainloop()
