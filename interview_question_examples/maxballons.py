# https://leetcode.com/problems/maximum-number-of-balloons/submissions/


def maxNumberOfBalloons(text: str) -> int:
    Bs = text.count('b')
    As = text.count('a')
    Ls = text.count('l')
    Os = text.count('o')
    Ns = text.count('n')

    count = 0
    while True:
        if Bs == 0 or As == 0 or Ls == 0 or Os == 0 or Ns == 0:
            return count

        Bs -= 1
        As -= 1
        Ls -= 2
        Os -= 2
        Ns -= 1

        if Bs < 0 or As < 0 or Ls < 0 or Os < 0 or Ns < 0:
            return count

        count += 1
