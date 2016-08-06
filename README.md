# bbcc_YACP

Introduction

Your teammate tried to fix the bug, but only managed to make it worse! Now the filter will only accept
words that are already palindromes.

You are now tasked with writing another add-on that determines how many different words you can
send through the system given a set of characters.

For example:
bbaa can be sent in two different ways: abba and baab
bbaacc can be sent in six different ways: baccab, abccba, acbbca, cabbac, bcaacb, and cbaabc.

Input Specifications
Your program will take
A string S denoting the set of characters to be tested. All letters in the alphanumeric input will be
lowercase (1 ≤ LENGTH(S) ≤ 500)

Output Specifications
Based on the input, print out the total number of unique palindromes that can be created from the
input.

Sample Input/Output
Input
bbaa
Output
2
Explanation
bbaa can be re-arranged to abba and baab, which are palindromes.

Input
abcdef
Output
0
Explanation
abcdef has no variations that are palindromes.
Input
bbaacc
Output
6
Explanation
bbaacc can make the following palindromes: baccab, bcaacb, cbaabc, cabbac, acbbca, abccba.
