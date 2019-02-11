
import DS1307
import time
import datetime
import csv
import pylepton_capture as pc
import numpy as np
import cv2
import RPi.GPIO as GPIO


clock = DS1307.DS1307(1, 0X68)

redLED = 19

GPIO.setmode(GPIO.BCM)	
GPIO.setup(redLED, GPIO.OUT)
GPIO.output(redLED, True)


with open ('bigguy/clockreadings.csv','w') as a:
	datetimewriter = csv.writer(a)
	datetimewriter.writerow(['Fulldate','Hours','minutes','Seconds','a','b','c'])
	count = 0
	while True:
		if GPIO.input(redLED):
			GPIOstatus = True
		else:
			GPIOstatus = False	
		while GPIOstatus:
			count = count+1
			rtc_time = clock.read_datetime()
			print "rtc_time = ", rtc_time
			rtc_time = rtc_time.timetuple()
			startTime = (rtc_time[3]*60*60) +(rtc_time[4]*60 +rtc_time[5])
			dtime = 0
			while dtime < 1:
				rtc_time2 = clock.read_datetime()
				rtc_time2 = rtc_time2.timetuple()
				currentTime = (rtc_time2[3]*60*60 + rtc_time2[4]*60 + rtc_time2[5])
				dtime = currentTime - startTime
			a,b,c = pc.capture()
			
			print clock.read_datetime()
			finaltime = clock.read_datetime()
			finaltime = finaltime.timetuple()
			secs = finaltime[5]
			mins = finaltime[4]
			hours = finaltime[3]
			fulldate = clock.read_datetime()
			datetimewriter.writerow ([fulldate,hours,mins,secs,a,b,c])	
			cv2.imwrite(str(count)+'.png', a)
			if count == 3:
				GPIO.output(redLED, False)
