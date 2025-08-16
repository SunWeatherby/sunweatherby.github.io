The artifact I have chosen for all three enhancements in this course are three java files from Project Two of CS 320: Software Testing, Automation, and Quality Assurance which were created April 28th, 2024. These three files contain only basic functions for creating and deleting Appointments, Contacts, or Tasks objects of their respective file names, and existed only to experiment with manual and automatic function testing. By taking a non-functional program and converting it into a fully-functional service, I planned on demonstrating my abilities throughout the course.

## Code Review

There will be a summary of the code review here

---

Original build files: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/Original).

## Enhancement 1: Software Engineering and Design

PHOTO HERE

For enhancement one of the artifacts, I rebuilt the code of each individual file in python as a singular file with separate class and model and service classes for each object. The appointment service originally did not have a function for updating existing appoints, so an update method was added. To ensure that users did not try to add an appointment that was set for a past date, an error throw was also added to prevent the user from doing so. Finally, I added a looping main method for users to access the create, read, update, and deleted methods for each class.
Since the original artifact was only meant for utilizing automatic testing, the process of enhancing the artifact essentially meant rebuilding from a scratch. The majority of time spent was on the main method. Since the main method initially didn’t exist, I had to think about how I wanted it to properly connect to the different functions of the program. Although the final result is still relatively basic, I believed I learned a bit more about date conversion and adjusting code to make it more user-friendly with the appointment method since the original artifact did not have a function for converting strings into date and time. My first attempt used date and military time to create appointments, but after some consideration I learned how to implement AM/PM into this since I believe most users would attempt to do this anyway or would have a harder time trying to read or write military time.
By enhancing three non-functional programs into a single functioning command line program, I believe this enhancment meets the course goal of using well-founded and innovative techniques, skills, and tools to deliver value and accomplish industry-specific goals.

Download the build files and narrative document for enhancement one: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/EnhancementOne).

## Enhancement 2: Algorithms and Data Structures

Summary of enhancement 2 here

PHOTO HERE

However upon completion of this enhancement, I found myself questing my initial idea for second enhancement, which was to combine all the objects my making Tasks and Appointments children of Contact objects. I believe it might be better to have them still separate, but tasks and/or appointments could require an assigned contact. This might also require contacts having a label for employees and customers or even splitting them into employee contacts and customer contacts, although I worry having an additional class to specify this would clutter the code or make it redundant.

Download the build files and narrative document for enhancement two: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/EnhancementTwo).

## Enhancement 3: Databases

PHOTO HERE

Summary of enhancement 3 here

Download the build files and narrative document for enhancement two: [here](https://github.com/SunWeatherby/sunweatherby.github.io/tree/EnhancementThree).

---

# Self-assessment

ASSESSMENT HERE
