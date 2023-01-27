# 🚨 Don't change the code below 👇
print("We`lcome to the Love Calculator!")
name1 = (input("What is your name? \n")).lower()
name2 = (input("What is their name? \n")).lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = name1 + name2
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t+r+u+e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l+o+v+e

true = str(true)
love = str(love)

loveScore = true+love
loveScore = int(loveScore)
# print(f"Your love score is: {trueLove}%")

if loveScore < 10  or loveScore > 90:
    print(f"Your score is {loveScore}%, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}%, you are alright together.")
else:
    print(f"Your score is {loveScore}%")

