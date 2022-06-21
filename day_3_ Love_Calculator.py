print ("Welcome to the Love Calculator!")
name1=str(input("What is your name? \n")).lower()
name2=str(input("What is their name? \n")).lower()
word1 = ['t', 'r', 'u', 'e']
word2 = ['l','o','v','e']
count1 = 0
count2 = 0
for letra in name1:
    if letra in word1:
        count1 = count1+1
for letra in name2:
    if letra in word1:
        count1=count1+1
for letra in name1:
    if letra in word2:
        count2=count2+1
for letra in name2:
    if letra in word2:
        count2 = count2+1
score = int(str(count1) + str(count2))

if score<10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print("your score is", score)
