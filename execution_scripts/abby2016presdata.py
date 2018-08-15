## Abby Nason
## File: mockconpres.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path="/Users/abbynason/Documents/MockCon/PresData2016/geckodriver")
##got to row 80 wait wait(30)
driver.implicitly_wait(90)

csvFile = open("presData2016.txt", "a")

##Texas
driver.get("https://data.opendatasoft.com/explore/dataset/"
           +"usa-2016-presidential-election-by-county%40public/"
           +"table/?sort=-rep16_frac&refine.state=Texas")

##Rhode Island
##driver.get("https://data.opendatasoft.com/explore/dataset/"
##           +"usa-2016-presidential-election-by-county%40public/"
##           +"table/?refine.state=Rhode+Island")



## for Texas: 254 rows in table, range(2, 256)
## for Rhode Island: 5 rows in table, range(2, 7)
for recordNumber in range(2, 256):
    listOfData = []
    for columnNumber in range(2, 9):
        dataLocation = driver.find_element_by_xpath("//tbody[@class='odswidget-table__records-tbody']"
                                                    +"/tr[" + str(recordNumber) + "]/td["+str(columnNumber)+"]/div/span")

##        dataLocation = driver.find_element_by_xpath("//table[@class='odswidget-table__internal-table']"
##                                                    +"/tbody[@class='odswidget-table__records-tbody']"
##                                                    +"/tr[@class='odswidget-table__internal-table-row record-"
##                                                    +str(recordNumber)+"']/td["+str(columnNumber)+ "]"
##                                                    +"/div[@class='odswidget-table__cell-container']"
##                                                    +"/span")
        aPieceOfData = dataLocation.get_attribute("innerHTML")
        csvFile.write(aPieceOfData + ",")
        listOfData.append(aPieceOfData)
    csvFile.write("\n")
##    print(listOfData)

csvFile.close()
driver.quit()

##odswidget-table__records-tbody
    ##column 0: row number
    ##column 1: state
    ##column 2: county
    ##column 3: Republicans 2016
    ##column 4: Democrats 2016
    ##column 5: Libertarians 2016
    ##column 6: Green 2016
    ##column 7: Votes <total>
    ##for cells in row


