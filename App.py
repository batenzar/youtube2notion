""" Read URL for information and generate CSV string.

Sample Result ->
"Title","Channel",,,0:37:05,https://www.youtube.com/watch?v=xxxxxxx,8-Nov-18,,,,Video

:param url: the Youtube video url
"""

from pytube import YouTube
import time
import csv

urls = list(open("input.txt"))
with open("output.csv", mode="w", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file,
                            ["Name", "Author", "Category", "Finished On", "Length", "Link", "Publishing/Release Date",
                             "Score /5", "Status", "Summary", "Type"])

    writer.writeheader()
    for url in urls:
        yt = YouTube(url)

        # Other information that can be retrieved
        # print(yt.description)

        writer.writerow({
            "Status": "Not started yet",
            "Name": yt.title.replace(",", "."),  # remove comma from string to fix import to notion issue
            "Author": yt.author,
            "Length": time.strftime("%H:%M:%S", time.gmtime(yt.length)),
            "Link": url,
            "Publishing/Release Date": yt.publish_date.strftime("%d-%b-%y"),
            "Type": "Video"
        })

# Ref
# https://github.com/pytube/pytube
# https://thecleverprogrammer.com/2020/08/23/scraping-youtube-with-python/
# https://python-pytube.readthedocs.io/en/latest/api.html#youtube-object
# https://stackabuse.com/how-to-format-dates-in-python/
# https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/
# https://realpython.com/python-csv/
# https://stackoverflow.com/questions/904041/reading-a-utf8-csv-file-with-python
