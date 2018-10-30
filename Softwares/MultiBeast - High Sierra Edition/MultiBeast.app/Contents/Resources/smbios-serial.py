#!/usr/bin/python
# Copyright (C) tonymacx86 LLC

import sys
import datetime
from random import choice
from random import randint

alphanumerics = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
				 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
				 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
				 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

weeks = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
		 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M',
		 'N', 'P', 'Q', 'R', 'T', 'V', 'W', 'X']

		 	  # (1, 26) (27, 52)
years = {"2007" : ['T', 'V'],
		 "2008" : ['W', 'X'],
		 "2009" : ['Y', 'Z'],
		 "2010" : ['C', 'D'],
		 "2011" : ['F', 'G'],
		 "2012" : ['H', 'J'],
		 "2013" : ['K', 'L'],
		 "2014" : ['M', 'N'],
		 "2015" : ['P', 'Q'],
		 "2016" : ['R', 'S'],
		 "2017" : ['T', 'V']}

def old_serial(start_string, start_date, end_date, end_string):
	# manufacturing location
	serial = start_string

	# pick a random manufacture date between the start and end
	manufacture_date = datetime.date.fromordinal(randint(datetime.date.toordinal(start_date), datetime.date.toordinal(end_date)))

	# year of manufacture
	serial += str(manufacture_date.year)[-1]
	
	# week of manufacture
	serial += str(manufacture_date.isocalendar()[1]).zfill(2)
	
	# unique identifier
	serial += choice(alphanumerics)
	serial += choice(alphanumerics)
	serial += choice(alphanumerics)
	
	# model number
	serial += end_string
	
	return serial

def new_serial(start_string, start_date, end_date, end_string):
	# manufacturing location
	serial = start_string

	# pick a random manufacture date between the start ane end
	manufacture_date = datetime.date.fromordinal(randint(datetime.date.toordinal(start_date), datetime.date.toordinal(end_date)))

	# year and week of manufacture
	week = manufacture_date.isocalendar()[1]
	if (week <= 26):
		serial += years[str(manufacture_date.year)][0]
		serial += weeks[week-1]
	else:
		serial += years[str(manufacture_date.year)][1]
		serial += weeks[week-26-1]

	# unique identifier
	serial += choice(alphanumerics)
	serial += choice(alphanumerics)
	serial += choice(alphanumerics)

	# model number
	serial += end_string

	return serial

model = sys.argv[1]
if model == "iMac11,1":
	print(old_serial("QP", datetime.date(2009, 6, 20), datetime.date(2010, 7, 27), "5RU")) # OLD - QP******5RU - 6/20/09 to 7/27/10
elif model == "iMac11,2":
	print(old_serial("CK", datetime.date(2010, 7, 27), datetime.date(2011, 5, 3), "DAS")) # OLD - CK******DAS - 7/27/10 to 5/3/11
elif model == "iMac11,3":
	print(old_serial("CK", datetime.date(2010, 7, 27), datetime.date(2011, 5, 3), "DNP")) # OLD - CK******DNP - 7/27/10 to 5/3/11
elif model == "iMac12,1":
	print(new_serial("C02", datetime.date(2011, 5, 3), datetime.date(2012, 10, 23), "DHJF")) # NEW - C02*****DHJF - 5/3/11 to 10/23/12
elif model == "iMac12,2":
	print(new_serial("C02", datetime.date(2011, 5, 3), datetime.date(2012, 10, 23), "DHJP")) # NEW - C02*****DHJP - 5/3/11 to 10/23/12
elif model == "iMac13,1":
	print(new_serial("C02", datetime.date(2012, 10, 23), datetime.date.today(), "DNCR")) # NEW - C02*****DNCR - 10/23/12 to 9/24/13
elif model == "iMac13,2":
	print(new_serial("C02", datetime.date(2012, 10, 23), datetime.date.today(), "F29N")) # NEW - C02*****F29N - 10/23/12 to 9/24/13
elif model == "iMac14,1":
	print(new_serial("C02", datetime.date(2013, 9, 24), datetime.date(2015, 5, 19), "F8J2")) # NEW - C02*****F8J2 - 9/24/13 to 5/19/15
elif model == "iMac14,2":
	print(new_serial("C02", datetime.date(2013, 9, 24), datetime.date(2015, 5, 19), "FLHH")) # NEW - C02*****FLHH - 9/24/13 to 5/19/15
elif model == "iMac15,1":
	print(new_serial("C02", datetime.date(2014, 10, 16), datetime.date.today(), "FY11")) # NEW - C02*****F8JC - 10/16/14 to 6/5/17
elif model == "iMac16,2":
    print(new_serial("C02", datetime.date(2015, 10, 13), datetime.date.today(), "GG78")) # NEW - C02*****F8JC - 10/13/15 to 6/5/17
elif model == "iMac17,1":
    print(new_serial("C02", datetime.date(2015, 10, 13), datetime.date.today(), "GG7L")) # NEW - C02*****F8JC - 10/13/15 to 6/5/17
