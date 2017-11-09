from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_from():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or Password', username=username)


@app.route('/test', methods=['GET'])
def test():
    l1 = [1, 2, 3, 4, 5]
    return render_template("test.html", res_list = l1)


if __name__ == '__main__':
    app.run()


"""
Flask 会在 templates 文件夹里寻找模板
所以，如果你的应用是个模块，这个文件夹应该与模块同级；如果它是一个包，那么这个文件夹作为包的子目录
"""