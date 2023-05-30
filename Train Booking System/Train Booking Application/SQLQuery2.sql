CREATE database TrainStation
CREATE TABLE Ticket (
  ticket_id INT PRIMARY KEY,
  train_id INT,
  passenger_id INT,
  seat_number VARCHAR(10),
  date DATE,
  time TIME,
  FOREIGN KEY (train_id) REFERENCES Train(train_id),
  FOREIGN KEY (passenger_id) REFERENCES Passenger(passenger_id)
);

CREATE TABLE Train (
  train_id INT PRIMARY KEY,
  train_name VARCHAR(50),
  source_station VARCHAR(50),
  destination_station VARCHAR(50),
  total_seats INT
);

CREATE TABLE Trip (
  trip_id INT PRIMARY KEY,
  train_id INT,
  departure_time TIME,
  arrival_time TIME,
  FOREIGN KEY (train_id) REFERENCES Train(train_id)
);

CREATE TABLE Passenger (
  passenger_id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  gender VARCHAR(10)
);

CREATE TABLE Seat (
  seat_number VARCHAR(10),
  train_id INT,
  PRIMARY KEY (seat_number, train_id),
  FOREIGN KEY (train_id) REFERENCES Train(train_id)
);
CREATE TABLE Booking (
  booking_id INT PRIMARY KEY,
  passenger_id INT,
  trip_id INT,
  FOREIGN KEY (passenger_id) REFERENCES Passenger(passenger_id),
  FOREIGN KEY (trip_id) REFERENCES Trip(trip_id)
);
