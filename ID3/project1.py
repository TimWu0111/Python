import math
import sys

def readdata(filename):
    """"create matrix"""
    f = open(filename, "r")
    list = []
    for line in f.readlines():
        line = line.strip() #delete \n
        listWords = line.split()
        list.append(listWords)
    f.close()
    return list

def findTarget(filename, index):
    """"find whole row"""
    list = readdata(filename)
    listvalue = list[index][1:]
    return listvalue

def calculate(list, totalrNum):
    """"list is one group"""
    rNum = len(list)
    cNum = len(list[0])
    entropy = 0.0
    pNum = 0.0
    nNum = 0.0
    for i in range(rNum):
        if list[i][-1] == '1':
            pNum = pNum + 1.0
        else:
            nNum = nNum + 1.0
    entropy = calcEntropy(pNum, nNum)

    infoGain = 0.0
    bestAttr = -1
    """"count how many 1,0 under 0,1,2"""
    for i in range(cNum - 1):
        zero_p = 0.0
        zero_n = 0.0
        one_p = 0.0
        one_n = 0.0
        two_p = 0.0
        two_n = 0.0
        for j in range(rNum):
            if list[j][i] == '0':
                if list[j][-1] == '1':
                    zero_p = zero_p + 1.0
                else:
                    zero_n = zero_n + 1.0
            elif list[j][i] == '1':
                if list[j][-1] == '1':
                    one_p = one_p + 1.0
                else:
                    one_n = one_n + 1.0
            elif list[j][i] == '2':
                if list[j][-1] == '1':
                    two_p = two_p + 1.0
                else:
                    two_n = two_n + 1.0
        zeroEntro = calcEntropy(zero_p, zero_n)
        oneEntro = calcEntropy(one_p, one_n)
        twoEntro = calcEntropy(two_p, two_n)

        condEntro = zeroEntro * (zero_p + zero_n) / float(rNum) + \
                    oneEntro * (one_p + one_n) / float(rNum) + \
                    twoEntro * (two_p + two_n) / float(rNum)

        #print(condEntro)
        """"calculate gain"""
        infoGainTmp = (entropy - condEntro)*rNum/totalrNum
        #print(infoGainTmp)
        """"find the largest gain"""
        if infoGainTmp >= infoGain:
            infoGain = infoGainTmp
            bestAttr = i
    #print(infoGain)
    return bestAttr, infoGain

def writedata(input,output, index, newdata):
    """"clear data"""
    fout = open(output, 'w')
    fout.truncate()
    fout.close()

    """"copy and insert"""
    fin = open(input, 'r')
    for line in fin:
        fout = open(output, 'a')  # 这里用追加模式
        if index in line:
            fout.write(newdata)
        else:
            fout.write(line)
    fin.close()
    fout.close()

def calcEntropy(pNum, nNum):
    if pNum == 0 or nNum == 0:
        return 0.0
    else:
        pPro = pNum / (pNum + nNum)
        nPro = nNum / (pNum + nNum)
        return -(pPro * math.log(pPro, 2) + nPro * math.log(nPro, 2))

if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print(sys.argv[0], ": takes 3 arguments, not ", len(sys.argv) - 1, ".")
        print("Expecting arguments: dataset.txt partition-input.txt partition-output.txt.")
        sys.exit()

    dataset = str(sys.argv[1])
    read = str(sys.argv[2])
    write = str(sys.argv[3])

    print('dataset:', dataset)
    print('partition_input:', read)
    print('partition_output:', write)

    """dataset = 'dataset.txt'
    read = 'partition-input.txt'
    write = 'partition-output.txt'"""

    total = len(readdata(dataset)) #total line of dataset
    index = readdata(read)         #read partition-2
    attr = readdata(dataset)       #read dataset

    """"find S1?S2?S3 and A1?A2?A3"""
    list=[]
    GAIN = 0.0
    for i in range(len(index)):
        for j in range(1,len(index[i])):
            #find every row by using index
            Target = findTarget(dataset, int(index[i][j]))
            #same group index at the same arry
            list.append(Target)
        bestAttr, GAINtmp = calculate(list,total-1)
        list.clear()
        if GAINtmp >= GAIN:
           GAIN = GAINtmp
           S = i
    #print(bestAttr, S)

    """"partition"""
    zerolist=[]
    onelist = []
    twolist = []
    for k in range(1, len(index[S])):
        partition = findTarget(dataset, int(index[S][k]))
        if partition[bestAttr] == '0':
            zerolist.append(index[S][k])
        elif partition[bestAttr] == '1':
            onelist.append(index[S][k])
        elif partition[bestAttr] == '2':
            twolist.append(index[S][k])

    #print(zerolist)
    #print(onelist)
    #print(twolist)

    """"count how many different element"""
    cnt=0
    if zerolist:
        cnt = cnt + 1
    if onelist:
        cnt = cnt + 1
    if twolist:
        cnt = cnt + 1
    #print(cnt)

    """"prepare newdata"""
    newdata=''
    alllist=[]
    if zerolist:
        alllist.append(zerolist)
    if onelist:
        alllist.append(onelist)
    if twolist:
        alllist.append(twolist)
    #print(alllist)
    for i in range(1,cnt+1):
                newdata = newdata + index[int(S)][0] + str(i) + str(alllist[i-1]) + '\n'

    newdata = newdata.replace('[',' ').replace(']', '').replace(',', '').replace("'",'')
    #print(newdata)

    """"write data into txt"""
    writedata(read, write, index[S][0], newdata)

    """"show context"""
    text = ''
    for i in range(1,cnt+1):
            text = text + index[int(S)][0] + str(i) +','
    print("Partition "+ index[int(S)][0] +" was replaced with partitions " + text + " using Feature " +attr[0][int(bestAttr)+1])