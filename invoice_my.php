<?php

$date = null;
$number = null;
$ttc = null;
$ht = null;
$tva = null;

$file=$argv[1];
#echo $file;
#die;
$myfile = fopen($file, "r") or die("Unable to open file!");
#$output=fread($myfile,filesize($file));
#echo($output);

#foreach ($output as $line) {

while(!feof($myfile)) {
    $line=fgets($myfile);
    #echo $line;

    if ($number === null && mb_strstr(mb_strtolower($line), "n°")) {
        $pos = mb_strpos($line, "N°") + 2;
        $number = explode(" ", trim(mb_substr($line, $pos)))[0];
    } else {
        if ($date === null && preg_match('/([0-9]?[0-9])[\.\-\/ ]+([0-1]?[0-9])[\.\-\/ ]+([0-9]{2,4})/', $line, $matches)) {
            #$date = date($matches[0]);
            $d = new DateTime($matches[0]);
            $date=$d->format('m.Y');
        }
    }
}

echo $date;

fclose($myfile);

?>