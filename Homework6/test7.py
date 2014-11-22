from wsgiref.simple_server import make_server
import psutil, datetime


#def get_form_vals(post_str):
    #form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
    #return form_vals

def server_health(environ, start_response):
    #print("ENVIRON:", environ)
    #message=""
    #status = '200 OK'
    #headers = [('Content-type', 'html; charset=utf-8')]
    #start_response(status, headers)
    #if(environ['REQUEST_METHOD'] == 'POST'):
        #message += "<br>Your data has been recorded:"
        #request_body_size = int(environ['CONTENT_LENGTH'])
        #request_body = environ['wsgi.input'].read(request_body_size)
        #form_vals = get_form_vals(request_body)
        #for item in form_vals.keys():
            #message += "<br/>"+item + " = " + form_vals[item]
    message += "<h1>Server Health Monitor</h1>"
    message +="<table style=\"width:100%\">"
    message += "<tr>"
    message +="<td style=\"background-color:lightblue\"><strong>BOOT TIME:</strong></td>"
    
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    message +="<td style=\"background-color:Aqua\">"+str(boot_time)+"</td>"

    message += "<tr>"
    message +="<td style=\"background-color:white\"><strong>CPU UTILIZATION:</strong></td>"
    message += "<tr>"
    message +="<td style=\"background-color:lightblue\"><strong>AVAILABLE MEMORY:</strong></td>"
    
    #mem = psutil.virtual_memory()
    #THRESHOLD = 100 * 1024 * 1024  # 100MB
    #message += 
    message += "<tr>"
    message +="<td style=\"background-color:white\"><strong>USED MEMORY:</strong></td>"
    message += "<tr>"
    message +="<td style=\"background-color:lightblue\"><strong>USED PERCENTAGE:</strong></td>"

    message += "<br><br><input type='Submit' name='Done' ></table>"
    return[bytes(message,'utf-8')]

httpd = make_server('', 8000, server_health)
print("Serving on port 8000...")


httpd.serve_forever()