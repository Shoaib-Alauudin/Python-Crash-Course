# UnSortedList = [1,2,5,14,25,6,10,8,12]
# SortedList = [1,6,7,8,9,30,50]
#
# def binarySearch(itemList,item):
#     print(itemList)
#     first = 0
#     last = len(itemList)-1
#     found = False
#     while(first<=last and not found):
#         mid = (first+last)//2
#         if itemList[mid] == item:
#             found = True
#         else:
#             if(itemList[mid] > item):
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return found
# print("-----------Sorted list binary search-------")
# print("Sorted list : ",SortedList)
# user = int(input("Please Enter any to find in the above list"))
# print(binarySearch(SortedList,user))
#
#
# def binarySearch(itemList,item):
#     itemList.sort(reverse=False)
#     print(itemList)
#     first = 0
#     last = len(itemList)-1
#     found = False
#     while(first<=last and not found):
#         mid = (first+last)//2
#         if itemList[mid] == item:
#             found = True
#         else:
#             if(itemList[mid] > item):
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return found
#
#
# print("------Binary Search----------")
# print("Unsorted List : ",UnSortedList)
# user = int(input("Please Enter any to find in the above list"))
# print(binarySearch(UnSortedList,user))
#
# def Sequencial_Search(list,SearchItem):
#     position = 0
#     found = False
#     print(list)
#     while(position<len(list) and not found):
#         if list[position] == SearchItem:
#             found = True
#         else:
#             position +=1
#     return found
#
# print("------Sequencial Search------")
# print("Unordered List : ",UnSortedList)
# user = int(input("Please Enter any to find in the above list"))
# print(Sequencial_Search(UnSortedList,user))
# print("----------------------------------")
# print("Ordered List : ",SortedList)
# user = int(input("Please Enter any to find in the above list"))
# print(Sequencial_Search(SortedList,user))
#
# def Bubble_Sort(list):
#     for passNumber in range(len(list)-1,0,-1):
#         for i in range(passNumber):
#             if list[i] > list[i+1]:
#                 temp =list[i]
#                 list[i] = list[i+1]
#                 list[i+1] = temp
#                 i += 1
# print("----------Bubble Sorting--------------")
# print("UnOrdered list : ",UnSortedList)
# Bubble_Sort(UnSortedList)
# print("After Bubble Sort UnOrdered list : ",UnSortedList)
#


a = 1
b = 2
a , b = b , a
print(a)
print(b)