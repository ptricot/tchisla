# coding : utf-8

print('Faire : ?')
res = int(input())
print('Avec : ?')
x = int(input())
print('En cb iterations: ?')
maxit = int(input())
max=10000
maxfac=8

ways = {x:(str(x), 1), 10*x+x: (str(10*x+x), 2), 100*x+10*x+x: (str(100*x+10*x+x), 3)}
temp = []

def fact(a):
    if (a<=1):
        return 1
    else:
        return a*fact(a-1)

for _ in range (maxit):
    for a in ways:
        for b in ways:
            if(ways[a][1]+ways[b][1]<=maxit):
                if (a+b<max and (not ((a+b) in ways) or ways[a+b][1]>ways[a][1]+ways[b][1])):
                    temp.append((a+b,'('+ways[a][0]+'+'+ways[b][0]+')', ways[a][1]+ways[b][1]))
                if (a-b<max and a>b and (not ((a-b) in ways) or ways[a-b][1]>ways[a][1]+ways[b][1])):
                    temp.append((a-b, '('+ways[a][0]+'-'+ways[b][0]+')', ways[a][1]+ways[b][1]))
                if (a*b<max and (not ((a*b) in ways) or ways[a*b][1]>ways[a][1]+ways[b][1])):
                    temp.append((a*b, '('+ways[a][0]+'*'+ways[b][0]+')', ways[a][1]+ways[b][1]))
                if (b != 0 and a > 1 and float(a)/b%1==0):
                    if (not ((a/b) in ways) or ways[a/b][1]>ways[a][1]+ways[b][1]):
                        temp.append((a/b, '('+ways[a][0]+'/'+ways[b][0]+')', ways[a][1]+ways[b][1]))
                if (a**b<max and a>1 and a<20 and b<12 and b>1 and b%1==0):
                    if (not ((a**b) in ways) or ways[a**b][1]>ways[a][1]+ways[b][1]):
                        temp.append((a**b, '('+ways[a][0]+'^'+ways[b][0]+')', ways[a][1]+ways[b][1]))
                if (a>1 and a**0.5%1==0):
                    sq = int(a**0.5)
                    if (not ((sq) in ways) or ways[sq][1]>ways[a][1]):
                        temp.append((sq, 'sq('+ways[a][0]+')', ways[a][1]))
                if (a>1 and a<=maxfac):
                    if (not (fact(a) in ways) or ways[fact(a)][1]>ways[a][1]):
                        temp.append((fact(a), ways[a][0]+'!', ways[a][1]))
    for trip in temp:
        ways[trip[0]]=(trip[1], trip[2])
    temp=[]

if (res in ways):
    text=ways[res][0]
    if (text[0]=='('):
        print(ways[res][0][1:-1]+' = '+str(res))
    else:
        print(ways[res][0]+' = '+str(res))
    print('En '+str(ways[res][1])+' coups')
else :
    print('Pas trouve')
