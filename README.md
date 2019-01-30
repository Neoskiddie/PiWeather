# PiWeather
Raspberry Pi weather station sending updates with temperature, pressure and humidity to Twitter.

You should use your own api keys in place of "password" is script.

If you want to add this script to cron add python shebang at the beggining:  
```
#!/usr/bin/env python3
```
and make it executable with: 
```
chmod u+x /path/to/thisScript.py
```
Open cron 
```
crontab -e
```
and add:
```
*/30 * * * * /path/to/thisScript.py 
```
It will run every thirty minutes
