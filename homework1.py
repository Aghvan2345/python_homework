#home work one
#this code prints  letters from the middle of the line 
x = input("pleas enter your word")
def word(x):
    if len(x)<7:
        print("your word should be len 7")
        return "error"
    elif len(x)%2 == 0:
        return"please insert an oddword len then 7"
        
    else:
        c = len(x)//2-1
        d = c+3
        return(x[c:d])

print( word(x))