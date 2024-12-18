# Simple Program to Show Topics and Activities

This project implements a **Simple Program to Show Topics and Activities** using Python. It allows users to display topics along with their associated activities in a structured format.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Data Structures](#data-structures)
4. [How to Use](#how-to-use)
5. [Example Usage](#example-usage)
6. [Acknowledgments](#acknowledgments)

---

## Project Overview

The Simple Program to Show Topics and Activities enables users to:

1. **Display Topic Details** (Title and Description).
2. **List Activities** associated with each topic.
3. **Show Activity Details** (Title, Type, and Description).

This system uses Python dictionaries and lists to manage topics and activities efficiently.

---

## Features

1. **Display Topics**  
   Users can view the title and description of each topic.

2. **List Activities**  
   Each topic's associated activities are listed with their details.

3. **Structured Output**  
   The program displays information in a clear and structured format.

---

## Data Structures

### Topic List Structure

The system uses a list of dictionaries to store topics, where each topic contains:

1. **Title**: The title of the topic.
2. **Description**: A brief description of the topic.
3. **Activities**: A list of activity IDs associated with the topic.

### Activity Dictionary Structure

The system uses a dictionary to store activities, where each activity is identified by an ID and contains:

1. **Title**: The title of the activity.
2. **Type**: The type of the activity (e.g., assignment, material).
3. **Description**: A brief description of the activity.

---

## How to Use

### Step 1: Clone the Repository

```bash
git clone https://github.com/filzarahma/Simpel-LMS-Registrasi-Mata-Kuliah
```

### Step 2: Run the Program

Navigate to the project directory and run the `topic.py` script:

```bash
cd Simple-Program-Show-Topic
python topic.py
```

### Step 3: Follow the Output

The program will display the topics and their associated activities in a structured format.

---

## Example Usage

### Display Topics and Activities

```plaintext
----Function "show_topic" is running----

Title       : Dummy Topic 1
Description : This is the description for topic 1
List of Activities    :
ID  | Title                  | Type          | Description
----------------------------------------------------------------------
0   | Dummy Assignment 1     | assignment    | Create a Game program
1   | Dummy Material         | material      | This week's slides

Title       : Dummy Topic 2
Description : This is the description for topic 2
List of Activities    :
ID  | Dummy Assignment 2     | assignment    | Create an LMS program

Press Enter to return to the main menu...
```

---

## Acknowledgments

This project demonstrates a basic **topic and activity display system** using Python. It serves as an excellent resource for learning Python programming and data structure management.

Feel free to use this project for educational purposes or extend it for more advanced use cases. Feedback and contributions are welcome! 😊
