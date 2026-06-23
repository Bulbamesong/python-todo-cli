# Python To-Do App

A simple console-based To-Do application written in Python.

## Description

This project is a command-line task manager that allows users to manage a list of tasks.

All data is stored in a local text file (`tasks.txt`), which ensures that tasks persist after the program is closed.

This project was built as part of learning Python fundamentals such as file handling, lists, loops, and user input.

## Features

- Add new tasks
- View all tasks
- Delete tasks by index
- Persistent storage using a text file
- Simple menu-based interface

## How it works

The program works with a simple flow:

1. Reads tasks from `tasks.txt`
2. Loads them into a list
3. Allows the user to modify the list
4. Saves changes back to the file

Each line in the file represents one task.

## How to run

Make sure Python is installed.

Run the program:

```bash
python main.py
```
## Example

Do you want to see/add/delete the tasks? see/add/delete:
see

0 Buy milk
1 Do homework
2 Call friend
Notes
Tasks are indexed starting from 0
Data is stored locally in a text file
Console-based application (no graphical interface)

## Author

Created as a Python learning project to practice file handling, loops, and basic program structure.
