class Solution {
    public boolean isPowerOfThree(int n) {
        if(n == 1) {
            return true;
        } else if(n % 3 == 0 && n != 0) {
            n /= 3;
            return isPowerOfThree(n);
        } 
        return false;
        
    }
}
