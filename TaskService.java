import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

public class TaskService {
	//arraylist and input scanner
	private List<Task> tasks;
	Scanner scn = new Scanner(System.in);
	
	//creates and arraylist named contacts
	public TaskService() {
		tasks = new ArrayList<>();
	}
	
	//creates a new task
	public Task addTask(String id, String name, String desc) {
		//IllegalArgumentException if id already exists
		for (Task existingTask : tasks) {
			if(existingTask.getID().equals(id)) {
				throw new IllegalArgumentException("Error: ID already exists.\n");
			}
		}
		Task task = new Task(id, name, desc);
		tasks.add(task);	
		return task;
	}
	
	//iterates through the task list to delete task of same ID
	public void deleteTask(String id) {
		Iterator<Task> iterator = tasks.iterator();
		while (iterator.hasNext()) {
			Task task = iterator.next();
			if (task.getID().equals(id)) {
				iterator.remove();
				System.out.println("Task deleted.");
				return;
			}
			//displays error message if ID not found
			else {
				System.out.println("Task ID not found.");
			}
		}
	}
	
	//updates task information using a switch
	public void updateTask(String id, String field, String value) {
		//sets field to lower case in case user changes casing
		field.toLowerCase();
		for (Task task : tasks) {
			if (task.getID().equals(id)){
				switch (field) {
					case "name":
						task.setName(value);
						break;
					case "description":
						task.setDesc(value);
						break;
					case "desc":
						task.setDesc(value);
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
	
	//returns a copy of the task list
	public List<Task> getAllTasks(){
		return new ArrayList<>(tasks);
	}
	
}