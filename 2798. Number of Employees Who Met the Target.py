<<<<<<< HEAD
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        c=0
        for i in hours:
            if i >= target:
                c+=1
        return c
=======
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        c=0
        for i in hours:
            if i >= target:
                c+=1
        return c
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
