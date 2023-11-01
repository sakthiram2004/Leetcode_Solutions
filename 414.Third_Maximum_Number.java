<<<<<<< HEAD
class Solution {
    public int thirdMax(int[] nums) {
        HashSet<Integer> hs=new HashSet<>();
        for (int i:nums)
        hs.add(i);
        int[] arr=new int[hs.size()];
        int k=0;
        for(int i:hs)
        {
            arr[k]=i;
            k++;
        }
        Arrays.sort(arr);
        if(arr.length<3)
        return arr[arr.length-1];
        return arr[arr.length-3];
    }
=======
class Solution {
    public int thirdMax(int[] nums) {
        HashSet<Integer> hs=new HashSet<>();
        for (int i:nums)
        hs.add(i);
        int[] arr=new int[hs.size()];
        int k=0;
        for(int i:hs)
        {
            arr[k]=i;
            k++;
        }
        Arrays.sort(arr);
        if(arr.length<3)
        return arr[arr.length-1];
        return arr[arr.length-3];
    }
>>>>>>> c7b4b56f48450f4fdaa84bb6d24ce62538dd75c7
}