<?php
//Function to write data to file
function updateStatus($new) {
    $f = fopen('./period.dat', 'w');
    if (!$f) return false;
    if (flock($f, LOCK_EX)) {
        ftruncate($f, 0);
        fwrite($f, $new);
        flock($f, LOCK_UN);
        fclose($f);
        return true;
    }
    fclose($f);
    return false;
}

echo "PHP changing LED blinking period script.<br>";


if(isset($_GET['period'])) {
    $period = $_GET['period'];

    $json_to_send = json_encode(array("period" => (float)$period));
    echo 'Sending json: ' . $json_to_send . '<br>';

    $result = updateStatus($json_to_send);
    if ($result == true)
        echo "Data saved to fully succesfully.<br>";
    else
        echo "Saving data failure!<br>";
}
else {
    echo 'Requires argument - "period" not specified!<br>';
}

?>
