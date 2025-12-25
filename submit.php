<?php
include "db_connect.php";
$data = implode(" ", [
$_POST['attendance'],
$_POST['study_hours'],
$_POST['previous_score'],
$_POST['internal_marks'],
$_POST['participation']
]);

$cmd = "python predict.py ".$data;
$output = shell_exec($cmd);
$pred = trim($output);

$sql="INSERT INTO students(name,attendance,study_hours,previous_score,internal_marks,participation,predicted_result)
VALUES('$_POST[name]','$_POST[attendance]','$_POST[study_hours]','$_POST[previous_score]','$_POST[internal_marks]','$_POST[participation]','$pred')";
mysqli_query($conn,$sql);

echo "<h2>Prediction Result: $pred</h2>";
?>