#!/usr/bin/python

#fruits = ['banana', 'apple',  'mango', 'raspberry']
numbers = [6, 5, 1, 3, 8, 4, 7, 9, 2]

#def quicksort(list):
#    size = len(list)
#    pivot = list[size-1]
#    wall = -1
#    currentElement = list[0];
#    print 'size=', size , ',pivot=',pivot
#    for
#    if (currentElement < pivot) :
#        result = swap(currentElement, pivot)
#        pivot = result[0];
#        currentElement = result[1];
#    else:
#        print "Bad"
#
#    for number in numbers:
#        print number
#    return
#
#def swap(ele1, ele2):
#    print 'b4 ele1=',ele1
#    print 'b4 ele2=',ele2
#
#    swapper = ele1
#    ele1 = ele2
#    ele2 = swapper
#    print 'ele1=',ele1
#    print 'ele2=',ele2
#    return [ele1, ele2]
#
#quicksort(numbers)


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   print "quickSortHelper alist=" , alist, ",first=", first, ",last=", last
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


