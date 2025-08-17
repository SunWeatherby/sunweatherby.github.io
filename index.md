The artifact I have chosen for all three enhancements in this course are three java files from Project Two of CS 320: Software Testing, Automation, and Quality Assurance which were created April 28th, 2024. These three files contain only basic functions for creating and deleting Appointments, Contacts, or Tasks objects of their respective file names, and existed only to experiment with manual and automatic function testing. By taking a non-functional program and converting it into a fully-functional service, I planned on demonstrating my abilities throughout the course.

## Code Review

There will be a summary of the code review here

---

Download the original build files: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/Original).

## Enhancement 1: Software Engineering and Design

![screenshot](/assets/enhancementOne.png)

For enhancement one of the artifacts, I rebuilt the code of each individual file in python as a singular file with separate class and model and service classes for each object. The appointment service originally did not have a function for updating existing appoints, so an update method was added. To ensure that users did not try to add an appointment that was set for a past date, an error throw was also added to prevent the user from doing so. Finally, I added a looping main method for users to access the create, read, update, and deleted methods for each class.
Since the original artifact was only meant for utilizing automatic testing, the process of enhancing the artifact essentially meant rebuilding from a scratch. The majority of time spent was on the main method. Since the main method initially didn’t exist, I had to think about how I wanted it to properly connect to the different functions of the program. Although the final result is still relatively basic, I believed I learned a bit more about date conversion and adjusting code to make it more user-friendly with the appointment method since the original artifact did not have a function for converting strings into date and time. My first attempt used date and military time to create appointments, but after some consideration I learned how to implement AM/PM into this since I believe most users would attempt to do this anyway or would have a harder time trying to read or write military time.
By enhancing three non-functional programs into a single functioning command line program, I believe this enhancment meets the course goal of using well-founded and innovative techniques, skills, and tools to deliver value and accomplish industry-specific goals.

Download the build files and narrative document for enhancement one: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/EnhancementOne).

## Enhancement 2: Algorithms and Data Structures

![screenshot](/assets/enhancementTwo.png)

For the second enhancement, I chose to continue improving the previous artifact because I believe that the best way to demonstrate my abilities is by following up on previous enhancements and show my skill in data structures by developing the object classes further. Originally I had planned to combine all the objects my making Tasks and Appointments children of Contact objects, but I found myself questioning this idea after completion of enhancement one. I instead came to the decision to keep them separate, but have tasks and appointments require an assigned contact. Contacts were also given a sub-type for employees and customers to differentiate the two. In addition to this, appointments and tasks now required an assigned customer or employee respectively in order to be created, which are listed when attempting to create one. If the user attempts to create an appointment/task while there are no existing customers/employees, the program will stop before any information can be entered and inform the user no customer/employees exist. During this enhancement I also decided to re-organize the code to have a reading flow that made more sense, as previously the first option on the menu was appointments instead of contacts, which couldnt exist without a contact. 
By implementing these changes, I believe this enhancement meets the course goals of utilizing computer science practices and standards to solve a given problem while managing the trade-offs and using a security mindset to mitigate design flaws in the program.

Download the build files and narrative document for enhancement two: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/EnhancementTwo).

## Enhancement 3: Databases

![screenshot](/assets/enhancementThree.png)

For the final enhancement, I chose to finish improving the previous artifact in order to create a complete version of the program. For this enhancement, I demonstrated my skill in databases by adding external data saving and exporting the information to MongoDB to be displayed on an interactive HTML page. All information on contacts, tasks, and appoints are saved to respective json files, which are exported after exit is selected on the main menu. A few objects were pre-created and saved to the files for easy testing. A flask backend is used to fetch the information from MongoDB and render the page using the index template. Additionally, this backend also sorts the appointments by date. The index file creates an interactive page which lets users select whether to display contacts, tasks, or, appointments using buttons. Contacts also has additional buttons for displaying all contacts or just customers or employees. Each of these lists also has a search bar to be able to search the list by ID.
This enhancement took the longest out of the three enhancements, as it required needing to code 3 different files to ensure everything worked instead of just one. While the json saving and exporting went smoothly, I struggled with coding the application properly as I have not used Flask before. I believe I learned a lot about Flask as a result. I also had difficulty properly organizing the HTML to look clean during runtime and had to learn how to properly code the spacing to ensure the page elements would be displayed as I intended them to. By providing a visual interface to users and creating a database for employees to oraganize information, this enhancement meets the course goals of deliver professional-quality written and visual comminations and employing strategies for building collaborative environments.

