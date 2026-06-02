# suspicious link detector v1

# ask user for link
link = input("enter a website link : ")

# predetermined score
score = 0

# give intel to train the detector                                     
has_tinyurl = "tinyurl" in link
has_bitly = "bit.ly" in link
free = "free" in link
money = "money" in link
prize = "prize" in link
winner = "winner" in link

# checking for scammy lines
if has_tinyurl == True:
    score = score + 1
    print("'tinyurl' detected")

if has_bitly == True:
    score = score + 1
    print("'bit.ly' detected")

if free == True:
    score = score + 1
    print("'free' detected")

if money == True:
    score = score + 1
    print("'money' detected")

if prize == True:
    score = score + 1
    print("'prize' detected")

if winner == True:
    score = score + 1
    print("'winner' detected")

# counting final score to check possibilities of suspicious links
if score <= 2 :
    print("scam possibility : LOW")
elif score >= 3 and score <= 4:
    print("scam possibility : MEDIUM")
else :
    print("scam possibility : HIGH")
