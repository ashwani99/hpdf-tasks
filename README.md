# hpdf-tasks

## Description
This repository contains tasks that I have worked on during HPDF Week 1

## How to use
1. Clone the repository
```bash
git clone https://github.com/ashwani99/hpdf-tasks
```
2. Create a virtual environment and activate it. We will be setting Python 3 as default in the virtual environment. Although this step is not mandatory but it is recommended so that the development environment is isolated.
```bash
virtualenv venv --python=`which python3`
```
```bash
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the application within the devserver provided by flask
```bash
cd hpdf-tasks/
```
```bash
python run.py
```
5. All set. Fire up any web browser and go to `http://127.0.0.1:5000/` to see the application live!

## Tasks
These tasks consists of implementation of multiple endpoints which serve different needs. The following tasks are are accomplished.
* [x] Add an endpoint at `/` that displays `Hello World` along with your first name (and slack username)
* [x] Add and endpoint at `/authors` which fetches a list of authors and count of their posts using the given JSON data available via URLs [https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users) and [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)  
* [x] Add an endpoint at `/setcookie` which sets a cookie with values `name=<your-first-name>` and `age=<your-age` if not set already.
* [x] Add an endpoint at `/getcookies` which displays the values of the cookie that has been set with `/setcookie` endpoint.
* [x] Deny request to `/robots.txt` endpoint with 403 (Forbidden) status code.
* [x] Add an endpoint at `/html` displaying some placeholder HTML text. [Lorem Ipsum](https://loremipsumgenerator.com/) was used here.
* [x] Display a form containing a textbox at `/input` endpoint.
* [x] Upon submitting the form at `/input`, send the data via a `POST` request to `/input` endpoint. This `/input` endpoint should display the text data received via the request instead of the form. Also log the received data to STDOUT.

## Requires
- Python 3.x
- Flask

## License
MIT
