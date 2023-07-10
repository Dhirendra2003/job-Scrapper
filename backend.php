<html>
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
    *{
        font-family: 'Poppins', sans-serif;
    }
</style>
</head>

<body>
  
    <header>
        <a href="home.html">
        <img src="logo.png" class="logo" alt="">
        </a>
        <h1>find your dream</h1>
        <nav>
            <p>home</p>
            <p>suggestions</p>
            <p>contact</p>

        </nav>
    </header>
    
    </body>
</html>

<?php
      $site=$_GET['site'] ;
      $post=$_GET['post'] ; 
      $loc=$_GET['location'] ;
    
      

      if ($site=="shine"){
        echo("<p class='sdata'>".$post."@".$loc. "</p>");
        echo "<div class='layout'>";
        $output = shell_exec("python test1.py $post, $loc");
        echo $output;
        echo "</div>";
      }
      elseif ($site=="talent"){
        echo("<p class='sdata'>".$post."@".$loc. "</p>");
        echo "<div class='layout'>";
        $output = shell_exec("python test2.py $post, $loc");
        echo $output;
        echo "</div>";
      }
      else{
        echo("<p class='sdata'>".$post."@".$loc. "</p>");
        echo "<div class='layout'>";
        $output = shell_exec("python test3.py $post, $loc");
        echo $output;
        echo "</div>";
      }
    
    

    ?>

