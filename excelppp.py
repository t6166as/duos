#!/usr/local/bin/python3
import xlrd as exc
import csv
import argparse
from abbv import abbvtool

def parse_args():
	parser=argparse.ArgumentParser( description ='supply file that need to be parsed')
	parser.add_argument('--filename',required=True)
	parser.add_argument('--outputname',required=True)
	return parser.parse_args()


def csvconvert(filename,outputname):
	workbook = exc.open_workbook(filename)
	intial_li=[]
	for i in workbook.sheet_names():
		processing_sheet=i
		worksheet = workbook.sheet_by_name(processing_sheet)
		for j in range(2, worksheet.nrows):
			acronym=abbvtool(worksheet.cell_value(j,3))
			txt_val = worksheet.cell_value(j,4)
			label = worksheet.cell_value(j,3)
			prefix=''
			suffix=''
			try:
				if label.upper() in txt_val.upper():
					prefix = txt_val.upper().split(label.upper())[0]
					suffix = txt_val.upper().split(label.upper())[1]
				elif  acronym.upper() in txt_val.upper():
					prefix = txt_val.upper().split(acronym.upper())[0]
					suffix = txt_val.upper().split(acronym.upper())[1]
				else:
					prefix='NA'
					suffix='NA'
			except:
				pass 
			initial_li=intial_li.append([i]+worksheet.row_values(j)+[acronym]+[prefix]+[suffix]) 
	##print(intial_li)
	with open(outputname, "w",encoding='utf-8') as f:
    		writer = csv.writer(f,delimiter='~',quotechar ='"')
    		writer.writerows(intial_li)


def main():
	args = parse_args()
	csvconvert(args.filename,args.outputname)


if __name__ == "__main__":
	main()	
