SAVAH DATA PROCESS
=====

Technology used:
    1. Python
    2. SQLite
    3. Javascript (chart)

1. The file which contains all the logic is main.py.

2. The script insert the output in a table in SQLite. The database is the file called havas.db

3. These files are also hosted in a AWS server where there is a chart which visualizes some parameters of the table: http://54.69.30.117/

4. The script is developed to run once per day using a Crontab to automate the processes. For testing purpose the crontab is not running.
    Create a Crontab with this command:
    13 20 * * * python /Users/ebertoburgosmendoza/Desktop/Interview/main.py   >> /var/log/script_output.log 2>&1

