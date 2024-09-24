class GFG:
    class Point:
        x = 0
        y = 0

        def __init__(self, x, y):
            self.x = x
            self.y = y

    @staticmethod
    def area(points, i, j, k, l):
        p1 = points[i]
        p2 = points[j]
        p3 = points[k]
        p4 = points[l]
        return (p1.x*p2.y - p2.x*p1.y + p2.x*p3.y - p3.x*p2.y + p3.x*p4.y - p4.x*p3.y + p4.x*p1.y - p1.x*p4.y)*0.5

    @staticmethod
    def mQDP(points, n):
        if n < 4:
            return 0
        table = [[0.0] * n for _ in range(n)]
        quadrangulation = [[-1] * n for _ in range(n)]
        gap = 2
        while gap < n:
            i = 0
            j = gap
            while j < n:
                if j < i + 3:
                    table[i][j] = -1
                else:
                    table[i][j] = float('-inf')
                    for k in range(i + 1, j, 2):
                        for l in range(k + 1, j, 2):
                            quad_area = GFG.area(points, i, k, l, j)
                            if(table[i][k] == -1 or table[k][l]==-1 or table[l][j]==-1):
                                val = -1
                            elif(table[i][k] > 0):
                                val = min(quad_area,table[i][k])
                            elif(table[k][l] > 0):
                                val = min(quad_area,table[k][l])
                            elif(table[l][j] > 0):
                                val = min(quad_area,table[l][j])
                            else:
                                val = quad_area
                            if table[i][j] < val:
                                table[i][j] = val
                                quadrangulation[i][j] = (k, l)
                i += 1
                j += 1
            gap += 1

        print("Optimal Quadrangulation:")
        GFG.printQuadrangulation(quadrangulation, 0, n - 1)
        return table[0][n - 1]

    @staticmethod
    def printQuadrangulation(quadrangulation, i, j):
        if j <= i + 2:
            return
        if quadrangulation[i][j] ==  -1:
            return
        k, l = quadrangulation[i][j]
        quad_area = GFG.area(points,i,k,l,j)
        print(f"Quadrilateral: ({i}, {k}, {l}, {j})"+", area = "+str(quad_area))
        GFG.printQuadrangulation(quadrangulation, i, k)
        GFG.printQuadrangulation(quadrangulation, k, l)
        GFG.printQuadrangulation(quadrangulation, l, j)

if __name__ == "__main__":
    points = [GFG.Point(0, 5), GFG.Point(0, 3), GFG.Point(1, 1), GFG.Point(2, 0), GFG.Point(5, 2), GFG.Point(4,6), GFG.Point(3, 8), GFG.Point(1, 7)]
    n = len(points)
    GFG.mQDP(points, n)
    