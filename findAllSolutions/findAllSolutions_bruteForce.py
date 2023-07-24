import time

tstart = time.time()

outputFile = "results_bruteforce.txt"
max = 20
allSolutions = []

for a in range(1, max):
    print(" a is", a)

    for b in range(1, max):
        if (b == a):
            continue

        for c in range(1, max):
            if (c == a or c == b):
                continue

            if (a + b + c != 38):
                continue

            for d in range(1, max):
                if (d == a or d == b or d == c):
                    continue

                for e in range(1, max):
                    if (e == a or e == b or e == c or e == d):
                        continue

                    for f in range(1, max):
                        if (f == a or f == b or f == c or f == d or f == e):
                            continue

                        for g in range(1, max):
                            if (g == a or g == b or g == c or g == d or g == e or g == f):
                                continue

                            if (d+e+f+g != 38):
                                continue

                            for h in range(1, max):
                                if (h == a or h == b or h == c or h == d or h == e or h == f or h == g):
                                    continue

                                if (h+d+a != 38):
                                    continue

                                for i in range(1, max):
                                    if (i == a or i == b or i == c or i == d or i == e or i == f or i == g or i == h):
                                        continue

                                    for j in range(1, max):
                                        if (j == a or j == b or j == c or j == d or j == e or j == f or j == g or j == h or j == i):
                                            continue

                                        for k in range(1, max):
                                            if (k == a or k == b or k == c or k == d or k == e or k == f or k == g or k == h or k == i or k == j):
                                                continue

                                            for l in range(1, max):
                                                if (l == a or l == b or l == c or l == d or l == e or l == f or l == g or l == h or l == i or l == j or l == k):
                                                    continue

                                                if (c+g+l != 38):
                                                    continue

                                                if (h+i+j+k+l != 38):
                                                    continue

                                                for m in range(1, max):
                                                    if (m == a or m == b or m == c or m == d or m == e or m == f or m == g or m == h or m == i or m == j or m == k or m == l):
                                                        continue

                                                    if (b+e+i+m != 38):
                                                        continue

                                                    for n in range(1, max):
                                                        if (n == a or n == b or n == c or n == d or n == e or n == f or n == g or n == h or n == i or n == j or n == k or n == l or n == m):
                                                            continue

                                                        for o in range(1, max):
                                                            if (o == a or o == b or o == c or o == d or o == e or o == f or o == g or o == h or o == i or o == j or o == k or o == l or o == m or o == n):
                                                                continue

                                                            for p in range(1, max):
                                                                if (p == a or p == b or p == c or p == d or p == e or p == f or p == g or p == h or p == i or p == j or p == k or p == l or p == m or p == n or p == o):
                                                                    continue

                                                                if (b+f+k+p != 38):
                                                                    continue

                                                                if (m+n+o+p != 38):
                                                                    continue

                                                                for q in range(1, max):
                                                                    if (q == a or q == b or q == c or q == d or q == e or q == f or q == g or q == h or q == i or q == j or q == k or q == l or q == m or q == n or q == o or q == p):
                                                                        continue
                                                                    if (q+m+h != 38):
                                                                        continue

                                                                    if (c+f+j+n+q != 38):
                                                                        continue

                                                                    for r in range(1, max):
                                                                        if (r == a or r == b or r == c or r == d or r == e or r == f or r == g or r == h or r == i or r == j or r == k or r == l or r == m or r == n or r == o or r == p or r == q):
                                                                            continue

                                                                        if (d+i+n+r != 38):
                                                                            continue

                                                                        if (g+k+o+r != 38):
                                                                            continue

                                                                        for s in range(1, max):
                                                                            if (s == a or s == b or s == c or s == d or s == e or s == f or s == g or s == h or s == i or s == j or s == k or s == l or s == m or s == n or s == o or s == p or s == q or s == r):
                                                                                continue

                                                                            else:
                                                                                # alle Params ungleich
                                                                                if (l+p+s != 38):
                                                                                    continue
                                                                                if (s+r+q != 38):
                                                                                    continue

                                                                                if (a+e+j+o+s != 38):
                                                                                    continue

                                                                                solution = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]
                                                                                allSolutions.append(solution)

                                                                                with open(outputFile, "a") as daten:
                                                                                    daten.write("\n{}".format(solution))

execution_time = time.time() - tstart

print("Program finished")
print("all Solutions: {}".format(allSolutions))
print("execution time: {}".format(execution_time))
