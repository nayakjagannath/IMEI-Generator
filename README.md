# IMEI-Generator
PyGolang IMEI List Generator for Custom Mobile Devices.

This python Golang program is made for generating IMEI numbers for LwM2M connected devices to get configured with IMEI numbers. from 14 digit input IMEI number to 15 digit IMEI number it can generate. It takes on PSK key to generate IMEI numbers with checksum calculations. 

Command: >[python3 Script.py [-r IMEI1-IMEI2] [-m Model] [-f inputfile_ImeiList] [-a -o Outputfile.csv]   # if need log postfix: 2>&1 | tee output.log 

Sample Output:

	 Executing... Python script: IMEI_List_Generator.py
 

	 Arguments passed: 99001804000000 99001804000999 MD2000 
	  Valid Range Input.

	 Preparing CSV output From Start Range IMEI: 99001804000000 to End Range IMEI: 99001804000999


	 Writing to output csv file...wait... 
 

 endpoint-name, DTLS-ID\(IMEI\),  DTLS-PSK, Model-Name 


	 The input 14 digit IMEI Number is: 99001804000000
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:24 + 10 = 34


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000006
 

urn:imei:990018040000006, 990018040000006, ec0669c930e22555cd49d28605aad822
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000001
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:26 + 10 = 36


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000014
 

urn:imei:990018040000014, 990018040000014, bee1d9c928e0d53c9c5b5dc227c4520d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000002
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:28 + 10 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000022
 

urn:imei:990018040000022, 990018040000022, c6fb6136edc4fe7dd698a6b5445b9a0e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000003
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:30 + 10 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000030
 

urn:imei:990018040000030, 990018040000030, 3aa0fd8c9ec2464e46492c5883dac41f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000004
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:32 + 10 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000048
 

urn:imei:990018040000048, 990018040000048, 3ba12cf0fdd9df7d3011f1ee323598ee
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000005
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:25 + 10 = 35


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000055
 

urn:imei:990018040000055, 990018040000055, c5549894e1a34f8354ed8316c69d08ff
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000006
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:27 + 10 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000063
 

urn:imei:990018040000063, 990018040000063, d4cf50e615ba242fbbf9211d6b7926bc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000007
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:29 + 10 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000071
 

urn:imei:990018040000071, 990018040000071, fee47514212feee7febd86569c1c5747
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000008
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:31 + 10 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000089
 

urn:imei:990018040000089, 990018040000089, 34ec7e6c8b86bf26f5ed22ea28a32999
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000009
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000097
 

urn:imei:990018040000097, 990018040000097, 0e29584a6e1c101fd1fd918b8eb9f1cb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000010
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:24 + 11 = 35


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000105
 

urn:imei:990018040000105, 990018040000105, 42fce64b451944a9b63127e18956b02c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000011
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:26 + 11 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000113
 

urn:imei:990018040000113, 990018040000113, a4555242fc6228ff2e82fcebf76f9b91
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000012
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:28 + 11 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000121
 

urn:imei:990018040000121, 990018040000121, f5d24de5f65c6421d58684aaf3121afe
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000013
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:30 + 11 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000139
 

urn:imei:990018040000139, 990018040000139, 9f8ecf9b2b7efa3792443bc0fccefdc5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000014
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:32 + 11 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000147
 

urn:imei:990018040000147, 990018040000147, c290c50810e75b95da6e01710c116296
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000015
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:25 + 11 = 36


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000154
 

urn:imei:990018040000154, 990018040000154, a5fece64380f92bb965e4c489476c221
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000016
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:27 + 11 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000162
 

urn:imei:990018040000162, 990018040000162, 90f522e5645302b511727bd14e978b75
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000017
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:29 + 11 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000170
 

urn:imei:990018040000170, 990018040000170, b463f41f1dc881381fd7cdbbc41525a8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000018
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:31 + 11 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000188
 

urn:imei:990018040000188, 990018040000188, 23f3651dfc1847dc303cf031312f954a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000019
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000196
 

urn:imei:990018040000196, 990018040000196, 375dc924974f2317bad1ec3c4330b225
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000020
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:24 + 12 = 36


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000204
 

urn:imei:990018040000204, 990018040000204, c7b0997346519762727f018af8a4d777
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000021
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:26 + 12 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000212
 

urn:imei:990018040000212, 990018040000212, 55718876498943da619c4f7a2c11dce2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000022
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:28 + 12 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000220
 

urn:imei:990018040000220, 990018040000220, 185a59a5f3e45560459f1e84f5d819c1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000023
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:30 + 12 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000238
 

urn:imei:990018040000238, 990018040000238, 50f03383869e61f198358bcc58174db1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000024
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:32 + 12 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000246
 

urn:imei:990018040000246, 990018040000246, 2ff397fcfd17f9ec1f20cff5b1bf68c8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000025
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:25 + 12 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000253
 

urn:imei:990018040000253, 990018040000253, 0e02a3f15a20ac1b23220ab688d29d33
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000026
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:27 + 12 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000261
 

urn:imei:990018040000261, 990018040000261, 6f5ff57558bcfb280dfdeec68b34b03e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000027
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:29 + 12 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000279
 

urn:imei:990018040000279, 990018040000279, c701a6caf14480887c2a03cc38d5fddb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000028
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:31 + 12 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000287
 

urn:imei:990018040000287, 990018040000287, 8c9b3456fbf8e7fd94b8f52cf874c49d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000029
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000295
 

urn:imei:990018040000295, 990018040000295, d1e34c18505f4a461808527106c23b2c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000030
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:24 + 13 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000303
 

urn:imei:990018040000303, 990018040000303, 06eebbd3e69b31f2981d25bb681074b5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000031
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:26 + 13 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000311
 

urn:imei:990018040000311, 990018040000311, 6e67302400245e655f06f6d4c1078f8f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000032
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:28 + 13 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000329
 

urn:imei:990018040000329, 990018040000329, 9a32dd4cb3b1ea5ca0b0a06ca15aaa3d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000033
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:30 + 13 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000337
 

urn:imei:990018040000337, 990018040000337, caa6e87f0851bc0a8ba61f3324565e2b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000034
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:32 + 13 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000345
 

urn:imei:990018040000345, 990018040000345, c522eb40eef04dd6edf5e4d36b0f327c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000035
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:25 + 13 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000352
 

urn:imei:990018040000352, 990018040000352, 6d8365333a495588280bb73107182032
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000036
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:27 + 13 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000360
 

urn:imei:990018040000360, 990018040000360, cdac2450cbe05d4cc4b610f24b581e05
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000037
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:29 + 13 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000378
 

urn:imei:990018040000378, 990018040000378, 7ff4afa4678b7968eb2bf8e0b9e1be33
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000038
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:31 + 13 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000386
 

urn:imei:990018040000386, 990018040000386, 6fac7d9d75c22947242a04b7489cd874
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000039
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000394
 

urn:imei:990018040000394, 990018040000394, 5be0520bccdbf0166c0d80ef281a236b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000040
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:24 + 14 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000402
 

urn:imei:990018040000402, 990018040000402, d0219ef9ea213aac1c17088bbefb1b34
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000041
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:26 + 14 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000410
 

urn:imei:990018040000410, 990018040000410, b29bb4e588c6e75b0d297f8110acbc4e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000042
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:28 + 14 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000428
 

urn:imei:990018040000428, 990018040000428, 3e79d6e285d388b93b6fb9140e154255
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000043
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:30 + 14 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000436
 

urn:imei:990018040000436, 990018040000436, b13d5964aae1fc82b48c728812120b1d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000044
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:32 + 14 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000444
 

urn:imei:990018040000444, 990018040000444, 8ee6955f92ce7a38e24f02ddec4607c0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000045
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:25 + 14 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000451
 

urn:imei:990018040000451, 990018040000451, fd6543b966d2201ab1cde685d921cef3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000046
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:27 + 14 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000469
 

urn:imei:990018040000469, 990018040000469, 5595d7be73aeb582e84b59d1384f347c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000047
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:29 + 14 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000477
 

urn:imei:990018040000477, 990018040000477, ebaaaf055ccd0e46734ad9915392c33c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000048
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:31 + 14 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000485
 

urn:imei:990018040000485, 990018040000485, 11ae22ffb1609f659166ad4d208dd891
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000049
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000493
 

urn:imei:990018040000493, 990018040000493, a6cb47a6559f84e450489def56f7363c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000050
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:24 + 15 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000501
 

urn:imei:990018040000501, 990018040000501, cad16ba74d6e3f4800ef52a00ec3e724
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000051
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:26 + 15 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000519
 

urn:imei:990018040000519, 990018040000519, 5acb0d744ee503bb725dbd7d2106db76
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000052
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:28 + 15 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000527
 

urn:imei:990018040000527, 990018040000527, 80d79e56f866b32188160c9471f0541e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000053
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:30 + 15 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000535
 

urn:imei:990018040000535, 990018040000535, 0c41f80416639d0bb1fd7639882f6040
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000054
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:32 + 15 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000543
 

urn:imei:990018040000543, 990018040000543, 602c7dd970f53491874dae0455e3648d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000055
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:25 + 15 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000550
 

urn:imei:990018040000550, 990018040000550, ae7a7108a12d2f5fe8c2b339e558b3bf
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000056
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:27 + 15 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000568
 

urn:imei:990018040000568, 990018040000568, de07ec8ad118d4fac565df2fe30c6406
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000057
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:29 + 15 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000576
 

urn:imei:990018040000576, 990018040000576, 9dded8442d3206042b03baf7f3a58eff
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000058
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:31 + 15 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000584
 

urn:imei:990018040000584, 990018040000584, dbe706323a4533db697ddd40524b126a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000059
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000592
 

urn:imei:990018040000592, 990018040000592, 12e4f3cdb6f339e1034fd7732ba29979
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000060
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:24 + 16 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000600
 

urn:imei:990018040000600, 990018040000600, d0fa3010ce56c9e9aaa5a7fbad8eeb02
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000061
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:26 + 16 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000618
 

urn:imei:990018040000618, 990018040000618, 5d944aa60400a4423a60c98fe7bc34b7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000062
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:28 + 16 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000626
 

urn:imei:990018040000626, 990018040000626, d37a2e5efebd14293e620c5d50067a2a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000063
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:30 + 16 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000634
 

urn:imei:990018040000634, 990018040000634, 2dc0d5e0c75820c8699fbba0c640c1b0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000064
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:32 + 16 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000642
 

urn:imei:990018040000642, 990018040000642, 0737c5a1f73aef95e1a2ccb38319018c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000065
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:25 + 16 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000659
 

urn:imei:990018040000659, 990018040000659, 9f8e9843368e40fd208b084e38dbf647
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000066
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:27 + 16 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000667
 

urn:imei:990018040000667, 990018040000667, 0d49245f704ddfbad022e1071ff66488
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000067
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:29 + 16 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000675
 

urn:imei:990018040000675, 990018040000675, 5211be5110203580c8aee6e15c35b5bc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000068
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:31 + 16 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000683
 

urn:imei:990018040000683, 990018040000683, ce95b6edce3c11301ce1e7295b25693e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000069
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000691
 

urn:imei:990018040000691, 990018040000691, 55e6268c9e683e1552bda4be182e71f8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000070
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:24 + 17 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000709
 

urn:imei:990018040000709, 990018040000709, 01f70691cd16cb2b705e90fe2989fb6e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000071
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:26 + 17 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000717
 

urn:imei:990018040000717, 990018040000717, 687fe9a3659d04a71e688d7c18ccd696
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000072
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:28 + 17 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000725
 

urn:imei:990018040000725, 990018040000725, dc277e6e431b3859d6f803355f8fcdd9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000073
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:30 + 17 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000733
 

urn:imei:990018040000733, 990018040000733, a128248d75d1d7f2fb9e4921b82dfa1b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000074
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:32 + 17 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000741
 

urn:imei:990018040000741, 990018040000741, 1bcaac95c022c9e07c79b66a93633456
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000075
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:25 + 17 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000758
 

urn:imei:990018040000758, 990018040000758, 17fd949d5a176dd07e8072c34a9ec2e1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000076
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:27 + 17 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000766
 

urn:imei:990018040000766, 990018040000766, 4854cdf68fbd00819ee066a1d0790394
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000077
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:29 + 17 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000774
 

urn:imei:990018040000774, 990018040000774, 5f0f2f6badc00d3044cf19560d2eeb5b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000078
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:31 + 17 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000782
 

urn:imei:990018040000782, 990018040000782, 3dc696a850445386ae17799e90479ffe
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000079
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000790
 

urn:imei:990018040000790, 990018040000790, 84b105d3dc8152ea515ba9c8d3101eb0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000080
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:24 + 18 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000808
 

urn:imei:990018040000808, 990018040000808, f5718a315a5ffa179ef442a0009cf013
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000081
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:26 + 18 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000816
 

urn:imei:990018040000816, 990018040000816, be0e40255d09b97b37e4841868995684
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000082
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:28 + 18 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000824
 

urn:imei:990018040000824, 990018040000824, 43edcd1690b4b5600485876626a845cd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000083
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:30 + 18 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000832
 

urn:imei:990018040000832, 990018040000832, 56fc9f55aa392914b7ccfd3fe00b05c5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000084
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:32 + 18 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000840
 

urn:imei:990018040000840, 990018040000840, a7ca0434c3ec4558d4846d9a6fb39a03
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000085
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:25 + 18 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000857
 

urn:imei:990018040000857, 990018040000857, 7e3873005a15a37a2c02f1ab6a002be6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000086
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:27 + 18 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000865
 

urn:imei:990018040000865, 990018040000865, 0dc3cd9b627ddd40e465f8b325263bb5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000087
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:29 + 18 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000873
 

urn:imei:990018040000873, 990018040000873, 6fe15d193ff3eecf751c7a13808ad2ce
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000088
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:31 + 18 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000881
 

urn:imei:990018040000881, 990018040000881, 0021a390ab6ecfa8c85de6554096d365
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000089
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000899
 

urn:imei:990018040000899, 990018040000899, af0c71190898c79813bed701944e9274
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000090
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [0] 0 + ']

	 Even Sum is: 24


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:24 + 19 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040000907
 

urn:imei:990018040000907, 990018040000907, 158ecaa6207cdad9b70046443a7cd389
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000091
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [1] 2 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:26 + 19 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040000915
 

urn:imei:990018040000915, 990018040000915, f0193954b046fa62137f6129e041c78a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000092
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [2] 4 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:28 + 19 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040000923
 

urn:imei:990018040000923, 990018040000923, af73ca271a9dde817e9bfb2993f6cc48
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000093
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [3] 6 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:30 + 19 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040000931
 

urn:imei:990018040000931, 990018040000931, 89f1d6c2b18308456196eb16b45b3edd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000094
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [4] 8 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:32 + 19 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040000949
 

urn:imei:990018040000949, 990018040000949, 615346712e366f934b573f58c0689d85
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000095
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [5] 1 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:25 + 19 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040000956
 

urn:imei:990018040000956, 990018040000956, 7f8b2473a0a73d9d88726446ef595aa9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000096
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [6] 3 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:27 + 19 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040000964
 

urn:imei:990018040000964, 990018040000964, 21651cb8ebfce52d18db9207c6059b72
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000097
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [7] 5 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:29 + 19 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040000972
 

urn:imei:990018040000972, 990018040000972, 9dca7d95e0cb7065fdb6464a0c8dcce9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000098
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [8] 7 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:31 + 19 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040000980
 

urn:imei:990018040000980, 990018040000980, a1c4845a222ea98698661b243278cac9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000099
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [0] 0 + ', ' [9] 9 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040000998
 

urn:imei:990018040000998, 990018040000998, 76e269f402396ee3d068a10d2fabe15d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000100
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:26 + 10 = 36


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001004
 

urn:imei:990018040001004, 990018040001004, eb118ea4c52aeabd449492429da4548c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000101
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:28 + 10 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001012
 

urn:imei:990018040001012, 990018040001012, 01e7f017322a63d4b9fafcfebf4123c6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000102
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:30 + 10 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001020
 

urn:imei:990018040001020, 990018040001020, 1e0dc23e2f5333279d386235ba8794df
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000103
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:32 + 10 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001038
 

urn:imei:990018040001038, 990018040001038, 5a532b6cd4464a156d4864bc2d937a55
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000104
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:34 + 10 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001046
 

urn:imei:990018040001046, 990018040001046, b10a6d945d7272a4060120a5ad1773e4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000105
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:27 + 10 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001053
 

urn:imei:990018040001053, 990018040001053, b42e0531a3f7bda0c9e30b4b570d6ca2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000106
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:29 + 10 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001061
 

urn:imei:990018040001061, 990018040001061, 96894f0ff6f5dbd4f018ae6e714f2e17
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000107
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:31 + 10 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001079
 

urn:imei:990018040001079, 990018040001079, f153a9d0d22e47639e1d63df3723187e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000108
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001087
 

urn:imei:990018040001087, 990018040001087, 55ea414c9923f52457e3442ac3dda6c4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000109
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:35 + 10 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001095
 

urn:imei:990018040001095, 990018040001095, b31030c944b35aac2581237ac9e3fcd8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000110
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:26 + 11 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001103
 

urn:imei:990018040001103, 990018040001103, e89a663516054b255c791e8780aaa279
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000111
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:28 + 11 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001111
 

urn:imei:990018040001111, 990018040001111, aa7d01ad8fb643c21967f5a8fecdc066
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000112
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:30 + 11 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001129
 

urn:imei:990018040001129, 990018040001129, 7d4602e7b525b84b7c7305389a85d80c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000113
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:32 + 11 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001137
 

urn:imei:990018040001137, 990018040001137, 57222b13765291f6bee9a7b1179f0fd6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000114
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:34 + 11 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001145
 

urn:imei:990018040001145, 990018040001145, a93e817391993f89a13ba1835d766e73
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000115
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:27 + 11 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001152
 

urn:imei:990018040001152, 990018040001152, 3f9059c52c480512f714229f081cf7cb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000116
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:29 + 11 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001160
 

urn:imei:990018040001160, 990018040001160, bff1b19bb3cc77c6949991c3da875d3f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000117
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:31 + 11 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001178
 

urn:imei:990018040001178, 990018040001178, 4fecc18373f2a34c8ae0ef51d6626f6d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000118
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001186
 

urn:imei:990018040001186, 990018040001186, 16c1415b84f4d82726081a718aea968a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000119
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:35 + 11 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001194
 

urn:imei:990018040001194, 990018040001194, 74d149a001633df35a0c6900ef9bf922
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000120
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:26 + 12 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001202
 

urn:imei:990018040001202, 990018040001202, 8c18539d85246269b3e473846a16de3e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000121
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:28 + 12 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001210
 

urn:imei:990018040001210, 990018040001210, e2759db8a649de89028d48d66d1969eb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000122
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:30 + 12 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001228
 

urn:imei:990018040001228, 990018040001228, ba01f16b9b7b0a3e645b089601ff5380
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000123
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:32 + 12 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001236
 

urn:imei:990018040001236, 990018040001236, f003a74cc9dc43b6ee4db854f997b67c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000124
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:34 + 12 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001244
 

urn:imei:990018040001244, 990018040001244, 4b8087379220d1561fa21ccdbcffc1c1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000125
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:27 + 12 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001251
 

urn:imei:990018040001251, 990018040001251, 9c25a517269b9935e42577f911e6dc45
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000126
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:29 + 12 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001269
 

urn:imei:990018040001269, 990018040001269, 4f68c5f688bcd4261587b33714b0ba76
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000127
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:31 + 12 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001277
 

urn:imei:990018040001277, 990018040001277, 257eb73d073baed6f61ff4b8b7f6f476
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000128
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001285
 

urn:imei:990018040001285, 990018040001285, 2459b7ada719d12411e7bee78bf6c997
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000129
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:35 + 12 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001293
 

urn:imei:990018040001293, 990018040001293, f722bcaee0bf9dfe5598a63c632f3613
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000130
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:26 + 13 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001301
 

urn:imei:990018040001301, 990018040001301, 702bddcebadcc0e79032a85bb14331fe
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000131
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:28 + 13 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001319
 

urn:imei:990018040001319, 990018040001319, 6676e0c29f83eb81573803a2c1e70837
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000132
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:30 + 13 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001327
 

urn:imei:990018040001327, 990018040001327, 553f303d354ffb7df4f1a90f66a60b79
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000133
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:32 + 13 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001335
 

urn:imei:990018040001335, 990018040001335, 472ff2d81374ed71d54cef2f39e9ab5e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000134
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:34 + 13 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001343
 

urn:imei:990018040001343, 990018040001343, 7a706f7b717a6d014306dcdbf3b510b7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000135
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:27 + 13 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001350
 

urn:imei:990018040001350, 990018040001350, fdb2b1755780fa19697d4e756669df77
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000136
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:29 + 13 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001368
 

urn:imei:990018040001368, 990018040001368, 0fd5ccb8a45c21fab6926cd463da5a9a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000137
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:31 + 13 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001376
 

urn:imei:990018040001376, 990018040001376, 67832908d53bf228ce6c059a582e051d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000138
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001384
 

urn:imei:990018040001384, 990018040001384, fd296468407a17bc5820559d05b3fca7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000139
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:35 + 13 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001392
 

urn:imei:990018040001392, 990018040001392, 9aace2e4e29ce842a2ed602086ba658b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000140
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:26 + 14 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001400
 

urn:imei:990018040001400, 990018040001400, 878a6dbfa26dc189651b97ac9d91695b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000141
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:28 + 14 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001418
 

urn:imei:990018040001418, 990018040001418, 8fcd28c25116ebca755102ef4fbb017c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000142
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:30 + 14 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001426
 

urn:imei:990018040001426, 990018040001426, 7ab96c554a7fc0b4054b62ced35d71f6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000143
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:32 + 14 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001434
 

urn:imei:990018040001434, 990018040001434, bedb483e7478df52d20281b8780adac9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000144
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:34 + 14 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001442
 

urn:imei:990018040001442, 990018040001442, 47e36cf9eb878f898e5dbe3335794744
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000145
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:27 + 14 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001459
 

urn:imei:990018040001459, 990018040001459, 5b20271b4acb43fe657fcc37ddd74426
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000146
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:29 + 14 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001467
 

urn:imei:990018040001467, 990018040001467, c3bc5e34172ed1ffc189a764e3b41952
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000147
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:31 + 14 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001475
 

urn:imei:990018040001475, 990018040001475, 75b455618a2b113a75c68e610ca29723
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000148
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001483
 

urn:imei:990018040001483, 990018040001483, e7d20fe25e04ed8dc01bd258b54710a8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000149
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:35 + 14 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001491
 

urn:imei:990018040001491, 990018040001491, c5ef2132f81f855bfcb07045e16c5814
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000150
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:26 + 15 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001509
 

urn:imei:990018040001509, 990018040001509, 8f2fe7527c5e1a34999c84c07b6a54e4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000151
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:28 + 15 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001517
 

urn:imei:990018040001517, 990018040001517, 0bb82ce4248a1c6b2336577f3ae68da1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000152
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:30 + 15 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001525
 

urn:imei:990018040001525, 990018040001525, b96e407bff29daa1017b822bdc3b1824
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000153
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:32 + 15 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001533
 

urn:imei:990018040001533, 990018040001533, 4a29a91bb3d9e5d4ad64149d19c8bef7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000154
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:34 + 15 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001541
 

urn:imei:990018040001541, 990018040001541, 68197329a3a1cf490d6e56b490b343d1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000155
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:27 + 15 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001558
 

urn:imei:990018040001558, 990018040001558, d4576028ca5293e3be7b160ff5b73c46
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000156
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:29 + 15 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001566
 

urn:imei:990018040001566, 990018040001566, 247dfff9ecc3b96415f64f37e88efb04
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000157
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:31 + 15 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001574
 

urn:imei:990018040001574, 990018040001574, d0f3b0c071fa79373ffc0d14a0c54545
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000158
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001582
 

urn:imei:990018040001582, 990018040001582, 3b0c4f13716e578ab4e210a71bf33b41
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000159
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:35 + 15 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001590
 

urn:imei:990018040001590, 990018040001590, e3ae56dc100b34651be72b282bd8f9d1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000160
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:26 + 16 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001608
 

urn:imei:990018040001608, 990018040001608, 764534449e7b15fda278774b4127b0b0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000161
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:28 + 16 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001616
 

urn:imei:990018040001616, 990018040001616, d41455bfceb4c75b96ce75a079bb63a7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000162
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:30 + 16 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001624
 

urn:imei:990018040001624, 990018040001624, ba6a066f768aa38592e22d68926a1ed8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000163
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:32 + 16 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001632
 

urn:imei:990018040001632, 990018040001632, 9d9a3e0e568ad017f35611738290145f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000164
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:34 + 16 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001640
 

urn:imei:990018040001640, 990018040001640, 10e225558e8282d24bf6870945628754
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000165
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:27 + 16 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001657
 

urn:imei:990018040001657, 990018040001657, e14508e107640d738ac3dcbf76384c9b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000166
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:29 + 16 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001665
 

urn:imei:990018040001665, 990018040001665, 5665a8b9a3a087aa3b1eab1eb06bf98a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000167
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:31 + 16 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001673
 

urn:imei:990018040001673, 990018040001673, 6773e97e68adfc5a2e55fa37cf52dc84
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000168
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001681
 

urn:imei:990018040001681, 990018040001681, 5381214bb963aaa52390bea515e8a000
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000169
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:35 + 16 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001699
 

urn:imei:990018040001699, 990018040001699, e14e2e8d260e9ad6fa22df789274cc53
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000170
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:26 + 17 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001707
 

urn:imei:990018040001707, 990018040001707, 068533a9115bbf330dddeb0edcda7a70
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000171
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:28 + 17 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001715
 

urn:imei:990018040001715, 990018040001715, 70f07dfd3a3ee37f70c69e714509fdda
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000172
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:30 + 17 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001723
 

urn:imei:990018040001723, 990018040001723, b9146b8f8ee48d409f19556597159402
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000173
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:32 + 17 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001731
 

urn:imei:990018040001731, 990018040001731, d46de44b803f0006e1a2b8468521312b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000174
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:34 + 17 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001749
 

urn:imei:990018040001749, 990018040001749, 906df25db1bc7134ff392c4717f277ac
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000175
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:27 + 17 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001756
 

urn:imei:990018040001756, 990018040001756, 9e820549795fc8f0fcdcd69c47bd207a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000176
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:29 + 17 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001764
 

urn:imei:990018040001764, 990018040001764, 6600f5a715038dd911fb7e8a908224df
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000177
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:31 + 17 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001772
 

urn:imei:990018040001772, 990018040001772, b7259c0c83b5be89331772c3e2d54921
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000178
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001780
 

urn:imei:990018040001780, 990018040001780, f96686dbd4a4a5a8a224007159c7bf37
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000179
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:35 + 17 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001798
 

urn:imei:990018040001798, 990018040001798, c338bb452509eb9c3210405fd91d4932
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000180
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:26 + 18 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001806
 

urn:imei:990018040001806, 990018040001806, e180532bd7ec43049d5fec4294657efe
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000181
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:28 + 18 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001814
 

urn:imei:990018040001814, 990018040001814, c0ce7e7002913d03825393c5e5ee85b2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000182
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:30 + 18 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001822
 

urn:imei:990018040001822, 990018040001822, a554eae04892c76c80011d24ecefc53a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000183
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:32 + 18 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001830
 

urn:imei:990018040001830, 990018040001830, 9fd37e1f711ed4778dd8e59d40090b5b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000184
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:34 + 18 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001848
 

urn:imei:990018040001848, 990018040001848, 75b30b565a708972cf18802786a03bd7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000185
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:27 + 18 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001855
 

urn:imei:990018040001855, 990018040001855, 7fa536865049b2a2f09b326572ad7617
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000186
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:29 + 18 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001863
 

urn:imei:990018040001863, 990018040001863, 996ed922effa9eb6c91b6a615759633e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000187
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:31 + 18 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001871
 

urn:imei:990018040001871, 990018040001871, e1447b4d4ab77848d0f7e7492a230861
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000188
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001889
 

urn:imei:990018040001889, 990018040001889, 794d5016425a64e04148aee2562bd19e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000189
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:35 + 18 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001897
 

urn:imei:990018040001897, 990018040001897, 89ebd7b536efa69a3512bd614369d09b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000190
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [0] 0 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:26 + 19 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040001905
 

urn:imei:990018040001905, 990018040001905, 91c160ad7065733f921cecb798ea190e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000191
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [1] 2 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:28 + 19 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040001913
 

urn:imei:990018040001913, 990018040001913, eed8d5a79cd899d0e6504fe04fcb2093
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000192
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [2] 4 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:30 + 19 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040001921
 

urn:imei:990018040001921, 990018040001921, 22de8476487e9101cf647da86e991069
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000193
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [3] 6 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:32 + 19 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040001939
 

urn:imei:990018040001939, 990018040001939, cf15efb9bec35cc50a832ba928bb2671
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000194
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [4] 8 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:34 + 19 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040001947
 

urn:imei:990018040001947, 990018040001947, 93dfc60a2c9fa93a0d42466b3bdf680a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000195
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [5] 1 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:27 + 19 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040001954
 

urn:imei:990018040001954, 990018040001954, ecea42843954170c9ad99295a2bed530
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000196
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [6] 3 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:29 + 19 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040001962
 

urn:imei:990018040001962, 990018040001962, c1910e4d6eb5501c3fd12de6a1673a66
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000197
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [7] 5 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:31 + 19 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040001970
 

urn:imei:990018040001970, 990018040001970, 8c2de9c6e2c6b04d3617b21da8c3ccac
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000198
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [8] 7 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040001988
 

urn:imei:990018040001988, 990018040001988, 44315f0fc6cf187a548034337d251461
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000199
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [1] 2 + ', ' [9] 9 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:35 + 19 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040001996
 

urn:imei:990018040001996, 990018040001996, 521fdb9e34e196ab1f797e841f332186
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000200
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:28 + 10 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002002
 

urn:imei:990018040002002, 990018040002002, fa1039bd22df897c4971ef4a64887b23
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000201
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:30 + 10 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002010
 

urn:imei:990018040002010, 990018040002010, abf5884c4a8b22c553272cebeebd05c3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000202
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:32 + 10 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002028
 

urn:imei:990018040002028, 990018040002028, dc67253b6de9db89eddc2663c52f3226
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000203
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:34 + 10 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002036
 

urn:imei:990018040002036, 990018040002036, 132883a0ada128e04eda48b565367262
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000204
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:36 + 10 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002044
 

urn:imei:990018040002044, 990018040002044, a4d8227dda2d0d398246efe1e86a81d2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000205
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:29 + 10 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002051
 

urn:imei:990018040002051, 990018040002051, 0ebc31f5f22f4af3aca5f55fa54fe514
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000206
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:31 + 10 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002069
 

urn:imei:990018040002069, 990018040002069, e01efeb052b25b2ff7f2a182431d0aaa
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000207
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002077
 

urn:imei:990018040002077, 990018040002077, 2b31363ffcf371264520bd4d70cc9538
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000208
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:35 + 10 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002085
 

urn:imei:990018040002085, 990018040002085, 2990b220ca70acecdc001a254d71ca19
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000209
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:37 + 10 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002093
 

urn:imei:990018040002093, 990018040002093, a9673a5c30f99f234cc94aaa02918a86
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000210
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:28 + 11 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002101
 

urn:imei:990018040002101, 990018040002101, 45797a552216aec8b79e5fc8beac1ad7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000211
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:30 + 11 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002119
 

urn:imei:990018040002119, 990018040002119, 2921749e1e12617a7163687dc853e6e1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000212
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:32 + 11 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002127
 

urn:imei:990018040002127, 990018040002127, 7c2979aa6b55910d42047eda7664766b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000213
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:34 + 11 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002135
 

urn:imei:990018040002135, 990018040002135, 43350674a6f8d03c7b6eeaf7eb196d70
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000214
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:36 + 11 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002143
 

urn:imei:990018040002143, 990018040002143, c838908b29ffa21e433c2a2de58a7c5b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000215
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:29 + 11 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002150
 

urn:imei:990018040002150, 990018040002150, 30ba2da3df758db06c6120db195d19f4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000216
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:31 + 11 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002168
 

urn:imei:990018040002168, 990018040002168, e41912d4cae135a8005d4f22520929b3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000217
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002176
 

urn:imei:990018040002176, 990018040002176, efd3bed77c5b4d81441bd508e4d007ad
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000218
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:35 + 11 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002184
 

urn:imei:990018040002184, 990018040002184, cff71d6586c09b5fb7847db2976fa8b8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000219
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:37 + 11 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002192
 

urn:imei:990018040002192, 990018040002192, d35f306159a4501dbe0e4e4b751cf120
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000220
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:28 + 12 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002200
 

urn:imei:990018040002200, 990018040002200, d9ef1826e6ff21cf2ca86e6ae099a66c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000221
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:30 + 12 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002218
 

urn:imei:990018040002218, 990018040002218, a2b0067294273ad9c19fe8ae019c06e3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000222
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:32 + 12 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002226
 

urn:imei:990018040002226, 990018040002226, 1052716c4bbf37f87286b166234201ac
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000223
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:34 + 12 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002234
 

urn:imei:990018040002234, 990018040002234, 89f40ce174913b678817af7258928583
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000224
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:36 + 12 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002242
 

urn:imei:990018040002242, 990018040002242, cce3ec90478de389567bd0e056b91ee4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000225
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:29 + 12 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002259
 

urn:imei:990018040002259, 990018040002259, 2ef79f6d102d28d723a04ee8f5e8629a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000226
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:31 + 12 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002267
 

urn:imei:990018040002267, 990018040002267, 6ae492d4d38603b15027c2fee0d3e596
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000227
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002275
 

urn:imei:990018040002275, 990018040002275, d4e66617b7ea4d49e4a88743cf7caf68
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000228
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:35 + 12 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002283
 

urn:imei:990018040002283, 990018040002283, cca14eab146c3ce132da7c7cec5a3a51
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000229
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:37 + 12 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002291
 

urn:imei:990018040002291, 990018040002291, 6d2efb4d7588a40222ef73113698461b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000230
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:28 + 13 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002309
 

urn:imei:990018040002309, 990018040002309, ddf161d604e40bac5a00a9ccc7152d99
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000231
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:30 + 13 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002317
 

urn:imei:990018040002317, 990018040002317, adbeb606f5c0102060db3ef94b568c36
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000232
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:32 + 13 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002325
 

urn:imei:990018040002325, 990018040002325, cd264aea016f599c6d4991c6cee60cba
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000233
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:34 + 13 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002333
 

urn:imei:990018040002333, 990018040002333, e161c63359e1f80f26d0d7d844ecba97
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000234
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:36 + 13 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002341
 

urn:imei:990018040002341, 990018040002341, 1375a048a358e5ea2c64c2098da2d52f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000235
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:29 + 13 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002358
 

urn:imei:990018040002358, 990018040002358, 1c65b5f57b1c18697fe60436674c7bd4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000236
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:31 + 13 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002366
 

urn:imei:990018040002366, 990018040002366, 1c3fb27a095e8b96d5a379a5a904429c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000237
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002374
 

urn:imei:990018040002374, 990018040002374, a30df0c2ee2c67eaed4afe61bf1d17d3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000238
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:35 + 13 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002382
 

urn:imei:990018040002382, 990018040002382, 197a8e2de0e85b477493262bd9e7bee3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000239
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:37 + 13 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002390
 

urn:imei:990018040002390, 990018040002390, 1f3c2e533ca7e5e57ead4a5656272779
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000240
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:28 + 14 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002408
 

urn:imei:990018040002408, 990018040002408, 860cb8a9e9e6ce5a5226352929306999
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000241
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:30 + 14 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002416
 

urn:imei:990018040002416, 990018040002416, 4f0f96a51504b9823869004951bc810f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000242
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:32 + 14 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002424
 

urn:imei:990018040002424, 990018040002424, 80ec50a576aa265dfb437bca9da8908b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000243
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:34 + 14 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002432
 

urn:imei:990018040002432, 990018040002432, ebb1d2067e2c4c4ef6db08ad529a0691
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000244
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:36 + 14 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002440
 

urn:imei:990018040002440, 990018040002440, 2cab68cc2c360a89b16da993b327891f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000245
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:29 + 14 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002457
 

urn:imei:990018040002457, 990018040002457, d6195a48b11b4084f092e26b42411476
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000246
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:31 + 14 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002465
 

urn:imei:990018040002465, 990018040002465, 56f526d8ece56ff07669eb768f2552a7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000247
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002473
 

urn:imei:990018040002473, 990018040002473, 38af538c727382f0e331e8fe21c9947e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000248
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:35 + 14 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002481
 

urn:imei:990018040002481, 990018040002481, 324b1e5375e97e0a6dfad99c8368bdb4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000249
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:37 + 14 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002499
 

urn:imei:990018040002499, 990018040002499, 1b85d224c01d8dffdab22d85ef0b5eb6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000250
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:28 + 15 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002507
 

urn:imei:990018040002507, 990018040002507, dad5c92b19f413cd1f3ee526d4f885ec
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000251
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:30 + 15 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002515
 

urn:imei:990018040002515, 990018040002515, 968c71facb96ce28af8d2831e1e4b243
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000252
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:32 + 15 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002523
 

urn:imei:990018040002523, 990018040002523, a0a0ddbbc7447c4ab38a938d77dfeea0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000253
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:34 + 15 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002531
 

urn:imei:990018040002531, 990018040002531, 5bc07e5cace64dbe8f53459e0bbb2869
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000254
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:36 + 15 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002549
 

urn:imei:990018040002549, 990018040002549, d568f039d1163a3f0a03d8a1faf03b2f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000255
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:29 + 15 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002556
 

urn:imei:990018040002556, 990018040002556, 0692f40ac7e4f83495a432ff760d76cb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000256
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:31 + 15 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002564
 

urn:imei:990018040002564, 990018040002564, 8ae31fb9d5c4ac9b2c2d70d68f10add3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000257
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002572
 

urn:imei:990018040002572, 990018040002572, 8099ace326d36dd194ba6ea8e4735882
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000258
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:35 + 15 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002580
 

urn:imei:990018040002580, 990018040002580, 93b623c299228820372cd74fad7a2eee
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000259
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:37 + 15 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002598
 

urn:imei:990018040002598, 990018040002598, 707bb0978c837b6a719e569ad115d9f0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000260
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:28 + 16 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002606
 

urn:imei:990018040002606, 990018040002606, e0da4aa289e7f6cf66af68b59238f391
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000261
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:30 + 16 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002614
 

urn:imei:990018040002614, 990018040002614, 40b4f911189ea2c7747461d93cf8ac47
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000262
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:32 + 16 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002622
 

urn:imei:990018040002622, 990018040002622, a7cddb581b2add4d09461449907ac789
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000263
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:34 + 16 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002630
 

urn:imei:990018040002630, 990018040002630, cbb3e9d91a0a94b1c010e6929825599d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000264
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:36 + 16 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002648
 

urn:imei:990018040002648, 990018040002648, 8f3b57b4a2fffdefca9295a8cad1322a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000265
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:29 + 16 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002655
 

urn:imei:990018040002655, 990018040002655, 29c2d370dcf2b578fd33649f4241fe55
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000266
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:31 + 16 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002663
 

urn:imei:990018040002663, 990018040002663, 5947d8a73bdce64192480027ab25ea7b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000267
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002671
 

urn:imei:990018040002671, 990018040002671, 05583d5786dacf2546b580a068062030
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000268
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:35 + 16 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002689
 

urn:imei:990018040002689, 990018040002689, c4daf7650718fcfa773ceffac7b1edde
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000269
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:37 + 16 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002697
 

urn:imei:990018040002697, 990018040002697, 8be55c1fac82574ac5c5ba1a4226cd9c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000270
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:28 + 17 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002705
 

urn:imei:990018040002705, 990018040002705, 4fe520fe0f4aede971db816af608d366
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000271
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:30 + 17 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002713
 

urn:imei:990018040002713, 990018040002713, c7f5a8637225cfacd6132ce7096e7c71
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000272
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:32 + 17 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002721
 

urn:imei:990018040002721, 990018040002721, 0c39f16074c0a43d6f7bec5b9c94b4e8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000273
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:34 + 17 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002739
 

urn:imei:990018040002739, 990018040002739, d3cc3ba99d64da91b0a6f4853547dcda
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000274
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:36 + 17 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002747
 

urn:imei:990018040002747, 990018040002747, d5223a4ba23660a28afcc8100572a616
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000275
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:29 + 17 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002754
 

urn:imei:990018040002754, 990018040002754, 60649cd006652c5bce67a9c671f8ff1f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000276
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:31 + 17 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002762
 

urn:imei:990018040002762, 990018040002762, 2ebbfb7220882cd24a389b5524cd58af
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000277
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002770
 

urn:imei:990018040002770, 990018040002770, 25d8f5befd43815efad5163a0918e2c5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000278
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:35 + 17 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002788
 

urn:imei:990018040002788, 990018040002788, ca5985156a1ae3950fdfc458d52c78ee
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000279
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:37 + 17 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002796
 

urn:imei:990018040002796, 990018040002796, c5301bd806b08ffbd32c407691736874
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000280
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:28 + 18 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002804
 

urn:imei:990018040002804, 990018040002804, 13d9bf7c3934db14f83b368a7dbbbd1b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000281
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:30 + 18 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002812
 

urn:imei:990018040002812, 990018040002812, 0a3cf3d7431f2f730eaa5aeb56fb98cd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000282
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:32 + 18 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002820
 

urn:imei:990018040002820, 990018040002820, 6abe069ee83d800ac93cb8ce3dd1eb53
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000283
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:34 + 18 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002838
 

urn:imei:990018040002838, 990018040002838, ec561f79a4a610c2d8a4337adb1e941b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000284
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:36 + 18 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002846
 

urn:imei:990018040002846, 990018040002846, 042219538ddb73f87165163ab2710aa1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000285
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:29 + 18 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002853
 

urn:imei:990018040002853, 990018040002853, fd10cb6d4104b189489926939d29d5c0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000286
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:31 + 18 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002861
 

urn:imei:990018040002861, 990018040002861, 6ee340ed821408383eac7c0ab2ad980c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000287
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002879
 

urn:imei:990018040002879, 990018040002879, 4d127ef158dcc8b67917e9a7ebe14bd4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000288
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:35 + 18 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002887
 

urn:imei:990018040002887, 990018040002887, 9c763037f257a3121da7fa42934f412c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000289
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:37 + 18 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002895
 

urn:imei:990018040002895, 990018040002895, 002858ba1c4010e26cc29c183a1f24cf
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000290
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [0] 0 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:28 + 19 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040002903
 

urn:imei:990018040002903, 990018040002903, 0f1c2e693f0d0c0f214ecb15530e134b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000291
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [1] 2 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:30 + 19 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040002911
 

urn:imei:990018040002911, 990018040002911, 1f1852661b025bb9928cea68c209af7c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000292
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [2] 4 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:32 + 19 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040002929
 

urn:imei:990018040002929, 990018040002929, 53b441910c02cf2a87db57bf7486aca5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000293
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [3] 6 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:34 + 19 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040002937
 

urn:imei:990018040002937, 990018040002937, ba1d9e1486adb86292cce3d7ee00274e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000294
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [4] 8 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:36 + 19 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040002945
 

urn:imei:990018040002945, 990018040002945, 6e2da279832eb718f88dc5ba41304e63
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000295
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [5] 1 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:29 + 19 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040002952
 

urn:imei:990018040002952, 990018040002952, 8be861fa4afa8fa522b75c8a476ab920
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000296
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [6] 3 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:31 + 19 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040002960
 

urn:imei:990018040002960, 990018040002960, 9281dbf2fdcb0a517e49e3be2bca250f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000297
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [7] 5 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040002978
 

urn:imei:990018040002978, 990018040002978, b5619a73ee508fdaad1a5a288d8cb3a1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000298
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [8] 7 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:35 + 19 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040002986
 

urn:imei:990018040002986, 990018040002986, cc5f4f3d04e0a3a1db94a5f0d7e5ddf2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000299
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [2] 4 + ', ' [9] 9 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:37 + 19 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040002994
 

urn:imei:990018040002994, 990018040002994, b1e00b4f3aed346b0df8cc3ac2f00a3a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000300
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:30 + 10 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003000
 

urn:imei:990018040003000, 990018040003000, 2aa6086e6d108a8ee538d4d46b09b917
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000301
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:32 + 10 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003018
 

urn:imei:990018040003018, 990018040003018, 3961c0b59af20d1341b16ea4be571e78
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000302
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:34 + 10 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003026
 

urn:imei:990018040003026, 990018040003026, 17d98dc22764c91de2f0c2f33ffd162a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000303
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:36 + 10 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003034
 

urn:imei:990018040003034, 990018040003034, 53c6eeebc00ca7f1a6ebbf6b1f8d8184
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000304
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:38 + 10 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003042
 

urn:imei:990018040003042, 990018040003042, d33cc972b5c568b12d59cbd5af987921
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000305
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:31 + 10 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003059
 

urn:imei:990018040003059, 990018040003059, 62d036cd8a6e0eccb147b1e4cdf17583
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000306
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003067
 

urn:imei:990018040003067, 990018040003067, 9f7a3c88937dd923389d8f077a02e64f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000307
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:35 + 10 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003075
 

urn:imei:990018040003075, 990018040003075, e1a0270e2002e6adc151d89960442e10
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000308
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:37 + 10 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003083
 

urn:imei:990018040003083, 990018040003083, 317dc6b00e51b0c86dc44cb4abc4dcbf
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000309
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:39 + 10 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003091
 

urn:imei:990018040003091, 990018040003091, 5bb33669fcd0f7b5655f8d585c2a1222
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000310
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:30 + 11 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003109
 

urn:imei:990018040003109, 990018040003109, 60bc9b1d6c8afdb12beafd69552c7163
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000311
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:32 + 11 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003117
 

urn:imei:990018040003117, 990018040003117, 147dcf35d1c3af3a8649dd0a71bcf18b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000312
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:34 + 11 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003125
 

urn:imei:990018040003125, 990018040003125, f119c8dce98d08124d6ca0a91ffb3e78
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000313
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:36 + 11 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003133
 

urn:imei:990018040003133, 990018040003133, 8145b6fdb60d50054a237722bf90a7f9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000314
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:38 + 11 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003141
 

urn:imei:990018040003141, 990018040003141, f857da271c2106b84c44a03d198844d8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000315
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:31 + 11 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003158
 

urn:imei:990018040003158, 990018040003158, 6fddf85085fb17d4d015b0470571f70e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000316
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003166
 

urn:imei:990018040003166, 990018040003166, cbe5e602fff2369163d19f35bf567255
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000317
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:35 + 11 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003174
 

urn:imei:990018040003174, 990018040003174, abb50b4ef2b7f5b1e37fbbed120d1a88
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000318
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:37 + 11 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003182
 

urn:imei:990018040003182, 990018040003182, 0de5f129d50cde0564454b5299e1ff84
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000319
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:39 + 11 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003190
 

urn:imei:990018040003190, 990018040003190, 886fc5ba982e462403ec13c5795183a8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000320
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:30 + 12 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003208
 

urn:imei:990018040003208, 990018040003208, a4775f10cfae45fede5eecf9d543025c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000321
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:32 + 12 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003216
 

urn:imei:990018040003216, 990018040003216, d9791674a9ac3a2397ae0a6f6e7df3d6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000322
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:34 + 12 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003224
 

urn:imei:990018040003224, 990018040003224, d3089b4513282225df5413059267871b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000323
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:36 + 12 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003232
 

urn:imei:990018040003232, 990018040003232, 93417a43db9b4e1a6d29b20358afb4af
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000324
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:38 + 12 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003240
 

urn:imei:990018040003240, 990018040003240, afdc83c6826cef84df21c4fdaa62897a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000325
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:31 + 12 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003257
 

urn:imei:990018040003257, 990018040003257, 2dfd9d94058676296ba68b3e56c1667c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000326
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003265
 

urn:imei:990018040003265, 990018040003265, 48cb862af5567f17bfa83d846b5381f3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000327
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:35 + 12 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003273
 

urn:imei:990018040003273, 990018040003273, 55f0a4c5f231c4b1d521d553bff1f51b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000328
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:37 + 12 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003281
 

urn:imei:990018040003281, 990018040003281, 15c796b5431ae706806cf5ff6e54d85e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000329
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:39 + 12 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003299
 

urn:imei:990018040003299, 990018040003299, 1357ac71f5daba8b4429877bcc2dac70
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000330
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:30 + 13 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003307
 

urn:imei:990018040003307, 990018040003307, d40bd62a3208e4291b78a05fd159ff07
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000331
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:32 + 13 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003315
 

urn:imei:990018040003315, 990018040003315, 7aca7cde70441c4c145f360844bcfadc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000332
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:34 + 13 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003323
 

urn:imei:990018040003323, 990018040003323, f2531a3b0e16fc7d47d15ccbb32a5a90
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000333
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:36 + 13 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003331
 

urn:imei:990018040003331, 990018040003331, 1cdc861df0cdae993c376d9b0f223e9c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000334
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:38 + 13 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003349
 

urn:imei:990018040003349, 990018040003349, cfe6b59ca781e9e594ead8d0b3b0ecf9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000335
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:31 + 13 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003356
 

urn:imei:990018040003356, 990018040003356, 6dd7874602b331b5da02875e6c926a5c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000336
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003364
 

urn:imei:990018040003364, 990018040003364, 4f6b3f71dadeeb00cc88a6947496df24
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000337
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:35 + 13 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003372
 

urn:imei:990018040003372, 990018040003372, 5c4e590cf2b7e8e5ad9a4ea4a7a7aa3c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000338
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:37 + 13 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003380
 

urn:imei:990018040003380, 990018040003380, 946acd5fc130a550c359a330a20e89fa
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000339
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:39 + 13 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003398
 

urn:imei:990018040003398, 990018040003398, 9f61f4f4bb202d819a292247a43c6e99
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000340
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:30 + 14 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003406
 

urn:imei:990018040003406, 990018040003406, 4427b54689c08f727d16d3e6295c1560
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000341
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:32 + 14 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003414
 

urn:imei:990018040003414, 990018040003414, ef289b50305b7c4d8edf1de2b35e3523
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000342
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:34 + 14 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003422
 

urn:imei:990018040003422, 990018040003422, 17682dce02ce9efe20e625526ab27af8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000343
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:36 + 14 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003430
 

urn:imei:990018040003430, 990018040003430, 7ac43958f9a4178f43f36af925b0bd6e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000344
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:38 + 14 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003448
 

urn:imei:990018040003448, 990018040003448, 57989e0ab85f5349a1a66a8149660058
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000345
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:31 + 14 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003455
 

urn:imei:990018040003455, 990018040003455, c0e145be3f824455ebc5f366bc0caff1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000346
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003463
 

urn:imei:990018040003463, 990018040003463, 159ecdbb62507756a27096952ec6c1ef
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000347
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:35 + 14 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003471
 

urn:imei:990018040003471, 990018040003471, 41fd7e6c3073e8b08dc2f6c5103d0bb4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000348
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:37 + 14 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003489
 

urn:imei:990018040003489, 990018040003489, 8a28b35b89f94b329cbe335ece56f036
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000349
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:39 + 14 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003497
 

urn:imei:990018040003497, 990018040003497, 0fb58c2d074853ccc055072037a64cac
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000350
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:30 + 15 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003505
 

urn:imei:990018040003505, 990018040003505, b68c60af9a2fe75f4533c6f90f5ce9bf
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000351
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:32 + 15 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003513
 

urn:imei:990018040003513, 990018040003513, e17da53a5e0bda3e37a8e1504feac2b3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000352
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:34 + 15 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003521
 

urn:imei:990018040003521, 990018040003521, 6130fd991f53de1f457f9fa059925713
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000353
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:36 + 15 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003539
 

urn:imei:990018040003539, 990018040003539, 7e0b3af4f4122a8904bd0a782a49e038
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000354
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:38 + 15 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003547
 

urn:imei:990018040003547, 990018040003547, deb8e32e6dbda93b4e3d005be3ad7f17
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000355
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:31 + 15 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003554
 

urn:imei:990018040003554, 990018040003554, b1ee5590b155fee7caccd938a44b7d9b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000356
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003562
 

urn:imei:990018040003562, 990018040003562, 4969be1e7b2805233d5cbc388ba3ec44
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000357
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:35 + 15 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003570
 

urn:imei:990018040003570, 990018040003570, b6fbf2e071a0f961a5bacd6fcae7202c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000358
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:37 + 15 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003588
 

urn:imei:990018040003588, 990018040003588, defe69870736153144bb2aeeca4ca8c5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000359
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:39 + 15 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003596
 

urn:imei:990018040003596, 990018040003596, e127dd6e853fb86bd3628e2b985863af
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000360
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:30 + 16 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003604
 

urn:imei:990018040003604, 990018040003604, 2cb88432557e1a92e402162554e27f83
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000361
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:32 + 16 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003612
 

urn:imei:990018040003612, 990018040003612, 499ae1bdcaf173a9ce0ec20eb938b7db
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000362
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:34 + 16 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003620
 

urn:imei:990018040003620, 990018040003620, 0e40407f1fc5fea9d6b9650d565803ee
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000363
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:36 + 16 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003638
 

urn:imei:990018040003638, 990018040003638, 7c0df8fa0be31f4b216743efba59af0f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000364
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:38 + 16 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003646
 

urn:imei:990018040003646, 990018040003646, 83e847b12f3e4b8fd690d581e3cf8d03
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000365
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:31 + 16 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003653
 

urn:imei:990018040003653, 990018040003653, 46656854be2c51ac2860c74068e55beb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000366
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003661
 

urn:imei:990018040003661, 990018040003661, cee1ac2e04d70e5465f12e61a36c6d4f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000367
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:35 + 16 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003679
 

urn:imei:990018040003679, 990018040003679, 859dfa8b9b96d9dbbdc92f312a812428
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000368
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:37 + 16 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003687
 

urn:imei:990018040003687, 990018040003687, 5a5c4c0bd6d6d1289d3aab6c3e85c856
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000369
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:39 + 16 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003695
 

urn:imei:990018040003695, 990018040003695, d30d94213941177e5471ffad3be7bdd1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000370
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:30 + 17 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003703
 

urn:imei:990018040003703, 990018040003703, d59b389aae19912890a11c8569d6ad20
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000371
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:32 + 17 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003711
 

urn:imei:990018040003711, 990018040003711, 49732fcd802af8fcb29efdf2bd2234dc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000372
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:34 + 17 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003729
 

urn:imei:990018040003729, 990018040003729, 0015aa23d66581cfd5b30fc02ad1b8df
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000373
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:36 + 17 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003737
 

urn:imei:990018040003737, 990018040003737, 0a872116cf26f11ffc427073041a536a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000374
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:38 + 17 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003745
 

urn:imei:990018040003745, 990018040003745, c403899f405286130ec994af652b6a80
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000375
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:31 + 17 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003752
 

urn:imei:990018040003752, 990018040003752, 2848fa5bc606fc831e129cf4f284e826
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000376
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003760
 

urn:imei:990018040003760, 990018040003760, 850c9d9f9a246dba5d7dca59443ff49f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000377
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:35 + 17 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003778
 

urn:imei:990018040003778, 990018040003778, 1a7ba0e2be003af74bf59ca08ec7b7de
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000378
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:37 + 17 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003786
 

urn:imei:990018040003786, 990018040003786, e5085c5b58cc4d013c3edc3053fa5a74
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000379
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:39 + 17 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003794
 

urn:imei:990018040003794, 990018040003794, d9e60f40dddfe885a38cd05ce4c28b60
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000380
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:30 + 18 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003802
 

urn:imei:990018040003802, 990018040003802, 67d16f50ad51a44e0b314054dbd323ee
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000381
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:32 + 18 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003810
 

urn:imei:990018040003810, 990018040003810, d4259b8a233eb1a7e879b40f6cac6827
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000382
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:34 + 18 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003828
 

urn:imei:990018040003828, 990018040003828, 89655ca50aa02c858dc09c26c6147f74
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000383
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:36 + 18 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003836
 

urn:imei:990018040003836, 990018040003836, 59eb553a84a788df17d4ae399e596ac0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000384
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:38 + 18 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003844
 

urn:imei:990018040003844, 990018040003844, 9d134dadebc80e9790d9ff7f0f3c60e6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000385
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:31 + 18 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003851
 

urn:imei:990018040003851, 990018040003851, f99297f9862ebadd3fe8ef8539878535
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000386
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003869
 

urn:imei:990018040003869, 990018040003869, a72881a7f949954925dafedfeabc0340
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000387
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:35 + 18 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003877
 

urn:imei:990018040003877, 990018040003877, 8d9090b527270600f58ec50edff2d5ff
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000388
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:37 + 18 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003885
 

urn:imei:990018040003885, 990018040003885, 2dcc6d505efd72d53ce51ffc06819a68
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000389
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:39 + 18 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003893
 

urn:imei:990018040003893, 990018040003893, 0b7d94a87ad354d4f96b281c796aadbb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000390
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [0] 0 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:30 + 19 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040003901
 

urn:imei:990018040003901, 990018040003901, 784d9787d51560ea1aacb3b6f6b6d257
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000391
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [1] 2 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:32 + 19 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040003919
 

urn:imei:990018040003919, 990018040003919, f734ee73f7737aa0c5b0d70f22e35b0f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000392
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [2] 4 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:34 + 19 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040003927
 

urn:imei:990018040003927, 990018040003927, d86bddba3676cbe2bc575fe09d18d2d5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000393
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [3] 6 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:36 + 19 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040003935
 

urn:imei:990018040003935, 990018040003935, a7498a0d1b72020033f0a3b7e727171e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000394
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [4] 8 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:38 + 19 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040003943
 

urn:imei:990018040003943, 990018040003943, e337f805035da9ce282e79f859cdb5b9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000395
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [5] 1 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:31 + 19 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040003950
 

urn:imei:990018040003950, 990018040003950, 0604ad43c27e6d18d1791cae22107605
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000396
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [6] 3 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040003968
 

urn:imei:990018040003968, 990018040003968, 6416d155abaa9ec47fcb6041f0d393bc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000397
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [7] 5 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:35 + 19 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040003976
 

urn:imei:990018040003976, 990018040003976, 7cdef0d99e19a7396d18bd6927e6884a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000398
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [8] 7 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:37 + 19 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040003984
 

urn:imei:990018040003984, 990018040003984, 7738df72d6e884e440dc2c2802d826d3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000399
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [3] 6 + ', ' [9] 9 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:39 + 19 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040003992
 

urn:imei:990018040003992, 990018040003992, f5ad7e33480842404392e70a54e5ee4d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000400
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:32 + 10 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004008
 

urn:imei:990018040004008, 990018040004008, ef1b3bdee6a9bcd914ce8e58a460a4ba
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000401
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:34 + 10 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004016
 

urn:imei:990018040004016, 990018040004016, ccde30578b77a12678ac30e45ad84aa4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000402
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:36 + 10 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004024
 

urn:imei:990018040004024, 990018040004024, d5b83281d575acb7fc6fc32b6f31439e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000403
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:38 + 10 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004032
 

urn:imei:990018040004032, 990018040004032, 3add4625483e5c06001cb1a6eb87113f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000404
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:40 + 10 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004040
 

urn:imei:990018040004040, 990018040004040, 7d09418dd2a4c8c478baec9c180314a7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000405
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004057
 

urn:imei:990018040004057, 990018040004057, 25b372a2677f6d139caac9597fd686c3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000406
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:35 + 10 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004065
 

urn:imei:990018040004065, 990018040004065, 5c249e502790b7225375510157dea3cc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000407
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:37 + 10 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004073
 

urn:imei:990018040004073, 990018040004073, de8465b5596d961a51266d75546b430b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000408
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:39 + 10 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004081
 

urn:imei:990018040004081, 990018040004081, 072891a395c5254156bc33d9aa8203dd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000409
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:41 + 10 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004099
 

urn:imei:990018040004099, 990018040004099, 433c426983672f2d2cb68e9fc17af527
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000410
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:32 + 11 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004107
 

urn:imei:990018040004107, 990018040004107, a6919f94c052e87f561aae077b594af6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000411
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:34 + 11 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004115
 

urn:imei:990018040004115, 990018040004115, e0928c8029be4d2f6d0fde20338043be
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000412
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:36 + 11 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004123
 

urn:imei:990018040004123, 990018040004123, 3f88ee17ee8a9e7506378f1a63922f7b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000413
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:38 + 11 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004131
 

urn:imei:990018040004131, 990018040004131, 71e048c0fac3fc47e7b56e498b574d86
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000414
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:40 + 11 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004149
 

urn:imei:990018040004149, 990018040004149, 230642cf2a163bec9ef6b11a25bf8558
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000415
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004156
 

urn:imei:990018040004156, 990018040004156, 8fc0d41a6307b080033922da84f9e8c6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000416
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:35 + 11 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004164
 

urn:imei:990018040004164, 990018040004164, 540ee9ef022593eac6e1eb03b5983cec
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000417
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:37 + 11 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004172
 

urn:imei:990018040004172, 990018040004172, e1bac5791613b105f4acd6b67db4399e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000418
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:39 + 11 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004180
 

urn:imei:990018040004180, 990018040004180, a232a4daa051fbc910a7b6527d185408
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000419
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:41 + 11 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004198
 

urn:imei:990018040004198, 990018040004198, 4393bde756bbc9e8a1f2247c4e63e272
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000420
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:32 + 12 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004206
 

urn:imei:990018040004206, 990018040004206, 2a6f83a698dc0dffbe38ca9bcb64bdb4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000421
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:34 + 12 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004214
 

urn:imei:990018040004214, 990018040004214, 63f7ea14b3dce7c902347077ddd4c920
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000422
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:36 + 12 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004222
 

urn:imei:990018040004222, 990018040004222, 2a0989396eb642c6a8a6113c14dc5fd2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000423
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:38 + 12 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004230
 

urn:imei:990018040004230, 990018040004230, 57698c4326202f630ceef1f0ee11dc91
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000424
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:40 + 12 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004248
 

urn:imei:990018040004248, 990018040004248, 2c37095d63ac8275ab34c435ab56a65d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000425
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004255
 

urn:imei:990018040004255, 990018040004255, 53d5714b1297ebeea0244d9fc801e590
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000426
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:35 + 12 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004263
 

urn:imei:990018040004263, 990018040004263, e72ba834ecd5b6c317b13089cdf48af5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000427
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:37 + 12 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004271
 

urn:imei:990018040004271, 990018040004271, 10bb05324cd14a954ab638d161ce1ac3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000428
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:39 + 12 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004289
 

urn:imei:990018040004289, 990018040004289, 763548fe317947deeecaf93159ea4695
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000429
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:41 + 12 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004297
 

urn:imei:990018040004297, 990018040004297, a42face7a834768a6466ecb4146e8f8d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000430
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:32 + 13 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004305
 

urn:imei:990018040004305, 990018040004305, 9bf9231cffff66dd535d649cdf97b48e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000431
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:34 + 13 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004313
 

urn:imei:990018040004313, 990018040004313, 11312908f884aaab87c702cb3daa8b8e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000432
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:36 + 13 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004321
 

urn:imei:990018040004321, 990018040004321, 1f28b28606c8ab919f6a30d73739024c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000433
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:38 + 13 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004339
 

urn:imei:990018040004339, 990018040004339, 82699388b2dd76dcb82ee4377b2bbfd1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000434
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:40 + 13 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004347
 

urn:imei:990018040004347, 990018040004347, e2f9d7b5d035584f35d98871291c0e30
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000435
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004354
 

urn:imei:990018040004354, 990018040004354, 7944c421d68418eff54260b11f39147d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000436
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:35 + 13 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004362
 

urn:imei:990018040004362, 990018040004362, 067ee8ad343abd4b2ed54d40e6beb06f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000437
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:37 + 13 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004370
 

urn:imei:990018040004370, 990018040004370, a8fd44dd63df5d8e2b05d47abcf56939
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000438
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:39 + 13 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004388
 

urn:imei:990018040004388, 990018040004388, f184ffa8e31b7096765ea83fff939800
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000439
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:41 + 13 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004396
 

urn:imei:990018040004396, 990018040004396, 440825e6873f0a8e037bee3db7c0875b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000440
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:32 + 14 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004404
 

urn:imei:990018040004404, 990018040004404, ede89f92e5fb018acfdf9df1bd1f448f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000441
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:34 + 14 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004412
 

urn:imei:990018040004412, 990018040004412, 6a0729a963b8e8bbe4186a45f7ccd2f9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000442
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:36 + 14 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004420
 

urn:imei:990018040004420, 990018040004420, f1fa72e7572e7ee31034e9fbcd6e89b6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000443
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:38 + 14 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004438
 

urn:imei:990018040004438, 990018040004438, bc66fbf57e0a680d4bd8c99b0c361dd9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000444
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:40 + 14 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004446
 

urn:imei:990018040004446, 990018040004446, 2d161dd2bcf1d9608cea24cc81c28bbd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000445
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004453
 

urn:imei:990018040004453, 990018040004453, 152662017928794535a44ecc4025c884
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000446
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:35 + 14 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004461
 

urn:imei:990018040004461, 990018040004461, accbffe68ab674cc72d34f568901d639
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000447
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:37 + 14 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004479
 

urn:imei:990018040004479, 990018040004479, 69b0957c7b5c8bdb77d0e87c6d7d033e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000448
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:39 + 14 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004487
 

urn:imei:990018040004487, 990018040004487, fbce74c1738b9a69d37646de51c2a956
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000449
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:41 + 14 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004495
 

urn:imei:990018040004495, 990018040004495, e6262d1c260fda43bb4f19df301642a8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000450
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:32 + 15 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004503
 

urn:imei:990018040004503, 990018040004503, 2da39548c77ad1b04f0b352eb508855a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000451
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:34 + 15 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004511
 

urn:imei:990018040004511, 990018040004511, b05c5962e7530abcbd714bddf7840aef
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000452
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:36 + 15 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004529
 

urn:imei:990018040004529, 990018040004529, c9ac6276becb5be74e2cae131af6a318
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000453
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:38 + 15 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004537
 

urn:imei:990018040004537, 990018040004537, 50ae32ac7d1d10e5253a8e75b4b68c00
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000454
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:40 + 15 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004545
 

urn:imei:990018040004545, 990018040004545, e28aebd818d8a9156349d45c1b5ea16e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000455
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004552
 

urn:imei:990018040004552, 990018040004552, 457051c1248c27a821592df3b0b5e2c3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000456
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:35 + 15 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004560
 

urn:imei:990018040004560, 990018040004560, ddf3e5e71a5e27ba2da508ba93fabadb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000457
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:37 + 15 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004578
 

urn:imei:990018040004578, 990018040004578, 9754fe6414652d54e8199fc8659b2a94
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000458
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:39 + 15 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004586
 

urn:imei:990018040004586, 990018040004586, 084c2a055f227d8d3b2e22075e58f14d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000459
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:41 + 15 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004594
 

urn:imei:990018040004594, 990018040004594, 73d9e4d8f55eee3c7921ba07d827013c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000460
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:32 + 16 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004602
 

urn:imei:990018040004602, 990018040004602, fd50272861aaed32bef805ddd75e0f70
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000461
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:34 + 16 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004610
 

urn:imei:990018040004610, 990018040004610, e75493e8db0e527a36995a05e5b54f42
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000462
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:36 + 16 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004628
 

urn:imei:990018040004628, 990018040004628, 4ba5dfe0ef23327d7a5171efa5a81fec
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000463
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:38 + 16 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004636
 

urn:imei:990018040004636, 990018040004636, 605106f4b531db30fb50cb2ebdce9bf9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000464
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:40 + 16 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004644
 

urn:imei:990018040004644, 990018040004644, a80b3f892eccb01068362f61422bc251
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000465
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004651
 

urn:imei:990018040004651, 990018040004651, 89556548f226c2656684a75a10c17605
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000466
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:35 + 16 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004669
 

urn:imei:990018040004669, 990018040004669, b9d0ba42fb5563a4d5f33860e4a1f8e1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000467
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:37 + 16 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004677
 

urn:imei:990018040004677, 990018040004677, 2d4517356829722f09853dbd15e94892
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000468
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:39 + 16 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004685
 

urn:imei:990018040004685, 990018040004685, 429e9c1228038fa69f87a572b12e42e8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000469
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:41 + 16 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004693
 

urn:imei:990018040004693, 990018040004693, 467dbdb1fb1011a86167eea8c387b9ba
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000470
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:32 + 17 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004701
 

urn:imei:990018040004701, 990018040004701, 18faf1a72e83a7fdb6fa841a80f76188
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000471
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:34 + 17 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004719
 

urn:imei:990018040004719, 990018040004719, 51ce26c9787f8c04c5cba6596798834e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000472
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:36 + 17 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004727
 

urn:imei:990018040004727, 990018040004727, ebb45767e74872216b7e82733609581e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000473
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:38 + 17 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004735
 

urn:imei:990018040004735, 990018040004735, 57863b77104338471b7b521cb4b3202f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000474
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:40 + 17 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004743
 

urn:imei:990018040004743, 990018040004743, bdd7b566786c9ef947efc9161fa1d548
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000475
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004750
 

urn:imei:990018040004750, 990018040004750, 7e8e1944e996551e007e366846b6eafa
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000476
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:35 + 17 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004768
 

urn:imei:990018040004768, 990018040004768, 1e45c5dd936f080439bd0821aa1c187a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000477
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:37 + 17 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004776
 

urn:imei:990018040004776, 990018040004776, 26c137d856673b093a515ee68825832d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000478
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:39 + 17 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004784
 

urn:imei:990018040004784, 990018040004784, 8f7e5f580ea6e882eb5a5093b32d564e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000479
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:41 + 17 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004792
 

urn:imei:990018040004792, 990018040004792, b7a608244412f68775abcaa07c9f79dd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000480
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:32 + 18 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004800
 

urn:imei:990018040004800, 990018040004800, 65dc94a761e89c4052668724bda7de04
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000481
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:34 + 18 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004818
 

urn:imei:990018040004818, 990018040004818, ba0680dac8bf8cdcf899a5dac8e49ef6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000482
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:36 + 18 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004826
 

urn:imei:990018040004826, 990018040004826, 3d7583b9cd53c7178d87327b84cde567
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000483
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:38 + 18 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004834
 

urn:imei:990018040004834, 990018040004834, dfa1b8b64ac5f1739d3b1ad082b92e3f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000484
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:40 + 18 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004842
 

urn:imei:990018040004842, 990018040004842, 043bb8905d62eca7ffe435a79c0001dd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000485
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004859
 

urn:imei:990018040004859, 990018040004859, a40c3fc32463a53f81289c4e20318538
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000486
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:35 + 18 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004867
 

urn:imei:990018040004867, 990018040004867, cf5b3da8876b952d7e8c525445f0ad41
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000487
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:37 + 18 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004875
 

urn:imei:990018040004875, 990018040004875, b28ad032b8288299cb64a450c73acc8a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000488
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:39 + 18 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004883
 

urn:imei:990018040004883, 990018040004883, 4b4997780447d6654c9561c61915c294
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000489
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:41 + 18 = 59


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004891
 

urn:imei:990018040004891, 990018040004891, 3cae8abe5e0410f89df0b030a6c5aa6f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000490
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [0] 0 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:32 + 19 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040004909
 

urn:imei:990018040004909, 990018040004909, f5fe3750c1afb6a1547b0e1a41711ebc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000491
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [1] 2 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:34 + 19 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040004917
 

urn:imei:990018040004917, 990018040004917, b2b1fb6ce07e9a35c8b4c2f9afdbd47c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000492
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [2] 4 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:36 + 19 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040004925
 

urn:imei:990018040004925, 990018040004925, e984675b1076d7274d7d7fd7b972639c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000493
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [3] 6 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:38 + 19 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040004933
 

urn:imei:990018040004933, 990018040004933, 9de906b9fbd1c1ad875d4fd0545ed2f2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000494
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [4] 8 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:40 + 19 = 59


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040004941
 

urn:imei:990018040004941, 990018040004941, fee1c77cc007dc500ca9cd42a74090ad
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000495
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [5] 1 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040004958
 

urn:imei:990018040004958, 990018040004958, 4a93c16951be83dae938462b555434ac
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000496
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [6] 3 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:35 + 19 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040004966
 

urn:imei:990018040004966, 990018040004966, 5dda7789b34febea7c4a003b4b409dd6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000497
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [7] 5 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:37 + 19 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040004974
 

urn:imei:990018040004974, 990018040004974, 631394412816d438c24aca251b937a2e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000498
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [8] 7 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:39 + 19 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040004982
 

urn:imei:990018040004982, 990018040004982, 478e588ac36b2a3b5ca338f525bea073
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000499
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [4] 8 + ', ' [9] 9 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:41 + 19 = 60


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040004990
 

urn:imei:990018040004990, 990018040004990, 03e8d2ab6f975d2da57af4d2bd23fdac
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000500
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:25 + 10 = 35


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005005
 

urn:imei:990018040005005, 990018040005005, abbda816bb1b1c6229ad319645c82db3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000501
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:27 + 10 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005013
 

urn:imei:990018040005013, 990018040005013, f03e1bb91b247f6c097dab0fa04a6c7f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000502
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:29 + 10 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005021
 

urn:imei:990018040005021, 990018040005021, 062f7f7cbec7469bda01e59f83e75e8d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000503
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:31 + 10 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005039
 

urn:imei:990018040005039, 990018040005039, b0d947948bcc36a737b87f3353650c1a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000504
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005047
 

urn:imei:990018040005047, 990018040005047, cf66817469b4d87f4e476ff37f2c2f2d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000505
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:26 + 10 = 36


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005054
 

urn:imei:990018040005054, 990018040005054, ce5446e92c8719c2f94a7b9fb30daac1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000506
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:28 + 10 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005062
 

urn:imei:990018040005062, 990018040005062, 4031a81df1e76b744c4a8bc43366c88d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000507
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:30 + 10 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005070
 

urn:imei:990018040005070, 990018040005070, e595aa83f26fd91896433583d6a9afd3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000508
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:32 + 10 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005088
 

urn:imei:990018040005088, 990018040005088, 383bb468db59a58c55afe13cb2c03e48
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000509
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:34 + 10 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005096
 

urn:imei:990018040005096, 990018040005096, f6c6869e6b0c1212da0472903d29c0de
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000510
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:25 + 11 = 36


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005104
 

urn:imei:990018040005104, 990018040005104, 1e19e4fc3fb436b9fb722d25017629b9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000511
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:27 + 11 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005112
 

urn:imei:990018040005112, 990018040005112, 0e8d686722c7496c1368e8e4ff42c9a7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000512
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:29 + 11 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005120
 

urn:imei:990018040005120, 990018040005120, 434a98afa072f6914e82319f2db2035f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000513
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:31 + 11 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005138
 

urn:imei:990018040005138, 990018040005138, 98f6aa83fbaa93e5a5ba474238becef0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000514
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005146
 

urn:imei:990018040005146, 990018040005146, 16571c37f54f03a648cf64267f425387
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000515
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:26 + 11 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005153
 

urn:imei:990018040005153, 990018040005153, 27ca2e8be896e6b67e1b784ca69da11b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000516
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:28 + 11 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005161
 

urn:imei:990018040005161, 990018040005161, 1dde0a4e745256534418e28473b9d5ce
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000517
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:30 + 11 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005179
 

urn:imei:990018040005179, 990018040005179, 085d8e8d53919a6ba10b352519a2fd69
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000518
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:32 + 11 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005187
 

urn:imei:990018040005187, 990018040005187, e8c41b540cff4d2c8afd03e584aeb56e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000519
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:34 + 11 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005195
 

urn:imei:990018040005195, 990018040005195, aca442ecb13127e50ed2c1afd7107100
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000520
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:25 + 12 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005203
 

urn:imei:990018040005203, 990018040005203, 92305d3edfadac440179d3de497d10ad
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000521
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:27 + 12 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005211
 

urn:imei:990018040005211, 990018040005211, bffd2fffb61bbf6dbf29077f1c5aaafa
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000522
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:29 + 12 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005229
 

urn:imei:990018040005229, 990018040005229, 2376a61460698655a41f0a52be13740f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000523
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:31 + 12 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005237
 

urn:imei:990018040005237, 990018040005237, 46ca679f6d51dfba6df2c46684cfe235
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000524
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005245
 

urn:imei:990018040005245, 990018040005245, f3c03816f6955d7322dca4fbcefd8947
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000525
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:26 + 12 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005252
 

urn:imei:990018040005252, 990018040005252, a420897c64dc28369b563149dbcfed53
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000526
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:28 + 12 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005260
 

urn:imei:990018040005260, 990018040005260, ce1642acdd6a3d107b24fbaf513368e1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000527
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:30 + 12 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005278
 

urn:imei:990018040005278, 990018040005278, ad369b24645af02932c0b98dfc3b08ab
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000528
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:32 + 12 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005286
 

urn:imei:990018040005286, 990018040005286, ecb16038c2227018ededa26dab564872
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000529
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:34 + 12 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005294
 

urn:imei:990018040005294, 990018040005294, 0e513d041458d18b8f59bf4f7b0adc76
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000530
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:25 + 13 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005302
 

urn:imei:990018040005302, 990018040005302, 036901298524681c3bfe5d1c148fff1b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000531
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:27 + 13 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005310
 

urn:imei:990018040005310, 990018040005310, c9e1da302ccafcd9d0157fc7172aefbb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000532
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:29 + 13 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005328
 

urn:imei:990018040005328, 990018040005328, 6bc4ce036cf981cc38fdd739f81edc36
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000533
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:31 + 13 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005336
 

urn:imei:990018040005336, 990018040005336, fae2538bb7d7aeb6c1e1df29c8a11c99
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000534
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005344
 

urn:imei:990018040005344, 990018040005344, eaefa5382199bebd815c4006707fdbf0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000535
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:26 + 13 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005351
 

urn:imei:990018040005351, 990018040005351, 7a8d0f79971b40b2b85524a473dae6dc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000536
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:28 + 13 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005369
 

urn:imei:990018040005369, 990018040005369, ff26afcbfb420e0e797368a0e385b884
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000537
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:30 + 13 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005377
 

urn:imei:990018040005377, 990018040005377, 174160e0ef800abea5a6726877ef268f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000538
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:32 + 13 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005385
 

urn:imei:990018040005385, 990018040005385, ba1f8da376eb7c7610ddb45b722bb329
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000539
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:34 + 13 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005393
 

urn:imei:990018040005393, 990018040005393, 8ea38d632481667206f6deeb2ab930fe
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000540
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:25 + 14 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005401
 

urn:imei:990018040005401, 990018040005401, beaea9cd6747e689390b04662a533c7d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000541
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:27 + 14 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005419
 

urn:imei:990018040005419, 990018040005419, 0f800eead7795c4353a8d1f167293ee9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000542
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:29 + 14 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005427
 

urn:imei:990018040005427, 990018040005427, 8167d19a7f6e3b8333417286b4b1da80
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000543
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:31 + 14 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005435
 

urn:imei:990018040005435, 990018040005435, 812b4a2d1dd71aab731bf3b05916b158
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000544
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005443
 

urn:imei:990018040005443, 990018040005443, 62846341963fa007f8abfccbb4d4427d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000545
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:26 + 14 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005450
 

urn:imei:990018040005450, 990018040005450, a5b4a726c5222ac34b2ff93cf840cec0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000546
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:28 + 14 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005468
 

urn:imei:990018040005468, 990018040005468, 236953c304e7140b6ffb832014487b2a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000547
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:30 + 14 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005476
 

urn:imei:990018040005476, 990018040005476, 4a7a44401837b6e511e52f47a4f37552
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000548
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:32 + 14 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005484
 

urn:imei:990018040005484, 990018040005484, dd0753d0db050b9043c8eaa25d7705c7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000549
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:34 + 14 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005492
 

urn:imei:990018040005492, 990018040005492, 45b8cd7d0ed8e3ecd59099edd4bbfd68
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000550
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:25 + 15 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005500
 

urn:imei:990018040005500, 990018040005500, f7a0fb151d278c5a0c5ac1319bab7d69
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000551
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:27 + 15 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005518
 

urn:imei:990018040005518, 990018040005518, 0b9859416fb37673b235718a358a2c0b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000552
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:29 + 15 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005526
 

urn:imei:990018040005526, 990018040005526, d8478b184cd8f339dbc59a25b2be92ed
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000553
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:31 + 15 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005534
 

urn:imei:990018040005534, 990018040005534, e814ef69665d121f4a2521869fa27669
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000554
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005542
 

urn:imei:990018040005542, 990018040005542, 7f6dfa6d78b74e89c24708cba2e0170e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000555
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:26 + 15 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005559
 

urn:imei:990018040005559, 990018040005559, 9a5347bc34ba8284dfc0159d56e87cdc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000556
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:28 + 15 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005567
 

urn:imei:990018040005567, 990018040005567, 5677be13d9eaf9a756add14351924d1a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000557
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:30 + 15 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005575
 

urn:imei:990018040005575, 990018040005575, 11feba01ab32a1cdf628d261e2deb186
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000558
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:32 + 15 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005583
 

urn:imei:990018040005583, 990018040005583, e79447173e3d2fb2536f3a3b81817fde
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000559
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:34 + 15 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005591
 

urn:imei:990018040005591, 990018040005591, d0e65f28d2eccb92a7c8d93ebeafae1a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000560
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:25 + 16 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005609
 

urn:imei:990018040005609, 990018040005609, c45f244c19751fbe34b56bb70b2abf91
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000561
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:27 + 16 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005617
 

urn:imei:990018040005617, 990018040005617, 3317a8aa65f77682a1f3d2a0ec1ba646
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000562
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:29 + 16 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005625
 

urn:imei:990018040005625, 990018040005625, 969db9649c8ea9450526ae82d8351a08
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000563
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:31 + 16 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005633
 

urn:imei:990018040005633, 990018040005633, 1c7ae70419701971124124df481e8158
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000564
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005641
 

urn:imei:990018040005641, 990018040005641, a30274ce86073b4956c17c4d37e931e9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000565
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:26 + 16 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005658
 

urn:imei:990018040005658, 990018040005658, d7bc7dae443597d302c12c8582f2bf81
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000566
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:28 + 16 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005666
 

urn:imei:990018040005666, 990018040005666, dda459dbaf69b7d1745f7024fab3b8cb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000567
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:30 + 16 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005674
 

urn:imei:990018040005674, 990018040005674, 7b2fcd707b8f353bba50c005d891438a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000568
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:32 + 16 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005682
 

urn:imei:990018040005682, 990018040005682, 6465b6389d259ce734e087e2c4658d68
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000569
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:34 + 16 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005690
 

urn:imei:990018040005690, 990018040005690, 818df7317fea6b292fa7fbd873b162fd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000570
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:25 + 17 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005708
 

urn:imei:990018040005708, 990018040005708, 3b9a4c39bd7a6eb0e11ec994db5c3087
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000571
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:27 + 17 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005716
 

urn:imei:990018040005716, 990018040005716, 2c676560034cb034c955dafeb98e47af
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000572
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:29 + 17 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005724
 

urn:imei:990018040005724, 990018040005724, d7b8bc83ec62aa7ac0a7e113cb66aac4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000573
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:31 + 17 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005732
 

urn:imei:990018040005732, 990018040005732, 1aa5bd12655a2bee76e8cc60ddf28777
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000574
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005740
 

urn:imei:990018040005740, 990018040005740, 6ca5bd9ba7d3afa8559676bd23881de3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000575
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:26 + 17 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005757
 

urn:imei:990018040005757, 990018040005757, 26e51d4f89dec6da0955e0503841794d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000576
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:28 + 17 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005765
 

urn:imei:990018040005765, 990018040005765, e72eb1e14f490bc3d86b85c2f963ab3c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000577
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:30 + 17 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005773
 

urn:imei:990018040005773, 990018040005773, d5fa4048bfc327437c9c578f34be568f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000578
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:32 + 17 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005781
 

urn:imei:990018040005781, 990018040005781, ce69fc65f6afc3e172c48a78d69bca95
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000579
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:34 + 17 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005799
 

urn:imei:990018040005799, 990018040005799, d9e7a932e5a8f5ce292af082cf172648
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000580
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:25 + 18 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005807
 

urn:imei:990018040005807, 990018040005807, 292b4a4b4b2911742ff2b1e3222149ab
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000581
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:27 + 18 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005815
 

urn:imei:990018040005815, 990018040005815, 0e7da438d62ff65fe9ce0603be9b0552
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000582
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:29 + 18 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005823
 

urn:imei:990018040005823, 990018040005823, 3e5ec02d56e7f699a788a2967d9f1ea6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000583
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:31 + 18 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005831
 

urn:imei:990018040005831, 990018040005831, da6dda03be350d13e879c61d708e8d13
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000584
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005849
 

urn:imei:990018040005849, 990018040005849, 5a09723896c406e8f9a8555753b92759
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000585
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:26 + 18 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005856
 

urn:imei:990018040005856, 990018040005856, 31440f2af5e839f5f982564d47f66e27
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000586
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:28 + 18 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005864
 

urn:imei:990018040005864, 990018040005864, c384a5121559135c0af28b5edcda3e5f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000587
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:30 + 18 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005872
 

urn:imei:990018040005872, 990018040005872, 638f958c88cc486f2a342d4f6b52348b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000588
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:32 + 18 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005880
 

urn:imei:990018040005880, 990018040005880, 61db0b5a2e3e55ca346b3407b75b662c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000589
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:34 + 18 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005898
 

urn:imei:990018040005898, 990018040005898, dec0b2893c09beb5aafa59868dc4174c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000590
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [0] 0 + ']

	 Even Sum is: 25


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:25 + 19 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040005906
 

urn:imei:990018040005906, 990018040005906, 2623b9d3dfdc7d37d2ba1a076aab37e6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000591
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [1] 2 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:27 + 19 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040005914
 

urn:imei:990018040005914, 990018040005914, 836c5f0a6c2b922e6286ba8789d90168
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000592
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [2] 4 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:29 + 19 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040005922
 

urn:imei:990018040005922, 990018040005922, 41843d8bfb8384248075f022761576b9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000593
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [3] 6 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:31 + 19 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040005930
 

urn:imei:990018040005930, 990018040005930, 72e19a0ca5cbd1335ad84ed664dc6560
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000594
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [4] 8 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040005948
 

urn:imei:990018040005948, 990018040005948, f724ceddd6c5fe9927b1086f6096b35f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000595
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [5] 1 + ']

	 Even Sum is: 26


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:26 + 19 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040005955
 

urn:imei:990018040005955, 990018040005955, 79f5145e8ac885f479f87923ac7b98a9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000596
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [6] 3 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:28 + 19 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040005963
 

urn:imei:990018040005963, 990018040005963, 00811f9a3dc375a08a9fd144e080941d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000597
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [7] 5 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:30 + 19 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040005971
 

urn:imei:990018040005971, 990018040005971, dc32b43cc00b83e796e2e3b4f364b2a8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000598
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [8] 7 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:32 + 19 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040005989
 

urn:imei:990018040005989, 990018040005989, 4de6bf609dbcd3cb41fddbd70e4605a0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000599
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [5] 1 + ', ' [9] 9 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:34 + 19 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040005997
 

urn:imei:990018040005997, 990018040005997, f79bff7b0d92dcef34d32039ec29e74d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000600
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:27 + 10 = 37


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006003
 

urn:imei:990018040006003, 990018040006003, 7ade2f57b1c3999a4462accef77226d5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000601
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:29 + 10 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006011
 

urn:imei:990018040006011, 990018040006011, 64bf87051dcf4155c38dfa2953481bbd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000602
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:31 + 10 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006029
 

urn:imei:990018040006029, 990018040006029, 1a67acf1e2cf76ffe361358c116e311f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000603
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006037
 

urn:imei:990018040006037, 990018040006037, f0ff8185a58f4b6b884f71279509f51b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000604
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:35 + 10 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006045
 

urn:imei:990018040006045, 990018040006045, 023c69728fb74c4aedaecfc83da9e220
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000605
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:28 + 10 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006052
 

urn:imei:990018040006052, 990018040006052, 68f67309dd10a62f44bb8fa04fd6ee46
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000606
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:30 + 10 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006060
 

urn:imei:990018040006060, 990018040006060, 8f68a79ad9ecb3077af2bc5e4e03b773
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000607
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:32 + 10 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006078
 

urn:imei:990018040006078, 990018040006078, 37a5c21da9fe73fcf6ea919fcc2c67c8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000608
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:34 + 10 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006086
 

urn:imei:990018040006086, 990018040006086, 7d3d26f152198aa5b46a76b3e4c92c04
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000609
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:36 + 10 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006094
 

urn:imei:990018040006094, 990018040006094, 58b31f9bd156fd0adec70ae5325a3118
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000610
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:27 + 11 = 38


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006102
 

urn:imei:990018040006102, 990018040006102, f66b721a6fbc68a08dff718ebc23465d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000611
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:29 + 11 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006110
 

urn:imei:990018040006110, 990018040006110, 146000580b4aa75443c05587437725f5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000612
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:31 + 11 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006128
 

urn:imei:990018040006128, 990018040006128, abb4cd2fd8777bd38adaa60d61c6c217
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000613
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006136
 

urn:imei:990018040006136, 990018040006136, 8246fd905f09612758270ceced8ea79e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000614
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:35 + 11 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006144
 

urn:imei:990018040006144, 990018040006144, e3e9a0126ed41f2a61f0a8cca2276329
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000615
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:28 + 11 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006151
 

urn:imei:990018040006151, 990018040006151, 2b83a01712953d401402bf4b81615768
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000616
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:30 + 11 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006169
 

urn:imei:990018040006169, 990018040006169, 662dfe5775399ab82acc0f9d5cbb399e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000617
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:32 + 11 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006177
 

urn:imei:990018040006177, 990018040006177, 711f0640b37b937764f1994ca5858674
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000618
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:34 + 11 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006185
 

urn:imei:990018040006185, 990018040006185, 842e8ac42aad0af8f89be4675892a3fc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000619
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:36 + 11 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006193
 

urn:imei:990018040006193, 990018040006193, 35c1b4d82ab126a53b8d4272253bf2a4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000620
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:27 + 12 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006201
 

urn:imei:990018040006201, 990018040006201, b95428d8bcaf4486e0b3d666102393be
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000621
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:29 + 12 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006219
 

urn:imei:990018040006219, 990018040006219, b26426268a539df305ffc4bba3892e04
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000622
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:31 + 12 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006227
 

urn:imei:990018040006227, 990018040006227, 98194a035b1b5549f9bd96e5e8668ad2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000623
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006235
 

urn:imei:990018040006235, 990018040006235, 9ef578cee98d3ba86487b787d1253f57
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000624
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:35 + 12 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006243
 

urn:imei:990018040006243, 990018040006243, 3daec13a8a14855f891803def2562afb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000625
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:28 + 12 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006250
 

urn:imei:990018040006250, 990018040006250, 77e88652301a80f42c320d4c2a5576d5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000626
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:30 + 12 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006268
 

urn:imei:990018040006268, 990018040006268, edadf0727e427b46cf5d03b5da7af050
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000627
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:32 + 12 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006276
 

urn:imei:990018040006276, 990018040006276, 0c25fb0f5a5fc022ee68406f4679a1e3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000628
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:34 + 12 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006284
 

urn:imei:990018040006284, 990018040006284, 43e8da22e47b8aac09e774c4a44a34c0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000629
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:36 + 12 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006292
 

urn:imei:990018040006292, 990018040006292, 4bd7a6cf1b0e57d9bcb75c5d23873718
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000630
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:27 + 13 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006300
 

urn:imei:990018040006300, 990018040006300, 60654144d273f910a51b60374517f8e5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000631
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:29 + 13 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006318
 

urn:imei:990018040006318, 990018040006318, 3e9dc79048e5dd97a0151741cb57cc85
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000632
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:31 + 13 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006326
 

urn:imei:990018040006326, 990018040006326, edd9d5f474f334976670f047460b8605
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000633
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006334
 

urn:imei:990018040006334, 990018040006334, 423fe7e60a62fc9688650c812ac5b1ab
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000634
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:35 + 13 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006342
 

urn:imei:990018040006342, 990018040006342, f356d66b7f27089ee3181b01f33ee442
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000635
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:28 + 13 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006359
 

urn:imei:990018040006359, 990018040006359, b033502217f552e9ea611a5cce07e660
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000636
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:30 + 13 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006367
 

urn:imei:990018040006367, 990018040006367, 74859f79a1c5589a274e8a614afbd4cb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000637
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:32 + 13 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006375
 

urn:imei:990018040006375, 990018040006375, 4e30313a79b35c8489761cdcb4ecf1d5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000638
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:34 + 13 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006383
 

urn:imei:990018040006383, 990018040006383, a29f4b53ef7bef1814675696c252aa48
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000639
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:36 + 13 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006391
 

urn:imei:990018040006391, 990018040006391, af27b184f2b520d400a5d2ac667e5b08
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000640
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:27 + 14 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006409
 

urn:imei:990018040006409, 990018040006409, e51785d109b51d4a7fdccbcfd14f0af2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000641
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:29 + 14 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006417
 

urn:imei:990018040006417, 990018040006417, 190a0e2f9efef17d4185da64a5899e80
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000642
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:31 + 14 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006425
 

urn:imei:990018040006425, 990018040006425, b728476a3fe89bb1c1746753d6091831
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000643
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006433
 

urn:imei:990018040006433, 990018040006433, f761ce22e9161761e0d6c13a9c2439d4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000644
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:35 + 14 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006441
 

urn:imei:990018040006441, 990018040006441, 7e44b03c67763fd912d475d071f2c97d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000645
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:28 + 14 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006458
 

urn:imei:990018040006458, 990018040006458, 69afd903c448ab09eb8765ff62f31fce
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000646
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:30 + 14 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006466
 

urn:imei:990018040006466, 990018040006466, 5da64de6976c6f2e81746af0af1507be
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000647
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:32 + 14 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006474
 

urn:imei:990018040006474, 990018040006474, 24819eb85b51f1414ce81dca58859aeb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000648
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:34 + 14 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006482
 

urn:imei:990018040006482, 990018040006482, 74dca5df8d1d9c2120a260ad19903a9c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000649
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:36 + 14 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006490
 

urn:imei:990018040006490, 990018040006490, bfa839cd2da789b359bb9eff6630efb6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000650
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:27 + 15 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006508
 

urn:imei:990018040006508, 990018040006508, d0c9f7bb38fe6e3ad8dbbee8eed521ba
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000651
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:29 + 15 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006516
 

urn:imei:990018040006516, 990018040006516, da8c941e0f66f00708ad3188997dad33
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000652
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:31 + 15 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006524
 

urn:imei:990018040006524, 990018040006524, da327bc9735b132e296c039e217c5ea8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000653
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006532
 

urn:imei:990018040006532, 990018040006532, 565261d212ee33236628705bde522f1f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000654
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:35 + 15 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006540
 

urn:imei:990018040006540, 990018040006540, 3db69c089b0c10cd7776d73da9c2e8eb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000655
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:28 + 15 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006557
 

urn:imei:990018040006557, 990018040006557, df5b4efa94565c0d11b87325489fcd96
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000656
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:30 + 15 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006565
 

urn:imei:990018040006565, 990018040006565, 96aef3f07f753eb629fe6674a17c8005
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000657
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:32 + 15 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006573
 

urn:imei:990018040006573, 990018040006573, d594780b0e3469303f5c8b482c0c88ef
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000658
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:34 + 15 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006581
 

urn:imei:990018040006581, 990018040006581, bfa16056ba2627557f1c8a3201d8581a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000659
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:36 + 15 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006599
 

urn:imei:990018040006599, 990018040006599, eb536520fbd83b7701edd4c7a95fc29c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000660
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:27 + 16 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006607
 

urn:imei:990018040006607, 990018040006607, f05b813d7fb4f80b64735e417befd600
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000661
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:29 + 16 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006615
 

urn:imei:990018040006615, 990018040006615, c1f7031abfd81b2f0a168c9607c7773a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000662
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:31 + 16 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006623
 

urn:imei:990018040006623, 990018040006623, 5734bf139ccf11efa780d24063407a42
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000663
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006631
 

urn:imei:990018040006631, 990018040006631, 5a1a20eb44ec0d69074f03bbdf327d9b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000664
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:35 + 16 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006649
 

urn:imei:990018040006649, 990018040006649, 15c950de0663ada7e16995e2a734c9ed
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000665
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:28 + 16 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006656
 

urn:imei:990018040006656, 990018040006656, a85eabf8eb93a3d4ffdd550970924928
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000666
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:30 + 16 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006664
 

urn:imei:990018040006664, 990018040006664, bc17bf918a924a5ead7c5ceba92a7fc3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000667
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:32 + 16 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006672
 

urn:imei:990018040006672, 990018040006672, 553610ce1751eb83155f3a63dfe022b8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000668
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:34 + 16 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006680
 

urn:imei:990018040006680, 990018040006680, ae6bf6ffda8e21034d254917006fff3c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000669
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:36 + 16 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006698
 

urn:imei:990018040006698, 990018040006698, 1336395afd364471e076d214dd0141f5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000670
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:27 + 17 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006706
 

urn:imei:990018040006706, 990018040006706, a806de09c2a05a0585731745d6941660
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000671
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:29 + 17 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006714
 

urn:imei:990018040006714, 990018040006714, 6b0ee907cd17561ec100a015b42163b4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000672
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:31 + 17 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006722
 

urn:imei:990018040006722, 990018040006722, 9f6402781d0442d100cd0c039196c3a5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000673
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006730
 

urn:imei:990018040006730, 990018040006730, 21b3fd407f84a4f1e571e7300c4ad7a6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000674
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:35 + 17 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006748
 

urn:imei:990018040006748, 990018040006748, 122975fc7bb396be690d791e2e87e49d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000675
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:28 + 17 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006755
 

urn:imei:990018040006755, 990018040006755, e29f7e75f91a1e096cc4fa41589d6026
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000676
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:30 + 17 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006763
 

urn:imei:990018040006763, 990018040006763, b6e30bda2a7a998e29ca4c8ad0a2ebce
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000677
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:32 + 17 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006771
 

urn:imei:990018040006771, 990018040006771, c67c9a76c9cca5438b36f367120851f5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000678
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:34 + 17 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006789
 

urn:imei:990018040006789, 990018040006789, 1961d48c9b05a13be59d13987566a2f2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000679
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:36 + 17 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006797
 

urn:imei:990018040006797, 990018040006797, 735a38ac9fed9849c063c41c04582664
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000680
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:27 + 18 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006805
 

urn:imei:990018040006805, 990018040006805, 260e585c2749694b094b224091316c71
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000681
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:29 + 18 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006813
 

urn:imei:990018040006813, 990018040006813, 44120d99dabf056be3d9521f2c6a61b0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000682
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:31 + 18 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006821
 

urn:imei:990018040006821, 990018040006821, 1e0dc1f58ff56f8198b681ebfed3d04a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000683
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006839
 

urn:imei:990018040006839, 990018040006839, ec66394483c69acfe70324b972717c07
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000684
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:35 + 18 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006847
 

urn:imei:990018040006847, 990018040006847, a5dcd6e1a9007c6b220e9bfccb87dcfd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000685
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:28 + 18 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006854
 

urn:imei:990018040006854, 990018040006854, 9d9c84f3628cfd98f9630b91c426589e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000686
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:30 + 18 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006862
 

urn:imei:990018040006862, 990018040006862, 6321a1e967b87dee2b0f3e5ec7099db6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000687
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:32 + 18 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006870
 

urn:imei:990018040006870, 990018040006870, f2e4e12697a13866e4a0ebec77b8397e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000688
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:34 + 18 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006888
 

urn:imei:990018040006888, 990018040006888, 9c4396a4f46d7f57ad384e2bd5226e27
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000689
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:36 + 18 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006896
 

urn:imei:990018040006896, 990018040006896, 4debc69fcb02b2dc8bfda6572cb1bba0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000690
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [0] 0 + ']

	 Even Sum is: 27


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:27 + 19 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040006904
 

urn:imei:990018040006904, 990018040006904, a09a870e4e48def126a6c6854628227f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000691
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [1] 2 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:29 + 19 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040006912
 

urn:imei:990018040006912, 990018040006912, a28d4476a06197bd14d8891bb9a4edfc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000692
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [2] 4 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:31 + 19 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040006920
 

urn:imei:990018040006920, 990018040006920, c10a4b4092bb5ebe6b4963e5017d9b38
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000693
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [3] 6 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040006938
 

urn:imei:990018040006938, 990018040006938, 83a99fda6febd9750a0ad34cfc767dfd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000694
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [4] 8 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:35 + 19 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040006946
 

urn:imei:990018040006946, 990018040006946, 8de410dd610fe4b1e896ba47990ddb95
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000695
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [5] 1 + ']

	 Even Sum is: 28


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:28 + 19 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040006953
 

urn:imei:990018040006953, 990018040006953, cb73f567f9be2cd25776c35c10326bff
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000696
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [6] 3 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:30 + 19 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040006961
 

urn:imei:990018040006961, 990018040006961, 9a4a9e9861f4ac995337f6730138c9c0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000697
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [7] 5 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:32 + 19 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040006979
 

urn:imei:990018040006979, 990018040006979, 2d5daaa54ff2272d46136ed2d52418cb
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000698
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [8] 7 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:34 + 19 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040006987
 

urn:imei:990018040006987, 990018040006987, 242d9a635b6612b9ed2f46b2a81ce395
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000699
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [6] 3 + ', ' [9] 9 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:36 + 19 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040006995
 

urn:imei:990018040006995, 990018040006995, 24f7dc7c9e45a7fc53690e81281372c5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000700
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:29 + 10 = 39


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007001
 

urn:imei:990018040007001, 990018040007001, 97066e9bade178bfae5440aa4251f97e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000701
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:31 + 10 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007019
 

urn:imei:990018040007019, 990018040007019, 5b0afc39cf4bbb5fd9c7b6898a48dcb6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000702
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007027
 

urn:imei:990018040007027, 990018040007027, 4bda1cb604634bb7d806cc632f6e68c3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000703
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:35 + 10 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007035
 

urn:imei:990018040007035, 990018040007035, 49861ac49fd3fdc2e5eaa9f12c669d89
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000704
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:37 + 10 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007043
 

urn:imei:990018040007043, 990018040007043, 0e625ef9750e344cd698747cd97f3bab
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000705
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:30 + 10 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007050
 

urn:imei:990018040007050, 990018040007050, 62688ff01efc75bcc06f925de77ca8a8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000706
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:32 + 10 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007068
 

urn:imei:990018040007068, 990018040007068, 32e240c388aff8bb8cfacdedbcf98008
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000707
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:34 + 10 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007076
 

urn:imei:990018040007076, 990018040007076, 5cea293fab453c6bc2a5719591f3020c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000708
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:36 + 10 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007084
 

urn:imei:990018040007084, 990018040007084, 1c91d04847763fb26cf4f5d50e569654
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000709
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:38 + 10 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007092
 

urn:imei:990018040007092, 990018040007092, b297df6ce2b4875b9f31b27ab46358e8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000710
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:29 + 11 = 40


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007100
 

urn:imei:990018040007100, 990018040007100, 602561224fbd95b49660b297b48cd2f1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000711
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:31 + 11 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007118
 

urn:imei:990018040007118, 990018040007118, 0e46e2c5eda5b7c071fa7424bd01d73a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000712
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007126
 

urn:imei:990018040007126, 990018040007126, d69db09dc91f3d0f2fbe0ac8f4ec96ba
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000713
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:35 + 11 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007134
 

urn:imei:990018040007134, 990018040007134, c392aa5b8b74a4fcbb9872b005419190
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000714
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:37 + 11 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007142
 

urn:imei:990018040007142, 990018040007142, 90c402534c5daf2447c9322b19fd719c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000715
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:30 + 11 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007159
 

urn:imei:990018040007159, 990018040007159, 5cdf089c879ca9045d26ef1db3b5310f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000716
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:32 + 11 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007167
 

urn:imei:990018040007167, 990018040007167, 02deef2da58ef77f9b772148368a8465
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000717
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:34 + 11 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007175
 

urn:imei:990018040007175, 990018040007175, 471f88d7197395bd9ad0754fdd185029
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000718
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:36 + 11 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007183
 

urn:imei:990018040007183, 990018040007183, b1ea38e4860e367c85cb17e834bb836a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000719
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:38 + 11 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007191
 

urn:imei:990018040007191, 990018040007191, 5a9022e2fadb882ebb277b470a962b33
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000720
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:29 + 12 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007209
 

urn:imei:990018040007209, 990018040007209, 6e7a58404d01b1b532cdc93511db0c52
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000721
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:31 + 12 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007217
 

urn:imei:990018040007217, 990018040007217, 33c1aaa79cc2c2e3cc64d51488479405
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000722
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007225
 

urn:imei:990018040007225, 990018040007225, 6bc4a79301fcb6cc6a92a0f89ed91e9d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000723
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:35 + 12 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007233
 

urn:imei:990018040007233, 990018040007233, 7303cdabdd9fb930c9e708f9797e9de7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000724
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:37 + 12 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007241
 

urn:imei:990018040007241, 990018040007241, e9d0dbb82a5fda344b68a56d07623f97
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000725
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:30 + 12 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007258
 

urn:imei:990018040007258, 990018040007258, b2f1affe08961ec99767fd5ecc326a0a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000726
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:32 + 12 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007266
 

urn:imei:990018040007266, 990018040007266, 901a1f27cec8715e3d4600271b4e05ec
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000727
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:34 + 12 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007274
 

urn:imei:990018040007274, 990018040007274, cde974fc29f87728f58cb05c7abcda36
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000728
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:36 + 12 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007282
 

urn:imei:990018040007282, 990018040007282, 94c72eba8feb5d3b1468c1335b107c58
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000729
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:38 + 12 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007290
 

urn:imei:990018040007290, 990018040007290, 0092f1d7e37a25cdf0876018831bc5e1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000730
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:29 + 13 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007308
 

urn:imei:990018040007308, 990018040007308, 2f8c1c5cf6cc2fa663f45163fd4a8e20
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000731
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:31 + 13 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007316
 

urn:imei:990018040007316, 990018040007316, 0aa9c8154b55aac007dfb5bf5d8e5219
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000732
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007324
 

urn:imei:990018040007324, 990018040007324, d28c5d41ebd7bec54b9e9ae9c3b1a70b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000733
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:35 + 13 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007332
 

urn:imei:990018040007332, 990018040007332, 9fba76880eefa148ae51c5123e640f38
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000734
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:37 + 13 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007340
 

urn:imei:990018040007340, 990018040007340, d2607a66b0cd6ea22f09c49d05c340c7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000735
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:30 + 13 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007357
 

urn:imei:990018040007357, 990018040007357, 642cfc23b435083d1625f1706b52b290
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000736
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:32 + 13 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007365
 

urn:imei:990018040007365, 990018040007365, e8becbd161adb70b9862603e65debc7b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000737
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:34 + 13 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007373
 

urn:imei:990018040007373, 990018040007373, b30d7eacccfe4d892648ac80a9ca6470
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000738
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:36 + 13 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007381
 

urn:imei:990018040007381, 990018040007381, cd271bedeb6fb0b5d26383df37e32109
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000739
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:38 + 13 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007399
 

urn:imei:990018040007399, 990018040007399, 3103f283387d1b07274616031350e329
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000740
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:29 + 14 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007407
 

urn:imei:990018040007407, 990018040007407, b5bec4779f10a81de6610457c7e960d8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000741
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:31 + 14 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007415
 

urn:imei:990018040007415, 990018040007415, f7e88533876b857d513e03461f824235
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000742
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007423
 

urn:imei:990018040007423, 990018040007423, cffbb29b801355a818c0803e1e5584fe
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000743
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:35 + 14 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007431
 

urn:imei:990018040007431, 990018040007431, 1b254331a8a28f25df48254edef83a33
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000744
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:37 + 14 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007449
 

urn:imei:990018040007449, 990018040007449, cecda312fb941c6dfda49bab536fcda9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000745
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:30 + 14 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007456
 

urn:imei:990018040007456, 990018040007456, 429251086a10a35dd440a79f34b24c96
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000746
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:32 + 14 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007464
 

urn:imei:990018040007464, 990018040007464, 97bc8d721a7bf5c716c6b503c1c836e0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000747
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:34 + 14 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007472
 

urn:imei:990018040007472, 990018040007472, 6a985ca1660a6eb4e0f74c215781b2d4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000748
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:36 + 14 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007480
 

urn:imei:990018040007480, 990018040007480, cbf77a3468a12147a2419d72f9d14f88
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000749
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:38 + 14 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007498
 

urn:imei:990018040007498, 990018040007498, e78c8998b3e8abd4d5dd2e9863deb2c6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000750
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:29 + 15 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007506
 

urn:imei:990018040007506, 990018040007506, 33328c8fd6db8f10f1cf053afb794e34
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000751
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:31 + 15 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007514
 

urn:imei:990018040007514, 990018040007514, 5bf6b71850549018b99351a569a8bafd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000752
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007522
 

urn:imei:990018040007522, 990018040007522, 1a51412464e15896697d3cdbf9ebdd16
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000753
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:35 + 15 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007530
 

urn:imei:990018040007530, 990018040007530, 00628f906d0e6d4c77a5fff85cef598a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000754
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:37 + 15 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007548
 

urn:imei:990018040007548, 990018040007548, 50cc5fdbf376163a194984c848e50768
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000755
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:30 + 15 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007555
 

urn:imei:990018040007555, 990018040007555, 236a755e6406da66fa32c090345d3c45
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000756
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:32 + 15 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007563
 

urn:imei:990018040007563, 990018040007563, 7b897920e4a4a9ac3139c321c3c036f6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000757
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:34 + 15 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007571
 

urn:imei:990018040007571, 990018040007571, 4c18140424403f7a5a8027aa56ce54af
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000758
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:36 + 15 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007589
 

urn:imei:990018040007589, 990018040007589, 84cf559591d1c280fd17b61b409975a3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000759
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:38 + 15 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007597
 

urn:imei:990018040007597, 990018040007597, 46f223734e851d227f7a39563c4bce0c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000760
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:29 + 16 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007605
 

urn:imei:990018040007605, 990018040007605, 91a6134218a14ce9e32f2f5931ba8445
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000761
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:31 + 16 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007613
 

urn:imei:990018040007613, 990018040007613, ba37bae568d8f7eb5368a56917ae3040
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000762
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007621
 

urn:imei:990018040007621, 990018040007621, cb140f1881ce4715c460267be36514cd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000763
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:35 + 16 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007639
 

urn:imei:990018040007639, 990018040007639, 5f68e339235b6c24cda8b3f15ad666b4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000764
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:37 + 16 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007647
 

urn:imei:990018040007647, 990018040007647, 16ab790f03a9617a523da65dfe3df4a4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000765
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:30 + 16 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007654
 

urn:imei:990018040007654, 990018040007654, 475d8daa196df2905d5583333076322d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000766
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:32 + 16 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007662
 

urn:imei:990018040007662, 990018040007662, a342841a841099443fd37ad881221f71
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000767
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:34 + 16 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007670
 

urn:imei:990018040007670, 990018040007670, 2f41bc531879a3dbbc1f45ac0dcd2de3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000768
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:36 + 16 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007688
 

urn:imei:990018040007688, 990018040007688, b90ef094b0a9f1c16d8539870f5bd3d3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000769
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:38 + 16 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007696
 

urn:imei:990018040007696, 990018040007696, 81bb14920dece580a7e22f1d2645b0e7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000770
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:29 + 17 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007704
 

urn:imei:990018040007704, 990018040007704, b709fcd44b544bcd8f8bba47ef273f3b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000771
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:31 + 17 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007712
 

urn:imei:990018040007712, 990018040007712, 0908f0e55c1ce7b3f8cf025ad7d0d394
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000772
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007720
 

urn:imei:990018040007720, 990018040007720, 6a5460af2a237224950e2fea929c0452
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000773
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:35 + 17 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007738
 

urn:imei:990018040007738, 990018040007738, 27ba8a9e2e4152f0caa707adae1dff89
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000774
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:37 + 17 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007746
 

urn:imei:990018040007746, 990018040007746, f863da6efc2f266dc6e7d1c4a0d9e739
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000775
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:30 + 17 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007753
 

urn:imei:990018040007753, 990018040007753, f8270f7d7d4fac418a361a84fbc348c9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000776
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:32 + 17 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007761
 

urn:imei:990018040007761, 990018040007761, 042f8a663783ab5c423e1237b76fd06e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000777
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:34 + 17 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007779
 

urn:imei:990018040007779, 990018040007779, e193fca221bfaf160a4fc4694ce54126
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000778
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:36 + 17 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007787
 

urn:imei:990018040007787, 990018040007787, 609b70e539414acec54bc355e87278f2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000779
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:38 + 17 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007795
 

urn:imei:990018040007795, 990018040007795, 274e1135655bfa9de9b5d8af7aac74aa
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000780
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:29 + 18 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007803
 

urn:imei:990018040007803, 990018040007803, 757b5e568c70a9ed38d7a457b5e08716
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000781
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:31 + 18 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007811
 

urn:imei:990018040007811, 990018040007811, b30bee902d000c29230530f7e2685a88
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000782
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007829
 

urn:imei:990018040007829, 990018040007829, 55c62c816de701ef4697b744ded3db04
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000783
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:35 + 18 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007837
 

urn:imei:990018040007837, 990018040007837, 54959f7ab45c260f1f69c1b502842dca
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000784
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:37 + 18 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007845
 

urn:imei:990018040007845, 990018040007845, e4b4835a2f02fea9dd30afed806a5cbd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000785
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:30 + 18 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007852
 

urn:imei:990018040007852, 990018040007852, 433802b10820f9e343b6f83e99160a87
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000786
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:32 + 18 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007860
 

urn:imei:990018040007860, 990018040007860, 3ca87f9e535ab53f93644d739fefe66d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000787
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:34 + 18 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007878
 

urn:imei:990018040007878, 990018040007878, 169a14e31b08e35c0e2919482d8a4a0a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000788
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:36 + 18 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007886
 

urn:imei:990018040007886, 990018040007886, 2dd63775480ba0323aa37cd0fc984929
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000789
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:38 + 18 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007894
 

urn:imei:990018040007894, 990018040007894, 4026d14c24efea68a7b79171f33b1763
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000790
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [0] 0 + ']

	 Even Sum is: 29


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:29 + 19 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040007902
 

urn:imei:990018040007902, 990018040007902, 8f67eaf132726d6714c40ff07e8e52f8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000791
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [1] 2 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:31 + 19 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040007910
 

urn:imei:990018040007910, 990018040007910, 249e4f211c730ecf84b2d334c98c9b7a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000792
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [2] 4 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040007928
 

urn:imei:990018040007928, 990018040007928, 8bcdf9a3133d8f0ea8b44270c3c90a3a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000793
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [3] 6 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:35 + 19 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040007936
 

urn:imei:990018040007936, 990018040007936, 52f266215385d5f734b2fa648683c7be
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000794
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [4] 8 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:37 + 19 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040007944
 

urn:imei:990018040007944, 990018040007944, d856a9075cf611306daec1d00b3b55c3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000795
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [5] 1 + ']

	 Even Sum is: 30


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:30 + 19 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040007951
 

urn:imei:990018040007951, 990018040007951, 56f60772fd1c0faa26c55fa035be1cf0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000796
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [6] 3 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:32 + 19 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040007969
 

urn:imei:990018040007969, 990018040007969, 2e1b527c2aa358f7fafe0e754f19afd3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000797
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [7] 5 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:34 + 19 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040007977
 

urn:imei:990018040007977, 990018040007977, 16fbf14f1a48b20bbf80e10ef9ade15a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000798
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [8] 7 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:36 + 19 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040007985
 

urn:imei:990018040007985, 990018040007985, 306c167448ea45eb413054e825f61e9c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000799
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [7] 5 + ', ' [9] 9 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:38 + 19 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040007993
 

urn:imei:990018040007993, 990018040007993, b43a5d7112098bb9760616687e626e7b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000800
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:31 + 10 = 41


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008009
 

urn:imei:990018040008009, 990018040008009, 01357d0acb175f88d85af5bb1521da92
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000801
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008017
 

urn:imei:990018040008017, 990018040008017, 79025bd6a09fd8e949d85e459f0fca53
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000802
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:35 + 10 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008025
 

urn:imei:990018040008025, 990018040008025, 8e1617ff18558845035bcc458b1e4d01
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000803
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:37 + 10 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008033
 

urn:imei:990018040008033, 990018040008033, 4f9419ddd179e62714dbe23de792f863
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000804
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:39 + 10 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008041
 

urn:imei:990018040008041, 990018040008041, e1ff95217fffbabd3bddfa690330c6c9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000805
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:32 + 10 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008058
 

urn:imei:990018040008058, 990018040008058, 1bd82fc30a6652c78e046370e1758af6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000806
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:34 + 10 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008066
 

urn:imei:990018040008066, 990018040008066, 440cf1762fff321d822a1477d44206f7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000807
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:36 + 10 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008074
 

urn:imei:990018040008074, 990018040008074, cac61c3287fb94b28ed8a104e3b400c7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000808
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:38 + 10 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008082
 

urn:imei:990018040008082, 990018040008082, 81a6d7a25b1ef1d46359bd2d9dd4e78b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000809
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:40 + 10 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008090
 

urn:imei:990018040008090, 990018040008090, 4082ef6410b4960b1fa6f1b01e577d71
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000810
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:31 + 11 = 42


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008108
 

urn:imei:990018040008108, 990018040008108, 7be51cca2bbb8bd4a35d22bc222e7a63
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000811
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008116
 

urn:imei:990018040008116, 990018040008116, e19018df1f911fd4ddbba364fb11f0a8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000812
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:35 + 11 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008124
 

urn:imei:990018040008124, 990018040008124, 2b799bb47882a03456866e34d221bdc4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000813
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:37 + 11 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008132
 

urn:imei:990018040008132, 990018040008132, 6c941ca6258ee457957401cfe004f3f0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000814
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:39 + 11 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008140
 

urn:imei:990018040008140, 990018040008140, 17f0f9ca50e1e1d9dc98c92695629018
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000815
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:32 + 11 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008157
 

urn:imei:990018040008157, 990018040008157, f64757bb0389aacdde1745e19f119563
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000816
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:34 + 11 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008165
 

urn:imei:990018040008165, 990018040008165, 4bbfc77f5460b8e2f4f60e892eabaa1e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000817
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:36 + 11 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008173
 

urn:imei:990018040008173, 990018040008173, 1bc782ffe4b2849c1d8081b73edb5759
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000818
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:38 + 11 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008181
 

urn:imei:990018040008181, 990018040008181, 01fc3056235f4aeb5b561c16d1ada366
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000819
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:40 + 11 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008199
 

urn:imei:990018040008199, 990018040008199, ee5f6fe344ac46f3a387575b2b906175
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000820
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:31 + 12 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008207
 

urn:imei:990018040008207, 990018040008207, 58f3e3d06807e1ff10cc71907657a925
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000821
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008215
 

urn:imei:990018040008215, 990018040008215, 25bad42554936a58e2b69e01d1c66a1a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000822
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:35 + 12 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008223
 

urn:imei:990018040008223, 990018040008223, c96b08eebe2006638f15cc2509929710
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000823
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:37 + 12 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008231
 

urn:imei:990018040008231, 990018040008231, 9ff1b1a0d8174d832283fa1b0411ab9d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000824
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:39 + 12 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008249
 

urn:imei:990018040008249, 990018040008249, 00eb21ce2b4089639f6c2341df25a8f5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000825
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:32 + 12 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008256
 

urn:imei:990018040008256, 990018040008256, 6a96cd85bf993b3abd7548c457d923c6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000826
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:34 + 12 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008264
 

urn:imei:990018040008264, 990018040008264, ea5c6f7246b7519e2e7f0450c9cfe7cd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000827
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:36 + 12 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008272
 

urn:imei:990018040008272, 990018040008272, 9ac2a145f54611b8b53b1959a205ad3a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000828
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:38 + 12 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008280
 

urn:imei:990018040008280, 990018040008280, e6da508d1c6ecfc8f7bbeb52fe8f27ca
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000829
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:40 + 12 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008298
 

urn:imei:990018040008298, 990018040008298, 089b05cd087f48c913231f2e5cd3384e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000830
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:31 + 13 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008306
 

urn:imei:990018040008306, 990018040008306, c9602d493e7fba56865f25125c7310fa
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000831
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008314
 

urn:imei:990018040008314, 990018040008314, 88981ea29aef03e889032b4fc0d1dfaa
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000832
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:35 + 13 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008322
 

urn:imei:990018040008322, 990018040008322, 59a12d43b7bf7e5f6482edb8254f5c63
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000833
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:37 + 13 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008330
 

urn:imei:990018040008330, 990018040008330, 01abbbad45a23f60cba149d8280f959f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000834
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:39 + 13 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008348
 

urn:imei:990018040008348, 990018040008348, 15e3ebc34a21deb3b3d35a7b3cd794f0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000835
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:32 + 13 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008355
 

urn:imei:990018040008355, 990018040008355, 3bd420cff18dca2540b8caf48f893046
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000836
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:34 + 13 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008363
 

urn:imei:990018040008363, 990018040008363, 034d47cd5e89f5e80e1f9e556868e71f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000837
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:36 + 13 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008371
 

urn:imei:990018040008371, 990018040008371, fac30cf363164039360c753ac2c7bd17
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000838
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:38 + 13 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008389
 

urn:imei:990018040008389, 990018040008389, 25ce03d137e036f855e3fbaf67b54fcc
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000839
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:40 + 13 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008397
 

urn:imei:990018040008397, 990018040008397, f3b5f4339d626a6bacbebc1e6b474051
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000840
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:31 + 14 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008405
 

urn:imei:990018040008405, 990018040008405, ee85386ce1617d9251731427a879977c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000841
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008413
 

urn:imei:990018040008413, 990018040008413, 7752b88c57ef43ed6fac7fc6629d834a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000842
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:35 + 14 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008421
 

urn:imei:990018040008421, 990018040008421, d8b0fedbc130a37cf7a848205c51589c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000843
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:37 + 14 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008439
 

urn:imei:990018040008439, 990018040008439, 0ae284d5ef8555a9f7fb3e46696e929d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000844
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:39 + 14 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008447
 

urn:imei:990018040008447, 990018040008447, 858ad17ee25101e64b336a394f6937f1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000845
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:32 + 14 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008454
 

urn:imei:990018040008454, 990018040008454, 84ab909ff90ce8c92dceb99254152af9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000846
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:34 + 14 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008462
 

urn:imei:990018040008462, 990018040008462, f311478bfc7577c9d64af65c2fcdf22a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000847
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:36 + 14 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008470
 

urn:imei:990018040008470, 990018040008470, 1ec74ba0e1365b33bcebab889bc48637
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000848
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:38 + 14 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008488
 

urn:imei:990018040008488, 990018040008488, 3ccc5691b27e47276b1b06992f815482
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000849
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:40 + 14 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008496
 

urn:imei:990018040008496, 990018040008496, 71e42135d2e667d7c9b7ab90616c23cd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000850
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:31 + 15 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008504
 

urn:imei:990018040008504, 990018040008504, 27f815b6caa0814838a9260d4f00243f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000851
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008512
 

urn:imei:990018040008512, 990018040008512, 974ed2c58080979d2fc2ad9fdce8a877
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000852
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:35 + 15 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008520
 

urn:imei:990018040008520, 990018040008520, 937709e61902e5318d929de123bf274e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000853
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:37 + 15 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008538
 

urn:imei:990018040008538, 990018040008538, 41c2a3af32b413b70b381a00d8472818
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000854
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:39 + 15 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008546
 

urn:imei:990018040008546, 990018040008546, 33523214bf859bb8b351792f227cf6c4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000855
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:32 + 15 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008553
 

urn:imei:990018040008553, 990018040008553, b93d7ec207badb0ee6dab5b9a7e12ed9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000856
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:34 + 15 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008561
 

urn:imei:990018040008561, 990018040008561, f7ce09ae23990e50d08018760148e234
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000857
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:36 + 15 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008579
 

urn:imei:990018040008579, 990018040008579, 5c4927863b2b878fc106869309b649e7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000858
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:38 + 15 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008587
 

urn:imei:990018040008587, 990018040008587, dbd5dc8254965579e29ec0827ab7522d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000859
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:40 + 15 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008595
 

urn:imei:990018040008595, 990018040008595, 5c4ec17c74c913ad1a746888c4c5c13f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000860
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:31 + 16 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008603
 

urn:imei:990018040008603, 990018040008603, b300b9ab1aaf09d0f11503807249d693
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000861
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008611
 

urn:imei:990018040008611, 990018040008611, e75d6e8341150c549209a88961f00bbd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000862
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:35 + 16 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008629
 

urn:imei:990018040008629, 990018040008629, 0a90609115f428ab245480771ca31f45
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000863
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:37 + 16 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008637
 

urn:imei:990018040008637, 990018040008637, 2a966e5f7c84def8eb26059d006059d5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000864
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:39 + 16 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008645
 

urn:imei:990018040008645, 990018040008645, 2d8fd945f375f6573a67793ebd945290
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000865
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:32 + 16 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008652
 

urn:imei:990018040008652, 990018040008652, f31fb69d84a0026480c40152c7e7679c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000866
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:34 + 16 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008660
 

urn:imei:990018040008660, 990018040008660, 8ee674eddc061e8c92816f3ae8c535b4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000867
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:36 + 16 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008678
 

urn:imei:990018040008678, 990018040008678, d454978e5bdbcc19df6e10bea3d79ae1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000868
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:38 + 16 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008686
 

urn:imei:990018040008686, 990018040008686, 2bcd9a25fe61feb75957f63120e77126
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000869
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:40 + 16 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008694
 

urn:imei:990018040008694, 990018040008694, bbeebd512671ec9832e5142cdd799077
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000870
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:31 + 17 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008702
 

urn:imei:990018040008702, 990018040008702, 51e6c0a0b71f0032906a8cd915af5466
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000871
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008710
 

urn:imei:990018040008710, 990018040008710, aa0c69692c821368451060cdaaea98b2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000872
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:35 + 17 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008728
 

urn:imei:990018040008728, 990018040008728, 732aa0a84ec560327751b0a38f74f6ee
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000873
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:37 + 17 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008736
 

urn:imei:990018040008736, 990018040008736, 1eff914711d5ff758f2fe2659622b719
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000874
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:39 + 17 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008744
 

urn:imei:990018040008744, 990018040008744, 662db682f006acec93958637782cc7bf
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000875
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:32 + 17 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008751
 

urn:imei:990018040008751, 990018040008751, 2080878467be5566b6721f0746730548
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000876
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:34 + 17 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008769
 

urn:imei:990018040008769, 990018040008769, dea7f9bd904e59bb18bba6a8f8b6b2d1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000877
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:36 + 17 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008777
 

urn:imei:990018040008777, 990018040008777, 91966db2831b672b3e14637f496452f0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000878
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:38 + 17 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008785
 

urn:imei:990018040008785, 990018040008785, 5f9fdab22bafb590a68f5adcffd63b80
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000879
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:40 + 17 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008793
 

urn:imei:990018040008793, 990018040008793, 0e98dfc6729dd9d600f09ed79103688f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000880
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:31 + 18 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008801
 

urn:imei:990018040008801, 990018040008801, dab1ab047e9f9f6b2c18f6885d7ace40
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000881
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008819
 

urn:imei:990018040008819, 990018040008819, 46f9fe7e3332831faa11332ab07e530d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000882
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:35 + 18 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008827
 

urn:imei:990018040008827, 990018040008827, 64d252c699b955734d619a775294c482
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000883
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:37 + 18 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008835
 

urn:imei:990018040008835, 990018040008835, 3b36c22fe907ae79107fbe71b3dac14e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000884
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:39 + 18 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008843
 

urn:imei:990018040008843, 990018040008843, 51990f43f7ff91a7be035c397c0e0ada
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000885
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:32 + 18 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008850
 

urn:imei:990018040008850, 990018040008850, b1ba2345a10847cbdf3429402df240f7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000886
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:34 + 18 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008868
 

urn:imei:990018040008868, 990018040008868, c1593a23fd6f5ed1168e4df1fefb4b2f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000887
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:36 + 18 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008876
 

urn:imei:990018040008876, 990018040008876, 9d65798dbcf22fb51f859a565121932b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000888
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:38 + 18 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008884
 

urn:imei:990018040008884, 990018040008884, 1e57d3a40f693d18127be15ba7835b74
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000889
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:40 + 18 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008892
 

urn:imei:990018040008892, 990018040008892, f5d8b536f5cf519fd58d9e9a984cb929
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000890
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [0] 0 + ']

	 Even Sum is: 31


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:31 + 19 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040008900
 

urn:imei:990018040008900, 990018040008900, 01202710078d9ba17f3df5bae76d3198
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000891
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [1] 2 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040008918
 

urn:imei:990018040008918, 990018040008918, 8177505c9afe9f94b86ee0b7a18be728
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000892
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [2] 4 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:35 + 19 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040008926
 

urn:imei:990018040008926, 990018040008926, c177d630f13146beeb01f3b5a8610a6c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000893
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [3] 6 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:37 + 19 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040008934
 

urn:imei:990018040008934, 990018040008934, e9b1c0371cbe8f0f6af25c2c6d75c929
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000894
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:39 + 19 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040008942
 

urn:imei:990018040008942, 990018040008942, 1f6075a86c63d2f3ddf34c1dcd63a832
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000895
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [5] 1 + ']

	 Even Sum is: 32


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:32 + 19 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040008959
 

urn:imei:990018040008959, 990018040008959, 5b3b44f1dcdd97fa435bf2b815b56c15
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000896
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [6] 3 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:34 + 19 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040008967
 

urn:imei:990018040008967, 990018040008967, 06cba02dad4ef845fc1ceaeb43520786
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000897
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [7] 5 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:36 + 19 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040008975
 

urn:imei:990018040008975, 990018040008975, 497e6583a5b305fa0a0e7cd5e7763b58
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000898
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [8] 7 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:38 + 19 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040008983
 

urn:imei:990018040008983, 990018040008983, 7119ce034c8e0e93307fa1083c5c8282
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000899
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [8] 7 + ', ' [9] 9 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:40 + 19 = 59


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040008991
 

urn:imei:990018040008991, 990018040008991, 6133559d85680d623e5a30e5d161254a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000900
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:33 + 10 = 43


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009007
 

urn:imei:990018040009007, 990018040009007, bc9f20a68be823a5b3ac99b33625af5c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000901
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:35 + 10 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009015
 

urn:imei:990018040009015, 990018040009015, c32d2cdecdccf9c3482733e300a86ea0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000902
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:37 + 10 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009023
 

urn:imei:990018040009023, 990018040009023, 5f4f3e0a844e5c365855a18d2beeadfd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000903
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:39 + 10 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009031
 

urn:imei:990018040009031, 990018040009031, e21d3ea486e0f3fad43d2e40986b0e2c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000904
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:41 + 10 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009049
 

urn:imei:990018040009049, 990018040009049, e6e200a00ab0f4c98a890aaa531e08e6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000905
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:34 + 10 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009056
 

urn:imei:990018040009056, 990018040009056, e6a29c8abe944bdac03e5cf936aa4eff
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000906
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:36 + 10 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009064
 

urn:imei:990018040009064, 990018040009064, 8bb8157eade11144e883c7e741081ea0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000907
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:38 + 10 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009072
 

urn:imei:990018040009072, 990018040009072, ae1a6032949935462a79503866337c74
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000908
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:40 + 10 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009080
 

urn:imei:990018040009080, 990018040009080, 90561244235a095d9cf837b887e013b2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000909
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 0 + ']

	 Odd Sum is: 10


	 Total sum:42 + 10 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009098
 

urn:imei:990018040009098, 990018040009098, 9cd232c81b8076b9e533a9352a71dca8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000910
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:33 + 11 = 44


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009106
 

urn:imei:990018040009106, 990018040009106, 7717ccd99ba68cbcbb45119e5356f9ab
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000911
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:35 + 11 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009114
 

urn:imei:990018040009114, 990018040009114, e6905db28ed0fa71aae0c2d11d1e0f7c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000912
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:37 + 11 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009122
 

urn:imei:990018040009122, 990018040009122, c209f1ee5ac9c88546383c4339d043ba
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000913
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:39 + 11 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009130
 

urn:imei:990018040009130, 990018040009130, 2d1802285349bb86baa5e6e255f7893e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000914
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:41 + 11 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009148
 

urn:imei:990018040009148, 990018040009148, 0952b9b9d91e79fc89209a3b0d6085b9
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000915
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:34 + 11 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009155
 

urn:imei:990018040009155, 990018040009155, 5e9a76aa41ea93417bbe36e7ccca6666
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000916
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:36 + 11 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009163
 

urn:imei:990018040009163, 990018040009163, 79c03feb551f3c4596a18d291e2ca6e0
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000917
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:38 + 11 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009171
 

urn:imei:990018040009171, 990018040009171, ae1828a73c7547046d20d2d55d25ff5d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000918
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:40 + 11 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009189
 

urn:imei:990018040009189, 990018040009189, b087a3f3a35161492a8a35f5564fcf24
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000919
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 1 + ']

	 Odd Sum is: 11


	 Total sum:42 + 11 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009197
 

urn:imei:990018040009197, 990018040009197, 7467b8ed9384c1903036ce601007567a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000920
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:33 + 12 = 45


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009205
 

urn:imei:990018040009205, 990018040009205, 200034066dc113c76a1dab4084acc0d2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000921
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:35 + 12 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009213
 

urn:imei:990018040009213, 990018040009213, 5c66a4e46a67b2de8ff50d9de09d222c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000922
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:37 + 12 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009221
 

urn:imei:990018040009221, 990018040009221, be51ab257069ffc78a4354437170f101
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000923
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:39 + 12 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009239
 

urn:imei:990018040009239, 990018040009239, 58d47f7bce3e6d1de1d9541e1831d89c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000924
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:41 + 12 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009247
 

urn:imei:990018040009247, 990018040009247, d9d55ff263801346225c64dcd6106692
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000925
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:34 + 12 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009254
 

urn:imei:990018040009254, 990018040009254, 07650f69db3088a6d9c79596d583bc22
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000926
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:36 + 12 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009262
 

urn:imei:990018040009262, 990018040009262, bebbf0e9455d48e1b9719c4022611d06
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000927
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:38 + 12 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009270
 

urn:imei:990018040009270, 990018040009270, f5c66e5481990563542f3c1248258114
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000928
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:40 + 12 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009288
 

urn:imei:990018040009288, 990018040009288, c3c68eafb2ca9c303518140cb6552b03
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000929
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 2 + ']

	 Odd Sum is: 12


	 Total sum:42 + 12 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009296
 

urn:imei:990018040009296, 990018040009296, 59ace7aca8757f7f2c14c985ba476527
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000930
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:33 + 13 = 46


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009304
 

urn:imei:990018040009304, 990018040009304, 7646c17d3e2ef6d903ad1df5235ad228
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000931
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:35 + 13 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009312
 

urn:imei:990018040009312, 990018040009312, cc7458c0f8bb628c3979027bfcac070c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000932
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:37 + 13 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009320
 

urn:imei:990018040009320, 990018040009320, aafd521c82b589943cf19dda55682c5e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000933
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:39 + 13 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009338
 

urn:imei:990018040009338, 990018040009338, 66dd30b40dc5e17135751590a0f2e11f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000934
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:41 + 13 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009346
 

urn:imei:990018040009346, 990018040009346, 168a88d94d4f540c2e85b6d7f31b9cdd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000935
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:34 + 13 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009353
 

urn:imei:990018040009353, 990018040009353, da4fda27b7274123ebfb0f3ba7647cc4
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000936
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:36 + 13 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009361
 

urn:imei:990018040009361, 990018040009361, 4112de3971b9a9db49d6f528f118ae50
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000937
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:38 + 13 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009379
 

urn:imei:990018040009379, 990018040009379, 284de01e8c553ec2cf254887b3ff19b1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000938
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:40 + 13 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009387
 

urn:imei:990018040009387, 990018040009387, 3606ceb1361066ee57aeb53e3fe5f216
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000939
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 3 + ']

	 Odd Sum is: 13


	 Total sum:42 + 13 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009395
 

urn:imei:990018040009395, 990018040009395, 6877fb832220fa33ad9fa6ccabfca118
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000940
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:33 + 14 = 47


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009403
 

urn:imei:990018040009403, 990018040009403, 3e4cfa664c5adf2470104b672330e6aa
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000941
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:35 + 14 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009411
 

urn:imei:990018040009411, 990018040009411, d179521cfdf2cb5ab71623bd988808b5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000942
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:37 + 14 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009429
 

urn:imei:990018040009429, 990018040009429, 01d7b47ac0a5e1d04a2f5744f653894b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000943
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:39 + 14 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009437
 

urn:imei:990018040009437, 990018040009437, e127b160a9594bdc7a0212bfc5f59958
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000944
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:41 + 14 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009445
 

urn:imei:990018040009445, 990018040009445, 297a04c89e7b02b4979387f5f57e93a2
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000945
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:34 + 14 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009452
 

urn:imei:990018040009452, 990018040009452, c868d17b060bedd9d14df1b7aeda8320
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000946
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:36 + 14 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009460
 

urn:imei:990018040009460, 990018040009460, d4add3702204436004b38534e0cb4780
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000947
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:38 + 14 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009478
 

urn:imei:990018040009478, 990018040009478, f2e199790803ee733de7ca2cb9595df5
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000948
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:40 + 14 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009486
 

urn:imei:990018040009486, 990018040009486, b940d2fcf619e2b8a3df36b1ba125a80
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000949
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 4 + ']

	 Odd Sum is: 14


	 Total sum:42 + 14 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009494
 

urn:imei:990018040009494, 990018040009494, c54c12d957d8129e7f4d39af4aca30bd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000950
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:33 + 15 = 48


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009502
 

urn:imei:990018040009502, 990018040009502, 1d94934edc35c2f3414a2a060b8674d7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000951
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:35 + 15 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009510
 

urn:imei:990018040009510, 990018040009510, a89fca79df78a4950f501df6e07c33cd
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000952
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:37 + 15 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009528
 

urn:imei:990018040009528, 990018040009528, 6f28eb799461d7ae889e57b6080bc82a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000953
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:39 + 15 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009536
 

urn:imei:990018040009536, 990018040009536, 09f5e957939a93b3a36792cb03d02956
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000954
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:41 + 15 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009544
 

urn:imei:990018040009544, 990018040009544, 65c177a5b8889b470b44037b46398733
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000955
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:34 + 15 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009551
 

urn:imei:990018040009551, 990018040009551, 7bd51c1b7a3d5bdf053adf7d7621b7d6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000956
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:36 + 15 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009569
 

urn:imei:990018040009569, 990018040009569, 6838f1026441c39313e8d8c73ba4f00a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000957
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:38 + 15 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009577
 

urn:imei:990018040009577, 990018040009577, c5e6eeb1287ee737ea6e456a3d07d21f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000958
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:40 + 15 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009585
 

urn:imei:990018040009585, 990018040009585, 3a1aa1305eda3cb747fb1a8c4dfb002b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000959
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 5 + ']

	 Odd Sum is: 15


	 Total sum:42 + 15 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009593
 

urn:imei:990018040009593, 990018040009593, 0a2b5ac521fc0be59da35fe0d30e2065
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000960
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:33 + 16 = 49


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009601
 

urn:imei:990018040009601, 990018040009601, a1b81460fa42b08718106ae2edeaf59d
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000961
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:35 + 16 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009619
 

urn:imei:990018040009619, 990018040009619, 33859785b121850459859fb933cba6bf
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000962
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:37 + 16 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009627
 

urn:imei:990018040009627, 990018040009627, 1119326e34f12324371a197646d1a98e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000963
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:39 + 16 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009635
 

urn:imei:990018040009635, 990018040009635, 57146d4af81cb6ef4a67483088e1a52c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000964
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:41 + 16 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009643
 

urn:imei:990018040009643, 990018040009643, 527dac7aa634361e72e073e65ac70927
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000965
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:34 + 16 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009650
 

urn:imei:990018040009650, 990018040009650, d6d2355c752732fa1ff21b7f1b3d2a1c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000966
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:36 + 16 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009668
 

urn:imei:990018040009668, 990018040009668, 17b2e08f189ad437f70b7dc26d649225
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000967
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:38 + 16 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009676
 

urn:imei:990018040009676, 990018040009676, 705961c8d45fec79ad425a20f90c8f21
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000968
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:40 + 16 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009684
 

urn:imei:990018040009684, 990018040009684, 3d9acba9f5ec232fd2f4014eb1815e8c
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000969
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 6 + ']

	 Odd Sum is: 16


	 Total sum:42 + 16 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009692
 

urn:imei:990018040009692, 990018040009692, 69e755aa60bb55bd8bc816c7c7002197
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000970
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:33 + 17 = 50


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009700
 

urn:imei:990018040009700, 990018040009700, 5a4694d49a1912339a396a39be1ff089
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000971
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:35 + 17 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009718
 

urn:imei:990018040009718, 990018040009718, 8e2a0d9f31197ccf5c5872f5a64101f3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000972
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:37 + 17 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009726
 

urn:imei:990018040009726, 990018040009726, cbcb9b6de5b8af4fb9c887c359c0394b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000973
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:39 + 17 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009734
 

urn:imei:990018040009734, 990018040009734, 6c155ec8c451b0087e95dbdf629017e7
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000974
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:41 + 17 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009742
 

urn:imei:990018040009742, 990018040009742, 05f4a882c81bcee7d2b244ee3c9b8945
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000975
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:34 + 17 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009759
 

urn:imei:990018040009759, 990018040009759, 47ae3b2f7a485d0afa9e6ea629fe7588
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000976
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:36 + 17 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009767
 

urn:imei:990018040009767, 990018040009767, 326f7b2e453b0902a5f8fd35e6270e64
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000977
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:38 + 17 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009775
 

urn:imei:990018040009775, 990018040009775, 5ec4210f810f3e2a4eda68c6808439c6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000978
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:40 + 17 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009783
 

urn:imei:990018040009783, 990018040009783, 4d928ed3fa06b5c4dff5199b4c72ab5b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000979
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 7 + ']

	 Odd Sum is: 17


	 Total sum:42 + 17 = 59


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009791
 

urn:imei:990018040009791, 990018040009791, 48f234cbe11fe4d798072f113ab1ecc3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000980
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:33 + 18 = 51


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009809
 

urn:imei:990018040009809, 990018040009809, e85bc5bc413e1c050aa69888399885ae
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000981
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:35 + 18 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009817
 

urn:imei:990018040009817, 990018040009817, a3b7c58f18a452ed4837473f5c381b6f
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000982
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:37 + 18 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009825
 

urn:imei:990018040009825, 990018040009825, 631c91555696155bb436ccba2bb1392b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000983
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:39 + 18 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009833
 

urn:imei:990018040009833, 990018040009833, 0e9cd3399ddefb386ff08d7cb2b4c42a
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000984
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:41 + 18 = 59


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009841
 

urn:imei:990018040009841, 990018040009841, d47e4cc5e6af51e669aa3a83e343c290
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000985
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:34 + 18 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009858
 

urn:imei:990018040009858, 990018040009858, 942e9b33a184a4e611bccdffc133bbd6
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000986
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:36 + 18 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009866
 

urn:imei:990018040009866, 990018040009866, 9c1eb22957a6ec54b7bfc52debc41425
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000987
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:38 + 18 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009874
 

urn:imei:990018040009874, 990018040009874, 9115df013054a85d945d155b4a41435e
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000988
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:40 + 18 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009882
 

urn:imei:990018040009882, 990018040009882, f7e23e9c752116a68b257cafdd54e44b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000989
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 8 + ']

	 Odd Sum is: 18


	 Total sum:42 + 18 = 60


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009890
 

urn:imei:990018040009890, 990018040009890, 680049bcfdb93de41d9b21a0305bc899
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000990
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [0] 0 + ']

	 Even Sum is: 33


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:33 + 19 = 52


	 The Calculated IMEI Checksum digit  is: 8
 

	 The correct 15 digit IMEI Number is: 990018040009908
 

urn:imei:990018040009908, 990018040009908, 8331f19278df4107f8f1a0b1269f7c51
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000991
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [1] 2 + ']

	 Even Sum is: 35


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:35 + 19 = 54


	 The Calculated IMEI Checksum digit  is: 6
 

	 The correct 15 digit IMEI Number is: 990018040009916
 

urn:imei:990018040009916, 990018040009916, ba3a6c4d83b1c5d34e0839d7955bc33b
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000992
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [2] 4 + ']

	 Even Sum is: 37


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:37 + 19 = 56


	 The Calculated IMEI Checksum digit  is: 4
 

	 The correct 15 digit IMEI Number is: 990018040009924
 

urn:imei:990018040009924, 990018040009924, 4b2a3947440b644d0a193c5589579563
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000993
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [3] 6 + ']

	 Even Sum is: 39


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:39 + 19 = 58


	 The Calculated IMEI Checksum digit  is: 2
 

	 The correct 15 digit IMEI Number is: 990018040009932
 

urn:imei:990018040009932, 990018040009932, c8c06b7572f5194ac84a07fca1fb6ee1
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000994
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [4] 8 + ']

	 Even Sum is: 41


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:41 + 19 = 60


	 The Calculated IMEI Checksum digit  is: 0
 

	 The correct 15 digit IMEI Number is: 990018040009940
 

urn:imei:990018040009940, 990018040009940, f7f3627c027d952757d429b9ed1ebbc8
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000995
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [5] 1 + ']

	 Even Sum is: 34


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:34 + 19 = 53


	 The Calculated IMEI Checksum digit  is: 7
 

	 The correct 15 digit IMEI Number is: 990018040009957
 

urn:imei:990018040009957, 990018040009957, 5335b733ea56c0f043a6f1e8d502eebf
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000996
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [6] 3 + ']

	 Even Sum is: 36


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:36 + 19 = 55


	 The Calculated IMEI Checksum digit  is: 5
 

	 The correct 15 digit IMEI Number is: 990018040009965
 

urn:imei:990018040009965, 990018040009965, f025b9afedfd96228c5afddfa9c72572
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000997
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [7] 5 + ']

	 Even Sum is: 38


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:38 + 19 = 57


	 The Calculated IMEI Checksum digit  is: 3
 

	 The correct 15 digit IMEI Number is: 990018040009973
 

urn:imei:990018040009973, 990018040009973, 182188069253aadfc938c188bb24dac3
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000998
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [8] 7 + ']

	 Even Sum is: 40


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:40 + 19 = 59


	 The Calculated IMEI Checksum digit  is: 1
 

	 The correct 15 digit IMEI Number is: 990018040009981
 

urn:imei:990018040009981, 990018040009981, 6487dfd7957328ce4af8c45adf90bb05
, MD2000 


	 The input 14 digit IMEI Number is: 99001804000999
 

 Evens: 
[' [9] 9 + ', ' [0] 0 + ', ' [8] 7 + ', ' [4] 8 + ', ' [0] 0 + ', ' [9] 9 + ', ' [9] 9 + ']

	 Even Sum is: 42


 Odds: 
[' 9 + ', ' 0 + ', ' 1 + ', ' 0 + ', ' 0 + ', ' 0 + ', ' 9 + ']

	 Odd Sum is: 19


	 Total sum:42 + 19 = 61


	 The Calculated IMEI Checksum digit  is: 9
 

	 The correct 15 digit IMEI Number is: 990018040009999
 

urn:imei:990018040009999, 990018040009999, 5bb8e19910f96199e9d2276db54f0c4c
, MD2000 

