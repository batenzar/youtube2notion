# youtube2notion
Read YouTube video metadata and then create a CSV file for using with Notion.

## Required plugin(s)
- [pytube](https://github.com/pytube/pytube)

## Usage
1. Type YouTube URL in `input.txt` (One link per line)
1. Generate CSV by `python App.py` command
1. Go to a page in notion that you wish to import to
1. Prepare the following notion page properties (First-time only)
    - Name (Text)
    - Author (Text)
    - Category
    - Finished On (Date)
    - Length (Text)
    - Link (URL)
    - Publishing/Release Date (Date)
    - Score /5
    - Status
    - Summary (Text)
    - Type
3. Go to page option on the upper-right, then select `Merge with CSV`
4. Select the output csv file

### Sample CSV output
```
Name,Author,Category,Finished On,Length,Link,Publishing/Release Date,Score /5,Status,Summary,Type

"Authentication on the Web (Sessions, Cookies, JWT, localStorage, and more)","Code Realm",,,00:37:05,https://www.youtube.com/watch?v=2PPSXonhIck,08-Nov-18,,,,Video
```

## Note
- Notion always appends new rows even though they are imported.


