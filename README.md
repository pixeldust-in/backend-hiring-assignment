# backend-hiring-assignment
Pixeldust Backend Hiring Assignment

## Django Assignment(Mandatory)
Create a project in Django to demonstrate a task management system. The functionality should include the ability to manage projects and tasks

#### Features
1. Tasks 
    1. List all the tasks
    2. Create a new task
    3. Delete a task
    4. Edit the task status
2. Projects
    1. List all the projects(only the ones that have not ended)
    2. Create a new project
    3. Delete a project
    4. View a project
        1. Show list of all the tasks for that particular project


#### Database Design
**Project**:
1. Name
2. Description
3. Client(Foreign key to client)
4. StartDate(The day when the entry is created)
5. Enddate


**Task**:
1. Name
2. Description
3. Project(Foreign key to Project)
4. Status(TODO, WIP, ONHOLD, DONE)


## DRF Assignment(Optional):
It's good if the candidate knows DRF and can create REST API's as DRF is heavily used at Pixeldust.
If you are someone who knows DRF and wants an edge. Please create REST API's for the following
1. Fetch all projects(with pagination)
2. Fetch all tasks(with pagination)
3. View a project(should return all the tasks for the project too)
4. View a task
5. Delete a task
6. Delete a project
 


## Submission:
Fork this repository to your personal account and for submission raise a pull request againt base repository once you're done with your solution. 

## Timeline:
You will get one week to complete the assignment. Please let us know in advance if for whatever reasons you cannot complete it within the said duration but you intent to


### Hygiene:
1. Enter all the project dependencies in a requirements.txt within the project so that it is easy to setup the project
2. Explain with comments wherever you are doing something complex
3. Define your functions/classes/variables with clear naming conventions


