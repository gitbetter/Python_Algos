def find_2_sum(lt, t):
    for a in lt:
        b = t - a
        if b != a and b in lt:
            return (a, b)

    return None

if __name__ == "__main__":
    a = [] 
    with open("2sum_data.txt") as f:
        lines = f.readlines()
        for line in lines:
            a.append(int(line.rstrip()))

    lt = {}
    for i in a:
        lt[i] = i;

    sum_count = 0
    for t in range(-10000, 10001):
        s = find_2_sum(lt, t)
        if s is not None:
            sum_count += 1

    print(sum_count)
