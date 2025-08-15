import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;
import java.util.Date;

public class AppointmentService {
	
	//arraylist and input scanner
	private List<Appointment> appointments;
	Scanner scn = new Scanner(System.in);
	
	//creates and arraylist named appointments
	public AppointmentService() {
		appointments = new ArrayList<>();
	}
	
	//creates a new appointment
	public Appointment addAppointment(String id, Date appointmentDate, String desc) {
		//IllegalArgumentException if id already exists
		for (Appointment existingAppointment : appointments) {
			if(existingAppointment.getID().equals(id)) {
				throw new IllegalArgumentException("Error: ID already exists.\n");
			}
		}
		//Creates new appointment
		Appointment appointment = new Appointment(id, appointmentDate, desc);
		appointments.add(appointment);	
		return appointment;
	}
	
	//iterates through the appointment list to delete appointment of same ID
	public void deleteAppointment(String id) {
		Iterator<Appointment> iterator = appointments.iterator();
		while (iterator.hasNext()) {
			Appointment appointment = iterator.next();
			if (appointment.getID().equals(id)) {
				iterator.remove();
				System.out.println("Appointment deleted.");
				return;
			}
			//displays error message if ID not found
			else {
				System.out.println("Appointment ID not found.");
			}
		}
	}
	
	//returns a copy of the appointment list
	public List<Appointment> getAllAppointments(){
		return new ArrayList<>(appointments);
	}
	
}