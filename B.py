import collections

def count_rect(points):
    rows = collections.defaultdict(list)
    for x, y in points:
        rows[y].append(x)
    segments = collections.defaultdict(int)
    for y in sorted(rows):
        row = rows[y]
        row.sort()
        for j, x2 in enumerate(row):
            for i in range(j):
                x1 = row[i]
                segments[x1, x2] += 1
    count = 0
    for val in segments.values():
        count += val*(val-1)//2
    return count


def main():
    n = int(input())
    answers = []
    for _ in range(n):
        k = int(input())
        points = []
        for _ in range(k):
            points.append(list(map(int, input().split())))
        answers.append(count_rect(points))
        
    for ans in answers:
        print(ans)
        
if __name__ == "__main__":
    main()