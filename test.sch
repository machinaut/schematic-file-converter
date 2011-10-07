EESchema Schematic File Version 2  date Thu 06 Oct 2011 03:49:44 PM EDT
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
LIBS:noname-cache
EELAYER 24  0
EELAYER END
$Descr A4 11700 8267
Sheet 1 1
Title ""
Date "6 oct 2011"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	3250 4450 2950 4450
Wire Wire Line
	2950 4450 2950 6650
Wire Wire Line
	2950 6650 2700 6650
Wire Wire Line
	5150 4050 6900 4050
Wire Wire Line
	6900 4050 6900 4950
Wire Wire Line
	6900 4950 6100 4950
Connection ~ 6100 4950
Wire Wire Line
	6900 3500 7550 3500
Wire Wire Line
	7550 3500 7550 3100
Wire Wire Line
	7550 3100 6900 3100
Wire Wire Line
	5000 3000 5000 2000
Wire Wire Line
	5000 2000 6450 2000
Wire Wire Line
	6450 2000 6450 2700
Wire Wire Line
	6450 2700 5900 2700
Wire Wire Line
	5150 4650 6100 4650
Wire Wire Line
	6100 4650 6100 5350
Wire Wire Line
	6100 5350 5150 5350
Wire Wire Line
	2700 6450 2700 3950
Wire Wire Line
	2700 3950 3250 3950
$Comp
L LP3966 U?
U 1 1 4E8E0625
P 1900 6750
F 0 "U?" H 2000 7200 60  0000 L CNN
F 1 "LP3966" H 2000 6250 60  0000 L CNN
	1    1900 6750
	1    0    0    -1  
$EndComp
$Comp
L ATMEGA8-P IC?
U 1 1 4E8DFDD4
P 4150 4850
F 0 "IC?" H 3450 6100 50  0000 L BNN
F 1 "ATMEGA8-P" H 4400 3450 50  0000 L BNN
F 2 "DIL28" H 4650 3375 50  0001 C CNN
	1    4150 4850
	1    0    0    -1  
$EndComp
$EndSCHEMATC
