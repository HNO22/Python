from wsgiref.simple_server import make_server
import psutil, datetime

def server_health(environ, start_response):
	status    = '200 OK'
	headers   = [('Content-type', 'html; charset=utf-8')]
	start_response(status, headers)
	message   = "<h1 style=\"color:crimson\">Server Health Monitor</h1>"
	message  += "<table style=width:60%>"
	message  += "<tr>"
	message  += "<td style=\"background-color:lavender\"><strong>BOOT TIME:</strong></td>"
	boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
	message  += "<td style=\"background-color:LIGHTGRAY\">"+str(boot_time)+"</td>"
	message  += "<tr>"
	cpu_util  = psutil.cpu_percent(interval=1, percpu=True)
	message  += "<td rowspan=4 ><strong>CPU UTILIZATION:</strong>"
	
	count=1
	for cpu in cpu_util:
		if cpu < 70:
			message += "<td style=\"background-color:lightyellow\">"
		else:
			message += "<td style=\"background-color:pink\" \"color:green\">"

		message += "CPU {}".format(count)+str(30*"&nbsp;")+"{}%".format(cpu)
		message += "</td></tr>"
		count += 1
	
	message += "<tr>"
	message += "<td style=\"background-color:lavender\"><strong>AVAILABLE MEMORY:</strong></td>"
	mem = psutil.virtual_memory()
	message += "<td style=\"background-color:LIGHTGRAY\">"+str(mem.available)+"</td>"
	message += "<tr>"
	message += "<td style=\"background-color:white\"><strong>USED MEMORY:</strong></td>"
	message += "<td style=\"background-color:LIGHTGRAY\">"+str(mem.used)+"</td>"
	message += "<tr>"
	message += "<td style=\"background-color:lavender\"><strong>USED PERCENTAGE:</strong></td>"
	message += "<td style=\"background-color:LIGHTGRAY\">"+str(mem.percent)+"%"+"</td>"

	return[bytes(message,'utf-8')]
	
httpd = make_server('', 8000, server_health)
print("Serving on port 8000...")

httpd.serve_forever()
