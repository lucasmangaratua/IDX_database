# IDX's Stocks and Prices Database  

* Data extraction through Yahoo Finance stock price using ticker.
* Data storing to internal storage.
* Repeat extraction and data storing automatically using [crontab](https://crontab.guru).
* Programming Language: Python and SQL.  
  
## Final SQLite look  
![](https://github.com/lucasmangaratua/IDX_database/blob/main/Screen%20Shot%20SQLite.png) 

## Steps
* Run the python [code](https://github.com/lucasmangaratua/IDX_database/blob/main/database.py). Now you have all the IDX daily prices data.
* Use crontab for updated log in SQL database. Open terminal > type: `crontab -e` > paste this [line](https://github.com/lucasmangaratua/IDX_database/blob/main/crontab_line.odt) correspond to file directory.

## Future development
* This code is not yet take updated price data into account. Change looping data, and adjust it for current date only.
* Integrate API to update listed company in IDX regularly.
