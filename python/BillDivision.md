### Problem statement
>Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.


## Python
```python
def bonAppetit(bill, k, b):
    if b == (sum(bill) - bill[k]) / 2:
        print('Bon Appetit')
    else:
        print(b - (sum(bill) - bill[k])//2)

nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
bonAppetit(bill, k, b)
```