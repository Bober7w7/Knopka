from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Path to the file where the status is stored
STATUS_FILE = 'status.txt'

def get_status():
    try:
        with open(STATUS_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return 'OFF'

def set_status(status):
    with open(STATUS_FILE, 'w') as f:
        f.write(status)

@app.route('/')
def index():
    # Check for status change in URL parameters
    # Usage: /?status=knopka_on or /?status=knopka_off
    status_param = request.args.get('status')
    
    if status_param == 'knopka_on':
        set_status('ON')
    elif status_param == 'knopka_off':
        set_status('OFF')
    
    current_status = get_status()
    return render_template('index.html', status=current_status)

if __name__ == '__main__':
    # Listen on all interfaces (0.0.0.0) for Docker accessibility
    app.run(host='0.0.0.0', port=5000)
