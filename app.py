import json
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
web_info = {
    'dir_t': '歡迎光臨，目錄',
    'signin_t': '歡迎光臨，請輸入帳號密碼',
    'upload_t': 'Upload, maybe',
    'taipei_t': '歡迎光臨，台北',
    'member_t': '歡迎光臨，這是會員頁面',
    'error_t': '失敗頁面',
    'signout_t': '',
}


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('home.html',
                           web_info=web_info
                           )


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']  # , 'test')
    password = request.form['password']  # , 'test')
    if (username == 'test') and (password == 'test'):
        return redirect('/member/')
    else:
        return redirect('/error/')


@app.route('/member/', methods=['GET', 'POST'])
def member():
    return render_template('member.html',
                           web_info=web_info
                           )


@app.route('/error/')
def error():
    return render_template('error.html',
                           web_info=web_info
                           )


@app.route('/signout')
def signout():
    return render_template('signout.html',
                           web_info=web_info
                           )


if __name__ == '__main__':
    app.run(debug=True, port=3000)
