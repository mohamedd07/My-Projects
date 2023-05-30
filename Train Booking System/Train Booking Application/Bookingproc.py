import pypyodbc
import tkinter as tk
# from LOGIN import getid


# Establishing a connection to the database
connection_string = 'DRIVER={SQL Server};SERVER=ABD-ELRAHMAN;DATABASE=TrainStation'
conn = pypyodbc.connect(connection_string)


def cancel():
    def cancel_ticket():
        ticket_id = int(ticket_id_entry.get())
        booking_id = int(booking_id_entry.get())
        
        cursor = conn.cursor()
        q = f"SELECT Ticket.train_id, Ticket.seat_number from Ticket WHERE Ticket.ticket_id = '{ticket_id}'"
        cursor.execute(q)
        
        train_id = 0
        seat_number = 0
        for i in cursor.fetchall():
            train_id = i[0]
            seat_number = i[1]
            
        query = f"UPDATE Seat SET is_available = 'T' WHERE seat_number = '{seat_number}' AND train_id = '{train_id}'"
        cursor.execute(query)
        
        qe = f"DELETE FROM Booking WHERE booking_id = '{booking_id}'"
        cursor.execute(qe)
        
        qo = f"DELETE FROM Ticket WHERE ticket_id = '{ticket_id}'"
        cursor.execute(qo)
        
        conn.commit()
        
        # Update the message label
        message_label.config(text="Ticket canceled successfully.")

    # Create the main window
    window = tk.Tk()
    window.title("Ticket Cancellation")
    window.geometry("300x250")

    # Create and position the labels
    ticket_id_label = tk.Label(window, text="Ticket ID:")
    ticket_id_label.pack()
    booking_id_label = tk.Label(window, text="Booking ID:")
    booking_id_label.pack()

    # Create and position the entry fields
    ticket_id_entry = tk.Entry(window)
    ticket_id_entry.pack()
    booking_id_entry = tk.Entry(window)
    booking_id_entry.pack()

    # Create and position the cancel button
    cancel_button = tk.Button(window, text="Cancel Ticket", command=cancel_ticket)
    cancel_button.pack()

    # Create and position the message label
    message_label = tk.Label(window, text="")
    message_label.pack()

    # Start the main loop
    window.mainloop()

def PassengerBooking(passengerid):

    def avb_seat(trainID):
        cursor = conn.cursor()
        query = f"SELECT seat_number, train_name, Train.train_id, source_station, destination_station, departure_time, arrival_time FROM Train, Seat, Trip WHERE Seat.is_available = 'T' AND Seat.train_id = Train.train_id AND Train.train_id = '{trainID}' AND Train.train_id = Trip.train_id"
        cursor.execute(query)
        data = cursor.fetchall()

        # Create a new window to display the available seats
        seats_window = tk.Toplevel(window)
        seats_window.title("Available Seats")

        # Create a text widget to show the seat information
        text_widget = tk.Text(seats_window)
        text_widget.pack()

        for i in data:
            seat_info = f"Seat Number: {i[0]}\nTrain Name: {i[1]}\nTrain ID: {i[2]}\nSource Station: {i[3]}\nDestination Station: {i[4]}\nDeparture Time: {i[5]}\nArrival Time: {i[6]}\n\n"
            text_widget.insert(tk.END, seat_info)

        # Create an entry widget to enter the chosen seat
        label = tk.Label(seats_window, text="Choose a Seat:")
        label.pack()
        entry = tk.Entry(seats_window)
        entry.pack()

        # Create a button to trigger further actions
        button = tk.Button(seats_window, text="Confirm Seat", command=lambda: process_seat(entry.get(), trainID))
        button.pack()

    def process_seat(seat_number, trainID):
        # Process the chosen seat here (e.g., store it in a variable, update the database, etc.)
        global sn
        sn = seat_number

        # Call the confirmbooking function
        confirmbooking(trainID)

    def confirmbooking(trainID):
        cursor = conn.cursor()
        query = f"UPDATE Seat SET is_available = 'F' WHERE seat_number = '{sn}' and train_id = '{trainID}'"
        cursor.execute(query)

        # Retrieve trip_id based on train_id
        cursor = conn.cursor()
        query = f"SELECT Trip.trip_id FROM Trip, Train WHERE Train.train_id = '{trainID}' AND Train.train_id = Trip.train_id"
        cursor.execute(query)
        trip_id = 0
        for i in cursor.fetchall():
            trip_id = i[0]

        cursor = conn.cursor()
        query = f"INSERT INTO Booking (passenger_id, trip_id) VALUES ('{passengerid}', '{trip_id}')"
        cursor.execute(query)

        cursor = conn.cursor()
        query = f"INSERT INTO Ticket (train_id, passenger_id, seat_number) VALUES ('{trainID}', '{passengerid}','{sn}')"
        cursor.execute(query)

        cursor = conn.cursor()
        quii = f"SELECT booking_id FROM Booking  WHERE trip_id = '{trip_id}'"
        cursor.execute(quii)
        bn = 0
        for i in cursor.fetchall():
            bn = i[0]
        
        tn = 0
        cursor = conn.cursor()
        qaaa = f"SELECT ticket_id FROM Ticket  WHERE train_id = '{trainID}' AND seat_number = '{sn}'"
        cursor.execute(qaaa)
        for i in cursor.fetchall():
            tn = i[0]
        
        conn.commit()

        # Print the ticket information
        printticket(trainID, passengerid, sn,bn,tn)

    def printticket(td, pd, sn, bn, tn):
        print("Here's your ticket:")
        print("Booking ID:", bn)
        print("Ticket ID:", tn)
        print("Train ID:", td)
        print("Passenger ID:", pd)
        print("Seat Number:", sn)


    def display_trains():
        DEST = entry.get()  # Get the destination from the entry widget
        cursor = conn.cursor()
        query = f"SELECT destination_station, Train.train_id FROM Train, Seat WHERE Seat.is_available = 'T' AND Seat.train_id = Train.train_id AND Train.destination_station = '{DEST}'"
        cursor.execute(query)
        data = cursor.fetchall()

        # Create a new window to display the train selection
        trains_window = tk.Toplevel(window)
        trains_window.title("Select a Train")

        # Create a listbox to show the train information
        trains_listbox = tk.Listbox(trains_window)
        trains_listbox.pack()

        for row in data:
            train_info = f"Train Number: {row[1]}   Destination: {row[0]}"
            trains_listbox.insert(tk.END, train_info)

        # Create a button to view the seats for the selected train
        view_seats_button = tk.Button(trains_window, text="View Seats", command=lambda: avb_seat(row[1]))
        view_seats_button.pack()

    # Create the main window
    window = tk.Tk()
    window.title("Train Booking")
    window.geometry("400x200")

    # Create a label and entry widget for the destination
    label = tk.Label(window, text="Destination:")
    label.pack()
    entry = tk.Entry(window)
    entry.pack()

    # Create a button to trigger the display_trains function
    button = tk.Button(window, text="Show Trains", command=display_trains)
    button.pack()

    # Start the Tkinter event loop
    window.mainloop()
