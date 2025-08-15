# Susannah Weatherby CS499 Milestone Two Project
from datetime import datetime

# ======================= Models =======================

#Appointment class model
class Appointment:
    def __init__(self, id, appointment_date, description):
        self.id = id
        self.appointment_date = appointment_date
        self.description = description

    def get_id(self):
        return self.id

    def __str__(self):
        return f"[Appointment] ID: {self.id}, Date: {self.appointment_date.strftime('%Y-%m-%d %I:%M %p')}, Desc: {self.description}"

#Contact class model
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

#Task class model
class Task:
    def __init__(self, id, name, desc):
        self.id = id
        self.name = name
        self.desc = desc

    def get_id(self):
        return self.id

    def set_name(self, name): self.name = name
    def set_desc(self, desc): self.desc = desc

    def __str__(self):
        return f"[Task] ID: {self.id}, Name: {self.name}, Description: {self.desc}"


# ======================= Services =======================

#Appointment class service
class AppointmentService:
    def __init__(self):
        self.appointments = []

    #Adds new appointment with given information
    def add_appointment(self, id, appointment_date, description):
        for appt in self.appointments:
            #if given id already exists, throw error
            if appt.get_id() == id:
                raise ValueError("ID already exists.")
            #if given time is in the past, throw error
            if appointment_date < datetime.now():
                raise ValueError("Appointment date/time cannot be in the past.")
        appointment = Appointment(id, appointment_date, description)
        self.appointments.append(appointment)
     
    #Deletes an apointment with given information
    def delete_appointment(self, id):
        for i, appt in enumerate(self.appointments):
            if appt.get_id() == id:
                del self.appointments[i]
                print("Appointment deleted.")
                return
        print("Appointment ID not found.")        

    #Updates existing appointment with given information
    def update_appointment(self, id, field, value):
        for appt in self.appointments:
            if appt.get_id() == id:
                field = field.lower()
                if field in ["date", "appointment_date"]:
                    try:
                        new_date = datetime.strptime(value, "%Y-%m-%d %I:%M %p")
                        #if given time is in the past, throw error
                        if new_date < datetime.now():
                            raise ValueError("Cannot update to a past date/time.")
                        appt.appointment_date = new_date
                    #if value error, inform user
                    except ValueError:
                        raise ValueError("Invalid date format. Use YYYY-MM-DD HH:MM AM/PM")
                elif field == "description":
                    appt.description = value
                #if value error, inform user
                else:
                    raise ValueError("Invalid field. Must be 'date' or 'description'.")
                print("Appointment updated.")
                return
        raise ValueError("No appointment with given ID found.")
    
    #Returns the list of existing appointments
    def get_all_appointments(self):
        return list(self.appointments)


#Contact service class
class ContactService:
    def __init__(self):
        self.contacts = []

    #Adds a new contact using given information
    def add_contact(self, id, first_name, last_name, number, address):
        for contact in self.contacts:
            #if contact ID already exists, throw error
            if contact.get_id() == id:
                raise ValueError("ID already exists.")
        contact = Contact(id, first_name, last_name, number, address)
        self.contacts.append(contact)

    #Deletes a contact with given information
    def delete_contact(self, id):
        for i, contact in enumerate(self.contacts):
            if contact.get_id() == id:
                del self.contacts[i]
                print("Contact deleted.")
                return
        print("Contact ID not found.")

    #Updates existing contact with given information
    def update_contact(self, id, field, value):
        for contact in self.contacts:
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
    
    #Returns the list of existing contacts
    def get_all_contacts(self):
        return list(self.contacts)

#Task service class
class TaskService:
    def __init__(self):
        self.tasks = []

    #Adds a new task using given information
    def add_task(self, id, name, desc):
        for task in self.tasks:
            if task.get_id() == id:
                raise ValueError("Error: ID already exists.")
        task = Task(id, name, desc)
        self.tasks.append(task)

    #Deletes a task with given information
    def delete_task(self, id):
        for i, task in enumerate(self.tasks):
            if task.get_id() == id:
                del self.tasks[i]
                print("Task deleted.")
                return
        print("Task ID not found.")

    #Updates a task with given information
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

    #Returns the list of existing tasks
    def get_all_tasks(self):
        return list(self.tasks)


# ======================= Main Method =======================

