read -p "Contest number: " num

for file in `ls abc${num}`
do
git add "abc${num}/${file}"
done
git commit -m "Tackle abc${num}"
