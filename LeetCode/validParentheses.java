class Solution {
    public boolean isValid(String s)
    {
        Stack<Character> openBracket = new Stack<Character>();
        Character c;
        for(int i = 0; i < s.length(); i++)
        {
            c = s.charAt(i);

            if (c.equals('(') || c.equals('{') || c.equals('['))
                openBracket.add(c);
            else 
            {
                if (openBracket.isEmpty())
                    return false;
                if (s.charAt(i) == ')' && openBracket.peek() != '(' ||
                        s.charAt(i) == '}' && openBracket.peek() != '{' ||
                        s.charAt(i) == ']' && openBracket.peek() != '[')

                    return false;
                openBracket.pop();
            }
        }
        return openBracket.isEmpty();
    }
}
