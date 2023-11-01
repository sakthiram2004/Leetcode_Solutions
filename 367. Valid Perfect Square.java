<<<<<<< HEAD
class Solution {
    public boolean isPerfectSquare(int num) {
        if(num==1)
        return true;
        int n=num/2;
        for(int i=1;i<=n;i++)
        if(i*i==num)
        return true;
        return false;
        
    }
=======
class Solution {
    public boolean isPerfectSquare(int num) {
        if(num==1)
        return true;
        int n=num/2;
        for(int i=1;i<=n;i++)
        if(i*i==num)
        return true;
        return false;
        
    }
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
}