"""
Created March 7th 2018 Jianpu Ma
"""
import csv
import json
import openpyxl

INPUT_FILE = ''
MAPPING_FILE = ''
OUT_FILE = ''


def extract_comment(input):
    dict = {}
    with open(input, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            loan_num = row['LOAN_NUMBER']

            if loan_num in dict:
                comment_date = row['COMMENT_DATE']
                comment_time_sequence = row['COMMENT_TIME_SEQUENCE']
                department_category = row['DEPARTMENT_CATEGORY']
                comment_code = row['COMMENT_CODE']
                comment = row['COMMENT']
                dict[loan_num] = dict[loan_num] + ' ' + comment

            else:

                dict[loan_num] = ''
    print dict
    print 'down with extract comment, then length of the comment_map is %s' %len(dict)

    return dict


def extract_mapping_dict(map_file):
    key_to_category = {}

    with open(map_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            keyword = row['Keyword']
            category = row['Category']
            key_to_category[keyword] = category

    print 'down with extract map, the length of the map is %s' %len(key_to_category)

    return key_to_category


def create_report( input_dict, map_dict,outfile):

    with open(outfile, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Loan Number', 'Keyword','Category'])

        for loan_num, comment in input_dict.iteritems():
            for key in map_dict:
                if key in comment:
                    writer.writerow([loan_num, key, map_dict[key]])

    return



if __name__ == '__main__':
    input_dict = extract_comment(INPUT_FILE)
    map_dict = extract_mapping_dict(MAPPING_FILE)
    create_report(input_dict,map_dict,OUT_FILE)
