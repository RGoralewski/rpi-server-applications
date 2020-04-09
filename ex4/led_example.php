<?php
echo "Simple server-side PHP control script:<br>";
echo "LED control<br>";

$led_state='';

if(isset($_GET['state']))
    $led_state=$_GET['state'];

if(strcmp($led_state, "ON") == 0)
{
    exec('sudo ../AM_LAB_02/ex3/bash/gpio_output_set_bash.sh');
    echo "LED state: ON";
}
elseif(strcmp($led_state, "OFF") == 0)
{
    exec('sudo ../AM_LAB_02/ex3/bash/gpio_output_reset_bash.sh');
    echo "LED state: OFF";
}
else {
    echo "LED state undefined";
}

?>
