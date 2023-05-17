
# importing required modules:

import csv

import sys

import os

import argparse

############################################################### FUNCTION DECLARATIONS ####################################################################
#Decraling get_Pre_Shared_Key() function which is used to get a 16 byte random pre shared key (PSK).

def get_Pre_Shared_Key():

  PreSharedkey = os.popen('go run lwm2m-key.go|xargs echo -n').read()

  return PreSharedkey

#Decraling get_Correct_Imei_No() function which is used to get correct 15 Digit IMEI Number with Checksum Digit from 14 digit IMEI input.

def replace(i):
    switcher={
      0:int(0),
      1:int(2),
      2:int(4),
      3:int(6),
      4:int(8),
      5:int(1),
      6:int(3),
      7:int(5),
      8:int(7),
      9:int(9)
    }
    return switcher.get(i,-1)

def get_Correct_Imei_No(imei_input):

# IMEI Checksum Calculation
# To store the respective sums
   odd_sum = 0
   even_sum = 0
   total_sum = 0
   checksum = 0
   imei_number = str(imei_input)
   Odd_strings = []
   Even_strings = []
   print("\n\t The input 14 digit IMEI Number is: "+ imei_number +"\n ")
     
   # Traversing the string
   for i in range(len(imei_number)):
     # adding in particular summation according to value 
     # Replace the digits on even places by the formula: 0=>0, 1=>2, 2=>4, 3=>6, 4=>8, 5=>1, 6=>3, 7=>5, 8=>7, 9=>9 and add them.
     if(i % 2 == 0):
       odd_sum = odd_sum+int(imei_number[i]);
       Odd_strings.append(" " + str(imei_number[i]) +" + ");
     else:
       even_sum = even_sum+ replace(int(imei_number[i]));
       Even_strings.append( " [" + str(imei_number[i]) + "] " + str(replace(int(imei_number[i]))) + " + ")

   print("\n Evens: ")
   print(Even_strings)
   print("\n\t Even Sum is: "+ str(even_sum) +"\n")

   print("\n Odds: ")
   print(Odd_strings)
   print("\n\t Odd Sum is: "+ str(odd_sum) +"\n")

   total_sum = (even_sum + odd_sum)
   print("\n\t Total sum:" + str(even_sum) + " + " + str(odd_sum) + " = " + str(total_sum) +"\n")

   if  (total_sum % 10) == 0:
     checksum = 0
   else:
     if total_sum > 10:
       if int(total_sum/10) > 0:
         checksum = ((int(total_sum/10) +1)*10) - total_sum

   print("\n\t The Calculated IMEI Checksum digit  is: "+ str(checksum) +"\n ")

   correct_imei = str(imei_number) + str(checksum)

   print("\n\t The correct 15 digit IMEI Number is: "+ correct_imei +"\n ")
   return correct_imei

############################################################################################################################################

# Arguments passed:
print("\n\t Executing... Python script> python3 "+ sys.argv[0] +" # use -h option for help \n ");

Output_csv_file = "lwm2m_psks.csv"
Model_Name = "000000"
IMEI_Range = "99001804000000-99001804000999"
Usage = "\n\t Command: >[python3 Script.py [-r IMEI1-IMEI2] [-m Model] [-f inputfile_ImeiList] [-a -o Outputfile.csv]   # if need log postfix: 2>&1 | tee output.log \n"
print(Usage)
# Output .csv file header names
header = ['endpoint-name', 'DTLS-ID(IMEI)', 'DTLS-PSK', 'Model-Name']

ap = argparse.ArgumentParser()
ap.add_argument("-r", "--imei_range", required=False, help="14 digit imei range input in format imeiStart-imeiEnd")
ap.add_argument("-f", "--input_file", required=False, help="file containing imei list")
ap.add_argument("-m", "--model_name", required=False, help="model name [-m is mandatory if any of -r or -f option used]")
ap.add_argument("-a", "--append_output", required=False, action="store_true", help="append to output-file")
ap.add_argument("-o", "--output_file", required=False, help="output .csv file name. -o is mandatory if -a option given")
args = vars(ap.parse_args())