Download the build files and narrative document for enhancement three: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/EnhancementThree).

---

# Self-assessment

Throughout my time in the Computer Science program, I’ve consistently focused on building a strong foundation in core technical skills while also learning how to independently apply those skills to solve real-world problems. Completing this ePortfolio gave me the opportunity to reflect on how far I’ve come—from working on isolated functions to building a complete, functioning application with a backend database and interactive web interface.
The coursework and projects I completed helped me shape my professional goals and reaffirmed my interest in software development, particularly in areas such as backend design, data modeling, and user-focused functionality. I’m especially proud of my ability to take a basic, non-functional artifact—originally intended only for test automation—and turn it into a working application that saves, sorts, and displays data through both a command-line interface and a visual webpage. This growth reflects my core values as a developer: independence, adaptability, and a continuous learning mindset.

While I didn’t have team-based projects in the program, that meant I had the unique challenge and opportunity to work independently on every stage of development—from planning and design to implementation and debugging. For example, in my enhancements, I had to plan the architecture of my application on my own, decide how to structure object relationships, and troubleshoot logic errors and integration issues without relying on others. This required strong problem-solving skills and a high level of self-discipline, which I believe are essential in any professional software engineering role. This independent development also led me to approached my projects from the mindset of needing to communicate with future users or stakeholders who would need to interact with the system. This was especially true during my second and third enhancements, where I had to anticipate how users would navigate the program, input data, and interpret outputs. For instance, I redesigned the main menu structure to improve the logical flow of object creation, requiring contacts to exist before appointments or tasks. I also added clear prompts, error messages, and safeguards to make the system easier to understand and harder to misuse. These decisions mirror how developers must consider the needs of non-technical stakeholders—such as business users or clients—when building user-facing systems. My work on the HTML interface reinforced this, as I needed to organize the layout and filters in a way that would make sense to someone unfamiliar with the backend code.

The portfolio reflects my applied knowledge in multiple technical areas:
- Data Structures and Algorithms: I used basic data structures to organize user input and object relationships efficiently. For example, tasks and appointments required a valid contact ID to be created. I also built in error handling to prevent creating appointments in the past, demonstrating control flow and validation logic.
- Software Engineering and Design: I restructured a simple Java artifact into a modular Python application using service layers and separate classes for logic, storage, and interaction. This mirrors real-world application architecture and shows my ability to write maintainable, scalable code.
- Databases: In the third enhancement, I implemented persistent storage using JSON and integrated MongoDB to save and display data through a Flask-powered HTML interface. I had never used Flask before, so this required learning new tools quickly and applying them in a working system—demonstrating both technical ability and adaptability.
- Security and Data Integrity: I incorporated logic to ensure that invalid operations couldn’t occur—for example, disallowing appointment creation when no contacts exist or preventing use of outdated dates. These decisions reflect an awareness of basic secure coding practices and data integrity concerns.

Portfolio Overview

The three enhancements in my portfolio tell a continuous story of growth. Each stage adds new complexity to the same artifact: starting with a basic function tester, then building a working application with data relationships, and finally connecting it to a database and interactive interface. I chose to work from the same base throughout because I wanted to demonstrate not only my technical progression, but also my ability to refactor, build upon, and improve existing work—a highly relevant skill in real-world software maintenance and iteration.
