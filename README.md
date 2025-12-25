# Student Performance Prediction System (ML-Based)

## Overview
This project is a web-based student performance prediction system that uses machine learning to predict whether a student will pass or fail based on academic and behavioral factors.  
The system integrates a trained ML model with a PHP–MySQL web application to provide real-time predictions.

## Features
- Student data input through web interface
- Machine learning–based performance prediction
- PHP backend with MySQL database integration
- Stores student records and prediction results
- Simple and clean UI for easy interaction

## Technology Stack
**Frontend**
- HTML5
- CSS3

**Backend**
- PHP

**Database**
- MySQL

**Machine Learning**
- Python
- Scikit-learn
- Random Forest Classifier

## Input Parameters
- Attendance percentage
- Daily study hours
- Previous semester score
- Internal assessment marks
- Class participation score

## Output
- Predicted Result: **Pass / Fail**

## Machine Learning Workflow
1. Dataset preparation and preprocessing
2. Model training using Random Forest
3. Model saved as `.pkl` file
4. PHP backend sends user input to Python script
5. ML model predicts student performance
6. Result displayed and stored in database

## Project Structure

