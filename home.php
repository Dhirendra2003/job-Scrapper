<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="home.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap" rel="stylesheet">
    <style>
        * {
            font-family: 'Poppins', sans-serif;

        }
    </style>
</head>

<body>

    <header>
        <a href="home.php">
            <img src="logo.png" class="logo" alt="">
        </a>
        <h1>find your dream</h1>
        <nav>
            <p>home</p>
            <p>suggestions</p>
            <p>contact</p>

        </nav>
    </header>
    <div class="form">
        <form action="backend.php" method="get">
            <legend>Enter Your Details Below</legend>
            <br>
            <div class="inp">
                <img src="siteIC.png" class="icon">
                <select class="enter" name="site" id="site">
                    <option value="shine">Shine.com</option>
                    <option value="talent">Talent.com</option>
                    <option value="simply">SimplyHired.com</option>
                </select>
                <img src="postIC.png" class="icon">
                <input class="enter" type="text" placeholder="job title..." id="post" name="post">
                <img src="locationIC.png" class="icon">
                <input class="enter" type="text" placeholder="location..." id="place" name="location">

            </div>
            <button id="search" onclick="checkNet()">Search <img src="searchIC.png" class="icon"></button>
        </form>
    </div>

    <?php
        echo("<div class='newssec'>");
      echo("<h2 class='data'>Latest Alerts:</h2>");
      echo "<div class='news'>";
      $output = shell_exec("python news.py ");
      echo $output;
      echo "</div>";
      echo "</div>";
    ?>


</body>
<script>

    function checkNet() {
        if (!navigator.onLine) {
            document.write("<body><h1>Network error: You are not connected to the internet</h1></body>");
            alert("Network error: You are not connected to the internet.");
        }
    }   
</script>

</html>