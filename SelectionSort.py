
class SelectionSort():

    def sort(self, aList:list):

        for i in range(len(aList)):
            first_idx = i

            print(" {}.index = {}".format(i,aList[i]), end=", ")

            for j in range((i+1), len(aList)):
                if aList[first_idx] > aList[j]:
                    first_idx = j

            print("Smallest element found =", aList[first_idx], end = ",\n")
            aList[first_idx], aList[i] = aList[i], aList[first_idx]
            print(" {}.step = {}".format((i+1),aList), end="\n\n")
        print("Selection sorted list = ", aList)


def main():
    pass

if __name__ == '__main__':
    main()