if args["append_output"]:
  if args["output_file"]:
    Output_csv_file = args["output_file"];
  else:
    print("\n\t If you give -a option for appending to output file, you must pass -o [Output .csv file name] argument too \n ");
    print(Usage);
    sys.exit("Invalid Input ! Must Pass [-o <Output .csv file name> ] argument to append")
else:
  if args["output_file"]:
    Output_csv_file = args["output_file"];
  else:
    Output_csv_file = "lwm2m_psks.csv"

if args["model_name"]:
  Model_Name = args["model_name"];
else:
  if args["imei_range"] or args["input_file"]:
    print(Usage);
    sys.exit("Invalid Input ! Must Pass -m Model_Name  argument if range or inputfile option used")

if args["imei_range"]:
  IMEI_Range = args["imei_range"];
  IMEI_Endpoints = IMEI_Range.split('-', 1);
  IMEI_Endpoints = [x.strip(' ') for x in IMEI_Endpoints];
  for s in IMEI_Endpoints:
    l = len(str(s));
    # If length is not more than 14 then IMEI number is Invalid
    if l < 14:
      print("\n\t Enter at least 14 digit IMEI in the range. Invalid End points Range IMEI: "+ str(s) +"\n ");
      sys.exit("Invalid IMEI End points in range, passed number's length less than 14");

  imei_Lower = IMEI_Endpoints[0];
  imei_Upper = IMEI_Endpoints[1];

  if int(IMEI_Endpoints[1]) > int(IMEI_Endpoints[0]):
    print("\n\t  Valid Range Input.");
  else:
    imei_Lower = IMEI_Endpoints[1];
    imei_Upper = IMEI_Endpoints[0];

  print("\n\t Preparing CSV output From Start Range IMEI: "+ imei_Lower +" to End Range IMEI: " + imei_Upper + "\n");
  print("\n\t Writing to output csv file...wait... \n ");

  if os.path.isfile(Output_csv_file):
    os.remove(Output_csv_file)

  with open(Output_csv_file, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f, delimiter=',');
    # write the header
    writer.writerow(header);
    print("\n endpoint-name, DTLS-ID(IMEI),  DTLS-PSK, Model-Name \n");
    for imei in range(int(imei_Lower), int(imei_Upper)+1):
      correct_imei = get_Correct_Imei_No(imei);
      # write data rows
      writer.writerow([str("urn:imei:")+str(correct_imei), str(correct_imei), get_Pre_Shared_Key(), str(Model_Name)]);
      print("\n"+ str("urn:imei:") + str(correct_imei) +", " + str(correct_imei) + ", " + get_Pre_Shared_Key() + ", " + str(Model_Name) +" \n")

if args["input_file"]:
  with open(args["input_file"]) as f:
    content_list = f.readlines();
    # remove new line characters
    content_list = [x.strip() for x in content_list];
    print("\n\t Contents of Input File " + str(args["input_file"]) + ": \n");
    print(content_list);
    add_header = 1;
    if os.path.isfile(Output_csv_file):
      if args["append_output"]:
        add_header = 0;
      else:
        os.remove(Output_csv_file);
      
    with open(Output_csv_file, 'a+', encoding='UTF8', newline='') as f:
      writer = csv.writer(f, delimiter=',');
      # write the header if file newly created
      if add_header:
        writer.writerow(header);
      for imei in content_list:
        if len(str(imei)) < 15:
          print("\n\t Invalid IMEI: less than 15 digits in the input file "+ str(args["input_file"]) +" the invalid IMEI: " + str(imei) + "\n");
        writer.writerow([str("urn:imei:")+str(imei), str(imei), get_Pre_Shared_Key(), str(Model_Name)]);
        print("\n"+ str("urn:imei:") + str(imei) +", " + str(imei) + ", " + get_Pre_Shared_Key() + ", " + str(Model_Name) +" \n")

