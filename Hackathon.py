from wsgiref.simple_server import make_server
import psutil, datetime
import sqlite3

def server_health(environ, start_response):
	#print("ENVIRON:", environ)
	status = '200 OK'
	headers = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	message = "<h1>Server Health Monitor</h1>"
	message +="<table style=\"width:100%\">"
	message += "<tr>"
	message +="<td style=\"background-color:lightblue\"><strong>BOOT TIME:</strong></td>"
	boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
	message +="<td style=\"background-color:LIGHTGRAY\">"+str(boot_time)+"</td>"
	message += "<tr>"
	cpu_util = psutil.cpu_percent(interval=1, percpu=True)
	message += "<tr><th rowspan=\"4\"><strong>CPU UTILIZATION</strong></th>"
	
	count=1
	for cpu in cpu_util:
		if cpu < 50:
			message += "<td style=\"background-color:LIGHTYELLOW\">"
		else:
			message += "<td style=\"background-color:lightpink\">"
			
		message += "CPU {} : {}%".format(count, cpu)
		
		count+=1
		message += "</td></tr>"

	message += "<tr>"
	message +="<td style=\"background-color:lightblue\"><strong>AVAILABLE MEMORY:</strong></td>"
	mem = psutil.virtual_memory()
	message +="<td style=\"background-color:LIGHTGRAY\">"+str(mem.available)+"</td>"
	message += "<tr>"
	message +="<td style=\"background-color:lightblue\"><strong>USED MEMORY:</strong></td>"
	message +="<td style=\"background-color:LIGHTGRAY\">"+str(mem.used)+"</td>"
	message += "<tr>"

	# DUMP TO DATA BASE

	#create connection to server_health.sqlite database
	conn = sqlite3.connect("server_health.sqlite") 

	#provides are cursor to the above connection (the means of executing the SQL queries)
	cursor = conn.cursor()
	#cursor.execute("create table server_health(Parameter, Value)")
	Parameters = [ ('AVAILABLE MEMORY', str(mem.available)), ('BOOT TIME', str(boot_time)), ('CPU UTILIZATION', str(cpu_util))]
	#inset a row into the server_health table
	cursor.executemany("insert into server_health(name, count) values(?, ?)", Parameters)

	conn.commit() #commit changes to the database

	conn.close() #close the connection

	message += "<tr>"
	#message +="<td style=\"background-color:lightblue\"><strong>AVAILABLE MEMORY:</strong></td>"

	
	return[bytes(message,'utf-8')]

		
httpd = make_server('', 8000, server_health)
print("Serving on port 8000...")

httpd.serve_forever()

