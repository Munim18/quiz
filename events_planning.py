# Import necessary modules from Flask and Python's standard library
from flask import Flask, render_template, request, redirect, url_for
import json  # Used for reading and writing JSON files
import os    # Used to check if files exist

# Create a Flask web application instance
app = Flask(__name__)

# Define file paths for storing event and booking data
EVENTS_FILE = 'events.json'
BOOKINGS_FILE = 'bookings.json'
MAX_ID_FILE = 'max_id.json'  # Used to keep track of the latest used IDs


# Utility function to load data from a JSON file
def load_json(file, default):
    # Check if the file exists
    if os.path.exists(file):
        # If it exists, open and load its content as a Python object
        with open(file, 'r') as f:
            return json.load(f)
    # If file doesn't exist, return the default value provided
    return default

# Utility function to save data to a JSON file
def save_json(file, data):
    # Open the file for writing and save the JSON-formatted data
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)  # Indent for human-readable formatting

# Function to generate a new unique booking ID
def get_next_id():
    # Load the current max ID values or initialize with defaults
    data = load_json(MAX_ID_FILE, {"event_id": 0, "booking_id": 0})
    # Increment the booking ID
    data["booking_id"] += 1
    # Save the updated ID values back to file
    save_json(MAX_ID_FILE, data)
    # Return the new booking ID
    return data["booking_id"]

# Function to generate a new unique event ID
def get_next_event_id():
    # Load the current max ID values or initialize with defaults
    data = load_json(MAX_ID_FILE, {"event_id": 0, "booking_id": 0})
    # Increment the event ID
    data["event_id"] += 1
    # Save the updated ID values back to file
    save_json(MAX_ID_FILE, data)
    # Return the new event ID
    return data["event_id"]

# Function to group bookings by their corresponding event
def group_bookings_by_event(bookings):
    grouped = {}  # Dictionary to hold grouped bookings
    # Iterate over all bookings
    for b in bookings:
        # Add each booking to the appropriate event_id key in the dictionary
        grouped.setdefault(b["event_id"], []).append(b)
    return grouped


# Route to display all events and their associated bookings
@app.route("/book/")
def show_events():
    # Load list of events from JSON file
    events = load_json(EVENTS_FILE, [])
    # Load list of bookings from JSON file
    bookings = load_json(BOOKINGS_FILE, [])
    # Render a template and pass the events and grouped bookings
    return render_template("events_planning.html", events=events, event_bookings=group_bookings_by_event(bookings))

# Route to handle booking submissions for a specific event
@app.route("/book/<int:event_id>", methods=["POST"])
def book_event(event_id):
    # Load the list of existing events
    events = load_json(EVENTS_FILE, [])
    # Find the event matching the given event_id
    event = next((e for e in events if e["id"] == event_id), None)
    # If the event is not found, return an error
    if not event:
        return "Event not found", 

    # Extract form data from the submitted POST request
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    vendor = request.form["vendor"]

    # Create a booking record using the form data
    booking = {
        "id": get_next_id(),  # Assign a unique ID to the booking
        "event_id": event_id, # Link the booking to the selected event
        "name": name,
        "email": email,
        "phone": phone,
        "vendor": vendor
    }

    # Load existing bookings and append the new one
    bookings = load_json(BOOKINGS_FILE, [])
    bookings.append(booking)
    # Save the updated list of bookings back to file
    save_json(BOOKINGS_FILE, bookings)

    # Redirect the user back to the list of events
    return redirect(url_for("show_events"))

# Route to create/manage new events (e.g., adding a new event)
@app.route("/manage/", methods=["POST"])
def manage():
    # Load the current list of events
    events = load_json(EVENTS_FILE, [])
    # Extract new event data from the form submission
    name = request.form["name"]
    date = request.form["date"]
    location = request.form["location"]

    # Create a new event dictionary
    new_event = {
        "id": get_next_event_id(),  # Assign a unique event ID
        "name": name,
        "date": date,
        "location": location
    }

    # Add the new event to the list
    events.append(new_event)
    # Save the updated list of events
    save_json(EVENTS_FILE, events)

    # Redirect back to the event list page
    return redirect(url_for("show_events"))

# Entry point of the application
if __name__ == "__main__":
    # Run the Flask development server
    app.run()
