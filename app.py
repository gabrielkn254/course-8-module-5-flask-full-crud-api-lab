from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json(silent=True)
    event_title = data.get("title", None)

    if not event_title or len(event_title.strip()) == 0:
        return jsonify({"message": "Invalid title"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    event_id = len(events) + 1
    new_event = Event(id=event_id, title=event_title)
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify({"message": "Event was successfully created.", "id": event_id, "title":event_title}), 201



# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json(silent=True)
    event_title = data.get("title", None)

    if not event_title or len(event_title.strip()) == 0:
        return jsonify({"message": "Invalid title"}), 400
    
    # TODO: Task 3 - Implement the Loop and Process Each Element
    for event in events:
        if event.id == event_id:
            event.title = event_title

            return jsonify({"message": "Event was successfully updated.", "id": event.id, "title": event.title}), 200
        
    # TODO: Task 4 - Return and Handle Results
    return jsonify({"message": "Event not found"}), 404



# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    event_to_delete = next((event for event in events if event.id == event_id), None)
    if not event_to_delete:
        return jsonify({"message": "Event not found"}), 404

    # TODO: Task 3 - Implement the Loop and Process Each Element
    events.remove(event_to_delete)
    for index, event in enumerate(events):
        event.id = index + 1

    # TODO: Task 4 - Return and Handle Results
    return jsonify({"message": "Event was successfully deleted."}), 204

if __name__ == "__main__":
    app.run(debug=True)
