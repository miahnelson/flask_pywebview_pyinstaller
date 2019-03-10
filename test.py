from flask import Flask
import webview
import sys
import threading

app = Flask(__name__)

@app.route('/')
def initial_page(): 
    return 'Hello World!'

def start_server():
    app.run()

if __name__ == '__main__':
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()
    webview.create_window("This is just a test", "http://127.0.0.1:5000/")
    sys.exit()