elif model == "iMac18,2":
    print(new_serial("C02", datetime.date(2017, 6, 5), datetime.date.today(), "J1G5")) # NEW - C02*****J1G5 - 6/05/17 to N/A
elif model == "iMac18,3":
    print(new_serial("C02", datetime.date(2017, 6, 5), datetime.date.today(), "J1GJ")) # NEW - C02*****J1GJ - 6/05/17 to N/A
elif model == "MacBookPro6,1":
	print(new_serial("C02", datetime.date(2010, 4, 13), datetime.date(2011, 2, 24), "DC79")) # NEW - C02*****DC79 - 4/13/10 to 2/24/11
elif model == "MacBookPro6,2":
	print(old_serial("CK", datetime.date(2010, 4, 13), datetime.date(2011, 2, 24), "AGW")) # OLD - CK******AGW - 4/13/10 to 2/24/11
elif model == "MacBookPro8,1":
	print(new_serial("C02", datetime.date(2011, 2, 24), datetime.date(2012, 6, 11), "DH2G")) # NEW - C02*****DH2G - 2/24/11 to 6/11/12
elif model == "MacBookPro8,2":
	print(new_serial("C02", datetime.date(2011, 2, 24), datetime.date(2011, 10, 24), "DF8X")) # NEW - C02*****DF8X - 2/24/11 to 10/24/11
elif model == "MacBookPro8,3":
	print(new_serial("C02", datetime.date(2011, 2, 24), datetime.date(2011, 10, 24), "DF92")) # NEW - C02*****DF92 - 2/24/11 to 10/24/11
elif model == "MacBookPro9,1":
	print(new_serial("C02", datetime.date(2012, 6, 11), datetime.date(2013, 10, 22), "F1G4")) # NEW - C02*****F1G4 - 6/11/12 to 10/22/13
elif model == "MacBookPro9,2":
	print(new_serial("C02", datetime.date(2012, 6, 11), datetime.date(2013, 10, 22), "DTY3")) # NEW - C02*****DTY3 - 6/11/12 to 10/22/13
elif model == "MacBookPro10,1":
	print(new_serial("C02", datetime.date(2012, 6, 11), datetime.date(2013, 2, 13), "DKQ1")) # NEW - C02*****DKQ1 - 6/11/12 to 2/13/13
elif model == "MacBookPro11,1":
	print(new_serial("C02", datetime.date(2013, 10, 22), datetime.date(2014, 7, 29), "FGYY")) # NEW - C02*****FGYY - 10/22/13 to 7/29/14
elif model == "MacBookPro11,2":
	print(new_serial("C02", datetime.date(2013, 10, 22), datetime.date(2014, 7, 29), "FD56")) # NEW - C02*****FD56 - 10/22/13 to 7/29/14
elif model == "MacBookPro12,1":
	print(new_serial("C02", datetime.date(2015, 3, 9), datetime.date.today(), "FD56")) # NEW - C02*****FD56 - 3/9/15 to N/A
elif model == "Macmini5,1":
	print(new_serial("C02", datetime.date(2011, 7, 20), datetime.date(2012, 10, 23), "DJD0")) # NEW - C07*****DJD0 - 7/20/11 to 10/23/12
elif model == "Macmini6,1":
	print(new_serial("C02", datetime.date(2012, 10, 23), datetime.date.today(), "DWYL")) # NEW - C02*****DWYL - 10/23/12 to N/A
elif model == "Macmini6,2":
	print(new_serial("C02", datetime.date(2012, 10, 23), datetime.date.today(), "DWYN")) # NEW - C02*****DWYN - 10/23/12 to N/A
elif model == "MacPro3,1":
	print(old_serial("G8", datetime.date(2008, 1, 8), datetime.date(2009, 3, 3), "5J4")) # OLD - G8******5J4 - 1/8/08 to 3/3/09
elif model == "MacPro4,1":
	print(old_serial("FC", datetime.date(2009, 3, 3), datetime.date(2010, 7, 27), "4PC")) # OLD - FC******4PC - 3/3/09 to 7/27/10
elif model == "MacPro5,1":
	print(old_serial("G8", datetime.date(2010, 7, 27), datetime.date.today(), "GWR")) # OLD - G8******GWR - 7/27/10 to N/A
elif model == "MacPro6,1":
	print(new_serial("F5K", datetime.date(2013, 10, 22), datetime.date.today(), "F694")) # NEW - F5K*****F694 - 10/22/13 to N/A
elif model == "MacBookAir5,2":
	print(new_serial("C02", datetime.date(2012, 6, 11), datetime.date(2013, 6, 10), "DRVC")) # NEW - C02*****DRVC - 6/11/12 to 6/10/13
elif model == "MacBookAir6,2":
	print(new_serial("C02", datetime.date(2013, 6, 10), datetime.date(2014, 4, 29), "FAGW")) # NEW - C02*****FAGW - 6/10/13 to 4/29/14