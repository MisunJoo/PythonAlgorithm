<?php

function gradingStudents($grades) {
    // Write your code here
    foreach ($grades as &$grade) {
    	if ($grade < 38){
    		continue;
    	}

    	if (((100 - $grade)%5) < 3){
    		$grade = $grade + ((100 - $grade)%5);
    	}
    }
    return $grades
    # 점수가 38보다 작으면 로직을 실행하지 않음

    # 점수를 5로 나눈 나머지가 3보다 작으면 round 그 나머지를 더해줌


}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$grades_count = 4;

$grades = [73, 67, 38, 33];

// for ($i = 0; $i < $grades_count; $i++) {
//     $grades_item = intval(trim(fgets(STDIN)));
//     $grades[] = $grades_item;
// }

$result = gradingStudents($grades);

fwrite($fptr, implode("\n", $result) . "\n");

fclose($fptr);
?>