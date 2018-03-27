#!/usr/bin/python
# -*- coding: utf-8 -*-

logo = """
_     _                        _ _     ______                                              
| |   | |      _               (_) |   / _____)                             _               
| |__ | | ___ | |_  ____   ____ _| |  | /  ___  ____ ____   ____  ____ ____| |_  ___   ____ 
|  __)| |/ _ \|  _)|    \ / _  | | |  | | (___)/ _  )  _ \ / _  )/ ___) _  |  _)/ _ \ / ___)
| |   | | |_| | |__| | | ( ( | | | |  | \____/( (/ /| | | ( (/ /| |  ( ( | | |_| |_| | |    
|_|   |_|\___/ \___)_|_|_|\_||_|_|_|   \_____/ \____)_| |_|\____)_|   \_||_|\___)___/|_|   
"""

print(logo)

name = input("Enter Name To Generate >> ")
num = input("Enter Emails Number >> ")
main = 0

while True:
	main = main + 1
	print(str(name) + str(main) + "@hotmail.com")
	if(int(main) == int(num)):
		break