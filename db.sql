CREATE DATABASE student_performance_db;
USE student_performance_db;
CREATE TABLE students(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
attendance FLOAT,
study_hours FLOAT,
previous_score FLOAT,
internal_marks FLOAT,
participation FLOAT,
predicted_result VARCHAR(20)
);