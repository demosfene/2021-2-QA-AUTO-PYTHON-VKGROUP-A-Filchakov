
cat $1 | wc -l | awk '{printf "Общее колличество запросов:\n%s\n", $1}'> homework.txt

echo "">>homework.txt
echo "Количество запросов по типам:" >>homework.txt
awk -F \" '{split($2, a, "\""); print a[1]}' $1 | awk -F \" '{split($1, a, " "); print a[1]}' | sort | uniq -c >> homework.txt

echo "">>homework.txt
echo "Топ 10 самых частых запросов:" >>homework.txt
awk -F \"  '{split($2, a, " "); print a[2]}' $1 | sort | uniq -c | sort -bgr | head -n 10  >> homework.txt

echo "">>homework.txt
echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:" >> homework.txt
grep "\" 4[0-9][0-9] " $1 | awk -F \" '{split($3,a," "); print a[2]}' | sort | sort -rn |head -n 5 | uniq | while read  line; do grep " $line " $1| awk -F \" '{split($1,a," ");split($2,b," ");split($3,c," "); print b[2],c[1],c[2],a[1]}'; done |head -n 5 >> homework.txt

echo "">>homework.txt
echo "Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой" >> homework.txt
grep "\" 5[0-9][0-9] " $1 | awk -F \" '{split($1,a," "); print a[1]}' | sort |  uniq -c |sort -bgr |head -n 5 >> homework.txt
