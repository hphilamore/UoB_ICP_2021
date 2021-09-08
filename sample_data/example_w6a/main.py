# main.py
# import fruit.strawberry 
# print(fruit.strawberry.word)

# import fruit.strawberry as strawb
# print(strawb.word)

# main.py
import fruit              # banana module in __init__.py so automatically imported
#import fruit.strawberry   # strawberry module needs to be imported using full path 
print(fruit.banana.word) 
from fruit import strawberry as strawb
print(strawb.word) 