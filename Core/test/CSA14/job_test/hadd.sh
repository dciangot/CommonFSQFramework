rm hadd.txt

echo "hadd -f result.root" > hadd.txt

for i in `ls -altr | grep job_ | awk '{print $9}'`;
do

echo "`cat hadd.txt` $i/UE_test.root" > hadd.txt

done
`cat hadd.txt`
