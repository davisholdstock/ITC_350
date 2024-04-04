# ITC_350
This is for our ITC_350 project


To get started for windows download both the <a href="https://dev.mysql.com/downloads/mysql/">MySQL community server</a>, and the <a href="https://dev.mysql.com/downloads/shell/">MySQL shell

To install mySQL and mySQL shell on linux:
1. Run ```sudo apt-get install mysql-server``` (version 8.0.36)
2. Run ```sudo apt-get install mysql-shell``` (version 8.0.23)

Configure the Server, creating a password for the root user, which will be used to log in to the CLI.
![image](https://github.com/davisholdstock/ITC_350/assets/112412321/a6355fbb-580f-4cf3-9adf-7c9aa87edc68)

For remote users log in with this command: ```mysqlsh -u <username> -p<password> -h <hostname> --sql```

## To run the website using Flask
1. Install python (version 3.10.12)
2. Install pip (version 22.0.2)
3. Run ```pip install Flask``` (version 3.0.2)
4. Run ```pip install python-dotenv``` (version 1.0.1)
5. Run ```pip install mysql-connector-python```
