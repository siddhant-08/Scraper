import requests
from lxml import html
import xlwt

response=requests.get('http://cse.iitkgp.ac.in/faculty4.php?_=1450503917634')
parsed_body=html.fromstring(response.content)

count=0
name=[]
posn=[]
year=[]
email=[]
research=[]

for prof in parsed_body.xpath('.//td[@class="fcardcls"]'):
	count=count+1
	if(count==20):
		continue
	
	name_it=prof.xpath('.//tr[1]/td[2]/font[1]/b/a/b/text()')[0]
	name_it= ' '.join(name_it.split())  # removes the extra spaces between name and surname
	name.append(name_it)

	posn.append(prof.xpath('.//tr[1]/td[2]/font[2]/b[1]/text()')[0])
	
	joining=prof.xpath('.//tr[1]/td[2]/font[2]/text()[2]')[0]
	year.append(joining[-4:])

	email.append(prof.xpath('.//tr[1]/td[2]/font[2]/text()[6]')[0])

	research.append(prof.xpath('.//tr[2]/td/font/text()')[0])

# storing the results to an excel sheet
book=xlwt.Workbook()
sh=book.add_sheet("mysheet")
sh.write(0,0,"name")
sh.write(0,1,"posn")
sh.write(0,2,"year")
sh.write(0,3,"email")
sh.write(0,4,"research")
n=1

for m,e1 in enumerate(name,n+1):
	sh.write(m,0,e1)
for m,e2 in enumerate(posn,n+1):
	sh.write(m,1,e2)
for m,e3 in enumerate(year,n+1):
	sh.write(m,2,e3)
for m,e4 in enumerate(email,n+1):
	sh.write(m,3,e4)
for m,e5 in enumerate(research,n+1):
	sh.write(m,4,e5)
book.save("first.xlsx")
