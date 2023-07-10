<?php
echo"asdasdsada";
session_start();

// Database connection
$host = "localhost";
$dbUsername = "root";
$dbPassword = "";
$dbName = "login_system";


$conn = new mysqli($host, $dbUsername, $dbPassword, $dbName);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Login user
if (isset($_POST['login'])) {
  $username = $_POST['username'];
  $password = $_POST['password'];

  $loginQuery = "SELECT * FROM users WHERE username='$username' AND password='$password'";
  $result = $conn->query($loginQuery);

  if ($result->num_rows == 1) {
    $_SESSION['username'] = $username;
    header("Location: welcome.php");
  } else {
    echo "Invalid username or password!";
  }
}

$conn->close();
?>
