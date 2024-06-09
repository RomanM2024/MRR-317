from flask import Flask, render_template, url_for, request, flash, session, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'os.urandom(256)'

menu = [
    {'name': 'Домашняя страница', 'url': 'index'},
    {'name': 'О сайте', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'}
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


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    background_image_url = 'https://img.freepik.com/free-photo/top-view-white-toy-plane-and-map_23-2148666303.jpg?w=900&t=st=1717958641~exp=1717959241~hmac=a5ea16704396603e8ee3ce7a7978c5365963014f99cf0880080921bf8b910339'
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
    background_image_url = 'https://irbis39.ru/upload/medialibrary/82f/82f57c366d7ca36b0eb0e6858e86e76e.gif'
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


if __name__ == '__main__':
    app.run(debug=True)
