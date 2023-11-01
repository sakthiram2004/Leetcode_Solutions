<<<<<<< HEAD
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        x,y=1,2
        for i in range(3,n):
            x,y=y,x+y
        return x+y
=======
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        x,y=1,2
        for i in range(3,n):
            x,y=y,x+y
        return x+y
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
