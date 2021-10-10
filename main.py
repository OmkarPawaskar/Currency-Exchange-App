"""
This is executable file used to run application
"""

from app import flask_app

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port = 5000 )
