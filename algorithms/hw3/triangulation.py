import math


class GFG:
    # Structure of a point in 2D plane
    class Point:
        x = 0
        y = 0

        def __init__(self, x, y):
            self.x = x
            self.y = y

    # Utility function to find minimum of two double values
    @staticmethod
    def min(x, y):
        return x if (x <= y) else y

    # A utility function to find distance between two points in a plane
    @staticmethod
    def dist(p1, p2):
        return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

    # A utility function to find cost of a triangle. The cost is considered as perimeter
    # (sum of lengths of all edges) of the triangle
    @staticmethod
    def cost(points, i, j, k):
        p1 = points[i]
        p2 = points[j]
        p3 = points[k]
        return GFG.dist(p1, p2) + GFG.dist(p2, p3) + GFG.dist(p3, p1)

    # A function to find the optimal triangulation using dynamic programming and store the triangulation path
    @staticmethod
    def mTCDP(points, n):
        # There must be at least 3 points to form a triangle
        if n < 3:
            return 0

        # table to store results of subproblems.
        table = [[0.0] * n for _ in range(n)]
        # store the triangulation path
        triangulation = [[-1] * n for _ in range(n)]

        # Fill table using the recursive formula
        gap = 0
        while gap < n:
            i = 0
            j = gap
            while j < n:
                if j < i + 2:
                    table[i][j] = 0.0
                else:
                    table[i][j] = 1000000.0
                    for k in range(i + 1, j):
                        print("testing points i,k,j = "+str(i)+str(k)+str(j))
                        val = table[i][k] + table[k][j] + GFG.cost(points, i, j, k)
                        print(table[i][k])
                        print(table[k][j])
                        if table[i][j] > val:
                            table[i][j] = val
                            triangulation[i][j] = k  # store the index of the point used for triangulation
                i += 1
                j += 1
            gap += 1

        # Print the triangulation
        print("Minimum Triangulation Cost: ", table[0][n - 1])
        print("Optimal Triangulation:")
        GFG.printTriangulation(triangulation, 0, n - 1)
        return table[0][n - 1]

    # Function to print the triangulation based on the triangulation table
    @staticmethod
    def printTriangulation(triangulation, i, j):
        if j <= i + 1:
            return  # No triangulation possible between points i and j
        k = triangulation[i][j]
        if k == -1:
            return
        print(f"Triangle: ({i}, {k}, {j})")
        # Recursively print the left and right portions of the triangulation
        GFG.printTriangulation(triangulation, i, k)
        GFG.printTriangulation(triangulation, k, j)


# Driver program to test the above functions
if __name__ == "__main__":
    points = [GFG.Point(0, 0), GFG.Point(2, 0), GFG.Point(4, 2), GFG.Point(2, 4), GFG.Point(0, 4)]
    n = len(points)
    GFG.mTCDP(points, n)
