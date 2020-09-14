#### Problem Statement
>Kevin and Stuart want to play the 'The Minion Game'.

>Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
>SCORING: A player gets +1 point for each occurrence of the substring in the string S.

## Python
```python
from itertools import combinations
def minion_game(string):
    # your code goes here
    kevin , stuart = 0, 0
    for i in range(len(string)):
        if string[i] in ['A','E','I','O','U']:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        print("Kevin",kevin)
    elif kevin < stuart:
        print("Stuart",stuart)
    else:
        print("Draw")
```