import multiprocessing

bind = "127.0.0.1:5005"

##WORKER PROCESSES
#The number of worker processes for handling requests.
#--workers / -w
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 4

#The number of worker threads for handling requests.
#--threads INT
threads = 1

#----------------------------------------------------------------------------------------
##DEBUGGING
#To be used only for development environment and not in production
#--reload
reload = True 

#Install a trace function that spews every line executed by the server.
#--spew
spew = False

#Check the configuration and exit. The exit status is 0 if the configuration is correct, and 1 if the configuration is incorrect.
#--check-config
check_config = False

#Print the configuration settings as fully resolved. Implies check_config.
#--print-config
print_config = False

#----------------------------------------------------------------------------------------
##LOGGING
#The Access log file to write to. (Logs file in real-time)
#--access-logfile FILE
accesslog = "accessLog.txt"

#The Error log file to write to. (Doesn't show output if errorlog is mentioned)
#--error-logfile FILE
# errorlog = "errorLog.txt"

#Using '-' for FILE makes gunicorn log to stderr. (Show output)
errorlog = "-"

#The granularity of Error log outputs.
#Valid level names are: 'debug' 'info' 'warning' 'error' 'critical'
#--log-level LEVEL
loglevel = "info"

#Redirect stdout/stderr to specified file in errorlog.
#--capture-output
# capture_output = False

##PROCESS NAMING
#If you’re going to be running more than one instance of Gunicorn you’ll probably want to set a name to tell them apart.
#--name STRING
# proc_name = "ankesh"

##SSL