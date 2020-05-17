
class MergeSort():

    def sort(self, aList:list):
        if len(aList) > 1:
            mid = len(aList)//2
            L = aList[:mid]
            print("",L,end=" ")
            R = aList[mid:]
            print("",R,end=" \n")

            self.sort(L)
            self.sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    aList[k] = L[i]
                    i+=1
                else:
                    aList[k] = R[j]
                    j+=1
                k+=1

            while i < len(L):
                aList[k] = L[i]
                i+=1
                k+=1

            while j < len(R):
                aList[k] = R[j]
                j+=1
                k+=1
            print("",aList,"merged and sorted part",end="\n\n")

    def printList(self,aList):
        print("\nMerged sorted list = ", aList, end="\n\n")

def main():
    pass

if __name__ == '__main__':
    main()