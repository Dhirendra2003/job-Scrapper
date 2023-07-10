<?php
 $username = $_POST['username'];
 $password = $_POST['password'];
 $email = $_POST['email'];
echo $username;
echo $password;
echo $email;
$output = shell_exec("python register.py $username,$password,$email");
echo($output);
?>