def main():
    appointment_service = AppointmentService()
    contact_service = ContactService()
    task_service = TaskService()

    #Main Menu   
    while True:
        print("\n=== Main Menu ===")
        print("1. Manage Appointments")
        print("2. Manage Contacts")
        print("3. Manage Tasks")
        print("4. Exit")
        choice = input("Choose (1-4): ")

        #Appointment Menu
        if choice == "1":
            while True:
                print("\n--- Appointments ---")
                print("1. Add")
                print("2. View")
                print("3. Delete")
                print("4. Update")
                print("5. Back")
                appt_choice = input("Choose (1-5): ")
                #Adding Appointments
                if appt_choice == "1":
                    id = input("Appointment ID: ")
                    date_str = input("Enter Appointment Date (YYYY-MM-DD HH:MM AM/PM): ")
                    try:
                        appointment_date = datetime.strptime(date_str, "%Y-%m-%d %I:%M %p")
                        appointment_desc = input("Appointment Description: ")
                        appointment_service.add_appointment(id, appointment_date, appointment_desc)
                        print("\nAppointment added.")
                    except Exception as e:
                        print("\nError:", e)
                #Reading Appointments
                elif appt_choice == "2":
                    print("")
                    for appt in appointment_service.get_all_appointments():
                        print(appt)
                #Deleting Appointments
                elif appt_choice == "3":
                    id = input("Enter ID to delete: ")
                    appointment_service.delete_appointment(id)
                #Updating Appointments
                elif appt_choice == "4":
                    try:
                        id = input("Enter Appointment ID to update: ")
                        field = input("Which field to update (date or description): ")
                        value = input("New value: ")
                        appointment_service.update_appointment(id, field, value)
                    except Exception as e:
                        print("\nError:", e)  
                #Return to main menu
                elif appt_choice == "5":
                    break
                #Catch error if invalid input
                else:
                    print("Invalid option. Try again.")
                    
        #Contact Menu
        elif choice == "2":
            while True:
                print("\n--- Contacts ---")
                print("1. Add")
                print("2. View")
                print("3. Delete")
                print("4. Update")
                print("5. Back")
                c_choice = input("Choose: ")
                #Adding Contacts
                if c_choice == "1":
                    try:
                        id = input("Contact ID: ")
                        fn = input("First Name: ")
                        ln = input("Last Name: ")
                        num = input("Phone Number: ")
                        addr = input("Address: ")
                        contact_service.add_contact(id, fn, ln, num, addr)
                        print("\nContact added.")
                    except Exception as e:
                        print("\nError:", e)
                #Viewing Contacts
                elif c_choice == "2":
                    for c in contact_service.get_all_contacts():
                        print(c)
                #Deleting Contacts
                elif c_choice == "3":
                    id = input("Enter ID to delete: ")
                    contact_service.delete_contact(id)
                #Updating Contacts
                elif c_choice == "4":
                    try:
                        id = input("Enter ID to update: ")
                        field = input("Which field to update (first name, last name, number, address): ")
                        value = input("New value: ")
                        contact_service.update_contact(id, field, value)
                    except Exception as e:
                        print("\nError:", e)
                #Return to main menu
                elif c_choice == "5":
                    break
                #Catch error if invalid input
                else:
                    print("Invalid option. Try again.")
        
        #Task menu
        elif choice == "3":
            while True:
                print("\n--- Tasks ---")
                print("1. Add")
                print("2. View")
                print("3. Delete")
                print("4. Update")
                print("5. Back")
                t_choice = input("Choose (1-5): ")
                #Adding Tasks
                if t_choice == "1":
                    try:
                        id = input("Task ID: ")
                        name = input("Task Name: ")
                        desc = input("Task Description: ")
                        task_service.add_task(id, name, desc)
                        print("\nTask added.")
                    except Exception as e:
                        print("\nError:", e)
                #Viewing Tasks
                elif t_choice == "2":
                    print("")
                    for t in task_service.get_all_tasks():
                        print(t)
                #Deleting Tasks
                elif t_choice == "3":
                    id = input("Enter ID to delete: ")
                    task_service.delete_task(id)
                #Updating Tasks
                elif t_choice == "4":
                    try:
                        id = input("Enter ID to update: ")
                        field = input("Which field to update (name or description): ")
                        value = input("New value: ")
                        task_service.update_task(id, field, value)
                    except Exception as e:
                        print("\nError:", e)
                #Return to Main Menu
                elif t_choice == "5":
                    break
                #Catch error if invalid input
                else:
                    print("Invalid option. Try again.")
        #Exit program
        elif choice == "4":
            print("Goodbye!")
            break
        #Catch error if invalid input
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()


