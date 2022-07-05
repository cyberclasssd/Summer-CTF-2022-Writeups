def nth_root(x, n):
    # source: https://riptutorial.com/python/example/8751/computing-large-integer-roots
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            return mid
    return mid + 1

def decrypt(msg):
  return ''.join([chr(nth_root(i, 3)) for i in [int(c) for c in msg.split()]])
