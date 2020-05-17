
class QuickSort():

    def partition(self, aList:list, low:int, high:int):
        i = (low - 1)
        pivot = aList[high]
        print(" Pivot =", pivot)

        for j in range(low, high):

            if aList[j] < pivot:
                print(" {} < {}".format(aList[j], pivot))
                i = i + 1
                print(" {} <swap> {}".format(aList[i],aList[j]))
                aList[i], aList[j] = aList[j], aList[i]
        print(" {} <swap pivot> {}".format(aList[i+1], aList[high]))
        aList[i+1], aList[high] = aList[high], aList[i+1]
        print(" Pivot",pivot,"result =",aList,end="\n\n")
        return ( i+1 )


    def sort(self,aList:list, low:int, high:int):

        if low < high:

            pi = self.partition(aList, low, high)
            if aList[low:pi-1] != []:
                print(" L  =",aList[low:pi-1])
            self.sort(aList, low, pi-1)
            if aList[pi+1:high] != []:
                print(" R  =",aList[pi+1:high])
            self.sort(aList, pi+1, high)
    def printList(self,aList):
        print("\nQuick sorted list = ", aList, end="\n\n")

def main():
    pass

if __name__ == '__main__':
    main()