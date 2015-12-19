# lxml-Scraper
Scraping data from the faculty page of Computer Science Dept. IIT Kharagpur

Strictly for educational purposes
All the data is publicly available on the webpage 

Used requests and lxml to scrape data from [this page](http://cse.iitkgp.ac.in/index.php?secret=d2RkOUgybWlNZzJwQXdLc28wNzh6UT09)

The main content is loaded from a different endpoint via an XHR request. [Here](http://cse.iitkgp.ac.in/faculty4.php?_=1450509124999)

Used the xlwt library to import the data to an excel workbook.

Would like to thank SO user [alecxe](http://stackoverflow.com/users/771848/alecxe) for helping me out.
