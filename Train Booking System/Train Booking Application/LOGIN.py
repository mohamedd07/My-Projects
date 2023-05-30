from tkinter import Tk, Label, Entry, Button, Toplevel
import pypyodbc
import ADMIN
import Bookingproc

connection_string = 'DRIVER={SQL Server};SERVER=ABD-ELRAHMAN;DATABASE=TrainStation'
conn = pypyodbc.connect(connection_string)

ID = 0

def adminlogin():
    def open_login_window():
        login_window = Toplevel(root)
        login_window.title("Login")
        id_label = Label(login_window, text="ID:")
        id_label.pack()
        id_entry = Entry(login_window)
        id_entry.pack()

        password_label = Label(login_window, text="Password:")
        password_label.pack()
        password_entry = Entry(login_window, show="*")
        password_entry.pack()

        login_button = Button(login_window, text="Login", command=lambda: login(id_entry.get(), password_entry.get()))
        login_button.pack()

    def open_signup_window():
        signup_window = Toplevel(root)
        signup_window.title("Sign Up")
        id_label = Label(signup_window, text="ID:")
        id_label.pack()
        id_entry = Entry(signup_window)
        id_entry.pack()

        password_label = Label(signup_window, text="Password:")
        password_label.pack()
        password_entry = Entry(signup_window, show="*")
        password_entry.pack()

        signup_button = Button(signup_window, text="Sign Up", command=lambda: signup(id_entry.get(), password_entry.get()))
        signup_button.pack()

    def signup(id, password):
        cursor = conn.cursor()
        query = f"insert into Admin(admin_id, admin_pass) values ('{id}', '{password}')"
        cursor.execute(query)
        conn.commit()
        print("Registration successful!")

    def login(id, password):
        cursor = conn.cursor()
        query = f"select admin_pass from Admin where Admin_id = {id}"
        cursor.execute(query)
        data = cursor.fetchall()
        for i in data:
            if i[0] == password:
                print("Login successful")
                open_new_window()
                return  # Return after opening the new window
            else:
                print("Wrong data")

        print("Login failed")  # If no matching password is found

    def open_new_window():
        new_window = Toplevel(root)
        new_window.title("Welcome!")

        # Add your window content here

        # Add train button
        train_button = Button(new_window, text="Add train", command=add_train)
        train_button.pack()

        # Add trip button
        trip_button = Button(new_window, text="Add trip", command=add_trip)
        trip_button.pack()

        # Add update train button
        update_train_button = Button(new_window, text="Update train", command=update_train)
        update_train_button.pack()

        # Add update trip button
        update_trip_button = Button(new_window, text="Update trip", command=update_trip)
        update_trip_button.pack()

    def add_train():
        ADMIN.addingTrainGui()

    def add_trip():
        ADMIN.GUIADDINGTRIP()

    def update_train():
        ADMIN.GUI_Update_Train()

    def update_trip():
        ADMIN.GUI_Update_Trip()

    root = Tk()
    root.title("Main Window")

    # Create a button to open the login window
    open_login_window_button = Button(root, text="Login", command=open_login_window)
    open_login_window_button.pack()
    open_login_window_button = Button(root, text="Signup ", command=open_signup_window)
    open_login_window_button.pack()

    root.mainloop()

def passengerlogin():
    def open_login_window():
        login_window = Toplevel(root)
        login_window.title("Login")
        id_label = Label(login_window, text="ID:")
        id_label.pack()
        id_entry = Entry(login_window)
        id_entry.pack()

        password_label = Label(login_window, text="Password:")
        password_label.pack()
        password_entry = Entry(login_window, show="*")
        password_entry.pack()

        login_button = Button(login_window, text="Login", command=lambda: login(id_entry.get(), password_entry.get()))
        login_button.pack()

    def open_signup_window():
        signup_window = Toplevel(root)
        signup_window.title("Sign Up")
        id_label = Label(signup_window, text="ID:")
        id_label.pack()
        id_entry = Entry(signup_window)
        id_entry.pack()

        password_label = Label(signup_window, text="Password:")
        password_label.pack()
        password_entry = Entry(signup_window, show="*")
        password_entry.pack()

        name_label = Label(signup_window, text="Name:")
        name_label.pack()
        name_entry = Entry(signup_window)
        name_entry.pack()

        age_label = Label(signup_window, text="Age:")
        age_label.pack()
        age_entry = Entry(signup_window)
        age_entry.pack()

        gender_label = Label(signup_window, text="Gender:")
        gender_label.pack()
        gender_entry = Entry(signup_window)
        gender_entry.pack()

        signup_button = Button(signup_window, text="Sign Up", command=lambda: signup(id_entry.get(), name_entry.get(), age_entry.get(), gender_entry.get(), password_entry.get()))
        signup_button.pack()

    def signup(id, name, age, gender, password):
        cursor = conn.cursor()
        query = f"insert into Passenger(passenger_id, name, age, gender, pass) values ('{id}', '{name}', '{age}', '{gender}', '{password}')"
        cursor.execute(query)
        conn.commit()
        print("Registration successful!")

    def login(id, password):
        cursor = conn.cursor()
        query = f"select pass from Passenger where passenger_id = {id}"
        cursor.execute(query)
        data = cursor.fetchall()
        for i in data:
            if i[0] == password:
                print("Login successful")
                global ID
                ID = id
                open_new_window()
            else:
                print("Wrong data")
    
    def get_id():
        return ID

    def open_new_window():
        new_window = Toplevel(root)
        new_window.title("Welcome!")

        def book_ticket():
            Bookingproc.PassengerBooking(get_id())

        def cancel_booking():
            Bookingproc.cancel()

        # Add your window content here

        # Add book ticket button
        book_ticket_button = Button(new_window, text="Book Ticket", command=book_ticket)
        book_ticket_button.pack()

        # Add cancel booking button
        cancel_booking_button = Button(new_window, text="Cancel Booking", command=cancel_booking)
        cancel_booking_button.pack()

    root = Tk()
    root.title("Sign Up / Login")

    login_button = Button(root, text="Login", command=open_login_window)
    login_button.pack()

    signup_button = Button(root, text="Sign Up", command=open_signup_window)
    signup_button.pack()

    root.mainloop()

# Create the main window
root = Tk()
root.withdraw()  # Hide the main window

def open_login_window():
    login_window = Toplevel()
    login_window.title("Select User Type")

    admin_button = Button(login_window, text="Admin", command=adminlogin)
    admin_button.pack()

    passenger_button = Button(login_window, text="Passenger", command=passengerlogin)
    passenger_button.pack()

# Open the login window directly
open_login_window()

# Start the main event loop
root.mainloop()
