<<<<<<< HEAD
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=(set(nums))
        if l[0]==0:
            return len(l)-l.count(0)
        else:
            return len(l)
=======
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=(set(nums))
        if l[0]==0:
            return len(l)-l.count(0)
        else:
            return len(l)
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
