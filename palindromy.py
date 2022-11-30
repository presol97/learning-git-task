print("Proszę podać słowo, które mam sprawdzić: ")
word = input()

def isPalindrome(word):
    x=list(word)
    y=[]
    y.extend(x)
    x.reverse()
    if(x==y):
        return True
    return False

ans = isPalindrome(word)

if ans:
    print("Podane słowo", word, "to palindrom")
else:
    print("Podane słowo", word, ", nie jest palindromem")

    



