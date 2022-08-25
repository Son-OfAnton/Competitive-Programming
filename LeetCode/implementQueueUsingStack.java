// 232. Implement Queue using Stacks

class MyQueue {
    Stack<Integer> stk = new Stack<Integer>();
    
    public MyQueue() {
        
    }
    
    public void push(int x) {
        stk.add(x);
    }
    
    public int pop() {
        return stk.remove(0);
    }
    
    public int peek() {
        return stk.firstElement();
    }
    
    public boolean empty() {
        return stk.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
