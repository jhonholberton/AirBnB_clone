<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png" style="height:50%;width:50%" />

# Description

First step: Write a command interpreter to manage your AirBnB objects. This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

## The console

create your data model manage (create, update, destroy, etc) objects via a console / command interpreter store and persist objects to a file (JSON file) The first piece is to manipulate a powerful storage system.

## Features
As stated above, this particular piece of the AirBnB clone is a console, i.e. a command intepreter that allows for the developer to be able to contact and control various objects on a high level. See below for more details.

### Command Interpreter
#### Description

Modifies the application's functionality from the command line, i.e.:
+ Creates a new object.
+ Retrieves an object.
+ Provides data on objects such as their id numbers and details specific to the object, e.g. Place object can have a certain number of rooms which the console can display
+ Update and/or add attributes to an object.
+ Destroys object.

#### Usage

To launch the console application in interactive mode run the following:
```./console.py ```

If non-interactive mode is desired run:
```echo "command" | ./console.py ```

#### Commands
Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Also exits the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of a specified class. In addition, creates a Json file containing object representations while printing the id the object to stdout. | **create** \<class_name\>
**show**    | Prints the string representation of an instance as defined in the __str__ method. | **show** \<class_name class_id\>
**destroy** | Deletes an instance. | **destroy** \<class_name class_id\>
**all** | Prints the string representation of all instances of a class| **all** or **all** \<class_name class_id\>
**update** | Adds or modifies attribute(s) of an instance of a class | **update** \<class_name class_id key value\>

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

## Tests
We've created tests to verify the stability and functionality of the console and classes created. If there is a desire to run said tests, while in the AirBnB directory running the following command will execute the test modules that are in the test/test_models/ directory

**python3 -m unittest discover tests**

## Author

* **Reinaldo Castro**
* **Jhon Gonzalez**
