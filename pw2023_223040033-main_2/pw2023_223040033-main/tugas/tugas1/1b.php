<?php
$npm = 33;
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    // echo "Aku adalah angka <b> $npm </b> </br>";
    // echo "Jika aku dikali 5, maka aku sekarang menjadi ";
    // echo "<b>" . $npm * 5 . "</b>" . "</br>";
    // echo "Jika aku dibagi 2, maka aku sekarang menjadi ";
    // echo "<b>" . 165 / 2 . "</b>" . "</br>";
    // echo "Jika aku ditambah 75, maka aku sekarang menjadi ";
    // echo "<b>" . 82.5 + 75 . "</b>" . "</br>";
    // echo "Jika aku dikurang 20, maka aku sekarang menjadi ";
    // echo "<b>" . 157.5 - 20 . "</b>";


    ?>

    <?php
    echo "Aku adalah angka <b> $npm </b> </br>";
    echo "Jika aku dikali 5, maka aku sekarang menjadi 
    <b>" . ($npm = $npm * 5) . "</b> </br>";
    echo "Jika aku dibagi 2, maka aku sekarang menjadi 
    <b>" . ($npm = $npm / 2) . "</b></br>";
    echo "Jika aku ditambah 75, maka aku sekarang menjadi 
    <b>" . ($npm = $npm + 75) . "</b></br>";
    echo "Jika aku dikurang 20, maka aku sekarang menjadi 
    <b>" . ($npm = $npm - 20) . "</b>";
    ?>


</body>


</html>