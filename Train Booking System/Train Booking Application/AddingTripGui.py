import pypyodbc
import tkinter as tk

# Establishing a connection to the database
connection_string = 'DRIVER={SQL Server};SERVER=ABD-ELRAHMAN;DATABASE=TrainStation'
conn = pypyodbc.connect(connection_string)

# Create the main application window

def GUIADDINGTRIP():  
    root = tk.Tk()
    root.title("Train Station System")
    root.geometry("400x300")

    # Admin Data
    user_name = 'admin'
    password = 'admin'

    # Adding a trip (by admin)
    def add_trip(trip_id, train_id, departure_time, arrival_time):
        cursor = conn.cursor()
        
        # Check if the train_id exists in the Train table
        train_query = f"SELECT train_id FROM Train WHERE train_id = '{train_id}'"
        cursor.execute(train_query)
        existing_train = cursor.fetchone()
        
        if not existing_train:
            error_label.config(text="Train ID does not exist in the database.")
        else:
            # Check if the trip_id already exists in the Trip table
            trip_query = f"SELECT trip_id FROM Trip WHERE trip_id = '{trip_id}'"
            cursor.execute(trip_query)
            existing_trip = cursor.fetchone()

            if existing_trip:
                error_label.config(text="Trip ID already exists in the database.")
            else:
                insert_query = f"INSERT INTO Trip (trip_id, train_id, departure_time, arrival_time) VALUES ('{trip_id}', '{train_id}', '{departure_time}', '{arrival_time}')"
                cursor.execute(insert_query)
                conn.commit()
                error_label.config(text="Trip added successfully!")


    # Function to handle the form submission
    def submit_form():
        error_label.config(text="")
        trip_id = int(trip_id_entry.get())
        train_id = int(train_id_entry.get())
        departure_time = departure_time_entry.get()
        arrival_time = arrival_time_entry.get()
        add_trip(trip_id, train_id, departure_time, arrival_time)
        get_all_trips()

    # Function to retrieve and display all trips
    def get_all_trips():
        cursor = conn.cursor()
        query = "SELECT * FROM Trip"
        cursor.execute(query)
        trips = cursor.fetchall()
        for trip in trips:
            trip_info = f"Trip ID: {trip[0]}\nTrain ID: {trip[1]}\nDeparture Time: {trip[2]}\nArrival Time: {trip[3]}\n"
            print(trip_info)

    # Function to open a new window and display all trips in a table
    def open_trips_window():
        trips_window = tk.Toplevel(root)
        trips_window.title("All Trips")
        trips_window.geometry("600x400")

        # Create a text widget to display the trip information
        text_widget = tk.Text(trips_window)
        text_widget.pack()

        # Retrieve all trips and insert the information into the text widget
        cursor = conn.cursor()
        query = "SELECT * FROM Trip"
        cursor.execute(query)
        trips = cursor.fetchall()
        for trip in trips:
            trip_info = f"Trip ID: {trip[0]}\nTrain ID: {trip[1]}\nDeparture Time: {trip[2]}\nArrival Time: {trip[3]}\n"
            text_widget.insert(tk.END, trip_info + "\n")

    # Create labels and entry fields for the form
    trip_id_label = tk.Label(root, text="Trip ID:")
    trip_id_label.pack()
    trip_id_entry = tk.Entry(root)
    trip_id_entry.pack()

    train_id_label = tk.Label(root, text="Train ID:")
    train_id_label.pack()
    train_id_entry = tk.Entry(root)
    train_id_entry.pack()

    departure_time_label = tk.Label(root, text="Departure Time:")
    departure_time_label.pack()
    departure_time_entry = tk.Entry(root)
    departure_time_entry.pack()

    arrival_time_label = tk.Label(root, text="Arrival Time:")
    arrival_time_label.pack()
    arrival_time_entry = tk.Entry(root)
    arrival_time_entry.pack()

    error_label = tk.Label(root, text="", fg="red")
    error_label.pack()

    submit_button = tk.Button(root, text="Submit", command=submit_form)
    submit_button.pack()

    # Add a button to open a new window and display all trips
    show_trips_button = tk.Button(root, text="Show All Trips", command=open_trips_window)
    show_trips_button.pack()

    # Run the Tkinter main loop
    root.mainloop()
