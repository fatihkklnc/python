#1. ödev
dizi1=[[[1,4,'lion'],['a'],['cat'],[2,5]],[[3],['dog']]]
dizi2=[]
for a in dizi1:
    for l in a:
        for v in l:
            dizi2.append(v)
            
print(dizi2)   
#2.ödev
duzdizi= [[1, 2], [3, 4], [5, 6, 7]]
duzdizi.reverse()
for a in range(0,int(len(duzdizi))):
    duzdizi[a].reverse()
print(duzdizi)