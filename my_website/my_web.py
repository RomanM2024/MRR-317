from flask import Flask, render_template, url_for, request, flash, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'os.urandom(256)'

menu = [
    {'name': 'Домашняя страница', 'url': 'index'},
    {'name': 'О сайте', 'url': 'about'},
    {'name': 'Оставить отзыв', 'url': 'comments'},
    {'name': 'Обратная связь', 'url': 'contact'},
    {'name': 'Авторизация', 'url': 'login'},
    {'name': "Выйти из аккаунта", "url": "logout"}

]


@app.route('/')
@app.route('/index')
def index():
    background_image_url = 'https://img.freepik.com/free-photo/top-view-hands-holding-phone-and-photos_23-2149617680.jpg?w=996&t=st=1717958534~exp=1717959134~hmac=73f077eb8fef91154d6dfc5278d9842df239f3b8f0cfca7619fa5da77b1f84c8'
    return render_template('index.html', background_image_url=background_image_url, menu=menu)


@app.route('/about')
def about():
    background_image_url = 'https://img.freepik.com/free-photo/above-view-travel-items-assortment-still-life_23-2149617645.jpg?w=996&t=st=1717958692~exp=1717959292~hmac=afba459d63c264414e90a96c6a98900bbec9553fe54dd7883d2e638355c952ae'
    return render_template('about.html', background_image_url=background_image_url, title='О сайте', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    return f"Пользователь: {username}"


@app.route('/comments', methods=['POST', 'GET'], endpoint='comments')
def comments_view():
    if 'comments' not in session:
        session['comments'] = []

    if request.method == 'POST':
        comment_text = request.form['comment']
        username = request.form['username']

        if len(comment_text) > 0 and len(username) > 2:
            comment_id = len(session['comments'])
            session['comments'].append({'id': comment_id, 'username': username, 'comment': comment_text})
            flash('Комментарий успешно добавлен', 'success')
        else:
            flash('Ошибка добавления комментария', 'error')

        print(session)

    background_image_url = 'https://img.freepik.com/free-photo/christmas-travel-concept-with-laptop_23-2149573078.jpg?t=st=1718446088~exp=1718449688~hmac=6255cd1f4cca722069317f9b5b20249a7ef13f887f43bafbe9e502ba6a8566a0&w=996'
    return render_template('comments.html', background_image_url=background_image_url, title='Комментарии', menu=menu,
                           comments=session['comments'])


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    background_image_url = 'https://img.freepik.com/free-photo/flat-lay-hat-notebook-arrangement_23-2148786126.jpg?t=st=1718445793~exp=1718449393~hmac=f903cf5ff1f85bc0bf2580b907f3d7d7f1e154ae68c7d5afd283ffd0540bf670&w=1060'
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно", category='success')
            print(request.form)
        else:
            flash("Ошибка отправки", category='error')
    return render_template('contact.html', background_image_url=background_image_url, title='Обратная связь', menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


@app.route('/login', methods=['GET', 'POST'])
def login():
    background_image_url = 'https://img.freepik.com/free-photo/traveling-items-wooden-background_23-2148909611.jpg?t=st=1718446866~exp=1718450466~hmac=773a950adf947f338f1f14113de7198c4b89424f985e7fa0bacb2677e321c2fe&w=826'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['psw']

        if username == 'admin' and password == '123456':
            session['userLogged'] = True
            success_message = 'Вы успешно авторизовались'
            return render_template('login.html', background_image_url=background_image_url, success_message=success_message, menu=menu)
        else:
            error_message = 'Неверное имя пользователя или пароль'
            return render_template('login.html', background_image_url=background_image_url, error_message=error_message, menu=menu)
    elif 'userLogged' in session:
        success_message = 'Вы успешно авторизовались'
        return render_template('login.html', background_image_url=background_image_url, success_message=success_message, menu=menu)
    else:
        return render_template('login.html', background_image_url=background_image_url, menu=menu)


@app.route("/logout")
def logout():
    session.pop('userLogged', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
