import os
import time
import json
import random
from flask import Flask,url_for,render_template,request,make_response, redirect
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'
count = 0

@app.route("/")
def index(name=None):
    global count
    count = count + 1
    name = 'sds'
    names = ["张三", "李四"]
    
    key = request.args.get('key', 'default')
    print(key)
    res = make_response(render_template("index.html", name=name, names=names, count = count))
    visit_time = request.cookies.get('visit_time')
    res.set_etag("hello")
    # 向响应报文中增加响应头字段
    res.headers['token'] = random.randint(1, 100)
    res.headers.add("token2", random.randint(1, 100))
    if not visit_time:
        res.set_cookie("visit_time", str(time.time()))
    return res

@app.route("/hello")
def hello():
    return {
        "data": "hello world"
    }
    
@app.route("/getJSON", methods=['POST'])
def getJSON():
    d = request.get_data()
    print(d.decode('utf-8'))
    data = json.loads(d.decode('utf-8'))
    if data:
        return {
            "msg": "success",
            "name": data['name'],
            "age": data['age']
        }
    return {
        "msg": 'hello'
    }
    

@app.route("/upload", methods=['POST'])
def upload():
    visit_time = request.cookies.get('visit_time')
    print("该访客第一次访问时间:"+visit_time)
    names = ["张三", "李四"]
    name = 'ds'
    f = request.files['file']
    print(request.files)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    return render_template("index.html", name=name, names=names)

@app.route("/login", methods=['POST'])
def login():
    username = request.form.get("username")
    passwd = request.form.get("passwd")
    print(username, passwd)
    return redirect("/")

if __name__ == "__main__":
    # 模板更改后立即生效
    app.jinja_env.auto_reload = True
    app.run('0.0.0.0', 80, debug=True)