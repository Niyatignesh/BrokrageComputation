import csv
import os
#initial inputs
client_name='Sainath pai'  #as per written partner client mapping.csv 
pannumber='AKKPP8206D'
wbr4_camp='30122017223204_79175764R4.csv' #name of sheet at WBR/CAMPS/
birla_sun_life='ARN-66908-TF.csv' #name of sheet at /Birla sun life
SBI_MF='66908_TRA.csv'
UTI_MF='Commision from UTI.csv'
IDFC_MF='ARN-66908_TF_NOV2017.csv'
ICICI_MF='TRAIL FOR ARN-66908.csv'
DSP_Blackrock_MF='TRAIL.csv'
Kotak_MF='ARN-66908 (4).csv'
total_brokerage=0.0
print("our current working directory is :"+os.getcwd())


#searching for amc and folio number in wbr 4/cams csv
client_folio_and_amc=[]
directory_of_wbr4_cams_file=(os.getcwd()+'/WBR/cams/'+wbr4_camp)
wbr4_camp_csv_file=open(directory_of_wbr4_cams_file,mode='r',newline='')
reader_wbr4=csv.reader(wbr4_camp_csv_file)
for row in reader_wbr4:
	if row[22]==pannumber:
#		print(row[0],row[8])
		client_folio_and_amc.append([client_name,pannumber,row[0],row[8]])
#print(client_folio_and_amc)
wbr4_camp_csv_file.close()

total_investment=open('investment of '+client_name+'_.csv',mode='w',newline="")
writer=csv.writer(total_investment)
writer.writerow(["folio_number","client_name","pannumber","company_name","total_brokerage"]);
for row in client_folio_and_amc:
	folio_number=row[2]
	client_name=row[0]
	pannumber=row[1]
	company_name=row[3]
	writer.writerow(["{}".format(folio_number),"{}".format(client_name),"{}".format(pannumber),"{}".format(company_name)]);
total_investment.close()

#brokrage computation
brokrage_list=[]
finalresult=open('brokrage_calculation_'+client_name+'_.csv',mode='w',newline="")
writer=csv.writer(finalresult)
writer.writerow(["folio_number","client_name","pannumber","company_name","total_brokerage"]);
for row in client_folio_and_amc:
	if 'Birla' in row[3]:
		directory_of_birla_sun_life_file=(os.getcwd()+'/Birla Sun life/'+birla_sun_life)
		birla_sun_life_csv_file=open(directory_of_birla_sun_life_file,mode='r',newline='')
		reader_birla=csv.reader(birla_sun_life_csv_file)
		for row in client_folio_and_amc:
			folio_number=row[2]
			client_name=row[0]
			pannumber=row[1]
			company_name=row[3]
			for row in reader_birla:
				if (row[1]==folio_number) or (str(row[2])==client_name):
					print('matched birla')
					total_brokerage=total_brokerage+float(row[11])
				else:
					continue
			if total_brokerage > 0:
				brokrage_list.append([folio_number,client_name,pannumber,company_name,total_brokerage])
				writer.writerow(["{}".format(folio_number),"{}".format(client_name),"{}".format(pannumber),"{}".format(company_name),"{}".format(total_brokerage),"{}"]);
			else:
				continue	
			total_brokerage=0
#			print(brokrage_list)

		birla_sun_life_csv_file.close()

	elif 'Kotak' in row[3]:
		directory_of_Kotak_MF_file=(os.getcwd()+'/Kotak MF/'+Kotak_MF)
		Kotak_MF_csv_file=open(directory_of_Kotak_MF_file,mode='r',newline='')
		reader_Kotak_MF=csv.reader(Kotak_MF_csv_file)
		for row in client_folio_and_amc:
			folio_number=row[2]
			client_name=row[0]
			pannumber=row[1]
			company_name=row[3]
			total_brokerage=0
			for row in reader_Kotak_MF:
				if (row[1]==folio_number) or (str(row[2])==client_name):
					print('matched kotak')
					total_brokerage=total_brokerage+float(row[12])
					print (total_brokerage)
				else:
					continue
			if total_brokerage > 0:
				brokrage_list.append([folio_number,client_name,pannumber,company_name,total_brokerage])
				writer.writerow(["{}".format(folio_number),"{}".format(client_name),"{}".format(pannumber),"{}".format(company_name),"{}".format(total_brokerage),"{}"]);
			else:
				continue	
			total_brokerage=0
