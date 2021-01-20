from pytube import YouTube
import datetime
import time

# Ref
# https://github.com/pytube/pytube
# https://thecleverprogrammer.com/2020/08/23/scraping-youtube-with-python/
# https://python-pytube.readthedocs.io/en/latest/api.html#youtube-object
# https://stackabuse.com/how-to-format-dates-in-python/
# https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/

url = 'https://www.youtube.com/watch?v=2PPSXonhIck'
yt = YouTube(url)
print(url)
print(yt.title)
print(yt.author)
# print(yt.description)
#print(yt.length)
print(time.strftime("%H:%M:%S", time.gmtime(yt.length)))
#print(yt.publish_date)
print(yt.publish_date.strftime("%b %d, %Y"))

# Name,Author,Category,Finished On,Length,Link,Publishing/Release Date,Score /5,Status,Summary,Type
#"Authentication on the Web (Sessions, Cookies, JWT, localStorage, and more)",Code Realm,,,0:37:05,https://www.youtube.com/watch?v=2PPSXonhIck,8-Nov-18,,,,Video

header = "Name,Author,Category,Finished On,Length,Link,Publishing/Release Date,Score /5,Status,Summary,Type"
csv = "\""+ yt.title + "\","
csv = csv + "\""+ yt.author + "\","
csv = csv + ","
csv = csv + ","
csv = csv + time.strftime("%H:%M:%S", time.gmtime(yt.length)) + ","
csv = csv + url + ","
csv = csv + yt.publish_date.strftime("%d-%b-%y") + ","
csv = csv + ","
csv = csv + ","
csv = csv + ","
csv = csv + "Video"
print(header)
print(csv)
