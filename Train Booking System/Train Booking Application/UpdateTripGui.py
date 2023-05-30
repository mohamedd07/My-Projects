import tkinter as tk
import pypyodbc

# Establishing a connection to the database
connection_string = 'DRIVER={SQL Server};SERVER=ABD-ELRAHMAN;DATABASE=TrainStation'
conn = pypyodbc.connect(connection_string)

def GUI_Update_Trip():
    

    def update_trip(trip_id, train_id, departure_time, arrival_time):
        cursor = conn.cursor()
        query = f"UPDATE Trip SET train_id = '{train_id}' WHERE trip_id = '{trip_id}'"
        cursor.execute(query)
        query = f"UPDATE Trip SET departure_time = '{departure_time}' WHERE trip_id = '{trip_id}'"
        cursor.execute(query)
        query = f"UPDATE Trip SET arrival_time = '{arrival_time}' WHERE trip_id = '{trip_id}'"
        cursor.execute(query)
        conn.commit()
        print("Trip details updated successfully!")

    def submit_form():
        trip_id = int(trip_id_entry.get())
        train_id = int(train_id_entry.get())
        departure_time = departure_time_entry.get()
        arrival_time = arrival_time_entry.get()
        update_trip(trip_id, train_id, departure_time, arrival_time)
        status_label.config(text="Trip details updated successfully!")

    # Create the window form
    window = tk.Tk()
    window.title("Update Trip Details")

    # Create labels
    trip_id_label = tk.Label(window, text="Trip ID:")
    trip_id_label.pack()
    trip_id_entry = tk.Entry(window)
    trip_id_entry.pack()

    train_id_label = tk.Label(window, text="Train ID:")
    train_id_label.pack()
    train_id_entry = tk.Entry(window)
    train_id_entry.pack()

    departure_time_label = tk.Label(window, text="Departure Time (hh:mm:ss):")
    departure_time_label.pack()
    departure_time_entry = tk.Entry(window)
    departure_time_entry.pack()

    arrival_time_label = tk.Label(window, text="Arrival Time (hh:mm:ss):")
    arrival_time_label.pack()
    arrival_time_entry = tk.Entry(window)
    arrival_time_entry.pack()

    # Create a submit button
    submit_button = tk.Button(window, text="Update", command=submit_form)
    submit_button.pack()

    # Create a status label
    status_label = tk.Label(window, text="")
    status_label.pack()

    # Start the Tkinter event loop
    window.mainloop()
