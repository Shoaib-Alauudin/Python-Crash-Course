# def binary_search(item_list,item):
#     first = 0
#     last = len(item_list)-1
#     found = False
#     while( first<=last and not found):
#         mid = (first + last)//2
#         if item_list[mid] == item :
#             found = True
#         else:
#             if item < item_list[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return found
#
# print(binary_search([1,2,3,5,8],5))
# print(binary_search([1,2,3,5,8],6))

# def Ordered_binary_Search(olist, item):
#     if len(olist) == 0:
#         return False
#     else:
#         midpoint = len(olist) // 2
#         if olist[midpoint] == item:
#             return True
#         else:
#             if item < olist[midpoint]:
#                 return binarySearch(olist[:midpoint], item)
#             else:
#                 return binarySearch(olist[midpoint + 1:], item)
#
#
# def binarySearch(alist, item):
#     first = 0
#     last = len(alist) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found


# print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
# print(Ordered_binary_Search([0, 1, 3, 8, 14, 18, 19, 34, 52], 14))


# def bubbleSort(nlist):
#     for passnum in range(len(nlist)-1,0,-1):
#         for i in range(passnum):
#             if nlist[i]>nlist[i+1]:
#                 temp = nlist[i]
#                 nlist[i] = nlist[i+1]
#                 nlist[i+1] = temp
#
# nlist = [14,46,43,27,57,41,45,21,70]
# bubbleSort(nlist)
# print(nlist)
nlist = [14,46,43,27,57,41,45,21,70]
nlist.sort(reverse=True)
print(nlist)