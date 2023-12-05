#!/usr/bin/python3
""" pascal_triangle function documentation """


def pascal_triangle(n=4500):
    """print pascal triangle"""
    pascal_tri = [[0]*abc for abc in range(1, n+1)]
    cmpt = 0
    for abc in range(n):
        pascal_tri[abc][0] = 1
        pascal_tri[abc][-1] = 1
        for xyz in range(0, abc//2):
            pascal_tri[abc][xyz+1] = pascal_tri[abc-1][xyz] + \
                                    pascal_tri[abc-1][xyz+1]
            pascal_tri[abc][abc-xyz-1] = pascal_tri[abc-1][xyz] + \
                                         pascal_tri[abc-1][xyz+1]

    return pascal_tri
