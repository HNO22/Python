from wsgiref.simple_server import make_server
import psutil, datetime
import sqlite3
import re
import tkinter
from tkinter import messagebox


def server_health(environ, start_response):
    #print("ENVIRON:", environ)
    message=""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)

    message += "<h1>Server Health Monitor</h1>"
    message += "<table style=\"width:50%\" method='POST'>"
    message += "<tr>"
    message += "<td style=\"background-color:gray\"><strong>BOOT TIME:</strong></td>"
    boot_time= datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    message += "<td style=\"background-color:gray\">"+str(boot_time)+"</td>"
    message += "</tr>"
    cpu_util = psutil.cpu_percent(interval=1, percpu=True)
    message += "<tr><th rowspan=\"2\"><strong>CPU UTILIZATION</strong></th>"
    
    count =1
    for cpu in cpu_util:
        if cpu < 20:
            message += "<td style=\"background-color:blue\">"
        else:
            message += "<td style=\"background-color:red\">"
            
        message += "CPU {} : {}%".format(count, cpu)
        
        count+=1
        message += "</td></tr>"

    mem = psutil.virtual_memory()
    THRESHOLD = 100 * 1024 * 1024  # 100MB
    message += "<tr>"
    message +="<td style=\"background-color:gray\"><strong>AVAILABLE MEMORY:</strong></td>"
    message +="<td style=\"background-color:gray\">"+str(mem.available)+"</td>"
    message +="</tr>"
    message +="<td><strong>USED MEMORY:</strong></td>"
    message +="<td>"+str(mem.used)+"</td>"
    message +="</tr>"
    message +="<td style=\"background-color:gray\"<strong>USED PERCENTAGE:</strong></td>"
    message +="<td style=\"background-color:gray\">"+str(mem.percent)+"</td>"
    message +="</tr>"

    message += "<br><br><input type='Done' name='Done' ></form>"

    return[bytes(message,'utf-8')]

httpd = make_server('', 8000, server_health)
print("Serving on port 8000...")


httpd.serve_forever()


def ServerCallBack():
   messagebox.showinfo( "Server Health Monitor", server_health())

base = tkinter.Tk()
button = tkinter.Button(base, text="show the status of CPU", command=ServerCallBack)
button.pack()
base.mainloop()