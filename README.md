# Seek
Simple script to watch job listings on seek.co.nz

# Installation
requests, lxml, and cursor are required to be installed

    python3 -m pip install requests lxml cursor

# Usage
For now you will need to hand edit the following variables in order to get the results you want:
* WAIT - Number of seconds between refresh
* MAXRESULTS - Number of results to be displayed
* SEARCH - Search string
* SALMIN - Index of salaryValues that represents the minimum salary to be searched for
* SALMAX - Max salary searched for, leave it as is
* LOCATION - Index of locations that represents the area you are looking for work

Run the application with `./seek.py`

![Screenshot](Selection_009.png)
