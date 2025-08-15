import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class ContactService {
	
	//araylist and input scanner
	private List<Contact> contacts;
	Scanner scn = new Scanner(System.in);
	
	//creates and arraylist named contacts
	public ContactService() {
		contacts = new ArrayList<>();
	}
	
	//creates a new contact
	public Contact addContact(String id, String firstName, String lastName, String number, String address) {
		//IllegalArgumentException if id already exists
		for (Contact existingContact : contacts) {
			if(existingContact.getID().equals(id)) {
				throw new IllegalArgumentException("Error: ID already exists.\n");
			}
		}
		Contact contact = new Contact(id, firstName, lastName, number, address);
		contacts.add(contact);	
		return contact;
	}
	
	//iterates through the contact list to delete contact of same ID
	public void deleteContact(String id) {
		Iterator<Contact> iterator = contacts.iterator();
		while (iterator.hasNext()) {
			Contact contact = iterator.next();
			if (contact.getID().equals(id)) {
				iterator.remove();
				System.out.println("Contact deleted.");
				return;
			}
			//displays error message if ID not found
			else {
				System.out.println("Contact ID not found.");
			}
		}
	}
	
	//updates contact information using a switch
	public void updateContact(String id, String field, String value) {
		//sets field to lower case in case user changes casing
		field.toLowerCase();
		for (Contact contact : contacts) {
			if (contact.getID().equals(id)){
				switch (field) {
					case "firstname":
						contact.setFirstName(value);
						break;
					case "first name":
						contact.setFirstName(value);
						break;
					case "lastname":
						contact.setLastName(value);
						break;
					case "last name":
						contact.setLastName(value);
						break;
					case "number":
						contact.setNumber(value);
						break;
					case "phone number":
						contact.setNumber(value);
						break;
					case "address":
						contact.setAddress(value);
						break;
					//displays error message if input isn't a proper contact field
					default:
						throw new IllegalArgumentException("Error: invalid field type. Please check spelling.\n");
				}
				return;
			}
			else {
				throw new IllegalArgumentException("Error: No task with given ID found.\n");
			}
		}	
	}
	
	//returns a copy of the contact list
	public List<Contact> getAllContacts(){
		return new ArrayList<>(contacts);
	}
	
}
