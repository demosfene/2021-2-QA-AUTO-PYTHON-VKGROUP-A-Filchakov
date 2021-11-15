
cat $1 | wc -l | awk '{printf "Общее колличество запросов:\n%s\n", $1}'> homework.txt

echo "">>homework.txt
echo "Количество запросов по типам:" >>homework.txt
grep "\"POST" $1 | wc -l | awk '{printf "POST:%s \n", $1 }'>> homework.txt
grep "\"GET" $1 | wc -l | awk '{printf "GET:%s \n", $1 }'>> homework.txt
grep "\"HEAD" $1 | wc -l | awk '{if ($1 != 0) printf "HEAD:%s \n", $1 }'>> homework.txt
grep "\"PUT" $1 | wc -l | awk '{if ($1 != 0) printf "PUT:%s \n", $1 }'>> homework.txt
grep "\"DELETE" $1 | wc -l | awk '{if ($1 != 0) printf "DELETE:%s \n", $1 }'>> homework.txt
grep "\"PATCH" $1 | wc -l | awk '{if ($1 != 0) printf "PATCH:%s \n", $1 }'>> homework.txt
grep "\"TRACE" $1 | wc -l | awk '{if ($1 != 0) printf "TRACE:%s \n", $1 }'>> homework.txt
grep "\"CONNECT" $1 | wc -l | awk '{if ($1 != 0) printf "CONNECT:%s \n", $1 }'>> homework.txt
grep "\"OPTIONS" $1 | wc -l | awk '{if ($1 != 0) printf "OPTIONS:%s \n", $1 }'>> homework.txt


echo "">>homework.txt
echo "Топ 10 самых частых запросов:" >>homework.txt
awk -F \"  '{split($2, a, " "); print a[2]}' $1 | sort | uniq -c | sort -bgr | head -n 10  >> homework.txt

echo "">>homework.txt
echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:" >> homework.txt
grep "\" 4[0-9][0-9] " $1 | awk -F \" '{split($3,a," "); print a[2]}' | sort | sort -rn |head -n 5 | uniq | while read  line; do grep " $line " $1| awk -F \" '{split($1,a," ");split($2,b," ");split($3,c," "); print b[2],c[1],c[2],a[1]}'; done |head -n 5 >> homework.txt

echo "">>homework.txt
echo "Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой" >> homework.txt
grep "\" 5[0-9][0-9] " $1 | awk -F \" '{split($1,a," "); print a[1]}' | sort |  uniq -c |sort -bgr |head -n 5 >> homework.txt
