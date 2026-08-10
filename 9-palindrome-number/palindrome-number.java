class Solution {
    public boolean isPalindrome(int x) {
        int original = x;
        StringBuilder sb = new StringBuilder(String.valueOf(x));
        if ((sb.reverse().toString().equals(String.valueOf(original)))) return true;
        return false;

    }
}