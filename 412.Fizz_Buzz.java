<<<<<<< HEAD
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> l=new ArrayList<>();
        for(int i=1;i<=n;i++)
        {
            if(i%3==0 && i%5==0)
            l.add("FizzBuzz");
            else if(i%3==0)
            l.add("Fizz");
            else if(i%5==0)
            l.add("Buzz");
            else
            l.add(String.valueOf(i));

        }
        return (l);
        
    }
=======
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> l=new ArrayList<>();
        for(int i=1;i<=n;i++)
        {
            if(i%3==0 && i%5==0)
            l.add("FizzBuzz");
            else if(i%3==0)
            l.add("Fizz");
            else if(i%5==0)
            l.add("Buzz");
            else
            l.add(String.valueOf(i));

        }
        return (l);
        
    }
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
}