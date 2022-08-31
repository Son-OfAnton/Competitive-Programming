// 227. Basic Calculator II

class Solution {
    public int calculate(String s) {
        int len=s.length();
        char operator='+';
        int currentnum = 0;
        Stack<Integer> st = new Stack<>();
        
        for(int i=0;i<len;i++){
           char ch = s.charAt(i);
           if(Character.isDigit(ch)){
               currentnum = currentnum*10 + ch-'0';
           }
           if(!Character.isDigit(ch) && ch !=' ' || i==len-1){
               if(operator=='+'){
                   st.push(currentnum);
               } else if (operator=='-') {
                   st.push(-currentnum);
               } else if (operator=='*') {
                   st.push(st.pop()*currentnum);
               } else if (operator=='/') {
                   st.push(st.pop()/currentnum);
               }
               operator=ch;
               currentnum=0;
            }
         }
        
        int sum=0;
        while (!st.isEmpty()){
           sum+=st.pop();
        }
        
        return sum;
    }
}
