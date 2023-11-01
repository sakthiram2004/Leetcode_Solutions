<<<<<<< HEAD
class Solution {
    public void reverseString(char[] s) {
        int n=s.length;
        char t;
       for(int i=0;i<n/2;i++)
       {
           t=s[i];
           s[i]=s[n-i-1];
           s[n-i-1]=t;
       }
       for(int i=0;i<n;i++)
       System.out.println(s[i]);
    }
=======
class Solution {
    public void reverseString(char[] s) {
        int n=s.length;
        char t;
       for(int i=0;i<n/2;i++)
       {
           t=s[i];
           s[i]=s[n-i-1];
           s[n-i-1]=t;
       }
       for(int i=0;i<n;i++)
       System.out.println(s[i]);
    }
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
}