#! /usr/bin/env python3.4
import math

def find_median(list1,list2):
    list=list1+list2
    list.sort()
    return (list[math.floor((len(list)-1)/2)],list)

if __name__ == '__main__':
    first_list=input("Enter the first list of numbers: ").split()
    second_list=input("Enter the second list of numbers: ").split()
    first_list=list(map(int,first_list))
    second_list=list(map(int,second_list))
    value=find_median(first_list,second_list)
    print("First list: {}".format(first_list))
    print("Second list: {}".format(second_list))
    print("Merged list:{}".format(value[1]))
    print("Median: {}".format(value[0]))
