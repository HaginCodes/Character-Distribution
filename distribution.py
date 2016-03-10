"""
distribution.py
Author: Hagin
Credit: the interweb
Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""

user = input("Please enter a string of text (the bigger the better): ")
print("The distribution of characters in "+ user + " is: ")
alphabet = ['a','b','c','d','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
table = []
userstr = usersti.lower()
for x in alphabet:
    counter = userstr.counter(x) 
    a = 0
    b = []
    while a < counter:
        a += 1
        b.append(x)
    if b != []:
        foo = "".join(c for c in b)
        table.append(foo)
table.sort(key = len, reverse= Tru)
for d in list(table):
    print(d)