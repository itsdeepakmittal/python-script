import os
import json
import csv
import sys
import glob
import codecs

csv_files_folder = os.path.abspath(os.path.join('.', "Data", "GroupReferences_CSV"))
json_files_folder = os.path.abspath(os.path.join('.', "Data", "GroupReferences_JSON"))

csv_files = glob.glob(os.path.join(csv_files_folder, "*.csv*"))
print(csv_files)


def get_all_buisiness_ids_from_json_file(jsonFile):
    if not os.path.exists(jsonFile):
        print('Json File %s does not exist' % jsonFile)
        exit(0)
    json_data = None
    j_data = None
    with codecs.open(jsonFile, 'r') as f:
        j_data = f.read()
    try:
        json_data = json.loads(j_data)
    except:
        print("Unexpected error:", sys.exc_info()[0])

    json_buisness_ids = []
    if json_data:
        for index in range(len(json_data['groupReferenceDatas']['groupReference'])):
            json_buisness_ids.append(json_data['groupReferenceDatas']['groupReference'][index]['businessId'])
    return json_buisness_ids


def get_all_buisiness_ids_from_csv_file(csvFile):
    if not os.path.exists(csvFile):
        print("CSV File  %s doesnot exist" % jsonFile)
        exit(0)

    csv_buisness_ids = []
    with codecs.open(csvFile, 'r') as fin:
        file_reader = csv.reader(fin, delimiter=';')
        for row in file_reader:
            csv_buisness_ids.append(row[5])
    return csv_buisness_ids


if __name__ == '__main__':

    for each_csv_file in csv_files:
        folder, filename = os.path.split(each_csv_file)
        # fname, fext = os.path.splitext(filename)
        # json_file = "%s.json%s"%(fname, fext[3:])
        json_file_path = os.path.join(json_files_folder, filename)
        print("%s == %s [%s]" % (each_csv_file, json_file_path, get_all_buisiness_ids_from_csv_file(each_csv_file) == get_all_buisiness_ids_from_json_file(
                               json_file_path)))

