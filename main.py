from flask import Flask, render_template_string, redirect, request
import os

app = Flask(__name__)

# HTML templates
index_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Protected Page</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-image: url('https://iili.io/2Kfc5s2.jpg');
            background-size: cover;
            color: white;
            text-align: center;
        }
        input, button {
            margin-top: 10px;
        }
    </style>
</head>
<body>

<h1>SteVeN</h1>
<form method="POST">
    <input type="password" name="password" placeholder="Enter Password" required>
    <button type="submit">OK</button>
</form>

</body>
</html>
'''

welcome_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-image: url('https://iili.io/2Kfc5s2.jpg');
            background-size: cover;
            color: white;
            text-align: center;
        }
        #welcomeMessage {
            padding: 20px;
            border: 2px solid white;
            border-radius: 10px;
            background-color: rgba(0, 0, 0, 0.5);
        }
        button {
            margin-top: 20px;
            padding: 10px 20px;
            font-size: 16px;
            background-color: yellow;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>

<div id="welcomeMessage">
    <h2>Hello, I'm Steven X Shayan</h2>
    <a href="/visit"><button>Click to visit your server</button></a>
</div>

</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'STEVEN00':
            return render_template_string(welcome_html)
        else:
            return "Incorrect Password", 403
    return render_template_string(index_html)

@app.route('/visit')
def visit():
    return redirect('https://steven-zqlg.onrender.com/')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    
