def div_gen(n):
    """This Function generate the divisors(which are <= length of string/2 ) of the string length"""
    for i in range(1, int(n//2 + 1)):
        if n % i == 0:
            yield i

def max_str(s):
    """This Function return the max number k and substring t, so string s = t in k times """
    str_len = len(s)
    str_div = list(div_gen(str_len))
    k = 1
    for i in str_div:
        sub_str = s[:i]
        if int(s.count(sub_str)*i) == str_len:
            k = int(s.count(sub_str))
            break
    if k == 1:
        sub_str = s
    return k, sub_str

'''Example'''
print(max_str("abababab"))
