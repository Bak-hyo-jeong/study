def solution(a, b, c, d):
    
    x, y, w, z = sorted([a] + [b] + [c] + [d])
    
    if x == y and y == w and w == z:
        return 1111 * x
    elif x != y and y == w and w == z:
        return (10 * y + x) ** 2
    elif x == y and y == w and w != z:
        return (10 * x + z) ** 2
    elif x == y and w == z :
        return (x + w) * abs(x - w)
    elif x == y:
        return w * z
    elif y == w:
        return x * z
    elif w == z:
        return x * y
    else:
        return x
        