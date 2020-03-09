# https://leetcode.com/problems/daily-temperatures/

def daily_temperatures(T):
    t = T
    output = [0] * len(t)

    pending = []

    for i in range(len(t) - 1):
        if pending and t[i + 1] > t[pending[-1]]:
            index = pending.pop()
            output[index] = (i + 1) - index
            while pending and t[pending[-1]] < t[i + 1]:
                index = pending.pop()
                output[index] = (i + 1) - index
        if t[i] < t[i + 1]:
            output[i] += 1
        else:
            pending.append(i)

    return output
