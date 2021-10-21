print("***************************HELLO*******************")
print("..............Welcome TO Guessing the number Game................")
print(" Here you you have to guess the number set by the computer , you will be getting total 10 chances for the correct guess")
print("All the best")
n=18
i=0
while (i<10):
    x = int(input("Guess the no"))
    if x>n:
        print("ur no is greater")
        print("this is ur",i,"left out of 9")
    elif x<n:
        print("ur no is smaller")
        print("this is ur",i,"left out of 9")
    elif x==n:
        print("YOU GUESSED RIGHT")
        break
    else:
        continue
    i=i+1

print("Have a good day")    