import random
import string
import sys
import csv

#declarng choioces here
gender=['male','female']
state=['andhra','telengana']
district=['westgodavari','nalgonda']
village=['annadevarapeta','chityala','velachintalagudem']


state_dis_mapping = {
"andhra":['westgodavari'],
"telengana":['nalgonda']
}
district_village_mapping={
"westgodavari":["annadevarapeta","velachintalagudem"],
"nalgonda":["chityala"],
}
#RANDOM GENERATION OF STRING(FOR NAME OF CUSTOMOUR)
def randon_string_generator(size, type=None):
	if type == "char":
		chars = chars = string.ascii_uppercase + string.ascii_lowercase
	elif type == "string":
		chars = chars = string.ascii_uppercase + string.ascii_lowercase
	elif type == "number":
		chars = string.digits
	return ''.join(random.choice(chars) for _ in range(size))

#op list

#comandline arguments

#main function in python
def main(cus_num):
	cust_info = []
	for i in range(int(cus_num)):
		"""BUILDING CUSTOMOUR DATA HERE"""
		state_name = random.choice(state)
		district_name =random.choice(state_dis_mapping[state_name])
		village_name =random.choice(district_village_mapping[district_name])
		cust_data ={
		'cust_id':i,
		'name':randon_string_generator(random.randint(3,10), 'string'),
		'age':random.randint(20,30),
		'gender':random.choice(gender),
		'state':state_name,
		'district':district_name,
		'village':village_name
		}
		cust_info.append(cust_data)
	return cust_info

def write_to_csv(cust_info):
	#headers of csv
	fields = ['cust_id', 'name', 'gender','state','district','village','age'] 
	#create a csv file with the folloing name
	filename = "/home/chinni/customourinfo.csv"	
	with open(filename, 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(fields)
		each_cust_data = [[each_dict['cust_id'],[each_dict['name']],each_dict['gender'],each_dict['state'],each_dict['district'],each_dict['village'],each_dict['age']] for each_dict in cust_info ]
		each_cust_data = [ [cust_dict[item] for item in fields]  for cust_dict in cust_info]
		csvwriter.writerows(each_cust_data)
		print each_cust_data



if __name__ == '__main__':
	cus_num = sys.argv[1]
	cust_info = main(cus_num)
	write_to_csv(cust_info)