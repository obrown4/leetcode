#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Insert Interval #57

def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    if len(intervals) == 0:
        return [newInterval]

    res = []
    to_add = newInterval
    curr = []

    for curr in intervals:
        if curr[1] < to_add[0]:
            res.append(curr)
        elif to_add[1] < curr[0]:
            res.append(to_add)
            to_add = curr
        else:
            to_add = [min(curr[0], to_add[0]), max(curr[1], to_add[1])]

    if to_add[1] > curr[0]:
        res.append(to_add)
    else:
        res.append(curr)
    return res
