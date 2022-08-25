// 155. Min Stack

class MinStack {
    Stack<Integer> stk = new Stack<>();
    public MinStack() {
        
    }
    
    public void push(int val) {
        stk.add(val);
    }
    
    public void pop() {
        stk.pop();
    }
    
    public int top() {
        return stk.peek();
    }
    
    public int getMin() {
        int min = stk.elementAt(0);
        for(int i = 1; i < stk.size(); i++) {
            if(min > stk.elementAt(i))
                min = stk.elementAt(i);
            }
            return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
