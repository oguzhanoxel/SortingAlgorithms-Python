
class BubbleSort():

    def sort(self, aList:list):

        for i in range(len(aList)-1):
            if aList[i] > aList[i+1]:
                print(" {} > {} Swap".format(aList[i], aList[i+1]))
                aList[i], aList[i+1] = aList[i+1], aList[i]
                print(" {}.step = {}".format((i + 1), aList))
            else:
                print(" {} < {} NOT swap".format(aList[i], aList[i+1]))
                print(" {}.step = {}".format((i + 1), aList), end="\n\n")
        print("Bubble sorted list = ", aList, end="\n\n")

def main():
    pass

if __name__ == '__main__':
    main()