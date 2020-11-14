import csv
import subprocess

# open up csv file
with open('userlist.csv', 'r') as f:
    csv_reader = csv.reader(f)
    line_count = 0
    for line in csv_reader:
    # loop through the lines in file, run commands for all lines except the first one
        if line_count != 0:
            fullname, fname, lname, sam_name, upn, password = line
            subprocess.run(f'dsadd user "cn={sam_name},ou=NIITUSERS,dc=niit,dc=com" -samid {sam_name} -upn {upn} -pwd {password} -fn {fname} -ln {lname} -disabled no -mustchpwd yes ',capture_output=True, text=True)

