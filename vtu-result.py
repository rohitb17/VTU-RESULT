# python code to check if result of student is available in vtu result site and to download result into a html file which can be viewed by user

# INSTRUCTIONS
# change the usn in code as per need
# the below statement can be used to run the code
# python vtu-result.py &
# once the result is acquired the file will be created in same directory as this file

import schedule
import time
from mechanize import Browser


def job():
    print "started job"
    br = Browser()
    br.open("http://results.vtu.ac.in/vitavi.php")
    br.select_form(name="new")
    br.form[ 'rid' ] = '1pe12cs001'
    response = br.submit()  # submit current form
    html=response.read()

    if "1pe12cs001" in html:
        fo = open("VTU-result.html", "w")
        fo.write(html)
        fo.close()
        exit()


# i have kept it to start a job every 2 mins
schedule.every(2).minutes.do(job)

#the below statement can be used to schedule job at particular time each day as well
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)


