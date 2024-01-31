# Data Analysis System with Python

## Overview

This Python program implements a simple data analysis system, focusing on processing and analyzing student data stored in a CSV (Comma-Separated Values) file. The system provides functionalities such as reading data from a file, listing data, computing and showing grades, searching by name, calculating descriptive statistics, performing regression analysis, making predictions, and exiting the system.

## Project Guidelines

### File Structure

- `main.py`: The main Python script containing the data analysis system.
- `data.csv`: CSV file containing student data with variables: student's ID, name, number of study hours, and final score.

### Features

1. **Welcome Screen:**
   - Display a welcome screen when the system starts.

2. **Menu Options:**
   - The system provides the following menu options:
      1. Read Data
      2. List Data
      3. Compute and Show Grades
      4. Search by Name
      5. Descriptive Statistics
      6. Regression Analysis
      7. Prediction
      8. Exit

3. **Read Data:**
   - Ask for a file name and read the CSV file, storing its content in variables (4 list variables).
   - Print a message showing that reading data was successful.

4. **List Data:**
   - Display the content of the data file in a readable format.

5. **Compute and Show Grades:**
   - Compute and print student’s ID, name, and grade based on the score according to specified grade rules.

6. **Search by Name:**
   - Ask for a student's name or part of the name.
   - Print data for all students with names containing the given name/part.

7. **Descriptive Statistics:**
   - Calculate and show the mean, variance, and standard deviation of the variables: hours and score.

8. **Regression Analysis:**
   - Calculate the simple regression parameters b0 and b1 of the regression equation (score = b0 + b1 * hours).
   - Print the regression equation.

9. **Prediction:**
   - Ask for the number of hours and print the predicted score using the regression equation.

10. **Exit:**
    - Print a goodbye message and exit the system.

## Usage

1. Clone the repository to your local machine.
2. Run the `main.py` script using Python.
3. Follow the on-screen menu to interact with the data analysis system.

Feel free to customize the file names, add more features, or make any modifications as needed.
