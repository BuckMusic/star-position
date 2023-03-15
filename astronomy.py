#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      bucky
#
# Created:     23/06/2013
# Copyright:   (c) bucky 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#convert hh.mmssss to decimal time h.mmssss and str elements h,m,s,ms
def hms (tm):
    flag1 = 0           #flag initialy set to 0
    if float(tm) < 0:          #if number is negative
        flag1 = 1       #flag set to 1 means nenative number
        tm = abs(float(tm))    #use positive number to do equations
    t=('%.11f'%float(tm))      #make sure number is 11 decimal places
    h = t[:-12]         #h string is all left of decimal
    m = t[-11:-9]       #m string first 2 digits past decimal
    s = t[-9:-7]        #s string next 2 digits
    ms = t[-7:-5]       #ms string next 2 digits (not rounded up)
    dtm = (int(h) + (((int(s) + int(ms)/100)/60) + int(m))/60)
    if flag1 == 1:      #if negative then change back
        h = ('-' + h)   #h string with negative sign added
        dtm = dtm * -1  #decimal number changed to negative
    return dtm , h , m , s , ms
#convert decimal format HH.XXXX or DEGREE.XXXX to HH.MMSS or DEGREE.MMSS
def DecimaltoHMS (a):
    fract=a-int(a)              #fraction (remainder) of hour
    minutes=fract*60
    fract=minutes-int(minutes)  #fraction (remainder) of minutes
    seconds=fract*60
    hmstime=int(a)+int(minutes)/100+(round(seconds*100)/1000000)
    return hmstime
def date_leap_year(prompt,year,loyear,hiyear,month,day):
    running = True
    while running:
        date = input(prompt)
        try:
            i = float (date)
            running = False
            year = int(float(date))
            if year < loyear:
                print ('year too low')
                running = True
            if year > hiyear:
                print ('year too high')
                running = True
            leap_year=0
            if year%4==0:
                leap_year=1
                if year%100==0:
                    leap_year = 0
                    if (int(year/100)%4)==0:
                        leap_year=1
            Syear=str(year)
            month=int((float(date)-int(year))*100)
            Smonth = str(month)
            if month > 12:
                print ('month too high')
                running=True
            if month < 1:
                print ('month too low')
                running = True
            if month < 10:
                Smonth=('0'+str(month))
        # #determine number of days in Month
            Days_in_Month=30
            if month < 8:
                if month%2==1:
                    Days_in_Month=31
            if month > 7:
                if (month-7)%2==1:
                    Days_in_Month=31
            if month == 2:
                if leap_year==1:
                    Days_in_Month=29
                else:
                    Days_in_Month=28
            day=int(round((float(date)*100-int(float(date)*100))*100))
            Sday = str(day)
            if day < 10:
                Sday = ('0'+str(day))
            if day < 1:
                print ('days too low')
                running = True
            if day > Days_in_Month:
                print ('days too high')
                running = True
        except ValueError:
            print (date,'is not numeric')
    else:
            date = date
    return date,Syear,Smonth,Sday
def is_Number(name,hour,loH,hiH,minute,loM,hiM,second,loS,hiS):
    running = True
    while running:
        token = input(name)
        try:
            i = float(token)                #check if number and not string
            running = False
            dtoken,h,m,s,ms = hms(token)    #convert number to hh mm ss ms
            if int(h)<loH:                   #check if too low number
                running = True
                print (token,hour,'value',h,'less than',loH)
            if int(h) > hiH:                #check h not too high
                running = True
                print (token,hour,'value',h,'greater than',hiH)
            if int(m) < loM:
                runnin = True
                print (token,minute,'value',m,'less than',loM)
            if int(m) > hiM:                #check m not too high
                running = True
                print (token,minute,'value',m,'greater than',hiM)
            if int(s) < loS:
                running = True
                print (token,second,'value',s,'less than',loS)
            if int(s) > hiS:                #check s not too high
                running = True
                print (token,second,'value',s,'greater than',hiS)
        except ValueError:
            print (token,'is not numeric')  #input is not numeric
    else:
        token = token
    return token,h,m,s,ms,dtoken
