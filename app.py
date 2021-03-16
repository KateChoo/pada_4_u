import json
from flask import Flask, render_template, request, redirect, session, g
app = Flask(__name__)
app.secret_key = 'secretkey'
web_info = {
    'dir_t': '歡迎光臨，目錄',
    'signin_t': '歡迎光臨，請輸入帳號密碼',
    'upload_t': 'Upload, maybe',
    'taipei_t': '歡迎光臨，台北',
    'member_t': '歡迎光臨，這是會員頁面',
    'error_t': '失敗頁面',
    'signout_t': '',
}


@app.before_request
def before_request():
    g.username = '您'
    if 'username' in session:
        username = session['username']
        g.username = username


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home.html',
                           web_info=web_info
                           )


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    #session.pop('user_username', None)
    if (username == 'test') and (password == 'test'):
        session['username'] = username
        return redirect('/member/')
    else:
        return redirect('/error/')


@app.route('/member/', methods=['GET', 'POST'])
def member():
    # if 'username' in session:
    #     username = session['username']
    return render_template('member.html',
                           web_info=web_info,
                           # username=username
                           )


@app.route('/error/')
def error():
    return render_template('error.html',
                           web_info=web_info
                           )


@app.route('/signout')
def signout():
    session.pop('username', '您')
    return render_template('home.html',
                           web_info=web_info
                           )


if __name__ == '__main__':
    app.run(debug=True, port=3000)
