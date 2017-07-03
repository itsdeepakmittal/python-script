
import os
import json
import csv
import sys
import glob

csv_files_folder =  os.path.abspath(os.path.join('.', "data" , "csv"))
json_files_folder = os.path.abspath(os.path.join('.', "data", "json"))

csv_files = glob.glob(os.path.join(csv_files_folder, "*.csv*"))

import codecs

def get_all_buisiness_ids_from_json_file(jsonFile):
    if not os.path.exists(jsonFile):
        print "Json File %s doesnot exist"%jsonFile 
        exit(0)   
    json_data = None
    j_data = None
    with open(jsonFile, 'r') as f:
        j_data = f.read()
    try:
        json_data = json.loads(j_data)
    except ValueError as e:
        print e
    except AttributeError as e:
        print e
    except :
        print "Unexpected error:", sys.exc_info()[0]
    
    json_buisness_ids = []
    if json_data:
        for index in range(len(json_data['ExternalReferenceDatas']['companyData'])):
            json_buisness_ids.append(json_data['ExternalReferenceDatas']['companyData'][index]['businessId'])
    return json_buisness_ids

def get_all_buisiness_ids_from_csv_file(csvFile):
    if not os.path.exists(csvFile):
        print "CSV File  %s doesnot exist"%jsonFile 
        exit(0)   
    
    csv_buisness_ids = []
    with open(csvFile, 'r') as fin:
        file_reader = csv.reader(fin, delimiter=';')
        for row in file_reader:
            csv_buisness_ids.append(row[5])
    return csv_buisness_ids

if __name__ == '__main__':
    
    for each_csv_file in csv_files:
        folder, filename = os.path.split(each_csv_file)
        #fname, fext = os.path.splitext(filename)
        #json_file = "%s.json%s"%(fname, fext[3:])
        json_file_path = os.path.join(json_files_folder, filename)
        print "%s == %s [%s]" %(each_csv_file, json_file_path, get_all_buisiness_ids_from_csv_file(each_csv_file) == get_all_buisiness_ids_from_json_file(json_file_path))
    