import math
#equatorial to horizon conversion to altitude
def subaltitude (declination,latitude,decimalHA):
    return (math.degrees(
                math.asin(
                    math.sin(math.radians(declination))*
                    math.sin(math.radians(latitude))+
                    math.cos(math.radians(declination))*
                    math.cos(math.radians(latitude))*
                    math.cos(math.radians(decimalHA))
                    )))
def subazmuth1 (dec,lat,alt):#a=dec,b=lat,c=alt
    return ((
    math.degrees(
        math.acos(
            (
             math.sin(math.radians(dec))-
             math.sin(math.radians(lat))*
             math.sin(math.radians(alt))
             )/
             (
             math.cos(math.radians(lat))*
             math.cos(math.radians(alt))
             )
             ))))
time,h,m,s,ms,dtm = is_Number('h.mmssss ','hour',0,23,'minute',0,59,'seconds',0,59)
print ('input time ',time+' = '+h+':'+m+':'+s+'.'+ms,'  decimal time %.6f'%dtm)
date,yr,mn,dy = date_leap_year('input date yyyy.mmdd ','year',1583,5000,'month','day')
print ('input date ',date,'=',yr+'/'+mn+'/'+dy)
latitude,latd,latm,lats,latms,dlatitude = is_Number('latitude ','degrees',-90,90,'arc minutes',0,59,'arc seconds',0,59)
print ('input latitude ',latitude,'=',latd+u'\N{DEGREE SIGN}',latm+'\'',lats+'"','  decimal %.6f'%dlatitude)
longitude,lond,lonm,lons,ms,dlongitude = is_Number('longitude ','degrees',-180,180,'arc minutes',0,59,'arc seconds',0,59)
print ('input longitude ',longitude,'=',lond+u'\N{DEGREE SIGN}',lonm+'\'',lons+'"','  decimal %.6f'%dlongitude)
declination,decd,decm,decs,ms,ddec=is_Number('declination d.mmss ','degree',-90,90,'arc minutes',0,59,'arc seconds',0,59)
print ('input declination ',declination,'=',decd+u'\N{DEGREE SIGN}',decm+'\'',decs+'"','  decimal %.6f'%ddec)
Right_ascention,RAh,RAm,RAs,ms,dRA = is_Number('right ascention ','hour',0,23,'arc minutes',0,59,'arc seconds',0,59)
print ('input Right ascention ',Right_ascention,'=',RAh+'h',RAm+'\'',RAs+'"','  decimal %.6f'%dRA )
print ()
repeat = int(input('Input Loop how many times?  '))
xx=0                                #loop number
for i in range (repeat):                #loop range reassign for your needs
    xx=xx+1                         #incriment loop number
    print ('############################################ loop number',xx)
    print ('time UT         ',h+':'+m+':'+s+'.'+ms,'   decimal time %.6f'%dtm)
    print ('date            ',yr+'/'+mn+'/'+dy)
    print ('latitude        ',latd+u'\N{DEGREE SIGN}',latm+'\'',lats+'"','  decimal %.6f'%dlatitude)
    print ('longitude        ',lond+u'\N{DEGREE SIGN}',lonm+'\'',lons+'"','  decimal %.6f'%dlongitude)
    print ('declination     ',decd+u'\N{DEGREE SIGN}',decm+'\'',decs+'"','  decimal %.6f'%ddec)
    print ('Right ascention ',RAh+'h',RAm+'\'',RAs+'"','  decimal %.6f'%dRA )
    #julian date for dates later then 1582 october 15
