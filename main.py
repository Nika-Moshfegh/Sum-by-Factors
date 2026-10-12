def sum_for_list(lst):
    my_set = set()
    for i in lst:
        my_set.update(get_factors(abs(i)))
    return final_sum(lst, my_set)


def get_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors


def final_sum(lst, prime_list):
    res = []
    for i in sorted(prime_list):
        c = sum(j for j in lst if j % i == 0)
        res.append([i, c])
    return res