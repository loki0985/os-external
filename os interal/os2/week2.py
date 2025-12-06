#echo -n "Enter your age: "
#read age

#if [ "$age" -gt 18 ]; then
    #echo "you are above 18."
#elif [ "$age" -lt 18 ]; then
    #echo "you are 18 years old."
#else
    #echo "you are below 18."
#fi 
#----------------------------
#echo -n "Enter a number: "
#read num
#sum=0
#temp=$num
#while [$temp -gt 0 ]; do
#do
#digit=$(( $temp % 10 ))
#sum=$(( $sum + digit*digit*digit ))
# temp=$(( $temp / 10 ))
#done
#if [ $sum -eq $num ]; then
#then
#echo "$num is an Armstrong number."
#else
#echo "$num is not an Armstrong number."
#fi
#----------------------------

#echo -n "enter first number:"
#read a
#echo -n "enter second number:"
#read b
#while [ $a -ne $b ]; do
#do
#if [ $a -gt $b ]; then
# a=$(( a - b ))
#else
# b=$(( b - a ))
#fi
#done
#echo "GCD is : $a"
#----------------------------

#chmod +x script.sh
#./file.sh
#----------------------------

#echo -n "Enter a number: "
#read num
#rev=0
#temp=$num
#while [ $temp -gt 0 ]; do
#digit=$(( $temp % 10 ))
#rev=$(( rev * 10 + digit ))
# temp=$(( $temp / 10 ))
#done
#if [$rev -eq $num ]; then
#echo "$num is a palindrome."
#else
#echo "$num is not a palindrome."
#fi
#----------------------------

#echo -n "Enter a number: "
#read num
#sum=0
#for (( i=1; i<=num; i++ )); do
# sum=$(( sum + i ))
#done
#echo "Sum of first $num natural numbers is: $sum"
#----------------------------