#    ddt,y,m,d,ms = hms(date)
    print ('DATE UT ymd     ' ,yr + '/' + mn + '/' + dy)
    iyr = int(yr)              #year
    imn = int(mn)              #month
    idy = int(dy)              #day
    ddy=dtm/24              #percentage of day
    if imn < 3:
        iyr = iyr - 1
        imn = imn + 12
    A= int (iyr/100)
    B = (2 - A + int(A/4))
    C = int(365.25 * iyr )
    D = int(30.6001 * (imn + 1))
    JDm = B + C + D + idy + 1720994.5
#    print ('Julian Date  ' , JDm , 'midnight') #used to calculate sideral time
    JD = JDm + ddy
    print ('Julian Date      %.6f' % JD)
    print()
    #sideral time
    S = JDm - 2451545
    T = S/36525
    TO = 6.697374558 + (T * 2400.051336) + (T**2 * 0.000025862)
    temp = int (TO/24)
    if iyr > 2000:
        temp = temp + 1
    if iyr < 2000:
        temp = temp - 1
    TO1 = TO - (24 * temp)
    GST = dtm * 1.002737909 + TO1  #decimal form used to calculate LST
    if GST > 24:
        GST=GST-24
    if GST < 0:
        GST = GST + 24
    GSdtm,GSh,GSm,GSs,GSms = hms(DecimaltoHMS (GST))
    print ('GST             ',GSh + 'h ' + GSm + 'm ' + GSs + '.' + GSms + 's')
#    print ('decimal       %.8f' % GSdtm)
    #convert GST to LST
    LST = GSdtm - dlongitude/15  #decimal form
    if LST < 0:
        LST = LST + 24
    if LST > 24:
        LST = LST - 24
    LSdtm,LSh,LSm,LSs,LSms = hms(DecimaltoHMS (LST))
    print('Local Sideral   ',LSh + 'h ' + LSm + 'm ' + LSs + '.' + LSms + 's')
#    print('decimal       %.8f' % LSdtm)
    print ()
    HourAngle = LST - dRA        #otherwise input '0' for RA at input area
    if HourAngle < -12:
        HourAngle = HourAngle + 24
    if HourAngle > 12:
        HourAngle = HourAngle - 24
    HourAngle = DecimaltoHMS(HourAngle)
    print ('declination     ',decd+u'\N{DEGREE SIGN}',decm+'\'',decs+'"')
    print ('Right ascention ',RAh+'h',RAm+'\'',RAs+'"')
    dHA,HAh,HAm,HAs,HAms = hms(HourAngle)
    print('Hour Angle      ',HAh + 'h ' + HAm + '\'' + HAs + '.' + HAms + '"')
    #print('decimal       %.8f' % dHA)
    print ()
    #conversion from equatorial to horizon ALTITUDE
    decHA = 15*dHA
    Ddeclination=ddec
    altitude=subaltitude(Ddeclination,dlatitude,decHA)
    dal,ald,alm,als,alms = hms(DecimaltoHMS(altitude))
#    print ('altitude        ',ald + u'\N{DEGREE SIGN}' + alm + '\'' + als + '.' + alms + '"')
    print ('altitude         %.2f' % dal+u'\N{DEGREE SIGN}')
    #conversion from equatorial to horizon AZMUTH METHOD 1
    azmuth1=subazmuth1(Ddeclination,dlatitude,altitude)
    aazz=(math.sin(math.radians(decHA)))
    if aazz > 0:
            azmuth1 = 360-azmuth1
    daz,azd,azm,azs,azms = hms(DecimaltoHMS(azmuth1))
#    print ('azmuth          ',azd + u'\N{DEGREE SIGN}' + azm + '\'' + azs + '.' + azms + '"')
    print ('azmuth           %.2f' % daz+u'\N{DEGREE SIGN}')
    print ('############################################')
    time,h,m,s,ms,dtm = is_Number('h.mmssss UT ','hour',0,23,'minute',0,59,'seconds',0,59)
    print ('input time UT ',time+' = '+h+':'+m+':'+s+'.'+ms,'  decimal time %.6f'%dtm)
