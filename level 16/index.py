# ```1) მოსწავლეს შემოატანინეთ აურების რაოდენობა, შემდეგ ამის მიხედვით ჩასვით A-F-მდე ერთ-ერთ კატეგორიაში if-elif-else-ის გამოყენებით```
# - A: 90 - 100 
# - B: 80-89
# - C: 70 - 79
# - D: 60 - 69
# - E: 50 - 59
# - F

score = int(input("შეიყვანეთ ქულა: "))
if 90 <=score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <=79:
    print("C")
elif 60 <= score <=69:
    print("D")
elif 50 <= score <=59:
    print ("E")
else: 
    print("F")


