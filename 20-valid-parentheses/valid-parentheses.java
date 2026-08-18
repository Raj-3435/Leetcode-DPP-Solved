class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        for (int i=0;i<s.length();i++){ 
            if (!stk.isEmpty() && (s.charAt(i) == ')' && stk.peek() == '(' || s.charAt(i) == '}' && stk.peek()=='{' || s.charAt(i) == ']' && stk.peek() == '[')){
                stk.pop();
            }
        else stk.add(s.charAt(i));
        }
        if (stk.isEmpty()) return true;
        return false;

    }
}