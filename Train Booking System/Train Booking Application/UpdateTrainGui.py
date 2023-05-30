import pypyodbc
import tkinter as tk

# Establishing a connection to the database
connection_string = 'DRIVER={SQL Server};SERVER=ABD-ELRAHMAN;DATABASE=TrainStation'
conn = pypyodbc.connect(connection_string)

def GUI_Update_Train():

    def update_train(train_id, train_name, source_station, destination_station, total_seats):
        cursor = conn.cursor()
        query = f"UPDATE Train SET train_name = '{train_name}' WHERE train_id = '{train_id}'"
        cursor.execute(query)
        query = f"UPDATE Train SET source_station = '{source_station}' WHERE train_id = '{train_id}'"
        cursor.execute(query)
        query = f"UPDATE Train SET destination_station = '{destination_station}' WHERE train_id = '{train_id}'"
        cursor.execute(query)
        query = f"UPDATE Train SET total_seats = '{total_seats}' WHERE train_id = '{train_id}'"
        cursor.execute(query)
        conn.commit()
        print("Train details updated successfully!")

    def simpleupdate_train():
        train_id = int(entry_train_id.get())
        train_name = entry_train_name.get()
        source_station = entry_source_station.get()
        destination_station = entry_destination_station.get()
        total_seats = int(entry_total_seats.get())
    
        update_train(train_id, train_name, source_station, destination_station, total_seats)

    # Create the main window
    window = tk.Tk()

    # Set the window title
    window.title("Train Details Update")

    # Create labels
    label_train_id = tk.Label(window, text="Train Id:")
    label_train_id.pack()
    entry_train_id = tk.Entry(window)
    entry_train_id.pack()

    label_train_name = tk.Label(window, text="Train Name:")
    label_train_name.pack()
    entry_train_name = tk.Entry(window)
    entry_train_name.pack()

    label_source_station = tk.Label(window, text="Source Station:")
    label_source_station.pack()
    entry_source_station = tk.Entry(window)
    entry_source_station.pack()

    label_destination_station = tk.Label(window, text="Destination Station:")
    label_destination_station.pack()
    entry_destination_station = tk.Entry(window)
    entry_destination_station.pack()

    label_total_seats = tk.Label(window, text="Total Seats:")
    label_total_seats.pack()
    entry_total_seats = tk.Entry(window)
    entry_total_seats.pack()



    # Create update button
    button_update = tk.Button(window, text="Update", command=simpleupdate_train)
    button_update.pack()

    # Start the main event loop
    window.mainloop()
