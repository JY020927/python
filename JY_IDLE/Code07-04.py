aa=[]
bb=[]
value=0

for i in range(0, 200) :
    aa.append(value)
    value += 3

for i in range(0, 200):
    bb.append(aa[199 - i])

print("aa의 길이 : ", len(aa))
print(aa, end="")
print("\n\n bb의 길이 : ", len(bb))
print(bb, end="")
print("\n\n bb[0]에는 %d이, bb[99]에는 %d이 입력됩니다." % (bb[0], bb[99]))
