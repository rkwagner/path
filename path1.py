

def make_path(matrix, x, y, l):
    n, m = len(matrix), len(matrix[0])

    for i in xrange(n):
        for j in xrange(m):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1]) if i*j > 0 else \
                (matrix[i-1][j] if i else (matrix[i][j-1] if j else 0))
    return matrix[-1][-1]

fname = 'p081_matrix.txt'
with open(fname) as f:
    matrix = [line.split(',') for line in f]
    matrix = [[int(i) for i in p] for p in matrix]
    #print matrix[0][1]
    print make_path(matrix, 0, 0, len(matrix)-1)
#    print len(matrix)