#			print(brokrage_list)

		Kotak_MF_csv_file.close()
	elif 'SBI' in row[3]:
		directory_SBI_MF_file=(os.getcwd()+'/SBI MF/'+SBI_MF)
		SBI_MF_csv_file=open(directory_SBI_MF_file,mode='r',newline='')
		reader_SBI_MF=csv.reader(SBI_MF_csv_file)
		for row in client_folio_and_amc:
			folio_number=row[2]
			client_name=row[0]
			pannumber=row[1]
			company_name=row[3]
			total_brokerage=0
			for row in reader_SBI_MF:
				if (row[1]==folio_number) or (str(row[2])==client_name):
					print('matched sbi')
					total_brokerage=total_brokerage+float(row[10])
					print(total_brokerage)
				else:
					continue
			if total_brokerage > 0:
				brokrage_list.append([folio_number,client_name,pannumber,company_name,total_brokerage])
				writer.writerow(["{}".format(folio_number),"{}".format(client_name),"{}".format(pannumber),"{}".format(company_name),"{}".format(total_brokerage),"{}"]);
			else:
				continue	
			total_brokerage=0

		SBI_MF_csv_file.close()
	elif 'DSP' in row[3]:
		directory_of_DSP_Blackrock_MF_file=(os.getcwd()+'/DSP Blackrock MF/'+DSP_Blackrock_MF)
		DSP_Blackrock_MF_csv_file=open(directory_of_DSP_Blackrock_MF_file,mode='r',newline='')
		reader_DSP_Blackrock_MF=csv.reader(DSP_Blackrock_MF_csv_file)
		for row in client_folio_and_amc:
			folio_number=row[2]
			client_name=row[0]
			pannumber=row[1]
			company_name=row[3]
			total_brokerage=0
			#print (folio_number)
			for row in reader_DSP_Blackrock_MF:
				#print(row[2])
				if (row[1]==folio_number) or (str(row[7])==client_name):
					print('matched dsp')
					total_brokerage=total_brokerage+float(row[11])
				else:
					continue
			if total_brokerage > 0:
				brokrage_list.append([folio_number,client_name,pannumber,company_name,total_brokerage])
				writer.writerow(["{}".format(folio_number),"{}".format(client_name),"{}".format(pannumber),"{}".format(company_name),"{}".format(total_brokerage),"{}"]);
			else:
				continue	
			total_brokerage=0

		DSP_Blackrock_MF_csv_file.close()
	elif 'ICICI' in row[3]:
		directory_of_ICICI_MF_file=(os.getcwd()+'/ICICI MF/'+ICICI_MF)
		ICICI_MF_csv_file=open(directory_of_ICICI_MF_file,mode='r',newline='')
		reader_ICICI_MF=csv.reader(ICICI_MF_csv_file)
		for row in client_folio_and_amc:
			folio_number=row[2]
			client_name=row[0]
			pannumber=row[1]
			company_name=row[3]
			total_brokerage=0
			for row in reader_ICICI_MF:
				if (row[0]==folio_number) or (str(row[1])==client_name):
					print('matched icici')
					total_brokerage=total_brokerage+float(row[20])
					print (total_brokerage)
				else:
					continue
			if total_brokerage > 0:
				brokrage_list.append([folio_number,client_name,pannumber,company_name,total_brokerage])
				writer.writerow(["{}".format(folio_number),"{}".format(client_name),"{}".format(pannumber),"{}".format(company_name),"{}".format(total_brokerage),"{}"]);
			else:
				continue	
			total_brokerage=0
#not done for icici
		ICICI_MF_csv_file.close()
	elif 'IDFC' in row[3]:
		directory_of_IDFC_MF_file=(os.getcwd()+'/IDFC MF/'+IDFC_MF)
		IDFC_MF_csv_file=open(directory_of_IDFC_MF_file,mode='r',newline='')
		reader_IDFC_MF=csv.reader(IDFC_MF_csv_file)
		for row in client_folio_and_amc:
			folio_number=row[2]
			client_name=row[0]
			pannumber=row[1]
			company_name=row[3]
			total_brokerage=0
			for row in reader_IDFC_MF:
				if (row[3]==folio_number) or (str(row[4])==client_name):
					print('matched idfc')
					total_brokerage=total_brokerage+float(row[12])
					print (total_brokerage)
				else:
					continue
			if total_brokerage > 0:
				brokrage_list.append([folio_number,client_name,pannumber,company_name,total_brokerage])
				writer.writerow(["{}".format(folio_number),"{}".format(client_name),"{}".format(pannumber),"{}".format(company_name),"{}".format(total_brokerage),"{}"]);
			else:
				continue	
			total_brokerage=0

		IDFC_MF_csv_file.close()
#not done for uti
	elif 'UTI' in row[3]:
		directory_of_UTI_MF_file=(os.getcwd()+'/UTI MF/'+UTI_MF)
		UTI_MF_csv_file=open(directory_of_UTI_MF_file,mode='r',newline='')
		reader_UTI_MF=csv.reader(UTI_MF_csv_file)
		for row in client_folio_and_amc:
			folio_number=row[2]
			client_name=row[0]
			pannumber=row[1]
			company_name=row[3]
			total_brokerage=0
			for row in reader_UTI_MF:
				if (row[1]==folio_number) or (str(row[2])==client_name):
					print('matched uti')
					total_brokerage=total_brokerage+float(row[11])
				else:
					continue
			if total_brokerage > 0:
				brokrage_list.append([folio_number,client_name,pannumber,company_name,total_brokerage])
				writer.writerow(["{}".format(folio_number),"{}".format(client_name),"{}".format(pannumber),"{}".format(company_name),"{}".format(total_brokerage),"{}"]);
			else:
				continue	
			total_brokerage=0

		UTI_MF_csv_file.close()
finalresult.close()










