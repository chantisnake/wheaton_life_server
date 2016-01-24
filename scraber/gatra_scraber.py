import requests
from bs4 import BeautifulSoup
from helpers.general_function import strip_html


def request():
    """
    this function send a GET request to gatra 140 website and get the html that it returns
    :return: html that the website returns
    """
    headers = {
        "Accept": "text/html, application/xhtml+xml, image/jxr, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3",
        "Connection": "Keep-Alive",
        "Cookie": "__utma=3743270.1260580897.1449938850.1449938850.1449938850.1; __utmz=3743270.1449938850.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); wptouch_customizer_use=desktop",
        "Host": "www.gatra.org",
        "If-Modified-Since": "Fri, 28 Aug 2015 15:20:22 GMT",
        "If-None-Match": '"e5ad8e266749369a3533dacbf541dfbd55867fdb"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"
    }
    r = requests.get("http://www.gatra.org/index.php/routes/mansfield-norton/wheaton-t-shuttleroute-140/",
                     headers=headers)
    return r.text


def phrase_html_row(row_html, am_or_pm="am"):
    items = row_html.findAll("td")
    am_pm_tag = strip_html(items[0])
    if am_or_pm == "am" and am_pm_tag == "pm":
        am_or_pm = "pm"
    times = items[1:]
    row = [am_or_pm] + [strip_html(time) for time in times]
    return row


def html_phrasing(html):
    """
    this function takes the html that the website(gatra 140) returns
    and turn it into a 2D array that has all the info that you need
    *THIS METHOD SHOULD NOT BE USED OUTSIDE OF THIS PROGRAM*

    :param html: the html of gatra 140 website
    :return: a 2D array with
                the first row equals all the station names
                the first column corresponding to the am or pm of the start time of this row
                    (the time that the bus leave wheaton college)
             each item in the array is the time that the bus arrives at the corresponding station
    """
    soup = BeautifulSoup(html, "lxml")
    tables = soup.find_all("table")
    weekday_html_table = tables[2]
    saturday_html_table = tables[3]
    sunday_html_table = tables[4]

    table_header = ["Howard Street/Wheaton College",
                    'Great Woods Plz 175 Mansfield Ave. Norton, MA',
                    'Mans. Crossing 280 School St Mansfield, MA',
                    "Mansfield MBTA Bus Arrives 1 Crocker St Mansfield, MA",
                    "Mansfield MBTA Bus Arrives 1 Crocker St Mansfield, MA",
                    'Mans. Crossing 280 School St Mansfield, MA',
                    'Great Woods Plz 175 Mansfield Ave. Norton, MA',
                    "Howard Street/Wheaton College", ]
    weekday_table = [table_header]
    saturday_table = [table_header]
    sunday_table = [table_header]

    # process weekday table
    table = weekday_html_table
    rows = table.findAll("tr")[3:-2]
    for row in rows:
        temp_row = phrase_html_row(row)
        weekday_table.append(temp_row)

    # process saturday table
    table = saturday_html_table
    rows = table.findAll("tr")[2:]
    for row in rows:
        temp_row = phrase_html_row(row)
        saturday_table.append(temp_row)

    # process sunday table
    table = sunday_html_table
    rows = table.findAll("tr")[2:-5]
    for row in rows:
        temp_row = phrase_html_row(row)
        sunday_table.append(temp_row)

    return weekday_table, saturday_table, sunday_table


def scrabe_gatra_info():
    """
    *THIS IS THE ONLY METHOD TO USE OUTSIDE OF THIS FILE*
    this method will return you the time table of gatra 140 with a 2D array

    :return: returns three 2D array corresponding to weekday schedule, saturday schedule and sunday schedule
    """
    html = request()
    return html_phrasing(html)


if __name__ == "__main__":
    html = request()
    weekday, saturday, sunday = html_phrasing(html)
    for row in weekday:
        print(row)
