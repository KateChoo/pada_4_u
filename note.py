pada_3 css無用 當初是幹嘛的？？？給home置中

通訊協定: // 主機名稱：縛好/路徑？要求字串

前端的立場：
主動發出請求給主動發出請求給後端伺服器
並且附帶上相關訊息

後端的立場：
被動從前端接受請求
並且取得其中附帶上相關訊息

flask接受請求的流程：
＊前端發送請求
＊flask套件協助我們套件協助我們處理網路套件協助我們處理網路連線底層
負責接受請求
並且將相關資訊並且將相關資訊封裝載並且將相關資訊封裝在request物件之中
＊根據路由決定要怎麼處理決定要怎麼處理請求

flask request 物件
＊載入request物件
＊在路由對應的函式中直接使用request取得物件
＊進一步取得相關訊息

使用request物件的各種屬性
method請求方法
scheme通訊協定
host主機名稱
path路徑
url完整網址

使用request物件的headers(標頭)屬性
user-agent
accept-language
referrer


@app.route('/')
def home():
    # print('[請求的方法]', request.method)
    # print('[通訊協定]',   request.scheme)
    # print('[主機名稱]',   request.host)
    # print('[路徑]', request.path)
    # print('[完整網址]', request.url)
    # print('[瀏覽器跟作業系統]', request.headers.get('user-agent'))
    # print('[語言偏好]', request.headers.get('accept-language'))
    # print('[引薦網址]', request.headers.get('referrer'))
    return render_template('home.html',
                           web_info=web_info
                           )


多語系的做法
lang = request.headers.get('accept-language')
if lang.startswith('zh'):
    return json.dumps({
        'status': 'ok',
        'text': '您好'
    }, ensure_ascii=False)
else:
    return render_template('home.html',
                           web_info=web_info
                           )


@app.route('/getSum')
def getSum():  # 1+2+3+...100 /getSum?max=最大數字&min=最小數字
    min = request.args.get('min', 0)
    max = request.args.get('max', 100)
    min = int(min)
    max = int(max)
    result = 0
    for i in range(min, max+1):  # 00 #01 #12 #33
        result += i
    return str(result)


後端回應方式
＊直接回應字串 return 字串
＊回應json格式 return json.dumps(字典)
＊重新導向 return redirect(網址路徑)
＊使用樣版引擎


前後端互動：表單
網址：最核心的部分
超連結：簡易的點擊頁面
表單：
可傳送額外資料可設定更多連線細節的介面


@app.route('/signin', methods=['GET'])
def signin():
    username = request.args.get('username', 'test')
    password = request.args.get('password', 'test')
    if (username == 'test') and (password == 'test'):
        return redirect('/member/')
    else:
        return redirect('/error/')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if (username == 'test') and (password == 'test'):
        return redirect('/member/')
    else:
        return redirect('/error/')


後端開發
網址是最重要的嗎？
圖片本身是一個獨立的請求
前端先跟後端要到html的程式碼
# *==========*===========*============*
flash message
