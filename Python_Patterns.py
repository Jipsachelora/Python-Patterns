#simple pyramid
# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("\n")

#trinagle pattern /pyramid with*
# n=int(input("entr the no"))
# for i in range(1,n):
#     for j in range(1,n-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(" * ",end=" ")
#     print("\n")

#reverse traingle pattern/pyramid with pyramid  *
# for i in range(1,8):
#     for j in range (i,i+1):
#         print(i*" ",end=" ")
#     for k in range(1,(8-i)):
#         print("*",end=" ")
#     print("\n")

#diamond using"*"
# rows = 5
# k = 2 * rows - 2
# for i in range(0, rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")
# k = rows - 2
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")

# Upper part of hollow diamond

# row = int(input('Enter number of row: '))
# for i in range(1, row + 1):
#     for j in range(1, row - i + 1):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#
#         if j == 1 or j == 2 * i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#number pattern 11111
#               2222
#               333
#               44
#               5
# h=1
# for i in range(1,7):
#     for j in range (i,i+1):
#         print(i*" ",end=" ")
#     for k in range(1,(7-i)):
#         print(h,end=" ")
#     h=h+1
#     print("\n")

#number pattern 1
#               21
#               321
#               4321
#               54321
# for i in range(6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print("\n")
# k=1
# for i in range(6):
#     for j in range(i+1):
#         print(k,end=" ")
#         k=k+1
#     print("\n")

#number pattern   12345
#                 22345
#                 33345
#                 44445
#                 55555

# r = 5
# for i in range(1, r+ 1):
#     for j in range(1, r + 1):
#         if j <= i:
#             print(i, end=' ')
#         else:
#             print(j, end=' ')
#     print("\n")

#pattern         A
#               ABA
#              ABCBA
#             ABCDCBA
#            ABCDEDCBA
# for i in range(65,70):
#     for m in range(1,70-i):
#         print(" ",end=" ")
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     for k in range(i-1,64,-1):
#         print(chr(k),end=" ")
#     print("\n")


 #NUMBER PATTERN
 #        1
 #        12
 #        123
 #        1234
 #        12345
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(" ")

#NUMBER PATTERN
#            11111
#            2222
#            333
#            44
#            5
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print(i,end=" ")
#     print("")


#NUMBER RPATTERN
#           1
#           23
#           456
#           78910
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end="")
#         k=k+1
#     print("")

#NUMBER PATTERN
#         55555
#         5555
#         555
#         55
#         5
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print(5,end="")
#     print("")

#NUMBER PATTERN
#         1
#         22
#         333
#         4444
#         55555
# for i in range(1,6):
#     for j in range(i+1,1,-1):
#         print(i,end="")
#     print("")

#NUMBER PATTERN
#     1
#     21
#     321
#     4321
#     54321

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print("")

#NUMBER PATTERN
#         012345
#         01234
#         0123
#         012
#         01
#         0

# for i in range(0,6):
#     for j in range(0,6-i):
#         print(j,end="")
#     print("")

#NUMBER PATTERN
#       2
#       43
#       765
# k=2
# a=1
# b=2
# k=b
# for i in range(2,5):
#
#     for j in range(a,b):
#         print(k,end="")
#         k=k-1
#     print("")
#     a=b
#     b=b+i
#     k=b


