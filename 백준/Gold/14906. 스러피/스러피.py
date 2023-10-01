n = int(input())
words = [input().strip() for _ in range(n)]
def checkSlump(word):
    if len(word) < 2 or (word[0] != 'D' and word[0] != 'E') :
        return False
    i = 1
    while i < len(word) and word[i] == 'F' :
        i += 1
    if i == len(word) :
        return False
    if word[-1] == 'G' :
        return True
    elif word[i] == 'D' or word[i] == 'E':
        return checkSlump(word[i:])
    return False
    

def checkSlimp(word):
    
    if len(word) <= 1 or word[0] != 'A' :
        return False
    if len(word) == 2:
        return word == 'AH'
    else :
        if word[1] == 'B':
            return checkSlimp(word[2:-1]) and word[-1] == 'C'
        else:
            return checkSlump(word[1:-1]) and word[-1] == 'C'

def checkSlurpy(word):
    for i in range(2,len(word)):
        
        if checkSlimp(word[:i]) and checkSlump(word[i:]):
            return True
    return False
print("SLURPYS OUTPUT")
for word in words:
    
    if checkSlurpy(word):
        print("YES")
    else:
        print("NO")
print("END OF OUTPUT")