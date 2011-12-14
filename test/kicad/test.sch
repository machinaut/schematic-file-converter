EESchema Schematic File Version 2  date Mon 12 Dec 2011 05:12:14 PM PST
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:test-cache
EELAYER 25  0
EELAYER END
$Descr A4 11700 8267
encoding utf-8
Sheet 1 1
Title ""
Date "13 dec 2011"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L LAA110 U3
U 1 1 4EE59331
P 1650 3400
F 0 "U3" H 1650 3600 60  0000 C CNN
F 1 "LAA110" H 1650 3200 60  0000 C CNN
	1    1650 3400
	0    -1   -1   0   
$EndComp
$Comp
L NSL-32 U2
U 1 1 4EE58F9A
P 1750 2400
F 0 "U2" H 1830 2580 40  0000 C CNN
F 1 "NSL-32" H 1750 2227 40  0000 C CNN
	1    1750 2400
	-1   0    0    1   
$EndComp
$Comp
L 74LS00 U1
U 1 1 4EE57ED5
P 1700 1250
F 0 "U1" H 1700 1300 60  0000 C CNN
F 1 "74LS00" H 1700 1150 60  0000 C CNN
	1    1700 1250
	0    1    1    0   
$EndComp
Wire Wire Line
	5150 4050 6900 4050
Wire Wire Line
	3250 3950 2700 3950
Wire Wire Line
	2700 3950 2700 6450
Wire Wire Line
	6100 4650 6100 4950
Wire Wire Line
	6100 4950 6100 5350
Wire Wire Line
	6100 4650 5150 4650
Wire Wire Line
	5900 2700 6450 2700
Wire Wire Line
	6450 2700 6450 2000
Wire Wire Line
	6450 2000 5000 2000
Wire Wire Line
	5000 2000 5000 3000
Wire Wire Line
	6900 3100 7550 3100
Wire Wire Line
	7550 3100 7550 3500
Wire Wire Line
	7550 3500 6900 3500
Wire Wire Line
	6900 4050 6900 4950
Wire Wire Line
	2700 6650 2950 6650
Wire Wire Line
	2950 6650 2950 4450
Wire Wire Line
	2950 4450 3250 4450
Wire Wire Line
	6900 4950 6100 4950
Connection ~ 6100 4950
Wire Wire Line
	6100 5350 5150 5350
Text Label 6350 4050 0    60   ~ 0
PWR
$Comp
L LP3966 U4
U 1 1 4E8E0625
P 1900 6750
F 0 "U4" H 2000 7200 60  0000 L CNN
F 1 "LP3966" H 2000 6250 60  0000 L CNN
	1    1900 6750
	1    0    0    -1  
$EndComp
$Comp
L ATMEGA8-P IC1
U 1 1 4E8DFDD4
P 4150 4850
F 0 "IC1" H 3450 6100 50  0000 L BNN
F 1 "ATMEGA8-P" H 4400 3450 50  0000 L BNN
F 2 "DIL28" H 4650 3375 50  0001 C CNN
	1    4150 4850
	1    0    0    -1  
$EndComp
$EndSCHEMATC
