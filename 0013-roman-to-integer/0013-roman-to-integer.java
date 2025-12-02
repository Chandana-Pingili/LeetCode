class Solution {
    public int romanToInt(String s) {
        //s="III";
        HashMap<Character,Integer> romanDict=new HashMap<>();
        romanDict.put('I',1);
        romanDict.put('V',5);
        romanDict.put('X',10);
        romanDict.put('L',50);
        romanDict.put('C',100);
        romanDict.put('D',500);
        romanDict.put('M',1000);
        s=s.replace("IV","IIII");
        s=s.replace("IX","VIIII");
        s=s.replace("XL","XXXX");
        s=s.replace("XC","LXXXX");
        s=s.replace("CD","CCCC");
        s=s.replace("CM","DCCCC");
        int num=0;
        for(char c:s.toCharArray())
        {
            num+=romanDict.get(c);
            //System.out.println(romanDict.get(c)+" "+c+" "+num);
        }
        return num;
    }
}