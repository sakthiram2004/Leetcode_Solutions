<<<<<<< HEAD
class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        if prices[0]+prices[1]<=money:
            return money-(prices[0]+prices[1])
        return money
=======
class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        if prices[0]+prices[1]<=money:
            return money-(prices[0]+prices[1])
        return money
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
