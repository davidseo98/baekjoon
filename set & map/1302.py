import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
books = list()
for i in range(n):
    books.append(sys.stdin.readline().rstrip())

candidate = list()
book_sales = Counter(books).most_common()
max_sale = book_sales[0][1]

for book in Counter(books).most_common():
    if book[1] == max_sale:
        candidate.append(book[0])
print(sorted(candidate)[0])
