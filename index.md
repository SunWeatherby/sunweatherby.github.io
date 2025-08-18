The artifacts I have chosen for all three enhancements in this course are three Java files from Project Two of CS 320: Software Testing, Automation, and Quality Assurance, which were created on April 28th, 2024. These three files contain only basic functions for creating and deleting Appointments, Contacts, or Tasks objects of their respective file names, and exist only to experiment with manual and automatic function testing. By taking a non-functional program and converting it into a fully-functional service, I planned on demonstrating my abilities throughout the course.

## Code Review

![video](https://youtu.be/DugBr6oFJ4M)

The above video contains the code review of my artifacts. As this was done early in the course, my intial plans for the project do not completely align with the final result due reconsidering my plans throughout the course.

---

Download the original build files: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/Original).

## Enhancement 1: Software Engineering and Design

![screenshot](/assets/enhancementOne.png)

For Enhancement One, I rebuilt the code of each file in Python as a singular file with separate classes and models for each object. The appointment service could not initially update existing appointments, so an update method was added. To ensure that users do not try to add an appointment for a past date, an error is thrown to prevent the user from doing so. Finally, I added a looping main method for users to access the create, read, update, and delete methods for each class.
Since the original artifact was only meant for utilizing automatic testing, the process of enhancing the artifact essentially meant rebuilding from scratch. I spent most of that time working on the main method. Since the main method initially didn't exist, I had to think about how I wanted it to connect to the different functions of the program. Although the final result is still relatively basic, I learned more about date conversion and adjusting code to make it more user-friendly with the appointment method, since the original artifact lacked a function for converting strings into dates and times. My first attempt used date and military time to create appointments. However, after some consideration, I learned how to implement AM/PM into this since I believe most users would attempt to do this anyway or would have a harder time trying to read or write military time.
By enhancing three non-functional programs into a single functioning command-line program, this enhancement meets the course goal of using well-founded and innovative techniques, skills, and tools to deliver value and accomplish industry-specific goals.

Download the build files and narrative document for enhancement one: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/EnhancementOne).

## Enhancement 2: Algorithms and Data Structures

![screenshot](/assets/enhancementTwo.png)

For the second enhancement, I chose to continue improving the previous artifact because the best way to demonstrate my abilities is by building on the previous enhancement and further developing the object classes to prove my skill in data structures. Initially, I had planned to combine all the objects by making Tasks and Appointments children of Contact objects, but I found myself questioning this idea after completing the first enhancement. I decided to keep them separate, but have tasks and appointments require an assigned contact. I also gave Contacts a subtype for employees and customers to differentiate the two. In addition to this, appointments and tasks now require an assigned customer or employee, respectively, to be created, which are listed when attempting to create one. If the user tries to make an appointment/task while there are no existing customers/employees, the program will inform the user that no customers/employees exist and cancel the action. During this enhancement, I also decided to reorganize the code to have a reading flow that made more sense, as previously, the first option on the menu was appointments instead of contacts, which couldn't exist without a contact. 
By implementing these changes, this enhancement meets the course goals of utilizing computer science practices and standards to solve a given problem while managing the trade-offs and using a security mindset to mitigate design flaws in the program.

Download the build files and narrative document for enhancement two: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/EnhancementTwo).

## Enhancement 3: Databases

![screenshot](/assets/enhancementThree.png)

For the final enhancement, I chose to finish improving the previous artifact to create a complete version of the program. For this enhancement, I demonstrated my skill in databases by adding external data saving and exporting the information to MongoDB to be displayed on an interactive HTML page. All information on contacts, tasks, and appointments is saved to respective JSON files, which are exported after exit is selected on the main menu. A few objects were pre-created and saved to the files for easy testing. A Flask backend fetches the information from MongoDB and renders the page using the index template.
Additionally, this backend also sorts the appointments by date. The index file creates an interactive page that allows users to select whether to display contacts, tasks, or appointments using buttons. The Contacts page also has additional buttons for displaying all contacts, or just customers or employees. Each of these lists also has a search bar to search by ID.
This enhancement took the longest, as it required coding three different files to ensure everything worked instead of just one. While the JSON saving and exporting went smoothly, I struggled with coding the application properly since I was new to Flask. I learned a lot about Flask as a result. I also had difficulty properly organizing the HTML to look clean during runtime. I had to learn how to properly code the spacing to ensure the page elements would be displayed as intended. By providing a visual interface to users and creating a database for employees to organize information, this enhancement meets the course goals of delivering professional-quality written and visual communications and employing strategies for building collaborative environments.

Download the build files and narrative document for enhancement three: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/EnhancementThree).

---

# Self-assessment

Throughout my time in the Computer Science program, I've focused on building a strong foundation in core technical skills while also learning how to apply those skills to solve real-world problems independently. Completing this ePortfolio allowed me to reflect on how far I have come, from working on isolated functions to building a complete, functioning application with a backend database and interactive web interface.
The coursework and projects I completed helped me shape my professional goals and reaffirmed my interest in software development. I am especially proud of my ability to take a basic, non-functional artifact—intended initially only for test automation and turn it into a working application that saves, sorts, and displays data.

While I didn't have team-based projects in the program, this allowed me to work independently on every stage of development, from planning and design to implementation and debugging. For example, I had to plan the architecture of my application independently, decide how to structure object relationships, and troubleshoot logic errors and integration issues without relying on others. This required strong problem-solving skills, which are essential in any professional software engineering job. This independent development also led me to approach my projects with a focus on communicating with future users or stakeholders who would need to interact with the system. This was especially true during the second and third enhancements, where I had to anticipate how users would navigate the program, input data, and interpret information. For instance, I redesigned the main menu structure to improve the flow of object creation, requiring contacts to be displayed before appointments or tasks. I also added clear prompts, error messages, and safeguards to make the program easier to understand and harder to misuse. These decisions mirror how developers must consider the needs of stakeholders, such as business users or clients, when building user-facing systems. My work on the HTML interface reinforced this, as I needed to organize the layout and filters in a way that would make sense to the average user.

These three enhancements of the artifacts demonstrate this growth through the course outcomes; 
- Data Structures and Algorithms: I used basic data structures to organize user input and object relationships. 
- Software Engineering and Design: I restructured a simple Java artifact into a modular Python application using service layers and separate classes for logic, storage, and interaction.
- Databases: I implemented persistent storage using JSON and integrated MongoDB to save and display data through a Flask-powered HTML interface. 
- Security and Data Integrity: I incorporated logic to ensure that invalid operations couldn't occur. For example, disallowing appointment creation when no contacts exist or preventing the use of outdated dates.

Each stage adds new complexity to the same artifact: starting with a basic function tester, then building a working application with data relationships, and finally connecting it to a database and interactive interface. I chose to work from the same base throughout because I wanted to demonstrate not only my technical progression, but also my ability to refactor, build upon, and improve existing work, a highly relevant skill in real-world software maintenance and iteration.


