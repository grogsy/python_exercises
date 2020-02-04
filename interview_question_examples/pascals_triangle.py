# https://leetcode.com/problems/pascals-triangle/

def pascals_triangle(numRows):
    def gen_level(prev_level):
        output = [1]
        if len(prev_level) > 1:
            for i in range(len(prev_level) - 1):
                output.append(prev_level[i] + prev_level[i + 1])
        output.append(1)

        return output

    if numRows == 0:
        return []

    triangle = [[1]]

    for i in range(2, numRows + 1):
        triangle.append(gen_level(triangle[-1]))

    return triangle
