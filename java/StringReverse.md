```java
public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        char []temp = A.toCharArray();
        int l = A.length();
        boolean flag = true;
        for (int i = 0; i < l/2; i++){
            if (temp[i] != temp[l-i-1]){
                flag = false;
            }
        }
        if (flag) System.out.println("Yes");
        else System.out.println("No");
    }
}
```