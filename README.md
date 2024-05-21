# AirBnB Clone

This is the first step towards building a full web application called the AirBnB clone. This project focuses on creating a command interpreter to manage objects for the AirBnB website. The command interpreter allows you to create, retrieve, update, and destroy objects representing different aspects of the AirBnB application, such as users, places, cities, and more.

## Description

The AirBnB clone project consists of several steps:

1. **Command Interpreter**: This initial step involves creating a parent class (`BaseModel`) to handle the initialization, serialization, and deserialization of future instances. Additionally, it includes creating a simple flow of serialization/deserialization between instances, dictionaries, JSON strings, and file storage. This step also involves creating all classes used for the AirBnB application (`User`, `State`, `City`, `Place`, etc.) that inherit from `BaseModel`.

2. **File Storage**: The first abstracted storage engine for the project is implemented as file storage, which allows you to persist object data in files.

3. **Unit Tests**: All classes and the storage engine are thoroughly tested using unit tests to ensure their correct functionality.

Future steps will involve integrating this command interpreter with web applications, databases, and APIs.

## Command Interpreter

The command interpreter is a Python script that allows you to manage AirBnB objects through various commands. Here's how to start and use the command interpreter:

### Starting the Command Interpreter

To start the command interpreter, navigate to the project directory and run the following command: ./console.py
This will launch the command interpreter, and you should see a prompt (`(hbnb)`) where you can enter commands.

### Using the Command Interpreter

The command interpreter supports several commands to interact with AirBnB objects. Here are some examples:

- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <id>`: Display the string representation of an instance based on its class and ID.
- `destroy <class_name> <id>`: Delete an instance based on its class and ID.
- `all [<class_name>]`: Retrieve all instances of the specified class (or all instances if no class is specified).
- `update <class_name> <id> <attribute_name> <attribute_value>`: Update an attribute of an instance.
- `quit`: Exit the command interpreter.

For example, to create a new `User` instance, you would enter:
**(hbnb) create User**

To show the details of a specific `Place` instance, you would enter:
**(hbnb) show Place <place_id>**

Replace `<place_id>` with the actual ID of the `Place` instance you want to display.

For more information and a complete list of available commands, please refer to the project documentation.

