
def distance_between(cord1, cord2):
    return min(
        abs(cord1[0] - cord2[0]),
        abs(cord1[1] - cord2[1])
    )


def distance_to_angle(cord):
    return min([
        distance_between(cord, angle_cord)
            for angle_cord in [(0, 0), (7, 0), (7, 7), (0, 7)]
    ])


def distance_to_egde(cord):
    return min([
        min(e, 7 - e) for e in cord
    ])


def get_8_char_s(s):
    for c in [str(i) for i in range(10)]:
        s = s.replace(c, '.' * int(c))
    return s


def get_fixed_s(s):
    s += '!'
    result = ''
    cnt = 0 

    for c in s:
        if c == '.':
            cnt += 1
        else:
            if cnt != 0:
                result += str(cnt)
                cnt = 0
            result += c

    return result[:-1]


class Piece:
    def __init__(self, row, col, typ):
        self.row = row # from 0 
        self.col = col # from 0
        self.typ = typ


    def update_str(self, s):
        splitted = s.split('/')
        row_str = splitted[self.row]
        row_str = get_8_char_s(row_str)
        
        l = list(row_str)
        l[self.col] = self.typ
        row_str = ''.join(l)

        row_str = get_fixed_s(row_str)
        l = splitted[:self.row] + [row_str] + splitted[self.row+1:]  
        return '/'.join(l)

    def get_cord(self):
        return (self.row, self.col)

    def __lt__(self, other):
        return (
            (self.row, self.col) < (other.row, other.col)
                if (self.row, self.col) != (other.row, other.col) else
            ord(self.typ) < ord(other.typ)
        )