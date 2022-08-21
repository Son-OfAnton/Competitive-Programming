class Solution {
    public String sortSentence(String s) {
        HashMap<Integer, String> theMap = new HashMap<>();
        s = s.replaceAll("\\s", ""); //removes all the spaces
        String word = "";
        int index;

        for (int i = 0; i < s.length(); i++) {
            int ascii = s.charAt(i);
            if (!(ascii >= 49 && ascii <= 57))
                word += s.charAt(i);
            else {
                index = s.charAt(i);
                theMap.put(index, word);
                word = "";
            }
        }
        for (int i = 49; i < 49 + theMap.size(); i++) {
            if(i == 48 + theMap.size()) {
                word += theMap.get(i);
                break;
            }
            word += theMap.get(i) + " ";
        }
        
        return word;
    }
}
