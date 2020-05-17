from os import system
from random import randint
from SelectionSort import SelectionSort
from BubbleSort import BubbleSort
from InsertionSort import InsertionSort
from MergeSort import MergeSort
from QuickSort import QuickSort
from HeapSort import HeapSort

menu1 = """
[1] Create Random Integer List
[0] Exit
"""
menu2 = """
[1] Selection Sort
[2] Bubble Sort
[3] Insertion Sort
[4] Merge Sort
[5] Quick Sort
[6] Heap Sort
"""
string1 = """
PRESS ENTER or ANY INPUT
"""
createdList = "\nCreated List = {}"

class CreateRandomList():

    def createList(self, x:int, y:int, aRange:int):
        aList = [randint(x, y) for i in range(aRange)]
        return aList

class Check():

    def checkSmallBig(self, small, big):
        if small>big:
            print("small number must be less than big number")

        else:
            return True

    def checkLength(self, length):
        if 0 >= length:
            print("length must be bigger than \"0\"")
        else:
            return True

def main():
    check = Check()
    create = CreateRandomList()
    selectionSort = SelectionSort()
    bubbleSort = BubbleSort()
    insertionSort = InsertionSort()
    mergeSort = MergeSort()
    quickSort = QuickSort()
    heapSort = HeapSort()

    while True:
        system("cls")
        print(menu1)
        choice0 = input("Enter a number = ")
        if choice0 == "1":
            system("cls")

            small = int(input("Enter smallest number = "))
            big = int(input("Enter biggest number = "))
            length = int(input("Enter length = "))

            if check.checkLength(length) == True and check.checkSmallBig(small, big) == True:
                aList = create.createList(small, big, length)
                print(createdList.format(aList), end="\n\n")
                while True:
                    print(menu2)
                    choice1 = input("Enter a number = ")

                    if choice1 == "1":
                        tempList = aList.copy()
                        print(createdList.format(tempList), end="\n\n")
                        selectionSort.sort(tempList)
                        input(string1)
                    elif choice1 == "2":
                        tempList = aList.copy()
                        print(createdList.format(tempList), end="\n\n")
                        bubbleSort.sort(tempList)
                        input("PRESS ENTER or ANY INPUT")
                    elif choice1 == "3":
                        tempList = aList.copy()
                        print(createdList.format(tempList), end="\n\n")
                        insertionSort.sort(tempList)
                        input("PRESS ENTER or ANY INPUT")
                    elif choice1 == "4":
                        tempList = aList.copy()
                        print(createdList.format(tempList), end="\n\n")
                        mergeSort.sort(tempList)
                        input("PRESS ENTER or ANY INPUT")
                    elif choice1 == "5":
                        tempList = aList.copy()
                        print(createdList.format(tempList), end="\n\n")
                        quickSort.sort(tempList, 0, len(tempList)-1)
                        input("PRESS ENTER or ANY INPUT")
                    elif choice1 == "6":
                        tempList = aList.copy()
                        print(createdList.format(tempList), end="\n\n")
                        heapSort.sort(tempList)
                        input("PRESS ENTER or ANY INPUT")



            else:
                input("PRESS ENTER or ANY INPUT")
        elif choice0 == "0":
            quit()

if __name__ == "__main__":
    main()