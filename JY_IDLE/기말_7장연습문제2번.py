import random
nn = []

for _ in range(10):
    num = random.randrange(1, 100)
    #randint( 1, 99 )와 동일
    nn.append(num)
hap = 0
for i in range(10):
    num = nn[i] #indexing
    hap+= num
print(hap)
