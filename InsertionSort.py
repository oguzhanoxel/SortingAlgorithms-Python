
class InsertionSort():

    def sort(self,aList:list):

        for i in range(1,len(aList)):
            temp = aList[i]
            print("\n temp = {}".format(aList[i]))
            j = i-1

            while j >= 0 and temp < aList[j]:
                print(" {}.idx({}) ---> {}.idx({})".format(j, aList[j],(j+1), aList[j+1]), end=", ")
                aList[j+1] = aList[j]
                j -= 1
                print("---",aList)

            print(" {} = temp".format(aList[j+1]))
            aList[j+1] = temp
            print(" {}.step = {}".format(i,aList))

        print("\nInsertion Sorted List = {}".format(aList), end="\n\n")