#! /usr/bin/env python3.4

if __name__ == '__main__':
    list=input("Please enter some values: ").split()
    sum=0
    for item in list:
        try:
            sum+=float(item)
        except ValueError:
            try:
                sum-=float(item[1:])
            except IndexError:
                pass
            except ValueError:
                pass

    print("The sum is: {}".format(sum))
