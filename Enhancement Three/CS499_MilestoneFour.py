# Susannah Weatherby CS499 Milestone Four Project

import json
from datetime import datetime
from pymongo import MongoClient

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["cs499_db"]

# ======================= Models =======================

# Contact class model
class Contact:
    def __init__(self, id, first_name, last_name, number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = address

    def get_id(self):
        return self.id

    def set_first_name(self, name): self.first_name = name
    def set_last_name(self, name): self.last_name = name
    def set_number(self, number): self.number = number
    def set_address(self, address): self.address = address

    def __str__(self):
        return f"[Contact] ID: {self.id}, Name: {self.first_name} {self.last_name}, Number: {self.number}, Address: {self.address}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "number": self.number,
            "address": self.address,
            "type": self.__class__.__name__
        }

# Contact Employee sub-type
class Employee(Contact):
    def __str__(self):
        return f"[Employee] ID: {self.id}, Name: {self.first_name} {self.last_name}, Number: {self.number}, Address: {self.address}"

# Contact Employee sub-type
class Customer(Contact):
    def __str__(self):
        return f"[Customer] ID: {self.id}, Name: {self.first_name} {self.last_name}, Number: {self.number}, Address: {self.address}"

# Appointment class model
class Appointment:
    def __init__(self, id, appointment_date, description, assigned_customer_id):
        self.id = id
        self.appointment_date = appointment_date
        self.description = description
        self.assigned_customer_id = assigned_customer_id

    def get_id(self):
        return self.id

    def format(self, contact_service):        
        name = contact_service.get_contact_name_by_id(self.assigned_customer_id)
        assigned_info = f"{name} (ID {self.assigned_customer_id})" if name else f"ID {self.assigned_customer_id}"

        return (f"[Appointment] ID: {self.id}, Date: {self.appointment_date.strftime('%Y-%m-%d %I:%M %p')}, "
                f"Desc: {self.description}, Customer: {assigned_info}")
    
    def to_dict(self):
        return {
            "id": self.id,
            "appointment_date": self.appointment_date.isoformat(),
            "description": self.description,
            "assigned_customer_id": self.assigned_customer_id
        }

# Task class model
class Task:
    def __init__(self, id, name, desc, assigned_employee_id):
        self.id = id
        self.name = name
        self.desc = desc
        self.assigned_employee_id = assigned_employee_id

    def get_id(self):
        return self.id

    def set_name(self, name): self.name = name
    def set_desc(self, desc): self.desc = desc

    def format(self, contact_service):
        name = contact_service.get_contact_name_by_id(self.assigned_employee_id)
        assigned_info = f"{name} (ID {self.assigned_employee_id})" if name else f"ID {self.assigned_employee_id}"
        
        return (f"[Task] ID: {self.id}, Name: {self.name}, Description: {self.desc}, Assigned Employee: {assigned_info}")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "assigned_employee_id": self.assigned_employee_id
        }


# ======================= Services =======================

