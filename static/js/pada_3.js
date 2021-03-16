function finalizeLogin(res){
    res.user.getIdToken().then(idToken => {
        console.log('[idToken]', idToken);
        //準備要給後端(Flask App)的資料{物件}
        const data = {
            'id_token': idToken
        };
        //透過axios把data送至/api/login
        axios    //@app.route...接收路由,只寫這段axios會發生main.js:15 [登入失敗] Error: Request failed with status code 404 要等後端建立路由
            .post('/', data)
            .then(res => {
                console.log('[登入成功]', res);
                //後端存入cookie後 重新整理畫面再向後端下req
                window.location.reload();
            })
            .catch(err => {
                console.log('[登入失敗]', err);
            })  

    })
}
//綁定id='loginForm' 的表單送出事件
// $('#loginForm').submit(function (event) {
//     event.preventDefault();   //防止重整
//     const form = {
//         email: $('#loginEmail').val(),
//         password: $('#loginPassword').val(),
//     };
//     console.log('[登入]', form);
//     //Add
//     firebase
//         .auth()
//         .signInWithEmailAndPassword(form.email, form.password)
//         //登入成功
//         .then(res => {
//             console.log('登入成功', res)
//             finalizeLogin(res);
//         }) //會回傳一個物件  .then(function(){}) 沒有使用this可用箭頭涵式,有用作用域不同this會是window
//         //都入失敗
//         .catch(err => {
//             console.log('登入失敗', err);
//             alert(err.message);
//         });
//     //END
// });

// $('#signUpForm').submit(function (event) {
//     event.preventDefault();
//     const form = {
//         email: $('#signUpEmail').val(),
//         password: $('#signUpPassword').val(),
//     };
//     console.log('[註冊]', form);
// });

// $('#logoutBtn').click(function () {
//     console.log('[登出]');
// });