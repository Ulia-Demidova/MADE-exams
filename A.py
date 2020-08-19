from bisect import bisect_left

def find_answer(k, s):
    mod = 35184372089371
    idx = bisect_left(s, k)
    return (2**idx + 2**(idx-1-s[idx]+k))%mod

def main():
    x = int(input())
    ks = []
    for _ in range(x):
        ks.append(int(input()))
        
    s_n = []
    for n in range(2*int(max(ks)**0.5)):
        s_n.append(n*(n+1)//2)  
    
    for k in ks:
        print(find_answer(k, s_n))
    
if __name__ == "__main__":
    main()