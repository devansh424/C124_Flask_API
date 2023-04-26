from flask import Flask, request, jsonify

app = Flask(__name__)
contacts = [
    {
        "ID": 1,
        "Name": "Devansh",
        "Contact": "3592029402",
        "done": False
    },
    {
        "ID": 2,
        "Name": "Raju",
        "Contact": "5930294982",
        "done": False
    }
]

@app.route("/add-data", methods = ["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data."
        }, 400)
    
    contact = {
        "ID": contacts[-1]["ID"] + 1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Added the contact provided by you."
    })

# Getting data to check if the data we entered exist or not.
@app.route("/get-data")
def get_data():
    return contacts

if __name__ == "__main__":
    app.run(debug = True)
