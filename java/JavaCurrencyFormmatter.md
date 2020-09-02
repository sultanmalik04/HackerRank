#### Use of NumberFormat Class
>Use getInstance or getNumberInstance to get the normal number format. Use getIntegerInstance to get an integer number format. Use getCurrencyInstance to get the currency number format. And use getPercentInstance to get a format for displaying percentages. With this format, a fraction like 0.53 is displayed as 53%.

```java
import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        NumberFormat usFormat = NumberFormat.getCurrencyInstance(Locale.US);
        String us = usFormat.format(payment);
        NumberFormat  indFormat= NumberFormat.getCurrencyInstance(new java.util.Locale("en","in"));
        String india = indFormat.format(payment);
        NumberFormat chinaFormat = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = chinaFormat.format(payment);
        NumberFormat franceFormat = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france = franceFormat.format(payment);
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
```