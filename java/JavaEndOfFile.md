> In computing, End Of File (commonly abbreviated EOF) is a condition in a computer operating system where no more data can be read from a data source.

The challenge here is to read  lines of input until you reach EOF, then number and print all  lines of content.

```java
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 0;
        while (sc.hasNext()){ 
            String line = sc.nextLine();
            System.out.println(++n+" "+line);
        }
    }
}
```