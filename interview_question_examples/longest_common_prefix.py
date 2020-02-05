# https://leetcode.com/problems/longest-common-prefix/submissions/

def longest_common_prefix(strs):
    if not strs:
        return ''

    shortest = len(min(strs, key=len))

    lcp = ''

    for i in range(shortest):
        prev = None
        for word in strs:
            if prev and word[i] != prev:
                return lcp
            prev = word[i]

        lcp += prev

    return lcp
