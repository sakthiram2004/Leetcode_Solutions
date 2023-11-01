<<<<<<< HEAD
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        for i in range(n+1):
            if i==0:
                l.append(0)
            elif i==1:
                l.append(1)
            elif i%2==0:
                l.append(l[i//2])
            else:
                l.append(l[i//2]+l[(i//2)+1])
        return max(l)

        
=======
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        for i in range(n+1):
            if i==0:
                l.append(0)
            elif i==1:
                l.append(1)
            elif i%2==0:
                l.append(l[i//2])
            else:
                l.append(l[i//2]+l[(i//2)+1])
        return max(l)

        
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
