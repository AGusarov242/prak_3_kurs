def div_gen(n):
    for i in range(1, int(n//2 + 1)):
        if n % i == 0:
            yield i

s = "agfh"
l = len(s)
L = list(divisorGenerator(l))
k = 1
for i in L:
	str = s[:i]
	if int(s.count(str)*i) == l:
	    k = s.count(str)
	    break

print(k)