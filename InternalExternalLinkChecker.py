import requests
from bs4 import BeautifulSoup
import csv
import datetime 


def extIntLinks(allLinks, pageUrl):
    #filename 
    currentTime = datetime.datetime.now()
    #create a unique .csv file name using the datetime module
    filename =  f"Links-{currentTime.day}-{currentTime.month}-{currentTime.year} {currentTime.hour}{currentTime.minute}{currentTime.second}.csv"

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Tested Url','Link', 'Type']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        internalLinks = 0
        externalLinks = 0 

        #go through all the <a> elements list 
        for anchor in allLinks:
            link = anchor.get("href")   #get the link from the <a> element
            
            #check if the link is internal
            if link.startswith(pageUrl) or link.startswith("/") or link.startswith("#") :
                writer.writerow({'Tested Url':pageUrl,'Link': link, 'Type': 'Internal'})
                internalLinks+=1
            #if the link is external
            else:
                writer.writerow({'Tested Url':pageUrl,'Link': link, 'Type': 'External'})
                externalLinks+=1
        writer = csv.writer(csvfile)
        writer.writerow(["Total Internal Links", f"{internalLinks}", "Total External Links", f"{externalLinks}"])
        
        print(f"The page {url} has {internalLinks} Internal Link(s) and {externalLinks} External Link(s)")
        print(f"And data has been saved in the {filename}")


#parse all the links from the web page
def parseLinks(pageHtml, pageUrl):
    soup = BeautifulSoup(pageHtml, 'html.parser')

    #get all the <a> elements from the HTML page
    allLinks = soup.find_all('a')

    extIntLinks(allLinks, pageUrl)

#to make the HTTP request to the give url
def requestMaker(url):
    try:
        #make the get request to the url
        response = requests.get(url)

        #if the request is successful
        if response.status_code in range(200, 300):
            #extract the page html content for parsing the links
            pageHtml = response.text
            pageUrl = response.url

            #call the parseLink function
            parseLinks(pageHtml, pageUrl)
        
        else:
            print("Sorry Could not fetch the result status code {response.status_code}!")

    except:
        print(f"Could Not Connect to url {url}")



if __name__ == "__main__":
    url = input("Enter the URL eg. https://example.com:  ")
    requestMaker(url)
