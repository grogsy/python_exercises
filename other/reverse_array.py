def r(a, c = 0):

    if c == len(a) - 1:

        return [a[len(a) -1]]

    out = r(a, c+1)

    out.append(a[c])

    return out

