<<<<<<< HEAD
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in words:
            f=0
            for j in range(len(i)):
                if f==0 and i[j] in allowed:
                    pass
                else:
                    f=1
            if f==0:
                c+=1
        return c
=======
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in words:
            f=0
            for j in range(len(i)):
                if f==0 and i[j] in allowed:
                    pass
                else:
                    f=1
            if f==0:
                c+=1
        return c
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
