score = input("Enter a score between 0.0 and 1.0:")
try :
    f_score = float(score)
except :
    print("please enter a number")
    quit()
if f_score < 0.0 :
    print("score can not be less than 0.0")
    quit()
elif f_score > 1.0 :
    print("score can not be more than 1.0")
    quit()
if f_score >= 0.9 :
    print("A")
elif f_score >= 0.8 :
    print("B")
elif f_score >= 0.7 :
    print("C")
elif f_score >= 0.6 :
    print("D")
else :
    print("F")

