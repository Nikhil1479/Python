# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
digit1 =  int(two_digit_number) %10
digit2 = int(two_digit_number)/10
digit_sum = digit1+digit2
print(int(digit_sum))