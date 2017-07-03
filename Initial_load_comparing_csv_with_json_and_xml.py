import xml.etree.ElementTree as ET
import json
import sys
import codecs
import os
import glob
import csv

# aFilelist = os.listdir(vDirectory)


csv_files_folder = os.path.abspath(os.path.join('.', "data", "CompanyBasics_CSV"))
json_files_folder = os.path.abspath(os.path.join('.', "data", "CompanyBasics_JSON"))
xml_files_folder = os.path.abspath(os.path.join('.', "data", "CompanyBasics_XML"))
csv_files = glob.glob(os.path.join(csv_files_folder, "*.csv*"))
json_files = glob.glob(os.path.join(json_files_folder, "*.csv*"))


# aFilelist = os.listdir(vDirectory)
#    print(aFilelist)

def get_all_buisiness_ids_from_csv_file(csvFile):
    if not os.path.exists(csvFile):
        print("CSV File  %s doesnot exist" % jsonFile)
        exit(0)

    csv_buisness_ids = []
    with codecs.open(csvFile, 'r', encoding='utf-8') as fin:
        file_reader = csv.reader(fin, delimiter=';')
        for row in file_reader:
            csv_buisness_ids.append(row[5])
    return csv_buisness_ids

# def read_all_xml_nodes(XMLfiles):
#     vDirectory = os.path.abspath(os.path.join('.', 'Data', 'CompanyBasics_XML'))
#     vOutputDirectory = os.path.abspath(os.path.join('.', 'Data', 'Temp'))
#     aFilelist = os.listdir(vDirectory)
#     # print(aFilelist)
#     global xml_party_ids
#     for file in aFilelist:
#         vFullFilename = vDirectory + '\\' + file
#         tree = ET.parse(vFullFilename)
#         root = tree.getroot()
#
#         # print ('Handling file', file)
#         xml_party_ids = []
#         for child in root:
#             # print(child.tag)
#             # print (child.tag)
#             for party in child.findall("partyId"):
#                 # print(party.text)
#                 xml_party_ids.append(party.text)
#                 # print(xml_party_ids)
#         # print(xml_party_ids)
#         return xml_party_ids


def read_all_xml_nodes(xml_file):
    xml_party_ids = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # print ('Handling file', file)
    for child in root:
        for party in child.findall("partyId"):
            xml_party_ids.append(party.text)
    return xml_party_ids


def get_all_buisiness_ids_from_json_file(jsonFile):
    if not os.path.exists(jsonFile):
        print("Json File %s does not exist" % jsonFile)
        exit(0)
    json_data = None
    j_data = None
    with codecs.open(jsonFile, 'r') as f:
        j_data = f.read()
    try:
        json_data = json.loads(j_data)
    except ValueError as e:
        print(e)

    except AttributeError as e:
        print(e)
    except:
        print("Unexpected error:", sys.exc_info()[0])

    json_buisness_ids = []
    if json_data:
        for index in range(len(json_data['ExternalReferenceDatas']['companyData'])):
            json_buisness_ids.append(
                json_data['ExternalReferenceDatas']['companyData'][index]['businessId'])
    return json_buisness_ids

if __name__ == '__main__':
    lineNumber = 1
    print('Comparison between CSV and JSON.......................................................................................')
    for each_csv_file in csv_files:
        folder, filename = os.path.split(each_csv_file)
        # fname, fext = os.path.splitext(filename)
        # json_file = "%s.json%s"%(fname, fext[3:])
        json_file_path = os.path.join(json_files_folder, filename)
        result = []
        try:
            singleResult = get_all_buisiness_ids_from_csv_file(each_csv_file) == get_all_buisiness_ids_from_json_file(json_file_path)
            if not singleResult:
                print('csv values', get_all_buisiness_ids_from_csv_file(each_csv_file))
                print('jsn values', get_all_buisiness_ids_from_json_file(json_file_path))
                print("LineNumber: %s [%s] %s, %s" % (lineNumber, singleResult, each_csv_file, json_file_path))
            test = each_csv_file, json_file_path, singleResult
            result.append(test)
        except:
                 print("Could not validate files %s, %s" % (each_csv_file, json_file_path))
        lineNumber += 1



    # print('\n\nComparison between JSON and XML.......................................................................................\n\n')
    # lineNumber = 1
    # for each_jason_file in json_files:
    #     folder, filename = os.path.split(each_jason_file)
    #     xml_file = os.path.join(xml_files_folder, filename)
    #     # print("%s == %s [%s]" % (each_jason_file, xml_file, get_all_buisiness_ids_from_json_file(json_file_path) == read_all_xml_nodes(xml_files_folder)))
    #     try:
    #         singleResult = get_all_buisiness_ids_from_json_file(each_jason_file) == read_all_xml_nodes(xml_file)
    #         if not singleResult:
    #             print('jsn values', get_all_buisiness_ids_from_json_file(each_jason_file))
    #             print('xml values', read_all_xml_nodes(xml_file))
    #             print("LineNumber: %s [%s] %s, %s" % (lineNumber, singleResult, each_jason_file, xml_file))
    #             break
    #     except:
    #         print("Could not validate files %s, %s" % (each_jason_file, xml_file))
    #     lineNumber += 1
    # print('\n\nComparison between CSV, JSON AND XML files is complete')




















        #
        # with codecs.open("C:\\Users\\dmittal\\PycharmProjects\\readingCSV\Data\CompanyBasics_JSON\\Company_Basics_2017_05_17.csvaa", 'r') as f:
        #     json_data = json.load(f)
        # json_buisness_ids = []
        #
        # if json_data:
        #     for index in range(len(json_data['ExternalReferenceDatas']['companyData'])):
        #         json_buisness_ids.append(json_data['ExternalReferenceDatas']['companyData'][index]['businessId'])
        #         print (index)
        #         if json_buisness_ids[index] != xml_party_ids[index]:
        #             print('this is match', json_buisness_ids[index], '!=', xml_party_ids[index])

# vFullFilename = "C:\\Users\\dmittal\\PycharmProjects\\readingCSV\Data\CompanyBasics_XML\\Company_Basics_2017_05_17.csvaa"
# tree = ET.parse(vFullFilename)
# root = tree.getroot()
# xml_party_ids = []
# for child in root:
#         for party in child.findall("partyId"):
#             xml_party_ids.append(party.text)
#
# with codecs.open("C:\\Users\\dmittal\\PycharmProjects\\readingCSV\Data\CompanyBasics_JSON\\Company_Basics_2017_05_17.csvaa", 'r') as f:
#     json_data = json.load(f)
# json_buisness_ids = []
#
# if json_data:
#     for index in range(len(json_data['ExternalReferenceDatas']['companyData'])):
#         json_buisness_ids.append(json_data['ExternalReferenceDatas']['companyData'][index]['businessId'])
#         if json_buisness_ids[index] != xml_party_ids[index]:
#             print('this is match', json_buisness_ids[index], '!=', xml_party_ids[index])
