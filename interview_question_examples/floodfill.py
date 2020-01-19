# https://leetcode.com/problems/flood-fill/submissions/

def floodFill(image, sr, sc, newColor):
    def _floodFill(image, sr, sc, newColor, colorToReplace):
        # Check invalid boundaries
        if sr >= len(image) or sr < 0 or sc >= len(image[0]) or sc < 0:
            return image

        # check color of current tile
        thisColor = image[sr][sc]
        if thisColor == newColor or thisColor != colorToReplace:
            return image

        image[sr][sc] = newColor

        # north
        image = _floodFill(image, sr-1, sc, newColor, colorToReplace)

        # south
        image = _floodFill(image, sr+1, sc, newColor, colorToReplace)

        # east
        image = _floodFill(image, sr, sc+1, newColor, colorToReplace)

        # west
        image = _floodFill(image, sr, sc-1, newColor, colorToReplace)

        return image

    oldColor = image[sr][sc]
    return _floodFill(image, sr, sc, newColor, oldColor)
