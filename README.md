## Scraper
Scraping faculty data from the faculty page of Computer Science and Engineering Dept. IIT Kharagpur

Strictly for educational purposes !!

Only the data publicly available on the webpage is used . 

Used requests and lxml to scrape data from [this page](http://cse.iitkgp.ac.in/index.php?secret=d2RkOUgybWlNZzJwQXdLc28wNzh6UT09)

The main content is loaded from a different endpoint via an XHR request. [Here](http://cse.iitkgp.ac.in/faculty4.php?_=1450509124999)

Used the xlwt library to export the data to an excel workbook.

Would like to thank SO user [alecxe](http://stackoverflow.com/users/771848/alecxe) for helping me out.

Report bugs and suggestions to [siddhantsingh707@gmail.com](mailto:siddhantsingh707@gmail.com)
