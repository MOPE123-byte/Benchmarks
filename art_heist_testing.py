from art_heist import Item, max_value

# Testing:

try:
    max_value([], -1)   
    print("Exception test failed (no exception raised)")
except ValueError:
    pass
except Exception as e:
    print(f"Exception test failed ({e})")

if max_value([], 0) != 0:
    print("Test 1A failed")
if max_value([], 5) != 0:
    print("Test 1B failed")
    
items = [Item(1, 5), Item(5, 15), Item(4, 7)]
if max_value(items, 4) != 7:
    print("Test 2A failed")
if max_value(items[::-1], 4) != 7:
    print("Test 2B failed")
    
items = [Item(4, 7)]
if max_value(items, 3) != 0:
    print("Test 3A failed")
if max_value(items, 4) != 7:
    print("Test 3B failed")
if max_value(items, 5) != 7:
    print("Test 3C failed")
    
items = [Item(3, 7), Item(4, 9), Item(2, 5), Item(6, 12), 
         Item(7, 14), Item(3, 6), Item(5, 12)]
if max_value(items, 15) != 34:
    print ("Test 4A failed")
if max_value(items[::-1], 15) != 34:
    print ("Test 4B failed")

items = [Item(5, 7), Item(3, 5), Item(1, 4)]
if max_value(items, 5) != 9:
    print("Test 5A failed")
if max_value(items[::-1], 5) != 9:
    print("Test 5B failed")
    
try:
# =============================================================================
#     from art_heist import max_value_with_list
#     if max_value_with_list([], 0) != [0, []]:
#         print("Challenge Test 1A failed")
#     if max_value_with_list([], 5) != [0, []]:
#         print("Challenge Test 1B failed")
#          
#     items = [Item(1, 5), Item(5, 15), Item(4, 7)]
#     if max_value_with_list(items, 4) != [7, [Item(4, 7)]]:
#         print("Challenge Test 2A failed")
#     if max_value_with_list(items[::-1], 4) != [7, [Item(4, 7)]]:
#         print("Challenge Test 2B failed")
#          
#     items = [Item(4, 7)]
#     if max_value_with_list(items, 3) != [0, []]:
#         print("Challenge Test 3A failed")
#     v, lst = max_value_with_list(items, 4)
#     if v != 7 or len(lst) != 1 or lst[0] != Item(4, 7):
#         print("Challenge Test 3B failed")
#     v, lst = max_value_with_list(items, 5)
#     if v != 7 or len(lst) != 1 or lst[0] != Item(4, 7):
#         print("Challenge Test 3C failed")
#          
#     items = [Item(3, 7), Item(4, 9), Item(2, 5), Item(6, 12), 
#              Item(7, 14), Item(3, 6), Item(5, 12)]
#     v, lst = max_value_with_list(items, 15)
#     if v != 34:
#         print ("Challenge Test 4A failed (value)")
#     if set(lst) != {Item(3, 7), Item(4, 9), Item(3, 6), Item(5, 12)}:
#         print ("Challenge Test 4A failed (list)")
#     v, lst = max_value_with_list(items[::-1], 15)
#     if v != 34:
#         print ("Challenge Test 4B failed (value)")
#     if set(lst) != {Item(3, 7), Item(4, 9), Item(3, 6), Item(5, 12)}:
#         print ("Challenge Test 4B failed (list)") 
#         
#     items = [Item(5, 7), Item(3, 5), Item(1, 4)]
#     v, lst = max_value_with_list(items, 5)
#     if v != 9:
#         print("Challenge Test 5A failed (value)")
#     if len(lst) != 2 or set(lst) != {Item(3, 5), Item(1, 4)}:
#         print("Challenge Test 5A failed (list)")
#     v, lst = max_value_with_list(items[::-1], 5)
#     if v != 9:
#         print("Challenge Test 5B failed (value)")
#     if len(lst) != 2 or set(lst) != {Item(3, 5), Item(1, 4)}:
#         print("Challenge Test 5B failed (list)")
# =============================================================================
    from art_heist import max_value_items
    if max_value_items([], 0) != []:
        print("Challenge Test 1A failed")
    if max_value_items([], 5) != []:
        print("Challenge Test 1B failed")
         
    items = [Item(1, 5), Item(5, 15), Item(4, 7)]
    if max_value_items(items, 4) != [Item(4, 7)]:
        print("Challenge Test 2A failed")
    if max_value_items(items[::-1], 4) != [Item(4, 7)]:
        print("Challenge Test 2B failed")
         
    items = [Item(4, 7)]
    if max_value_items(items, 3) != []:
        print("Challenge Test 3A failed")
    if max_value_items(items, 4)!= [Item(4, 7)]:
        print("Challenge Test 3B failed")
    if max_value_items(items, 4)!= [Item(4, 7)]:
        print("Challenge Test 3C failed")
         
    items = [Item(3, 7), Item(4, 9), Item(2, 5), Item(6, 12), 
             Item(7, 14), Item(3, 6), Item(5, 12)]
    lst = max_value_items(items, 15)
    if set(lst) != {Item(3, 7), Item(4, 9), Item(3, 6), Item(5, 12)}:
        print ("Challenge Test 4A failed")
    lst = max_value_items(items[::-1], 15)
    if set(lst) != {Item(3, 7), Item(4, 9), Item(3, 6), Item(5, 12)}:
        print ("Challenge Test 4B failed") 
        
    items = [Item(5, 7), Item(3, 5), Item(1, 4)]
    lst = max_value_items(items, 5)
    if len(lst) != 2 or set(lst) != {Item(3, 5), Item(1, 4)}:
        print("Challenge Test 5A failed")
    lst = max_value_items(items[::-1], 5)
    if len(lst) != 2 or set(lst) != {Item(3, 5), Item(1, 4)}:
        print("Challenge Test 5B failed")
except ImportError:
    print("Challenge not attempted")
except Exception as e:
    print(f'Challenge failed with exception: {e}')    