from flask import Flask, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["cs499_db"]

# collection imports
@app.route("/")
def index():
    contacts = list(db.contacts.find())
    tasks = list(db.tasks.find())
    appointments = list(db.appointments.find())
    
    # Create quick-lookup maps for contact ID -> full name
    contact_map = {str(c["id"]): f"{c.get('first_name', '')} {c.get('last_name', '')}" for c in contacts}
    
    # Add assigned employee name to each task
    for task in tasks:
        emp_id = str(task.get("assigned_employee_id"))
        task["assigned_employee_name"] = contact_map.get(emp_id, "Unknown")
        
    # Add assigned customer name to each appointment
    for appt in appointments:
        cust_id = str(appt.get("assigned_customer_id"))
        appt["assigned_customer_name"] = contact_map.get(cust_id, "Unknown")
        
    # Sort appointments by date
    for appt in appointments:
        appt["_parsed_date"] = datetime.fromisoformat(appt["appointment_date"])
        
    appointments.sort(key=lambda a: a["_parsed_date"])
    for appt in appointments:
        del appt["_parsed_date"]  # clean up helper field

    return render_template("index.html", contacts=contacts, tasks=tasks, appointments=appointments)

if __name__ == "__main__":
    app.run(debug=True)