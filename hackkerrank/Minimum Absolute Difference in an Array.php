<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

	$n = 5;
	$arr_temp = [1, -3, 71, 68, 17];
	$min = 99999999;


	function minimumAbsoluteDifference($arr_temp) {
		$min = 99999999;
//
		sort($arr_temp);
		// var_dump($arr_temp);

		for ($i = 0; $i < count($arr_temp); $i++){
			if ($i + 1 < count($arr_temp)){
				$abs_number = $arr_temp[$i+1] - $arr_temp[$i];
				if ($min > $abs_number){
					$min = $abs_number;
				}
			}
		}
		return $min;
	}

	$result = minimumAbsoluteDifference($arr_temp);
	print_r($result);
?>