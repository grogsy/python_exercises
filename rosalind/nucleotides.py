'''
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

    Given: A DNA string of length at most 1000 nt.

    Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in .
'''

from collections import Counter

data = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

c = Counter(data)

fmt = '%d '
out = ''
for n in 'ACTG':
    out += fmt % c[n]
    
print(out)
