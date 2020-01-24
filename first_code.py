import glob


def getFileName(filepath):
    dataindex = getFileNameIndex(filepath)
    name = filepath
    return (name[dataindex[2]:dataindex[1]])

def getFileNameIndex(name):
    newName = str(name).find(".jsx")
    index = newName
    startEndIndex = [""]
    startEndIndex.append(newName)
    while(index>0):
        if(name[index]=="/"):
            startEndIndex.append(index+1)
            return startEndIndex
        else:
            index = index -1

def findNextBracket(startIndex, line):
    for x in range(startIndex, len(line)):
        if(line[x]==')' or line[x]==","):
            return x-1
    return -1



fileNameData = glob.glob("/home/altizon//mint-content/pages/default/*.jsx")
#print(fileNameData)
count =1
for filename in fileNameData:
    nameOfFile = getFileName(filename)
    print("processing: "+nameOfFile+"........")
    file1 = open(filename, 'r')
    Lines = file1.readlines() 
    file2 = open("data/"+nameOfFile+".jsx",'w')
    keyWordFile = open("data/keywords/"+nameOfFile+".txt",'w')
    keyWordArray = [""]
    for line in Lines: 
        dataToBeWritten =line
        didFind = [i for i in range(len(line)) if line.startswith('t(\"local:', i)]
        
        for x in didFind:
            dataToBeWritten = line.replace('t(\"local:','t(\"')
            keyword = line[(x+9): findNextBracket(x , line)]
            keyWordArray.append(keyword)
       # print(didFind)
        file2.write(dataToBeWritten)
    for i in keyWordArray:
        keyWordFile.write(i+"\n")
    count= count+1
    print("file: "+nameOfFile+" done")
