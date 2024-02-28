#!/bin/bash
# VAR="HELLO"
# VAR=$VAR" WORLD"
# echo $VAR
rm -rf file*.py
FILES_NUMBER=60
for (( c=1; c<=$FILES_NUMBER; c++ ))
do 
SCRIPT=""
FILE="file${c}.py"
touch $FILE

   for (( n=1; n<=99; n++))
   do
    K=$(($n + 1))
    SCRIPT=$SCRIPT"def method"$n"():\n
\tmethod"$K"()\n"
    if [ $n -eq 99  ] && [ $c != $FILES_NUMBER ]
    then
    D=$(($c + 1))
    SCRIPT=$SCRIPT"def method"$K"():\n
\tprint(\"last method called from file"$c"\")\n
    "
    fi

    if [ $n -eq 99 ] && [ $c -eq $FILES_NUMBER ]
    then
    SCRIPT=$SCRIPT"def method"$K"():\n
\tprint(\"last method called from file"$c"\")\n
\tprint(\"finish\")\n "
    fi
    done
   
   echo -e $SCRIPT>$FILE
done