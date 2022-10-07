def adj_tuple(rc, direction):
    ''' return (row, col) adjacent to (r0, c0) in the given direction '''
    #print("RC = ", rc)
    r0, c0 = rc
    if direction == 'N':
        return (r0 - 1, c0)
    if direction == 'S':
        return (r0 + 1, c0)
    if direction == 'E':
        return (r0, c0 + 1)
    if direction == 'W':
        return (r0, c0 - 1)
    raise ValueError('invalid direction %s' % str(direction))


class Grid:
    directions = ['N','S','E','W']
    def __init__(self, size):
        self.size = size
    def valid_tuple(self, t):
        r, c = t
        return (0 <= r < self.size) and (0 <= c < self.size)
    def get_adj_tuple(self, rc, direction):
        """
        self.get_adj_tuple((r0, c0, direction)) return (row, col)
        """
        tup = adj_tuple(rc, direction)
        if self.valid_tuple(tup):
           # raise ValueError("get_adj_tuple: out of bound")
            return tup
    def get_directions(self, rc):
        """
        returns available directions, i.e., directions available for walking
        """
        dirs = []
        for _ in ['N','S','E','W']:
            t = adj_tuple(rc, _)
            if self.valid_tuple(t):
                dirs.append(_)
        return dirs

