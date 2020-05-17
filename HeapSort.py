
class HeapSort():

    def heapify(self, aList:list, n:int, i:int):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and aList[i] < aList[l]:
            largest = 1

        if r < n and aList[largest] < aList[r]:
            print("\nif {} < {} and {} < {}".format(r, n, aList[largest], aList[r]))
            print("{} = {}".format(aList[largest], aList[r]))
            largest = r

        if largest != i:
            print("\nif {} != {}".format(largest, i))
            print("{} <swap> {}".format(aList[i], aList[largest]))
            aList[i], aList[largest] = aList[largest], aList[i]
            print("++++++",aList,end="\n\n")
            self.heapify(aList, n, largest)

    def sort(self, aList:list):
        n = len(aList)

        for i in range(n//2 - 1, -1, -1):
            self.heapify(aList, n, i)

        for i in range(n-1, 0, -1):
            print("{} <swap> {}".format(aList[i], aList[0]))
            aList[i], aList[0] = aList[0], aList[i]
            self.heapify(aList, i, 0)

        print("\nHeap sorted list = ", aList, end="\n\n")
