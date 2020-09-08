#### PROGRAM, IT IS EXTENSION TO WEBDATA_EXTRACT, IN THIS WE SCROLLED OVER OTHER PAGES AND EXTRACTED THE DATA INTO csv. FILE(spreadsheet)


import csv
from selenium import webdriver

max_page=5  ### maximum no. of webpages, site can have
max_dig=3	### maximum no. of digits, a site page can have,,ex-001, this means max digits can be 3

with open('results1.csv','w') as f:  ### here we created a csv. file, and opened it in write mode, with f as variable name allocated to file
	f.write('Buyers'+'Price' +'\n')	 ### writing the headers in our file


fd=r"C:\\Users\\abhij\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\selenium\\geckodriver.exe"
 

driver=webdriver.Firefox(executable_path=fd)
									### here above, we defined the path for our driver


for i in range(1,max_page+1):       ### as we need to switch to different pages
	page_num=((max_dig - len(str(i)))*'0'+str(i))  ### this is the formula for current webpage number
	url='http://econpy.pythonanywhere.com/ex/'+page_num+'.html'  ### as the url gets changed for every webpage, we need to set variable URL according to 
																 ### the changes that are occuring from one webpage to another
	driver.get(url)   ### modified url, will be passed to our get method

	buyers=driver.find_elements_by_xpath('//div[@title="buyer-name"]')  ### extracting the data from current webpage
	prices=driver.find_elements_by_xpath('//span[@class="item-price"]') ### " "
	with open('results1.csv','a') as f:			### now we have to save our extracted data into a file, this time file will be opened up in 'append' mode
		for j in range(len(buyers)):			### range(len(buyers)), to be noted
			f.write(buyers[j].text+' : '+prices[j].text+'\n')   ### data is saved into respective form

driver.close()  ### driver and window both closed
