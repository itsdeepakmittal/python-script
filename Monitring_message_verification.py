import os
import json
import csv

# variable
csvData = []
businessId = []
json_real_data = []
csvLineCount = 0
dataAtom = ''
dataAtomJSON = ''
vIndex = 0


businessId = []


def reading_csv_files():
    # print('reading File:', vFullCSVFilename)

    with open(vFullCSVFilename, 'r', encoding='utf-8') as fin:
        file_reader = csv.reader(fin, delimiter=';')
        global businessId
        #print('this is from CSV', fin.name)
        for row in file_reader:
            # print(row[5])
            dataAtom = row[5]
            businessId.append(dataAtom)
        return businessId


def readlenght():
    global csvLineCount
    global csvData
    print("reading length csv")
    filename = os.path.abspath(os.path.join("data", "Company_Basics_2017_05_17.csvaa"))
    with open(filename, 'r') as fin:
        csvData = fin.readlines()
        csvLineCount = csvData.__len__()
        print(csvLineCount)


def readJSON():
    global json_real_data

    with open(vFullJsonFilename, 'r', encoding='utf-8') as csv_as_jason:
        json_real_data = json.load(csv_as_jason)
        #print('This is from jason', csv_as_jason.name)

def readJSONData():
    global dataAtomJSON
    dataAtomJSON = json_real_data['ExternalReferenceDatas']['companyData'][vIndex]['businessId']
    # print(i)


readlenght()

vValidateCSV = 'true'

vCSVDirectory = 'C:\\Users\\dmittal\\PycharmProjects\\readingCSV\\Data\\CompanyBasics_CSV\\'
vJsonDirectory = 'C:\\Projects\\OP\\Data\\CompanyBasics_JSON\\'
vXMLDirectory = 'C:\\Projects\\OP\\Data\\CompanyBasics_XML\\'
filelist = os.listdir(vCSVDirectory)

for file in filelist:
    vFullJsonFilename = vJsonDirectory + file
    vFullCSVFilename = vCSVDirectory + file

    if vValidateCSV == 'true':
        # read csv

        for tempIndex in range(csvLineCount):
            dataAtom = businessId
            reading_csv_files()
            readJSON()
            readJSONData()
            if (dataAtom[tempIndex] != dataAtomJSON):
                break

            else:
                print('found match', dataAtom[tempIndex], '==', dataAtomJSON)
                vIndex = vIndex + 1
                # if (vIndex != tempIndex):
                #           vIndex = 0


                # businessId = reading_csv_files(vFullCSVFilename)
                # print(businessId)
