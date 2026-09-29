import csv
import os

# checking if file is there or not, if not create it
def check_csv_exists():
    if os.path.exists("data.csv") == False:
        f = open("data.csv", "w", newline='')
        writer = csv.writer(f)
        writer.writerow(["App Name", "Type", "Minutes", "Time"])
        f.close()

def get_all_data():
    check_csv_exists()
    my_data = []
    
    # open file in read mode
    f = open("data.csv", "r")
    reader = csv.reader(f)
    
    count = 0
    for row in reader:
        if count == 0:
            count = 1
            continue # skipping the heading row
            
        if len(row) > 0:
            my_data.append(row)
            
    f.close()
    return my_data

def save_new_record(record_list):
    check_csv_exists()
    # append mode so old data is not deleted
    f = open("data.csv", "a", newline='')
    w = csv.writer(f)
    w.writerow(record_list)
    f.close()

def delete_everything():
    # overwriting file to clear all data
    f = open("data.csv", "w", newline='')
    writer = csv.writer(f)
    writer.writerow(["App Name", "Type", "Minutes", "Time"])
    f.close()