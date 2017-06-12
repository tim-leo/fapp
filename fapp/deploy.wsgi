import os
import sys
import site


# Path of execution

sys.path.append('/var/www/fapp/fapp')

# import my_flask_app as application
# from fapp  import app
# application = app
# def application(environ, start_response):
#     status = '200 OK'
#     output = 'Hello World!\n'
#     response_headers = [('Content-type', 'text/plain'),
#                         ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)
#     return [output]
path = os.path.join(os.path.dirname(__file__), os.pardir)
if path not in sys.path:
    sys.path.append(path)

# The application object is used by any WSGI server configured to use this
# file.

# Ensure there is an app.py script in the current folder
from fapp import app as application
