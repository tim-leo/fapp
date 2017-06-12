import os
import sys
import site


# Path of execution

# sys.path.append('/var/www/fapp')

# import my_flask_app as application
# from fapp import app
# application = app
def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!\n'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
