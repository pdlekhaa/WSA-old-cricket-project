#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:58:58 2022

@author: padmadanturty
"""

import requests
from bs4 import BeautifulSoup
import mysql.connector 

if __name__ == "__main__":
    cnx = mysql.connector.connect(user="wsa",
                                  host = "x",
                                  database = "x",
                                  password ="x")
    cursor = cnx.cursor(buffered=True)
 
    url = requests.get("https://stats.espncricinfo.com/ci/content/records/223646.html")
    soup = BeautifulSoup(url.text, 'html.parser')
    
    #rosterTable = soup.find("div", attrs={'class': 'd3-l-wrap' }).find("tbody")
    #rosterTable = soup.find("div", attrs={'id': 'div_roster' }).find("table")
   
    rosterTable = soup.find("div", attrs={'class': 'div630Pad'}).find("tbody")
    #print(rosterTable)
    
    
    tableRows = rosterTable.find_all("tr")
    #print(tableRows[1])
    
    for row in tableRows:
            columns = row.find_all("td")
            name = columns[0].text
            span = columns[1].text
            Matches = int(columns[2].text)
            Innings = int(columns[3].text)
            Not_outs = int(columns[4].text)
            Runs = int(columns[5].text)
            High_score = columns[6].text
            Avg = float(columns[7].text)
            Centuries = int(columns[8].text)
            Half_centuries = int(columns[9].text)
            Ducks = int(columns[10].text)
    
                      

        
            values = [name, span, Matches, Innings, Not_outs, Runs, High_score, Avg, Centuries, Half_centuries, Ducks]
            print(values)
            
     
            statement = "INSERT INTO Cricket_padma_danturty (name,span,Matches,Innings,Not_outs,Runs,High_score,Avg,Centuries,Half_centuries,Ducks)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(statement, values)
            cnx.commit()