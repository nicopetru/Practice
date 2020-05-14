listas = [1, 2, 3, 4],[1],[],[1,2,3,4,5,6,7,8],[1,2,3],[2,3,4,7,6]

def chequio(L):
    if len(L) < 2: 
        return L
    else:
        guardo = L[0]
        L.pop(0)
        L.append(guardo)
        #y = L#.append(guardo)
        #y.append(guardo)
        #print(y)
    return L

def pasarportodo(jota):
    for k in jota: 
        return chequio(k)
        

#        if len(x) < 1: return x
#        else: return "muy largo"

print(pasarportodo(listas))
print(chequio([2,3,4]))
print(chequio([]))
print(chequio([3,6,87,5,3,2,7]))