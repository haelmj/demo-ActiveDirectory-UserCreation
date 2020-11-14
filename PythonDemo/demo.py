import csv
import subprocess

with open('userlist.csv', 'r') as f:
    csv_reader = csv.reader(f)
    line_count = 0
    for line in csv_reader:
        if line_count != 0:
            fullname, fname, lname, sam_name, upn, password = line
            subprocess.run(f'dsadd user "cn={sam_name},ou=NIITUSERS,dc=niit,dc=com" -samid {sam_name} -upn {upn} -pwd {password} -fn {fname} -ln {lname} -disabled no -mustchpwd yes ')

