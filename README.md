# AI-Powered Personalized Study Planner

## Overview

The AI-Powered Personalized Study Planner is a machine learning application designed to help students organize their learning activities more effectively. The system recommends a suitable study focus area based on a student's academic year, career goal, available study hours, and skill level. It then generates a personalized timetable to support structured and goal-oriented learning.

This project was developed to explore the practical application of machine learning in educational planning and personalized recommendations.

## Problem Statement

Students often struggle to decide how to allocate their study time efficiently, especially when preparing for different goals such as placements, higher studies, research, competitive programming, or machine learning. A one-size-fits-all study plan may not address individual needs and priorities.

This project aims to provide personalized recommendations by analyzing student-specific information and generating a study plan tailored to their objectives.

## Features

* Personalized study focus recommendation
* Machine learning-based prediction system
* Dynamic timetable generation
* Career path suggestions based on predicted focus area
* Downloadable timetable in CSV format
* Interactive web application built with Streamlit

## Methodology

The project uses a supervised machine learning approach.

### Input Features

* Academic Year
* Career Goal
* Available Study Hours per Day
* Skill Level

### Output

The model predicts an appropriate focus area, such as:

* Data Structures and Algorithms (DSA)
* Machine Learning Foundations
* Machine Learning Projects
* Deep Learning
* Research
* Competitive Programming
* Core Subjects
* Mock Test Preparation
* GRE Preparation

Based on the predicted focus area, a personalized timetable is generated.

## Machine Learning Model

The recommendation engine is built using the Random Forest Classifier available in Scikit-Learn.

Categorical variables are encoded using Label Encoding before training. The trained model and encoders are stored using Joblib and loaded during application execution.

## Technologies Used

### Programming Language

* Python

### Libraries and Frameworks

* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

## Project Structure

```text
AI-Personalized-Study-Planner
│
├── app.py
├── train_model.py
├── timetable_generator.py
├── requirements.txt
├── README.md
│
├── dataset
│   └── student_dataset.csv
│
└── model
    ├── study_planner.pkl
    ├── goal_encoder.pkl
    ├── skill_encoder.pkl
    └── focus_encoder.pkl
```
## Installation

### Clone the Repository

```bash
git clone https://github.com/Vineeshakolla/AI-Personalized-Study-Planner.git
cd AI-Personalized-Study-Planner
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run app.py
```

The application will open in a web browser and allow users to generate personalized study plans.

## Future Improvements

* Expanding the training dataset
* Incorporating additional student attributes
* Weekly and monthly study planning
* Progress tracking and performance analytics
* Cloud deployment for public access
* Enhanced recommendation accuracy through larger datasets

## Conclusion

This project demonstrates how machine learning can be used to support personalized educational planning. By combining predictive modeling with an interactive user interface, the application provides students with customized study recommendations and structured learning schedules.

## Author

Vineesha Kolla

B.Tech Computer Science
