from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
      return "без слэша"

@lab2.route('/lab2/a/')
def a2():
      return "со слэшем"

flower_list = ['роза','тюльпан', 'незабудка','ромашка']
@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
      if flower_id >= len(flower_list):
            return 'нет такого цветка', 404
      else:
            return "цветок:" + flower_list[flower_id]
@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
      flower_list.append(name)
      return f'''
<!doctype html>
<html>
    <body>
        <h1>Добавлен новый уветок</h1>
        <p> Название нового цветка: {name}</p>
        <p> Всего цветов: {len(flower_list)}</p>
        <p> Полный список: {flower_list}</p>
    </body>
</html>
'''

@lab2.route('/lab2/add_flower/')
def no_name():
    return 'Вы не задали имя цветка', 400

@lab2.route('/lab2/kolvo_flowers')
def kolvo_flowers():
    return f'''
    <!doctype html>
    <html>
        <body>
            <p>Всего цветов: {len(flower_list)}</p>
            <p>Все цветы:{ flower_list }</p>
        </body>
    </html>
    '''
@lab2.route('/lab2/example')
def example():
    name, num, curs, gruppa = 'Бушуева Ирина Андреевна', 2, 3,'ФБИ-24' 
    fruits = [
            {'name':'яблоки' , 'price': 100},
            {'name':'груши' , 'price': 120},
            {'name':'апельсины' , 'price': 80},
            {'name':'мандарины' , 'price': 95},
            {'name':'манго' , 'price': 321}
    ]
    return render_template('example.html', name = name, num = num, curs = curs, gruppa = gruppa, fruits = fruits)

@lab2.route('/lab2/')
def lab():
      return render_template('lab2.html')

@lab2.route('/lab2/filters')
def filters():
      phrase = "О <b> скольно </b> <u>нам</u> <i>открытий</i> чудных..."
      return render_template('filter.html', phrase = phrase)
# -----------------
@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    # Здесь будет логика ваших вычислений
      return f'''
    <!doctype html>
    <html>
        <body>
        <p>{a} + {b} = {a+b}</p>
        <p>{a} - {b} = {a-b}</p>
        <p>{a} * {b} = {a*b}</p>
        <p>{a} / {b} = {a/b}</p>
        <p>{a} <sup>{b}</sup> = {a**b}</p>
        </body>
    </html>
'''

@lab2.route('/lab2/calc/')
def calc_one():
    return redirect(url_for('calc', a=1, b=1))

@lab2.route('/lab2/calc/<int:a>')
def calc_two(a):
    return redirect(url_for('calc', a=a, b=1))

@lab2.route('/lab2/calc/<int:a>')
def calc_three(a):
      return redirect(url_for('calc', a=a, b=1))
# ---------------------
books = [
      {'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин,', 'genre': 'роман-эпопея', 'pages': 900},
      {'title': 'Гордость и предубеждение', 'author': 'Джейн Остин', 'genre': 'роман' , 'pages': 430},
      {'title': 'Тёмные начала', 'author': 'Филип Пулман', 'genre': 'фантастическая трилогия', 'pages': 500},
      {'title': 'Автостопом по галактике', 'author': 'Дуглас Адамс', 'genre': 'юмористический научно-фантастический роман', 'pages': 400},
      {'title': 'Гарри Поттер и Кубок огня', 'author': 'Джоан Роулинг', 'genre': 'фэнтези', 'pages': 647},
      {'title': 'Убить пересмешника', 'author': 'Харпер Ли',  'genre': 'роман-бестселлер', 'pages': 280},
      {'title': 'Винни Пух', 'author': 'Алан Александр Милн', 'genre': 'детская повесть' , 'pages': 30},
      {'title': '1984', 'author': 'Джордж Оруэлл', 'genre': 'роман-антиутопия', 'pages': 330},
      {'title': 'Лев, колдунья и платяной шкаф', 'author': 'Клайв Стэйплз Льюис',  'genre': 'фэнтези', 'pages': 650},
      {'title': 'Джейн Эйр', 'author': 'Шарлотта Бронте',  'genre': 'роман', 'pages': 340}
]
@lab2.route('/lab2/books')
def book():
      return render_template('books.html', books=books)
# -------------------------
lists = [
      {'name': 'Клубника', 'img': 'im1.webp' },
      {'name': 'Ежевика', 'img': 'img2.webp' },
      {'name': 'Голубика', 'img': 'img3.webp' },
      {'name': 'Черника', 'img': 'img4.webp' },
      {'name': 'Малина', 'img': 'img5.jpg' }
]
@lab2.route('/lab2/berries')
def berries():
      return render_template('berries.html', lists=lists)