def print_rangoli(n):
    # your code goes here
    lists= [chr(n) for n in range(ord('a'),ord('z')+1)] 
    L = []
    for i in range(n):
        s = "-".join(lists[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3,'-'))

    print("\n".join(L[::-1]+L[1:n]))




