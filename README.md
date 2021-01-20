# youtube2notion

## Require plugin
- pytube

## How to generate
1. Type youtube URL in `input.txt` (One link per line)
1. Run `python App.py`

### Sample Console output (as CSV)
```
Name,Author,Category,Finished On,Length,Link,Publishing/Release Date,Score /5,Status,Summary,Type
"Authentication on the Web (Sessions, Cookies, JWT, localStorage, and more)","Code Realm",,,00:37:05,https://www.youtube.com/watch?v=2PPSXonhIck,08-Nov-18,,,,Video
```

## How to import CSV to Notion
1. Go to any notion page that you wish to import
1. Prepare page property
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
1. Go to page option on the upper-right, then select `Merge with CSV`