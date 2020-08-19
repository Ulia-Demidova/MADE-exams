def binomial(h):
    C = [[0]*h for _ in range(h)]

    for n in range(h):
        C[n][0] = C[n][n] = 1
        for k in range(1,h-1):
            C[n][k] = C[n-1][k-1] + C[n-1][k]
    return C

def find_sum(costs, C, h):
    s = 0
    for i, cost in enumerate(costs):
        for k, c in enumerate(cost):
            n = len(cost) - 1
            s += c*2**(h-1-i)*C[n][k]
    return s

def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b%a, a)

def main():
    x = int(input())
    data = []
    h_s = []
    for _ in range(x):
        h = int(input())
        h_s.append(h)
        costs = []
        for _ in range(h):
            costs.append(list(map(int, input().split())))
        data.append(costs) 
        
    C = binomial(max(h_s))
    answers = []
    for h, costs in zip(h_s, data):
        numerator  = find_sum(costs, C, h)
        denominator = 2**(h-1)
        if numerator == 0:
            answers.append((0, 1))
        else:
            g = gcd(abs(numerator), denominator)
            answers.append((numerator//g, denominator//g))
            
    for ans in answers:
        print(ans[0], ans[1])
if __name__ == "__main__":
    main()
            