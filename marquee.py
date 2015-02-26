import urllib2
import re
from bs4 import BeautifulSoup
import smtplib  

opener= urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

with open ("marqueemail.txt", "r") as myfile:
    data1=myfile.read()

url = ('http://marqueelasvegas.com/enhancedCalendar.cfm?date=06/05/14&showroom=0')

ourUrl = opener.open(url).read()

soup = BeautifulSoup(ourUrl)

sets = soup.find_all('div',class_='eventInfo')

outToFile = open('marquee.txt', mode='w')
outToFile.write(str(sets))
outToFile.close()
'''

for i in sets:
    i= re.match('eventInfo',str(sets))
    print i
    outToFile.write(str(i)+ '\n\n')

outToFile.close()

'''
f = open('marquee.txt')

strToSearch = ""

for line in f:
    strToSearch += line

#print(strToSearch)

#compile method says what regular expression you want to search for
patFinder1 = re.compile('<span>.*?</span>')
patFinder2 = re.compile('<span>')
patFinder3 = re.compile('</span>')

findPat1 = re.search(patFinder1, strToSearch)

#.group prints what was found
try:
    #print(findPat1.group())
    findPat1 = re.findall(patFinder1, strToSearch)
    outToFile = open('marqueemail.txt', mode='w')
    outToFile.write('')
    outToFile.close()

    outToFile = open('marqueemail.txt', mode='a+')
    for i in findPat1:
        print(i)
        outToFile.write(i+'\n')
    
    outToFile.close()
    with open ("marqueemail.txt", "r") as myfile:
        data=myfile.read()
        subFound = patFinder2.sub('', data)
        subFound2 = patFinder3.sub('', subFound)
    if data1==data:
        print 'No change'
    else:
        fromaddr = 'jwilksftw@gmail.com'  
        toaddrs  = 'jwilksftw@gmail.com'  
        msg = subFound2
  
  
        # Credentials (if needed)  
        username = ''  
        password = ''  
  
        # The actual mail send  
        server = smtplib.SMTP('smtp.gmail.com:587')  
        server.ehlo()
        server.starttls()
        server.ehlo()  
        server.login(username,password)  
        server.sendmail(fromaddr, toaddrs, msg)  
        server.quit()      

except AttributeError:
    print "no Marquee"


