class Solution {
    public boolean isPowerOfFour(int n) {
        if(n == 1) {
            return true;
        } else if(n % 4 == 0 && n != 0) {
            n /= 4;
            return isPowerOfFour(n);
        } 
        return false;
    }
}
