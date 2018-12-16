
    

import csv

def removeLinks(inputItem):
    lst=inputItem.split()
    outputLst=[]
    for item in lst:
        if "https" not in item:
            outputLst.append(item)
    return " ".join(outputLst)

def ignoreSomeCharacters(item):
    item=item.replace('\n', ' ')
    item=item.replace('…',' ')
    return item 

def createMinFile(inputCsv,outputFilename):
    with open(inputCsv, 'r') as f:
        reader = csv.reader(f)
        lst=[row[1] for row in list(reader)]
        with open(outputFilename, 'w') as file_handler:
            for item in lst[1:]:
                item=ignoreSomeCharacters(item)
                item=removeLinks(item)
                if len(item)>0:
                    file_handler.write("{}\n".format(item))

createMinFile('outputData/extractor/MEMEOPERU_full.csv','outputData/extractor/MEMEOPERU_min.csv')
