from flask import render_template, make_response, request
from app import app
import urllib
import json


@app.route('/')
def index():
    return render_template('index.html',
                            name='Ashwani',
                            slack_username='ashwani')


@app.route('/authors')
def authors():
    response = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users')
    users = json.loads(response.read().decode('utf-8'))
    response = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts')
    posts = json.loads(response.read().decode('utf-8'))
    for user in users:
        post_count = 0
        for post in posts:
            if user['id'] == post['userId']:
                post_count = post_count + 1
        user['post_count'] = post_count
    return render_template('authors.html',
                            authors=users)


@app.route('/setcookie')
def set_cookie():
    resp = make_response('<h1>Your cookies are now set!</h1><p>View them <a href="/getcookies">here</a></p>')
    resp.set_cookie('name', 'Ashwani')
    resp.set_cookie('age', '22')
    return resp


@app.route('/getcookies')
def get_cookies():
    return render_template('cookies.html',
                            name=request.cookies.get('name'),
                            age=request.cookies.get('age'))


@app.route('/robots.txt')
def deny_request():
    return '<h1>Access Denied</h1><a href="/">Go home</a>', 403


@app.route('/html')
def html():
    return render_template('text.html')


@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        input_text = request.form['input_text']
        print('Input given by client: ' + input_text)
        return render_template('input.html', input_text=input_text)
    return render_template('input.html')
