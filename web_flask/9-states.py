#!/usr/bin/python3
"""
Script that starts a Flask web application listening on 0.0.0.0:5000
Use storage for fetching data from the storage engine File or DB storage
from models import storage and storage.all(...)
After each request, remove current SQLAlchemy Session:
    Declare method to handle @app.teardown_appcontext
    Call in this method: storage.close()
Route /states: display a HTML page
    H1 tag: "States"
    UL tag: list of all State objects present in DBStorage sorted by name
        LI tag: Description of one State: <state.id>: <<B><state.name></B>
Route /states/<id> : display aHTML page
    If a State object is found with this id:
        H1 tag: "State: "
        H3 tag: "Cities:"
        UL tag: with the list of City objects linked to the state sorted A-Z
            LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
        H1 tag: "Not found!"
Must use option strict_slashes=False
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/<id>")
def states_id_route(id=None):
    """
    Displays an HTML formatted of cities with a given State id
    """
    states = storage.all(State)
    return render_template("9-states.html", state_list=states, id=id)


@app.teardown_appcontext
def teardown(stuff):
    """
    Remove current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
