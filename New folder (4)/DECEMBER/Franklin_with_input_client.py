import csv
import os
#initial inputs
client_name='Sainath pai'  #as per written partner client mapping.csv 
pannumber='AKKPP8206D'
wbr4_franklin='DMLBK3212756T.csv' #name of sheet at WBR/CAMPS/

print("our current working directory is :"+os.getcwd())


#searching for amc and folio number in wbr 4/cams csv
client_folio_and_amc=[]
directory_of_wbr4_franklin_file=(os.getcwd()+'/WBR/Franklin/'+wbr4_franklin)
wbr4_franklin_csv_file=open(directory_of_wbr4_franklin_file,mode='r',encoding='mac_roman',newline='')
reader_wbr4=csv.reader(wbr4_franklin_csv_file)
for row in reader_wbr4:
		if row[6]==client_name:
			print(row[0],row[3])
			client_folio_and_amc.append([client_name,pannumber,row[0],row[8]])	
print(client_folio_and_amc)
wbr4_franklin_csv_file.close()


#brokrage computation
brokrage_list=[]
finalresult=open('finalresultforbrokeragecomputation.csv',mode='w',newline="")
writer=csv.writer(finalresult)
writer.writerow(["folio_number","client_name","pannumber","company_name","total_brokerage","{}"]);
directory_of_wbr4_franklin_file=(os.getcwd()+'/WBR/Franklin/'+wbr4_franklin)
wbr4_franklin_csv_file=open(directory_of_wbr4_franklin_file,mode='r',encoding='mac_roman',newline='')
reader_wbr4=csv.reader(wbr4_franklin_csv_file)
for row in client_folio_and_amc:
	folio_number=row[2]
	client_name=row[0]
	pannumber=row[1]
	company_name=row[3]
	total_brokerage=0
	for row in reader_wbr4:
		if row[1]==folio_number:
			total_brokerage=total_brokerage+float(row[11])
		else:
			continue
		brokrage_list.append([folio_number,client_name,pannumber,company_name,total_brokerage])
		writer.writerow(["{}".format(folio_number),"{}".format(client_name),"{}".format(pannumber),"{}".format(company_name),"{}".format(total_brokerage),"{}"]);
		print(brokrage_list)

	wbr4_franklin_csv_file.close()


finalresult.close()










