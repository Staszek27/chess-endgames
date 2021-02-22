

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


    def __lt__(self, other):
        return (
            (self.row, self.col) < (other.row, other.col)
                if (self.row, self.col) != (other.row, other.col) else
            ord(self.typ) < ord(other.typ)
        )