# Contact service class
class ContactService:
    def __init__(self):
        self.employees = []
        self.customers = []

    # Adds a new contact using given information
    def add_contact(self, id, first_name, last_name, number, address, is_customer=True):
        # Check all existing contacts
        for contact in self.employees + self.customers:
            if contact.get_id() == id:
                raise ValueError("ID already exists.")
        if is_customer:
            contact = Customer(id, first_name, last_name, number, address)
            self.customers.append(contact)
        else:
            contact = Employee(id, first_name, last_name, number, address)
            self.employees.append(contact)

    # Deletes a contact with given information
    def delete_contact(self, id):
        for group in [self.employees, self.customers]:
            for i, contact in enumerate(group):
                if contact.get_id() == id:
                    del group[i]
                    print("Contact deleted.")
                    return
        print("Contact ID not found.")

    # Updates existing contact with given information
    def update_contact(self, id, field, value):
        for contact in self.employees + self.customers:
            if contact.get_id() == id:
                field = field.lower()
                if field in ["firstname", "first name"]:
                    contact.set_first_name(value)
                elif field in ["lastname", "last name"]:
                    contact.set_last_name(value)
                elif field in ["number", "phone number"]:
                    contact.set_number(value)
                elif field == "address":
                    contact.set_address(value)
                else:
                    raise ValueError("Invalid field type.")
                print("Contact updated.")
                return
        raise ValueError("No contact with given ID found.")
    
    # Returns the list of existing contacts
    def get_all_contacts(self):
        return {
            "customers": list(self.customers),
            "employees": list(self.employees)
        }
    
    def get_contact_name_by_id(self, id):
        for contact in self.employees + self.customers:
            if contact.get_id() == id:
                return f"{contact.first_name} {contact.last_name}"
        return None
    
    def save_contacts(self, filename="contacts.json"):
        data = [c.to_dict() for c in self.customers + self.employees]
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_contacts(self, filename="contacts.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    contact_type = item.pop("type", None)
                    if contact_type == "Customer":
                        self.customers.append(Customer(**item))
                    elif contact_type == "Employee":
                        self.employees.append(Employee(**item))
        except FileNotFoundError:
            pass
    
# Appointment class service
class AppointmentService:
    def __init__(self):
        self.appointments = []

    # Adds new appointment with given information
    def add_appointment(self, id, appointment_date, description, assigned_customer_id):
        for appt in self.appointments:
            # If given id already exists, throw error
            if appt.get_id() == id:
                raise ValueError("ID already exists.")
            # If given time is in the past, throw error
            if appointment_date < datetime.now():
                raise ValueError("Appointment date/time cannot be in the past.")
        appointment = Appointment(id, appointment_date, description, assigned_customer_id)
        self.appointments.append(appointment)
     
    # Deletes an apointment with given information
    def delete_appointment(self, id):
        for i, appt in enumerate(self.appointments):
            if appt.get_id() == id:
                del self.appointments[i]
                print(f"Task for {appt.assigned_customer_id} deleted.")
                return
        print("Appointment ID not found.")        

    # Updates existing appointment with given information
    def update_appointment(self, id, field, value):
        for appt in self.appointments:
            if appt.get_id() == id:
                field = field.lower()
                if field in ["date", "appointment_date"]:
                    try:
                        new_date = datetime.strptime(value, "%Y-%m-%d %I:%M %p")
                        # If given time is in the past, throw error
                        if new_date < datetime.now():
                            raise ValueError("Cannot update to a past date/time.")
                        appt.appointment_date = new_date
                    # If value error, inform user
                    except ValueError:
                        raise ValueError("Invalid date format. Use YYYY-MM-DD HH:MM AM/PM")
                elif field == "description":
                    appt.description = value
                # If value error, inform user
                else:
                    raise ValueError("Invalid field. Must be 'date' or 'description'.")
                print("Appointment updated.")
                return
        raise ValueError("No appointment with given ID found.")
    
    # Returns the list of existing appointments
    def get_all_appointments(self):
        return list(self.appointments)
    
    def save_appointments(self, filename="appointments.json"):
        data = [appt.to_dict() for appt in self.appointments]
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_appointments(self, filename="appointments.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    item["appointment_date"] = datetime.fromisoformat(item["appointment_date"])
                    self.appointments.append(Appointment(**item))
        except FileNotFoundError:
            pass

# Task service class
class TaskService:
    def __init__(self):
        self.tasks = []

    # Adds a new task using given information
    def add_task(self, id, name, desc, assigned_employee_id):
        for task in self.tasks:
            if task.get_id() == id:
                raise ValueError("Error: ID already exists.")
        task = Task(id, name, desc, assigned_employee_id)
        self.tasks.append(task)

    # Deletes a task with given information
    def delete_task(self, id):
        for i, task in enumerate(self.tasks):
            if task.get_id() == id:
                del self.tasks[i]
                print(f"Task for {task.assigned_employee_id} deleted.")
                return
        print("Task ID not found.")

    # Updates a task with given information
    def update_task(self, id, field, value):
        for task in self.tasks:
            if task.get_id() == id:
                field = field.lower()
                if field == "name":
                    task.set_name(value)
                elif field in ["desc", "description"]:
                    task.set_desc(value)
                else:
                    raise ValueError("Invalid field type.")
                print("Task updated.")
                return
        raise ValueError("No task with given ID found.")

    # Returns the list of existing tasks
    def get_all_tasks(self):
        return list(self.tasks)
    
    def save_tasks(self, filename="tasks.json"):
        data = [task.to_dict() for task in self.tasks]
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    self.tasks.append(Task(**item))
        except FileNotFoundError:
            pass


# ======================= Export to MongoDB =======================

def export_all_to_mongo(contact_service, task_service, appointment_service):
    mongo_db.contacts.delete_many({})
    mongo_db.tasks.delete_many({})
    mongo_db.appointments.delete_many({})

    mongo_db.contacts.insert_many([c.to_dict() for c in contact_service.customers + contact_service.employees])
    mongo_db.tasks.insert_many([t.to_dict() for t in task_service.tasks])
    mongo_db.appointments.insert_many([a.to_dict() for a in appointment_service.appointments])

# ======================= Main Method =======================

def main():
    contact_service = ContactService()
    appointment_service = AppointmentService()
    task_service = TaskService()
    
    contact_service.load_contacts()
    task_service.load_tasks()
    appointment_service.load_appointments()

    try:
        # Main Menu   
        while True:
            print("\n=== Main Menu ===")
            print("1. Manage Contacts") 
            print("2. Manage Appointments")
            print("3. Manage Tasks")
            print("4. Exit")
            choice = input("Choose (1-4): ")
        
            # Contact Menu
            if choice == "1":
                while True:
                    print("\n--- Contacts ---")
                    print("1. Add")
                    print("2. View")
                    print("3. Delete")
                    print("4. Update")
                    print("5. Back")
                    c_choice = input("Choose: ")
                    # Adding Contacts
                    if c_choice == "1":
                        try:
                            print("\nIs this contact an:")
                            print("1. Customer")
                            print("2. Employee")
                            type_choice = input("Enter choice (1 or 2): ").strip()
                            if type_choice not in ["1", "2"]:
                                raise ValueError("Invalid type selection.")
                            is_customer = type_choice == "1"

                            id = input("Contact ID: ")
                            fn = input("First Name: ")
                            ln = input("Last Name: ")
                            num = input("Phone Number: ")
                            addr = input("Address: ")
                            contact_service.add_contact(id, fn, ln, num, addr, is_customer)
                            print("\nContact added.")
                        except Exception as e:
                            print("\nError:", e)
                    # Viewing Contacts
                    elif c_choice == "2":
                        contacts = contact_service.get_all_contacts()
                        print("\n--- Customers ---")
                        for cust in contacts["customers"]:
                            print(cust)
                        print("\n--- Employees ---")
                        for emp in contacts["employees"]:
                            print(emp)
                    # Deleting Contacts
                    elif c_choice == "3":
                        id = input("Enter ID to delete: ")
                        contact_service.delete_contact(id)
                    # Updating Contacts
                    elif c_choice == "4":
                        try:
                            id = input("Enter ID to update: ")
                            field = input("Which field to update (first name, last name, number, address): ")
                            value = input("New value: ")
                            contact_service.update_contact(id, field, value)
                        except Exception as e:
                         print("\nError:", e)
                    # Return to main menu
                    elif c_choice == "5":
                        break
                    # Catch error if invalid input
                    else:
                        print("Invalid option. Try again.")

            # Appointment Menu
            elif choice == "2":
                while True:
                    print("\n--- Appointments ---")
                    print("1. Add")
                    print("2. View")
                    print("3. Delete")
                    print("4. Update")
                    print("5. Back")
                    appt_choice = input("Choose (1-5): ")
                    # Adding Appointments
                    if appt_choice == "1":
                        # Display customer IDs
                        customers = contact_service.get_all_contacts()["customers"]
                        if not customers:
                            print("No customers available. Please add one first.")
                            continue
                        print("\nAvailable Customers:")
                        for c in customers:
                            print(f"- {c.id}: {c.first_name} {c.last_name}")
                        
                        id = input("Appointment ID: ")
                        date_str = input("Enter Appointment Date (YYYY-MM-DD HH:MM AM/PM): ")
                        try:
                            appointment_date = datetime.strptime(date_str, "%Y-%m-%d %I:%M %p")
                            appointment_desc = input("Appointment Description: ")
                            assigned_id = input("Assign to Customer ID: ")
                        
                            if assigned_id not in [c.get_id() for c in customers]:
                                raise ValueError("Invalid Customer ID.")
                        
                            appointment_service.add_appointment(id, appointment_date, appointment_desc, assigned_id)
                            print("\nAppointment added.")
                        except Exception as e:
                            print("\nError:", e)
                    # Reading Appointments
                    elif appt_choice == "2":
                        print("")
                        for appt in appointment_service.get_all_appointments():
                            print(appt.format(contact_service))
                    # Deleting Appointments
                    elif appt_choice == "3":
                        id = input("Enter ID to delete: ")
                        appointment_service.delete_appointment(id)
                    # Updating Appointments
                    elif appt_choice == "4":
                        try:
                            id = input("Enter Appointment ID to update: ")
                            field = input("Which field to update (date or description): ")
                            value = input("New value: ")
                            appointment_service.update_appointment(id, field, value)
                        except Exception as e:
                            print("\nError:", e)  
                    # Return to main menu
                    elif appt_choice == "5":
                        break
                    # Catch error if invalid input
                    else:
                        print("Invalid option. Try again.")
        
            # Task menu
            elif choice == "3":
                while True:
                    print("\n--- Tasks ---")
                    print("1. Add")
                    print("2. View")
                    print("3. Delete")
                    print("4. Update")
                    print("5. Back")
                    t_choice = input("Choose (1-5): ")
                    # Adding Tasks
                    if t_choice == "1":
                        try:
                            # Display employee IDs
                            employees = contact_service.get_all_contacts()["employees"]
                            if not employees:
                                print("No employees available. Please add one first.")
                                continue
                        
                            print("\nAvailable Employees:")
                            for e in employees:
                                print(f"- {e.id}: {e.first_name} {e.last_name}")
                            
                            id = input("Task ID: ")
                            name = input("Task Name: ")
                            desc = input("Task Description: ")
                            assigned_id = input("Assign to Employee ID: ")
                        
                            if assigned_id not in [e.get_id() for e in employees]:
                                raise ValueError("Invalid Employee ID.")
                        
                            task_service.add_task(id, name, desc, assigned_id)
                            print("\nTask added.")
                        except Exception as e:
                            print("\nError:", e)
                    # Viewing Tasks
                    elif t_choice == "2":
                        print("")
                        for t in task_service.get_all_tasks():
                            print(t.format(contact_service))
                    # Deleting Tasks
                    elif t_choice == "3":
                        id = input("Enter ID to delete: ")
                        task_service.delete_task(id)
                    # Updating Tasks
                    elif t_choice == "4":
                        try:
                            id = input("Enter ID to update: ")
                            field = input("Which field to update (name or description): ")
                            value = input("New value: ")
                            task_service.update_task(id, field, value)
                        except Exception as e:
                            print("\nError:", e)
                    # Return to Main Menu
                    elif t_choice == "5":
                        break
                    # Catch error if invalid input
                    else:
                        print("Invalid option. Try again.")
            # Exit program
            elif choice == "4":
                print("Goodbye!")
                break
            # Catch error if invalid input
            else:
                print("Invalid option. Try again.")
    finally:
        # Save all information and export to mongoDB
        contact_service.save_contacts()
        task_service.save_tasks()
        appointment_service.save_appointments()
        export_all_to_mongo(contact_service, task_service, appointment_service)
        print("Data saved. Goodbye!")

if __name__ == "__main__":
    main()


