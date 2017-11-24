# readwords = []
# with open('abc.txt') as readFile:
# # with open('S:\Development\Android\Java\Java_Document_for_Revision.docx') as readFile:
#     # file_contents = readFile.readline();
#     for line in readFile:
#         words = line.split(" ")
#         readwords.append(words)
# print("---------------------------------")
# print(readwords)0
# for line in readwords:
#     counter = 0
#     for word in line:
#         print(word)
#         if 'Hello' or 'hello' in word:
#             counter += 1
# print("Counter Value ",counter)
#

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" } ]
friendships = [(0, 1),
               (0, 2),
               (1, 2),
               (1, 3),
               (2, 3),
               (3, 4),
               (4, 5),
               (5, 6),
               (5, 7),
               (6, 8),
               (7, 8),
               (8, 9)]

for user in users:
    user["friends"] = []

print(users)
# for user in users:
#     print(user)
# print("-------------------")
# for friend in friendships:
#     for value in friend:
#         print(value)
#     print("-----------")

for i,j in friendships:
    print[i][j]
#     print(i," ",j)
#     users[i]["friends"].append(users[j])
#     users[j]["friends"].append(users[i])
#
# for user in users:
#     print(user)


    # for key,value in keys:
    #     print("Key : ",key," value : ",Vlaue)
    # for key,value in values:
    #     print("key : ",key," value : ",value)