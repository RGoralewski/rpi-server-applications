$json_to_send = json_encode(array("period" => $period));

//Exit previous script if it was running
//shell_exec('\n');

//Run python script
$result = shell_exec('./blinking_led.py ' . escapeshellarg($json_to_send));
echo $result;
