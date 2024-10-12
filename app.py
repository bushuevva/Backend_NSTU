from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def start():
    return redirect('/menu', code=302)

@app.route('/lab1')
def lab1():
        return """
<!doctype html>
<html>
    <body>
        <head>
            <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        </head>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </div>

        <li>
            <a href='http://127.0.0.1:5000/menu'>Меню</a>
        </li>

        <h2>Релизованные роуты</h2>
        
        <li><a href="http://127.0.0.1:5000/lab1/oak">Дерево</a></li>
        
        <li><a href="http://127.0.0.1:5000/lab1/student">Студент</a></li>
        <li><a href="http://127.0.0.1:5000/lab1/python">Python</a></li>
        <li><a href="http://127.0.0.1:5000/lab1/kapibara">Kapibara</a></li>


        <footer>
            &copy; Ирина Бушуева, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route('/menu')
def menu():
        return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <div>
            <a href='http://127.0.0.1:5000/lab1'>Лабораторная работа 1</a>
        </div>
                <div>
            <a href='http://127.0.0.1:5000/lab2'>Лабораторная работа 2</a>
        </div>

        <footer>
            &copy; Ирина Бушуева, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route('/lab1/oak')
def oak():
        return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дерево</h1>
        <div>
            <img src="''' + url_for('static', filename='tree.webp') + '''">
        </div>

    </body>
</html>
'''

@app.route('/lab1/student')
def student():
        return '''
<!doctype html>
<html>
    <body>
        <h1>Бушуева Ирина Андреевна</h1>
        <div class="image">
            <img src="''' + url_for('static', filename='logo.jpg') + '''">
        </div>

    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div class='bl'>
            Python (в русском языке встречаются названия пито́н или па́йтон) — мультипарадигмальный высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью языка является выделение блоков кода отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++.
        </div> <br>
        <div class='bl'>
            Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, объектно-ориентированное программирование, метапрограммирование, функциональное программирование и асинхронное программирование. Задачи обобщённого программирования решаются за счёт динамической типизации. Аспектно-ориентированное программирование частично поддерживается через декораторы, более полноценная поддержка обеспечивается дополнительными фреймворками. Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений. Основные архитектурные черты — динамическая типизация, автоматическое управление памятью, полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL), высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты.
        </div> <br>
        <div class='bl'>
            Эталонной реализацией Python является интерпретатор CPython, который поддерживает большинство активно используемых платформ, являющийся стандартом де-факто языка. Он распространяется под свободной лицензией Python Software Foundation License, позволяющей использовать его без ограничений в любых приложениях, включая проприетарные. CPython компилирует исходные тексты в высокоуровневый байт-код, который исполняется в стековой виртуальной машине[30]. К другим трём основным реализациям языка относятся Jython (для JVM), IronPython (для CLR/.NET) и PyPy. PyPy написан на подмножестве языка Python (RPython) и разрабатывался как альтернатива CPython с целью повышения скорости исполнения программ, в том числе за счёт использования JIT-компиляции. Поддержка версии Python 2 закончилась в 2020 году. На текущий момент активно развивается версия языка Python 3. Разработка языка ведётся через предложения по расширению языка PEP (англ. Python Enhancement Proposal), в которых описываются нововведения, делаются корректировки согласно обратной связи от сообщества и документируются итоговые решения.
        </div>

        <div class="image">
            <img src="''' + url_for('static', filename='python.png') + '''">
        </div>

    </body>
</html>
'''

@app.route('/lab1/kapibara')
def kapibara():
    return '''
<!doctype html>
<html>
    <head>
    <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div class='kapibara'>

            <div>
                Капиба́ра, или водосви́нка (лат. Hydrochoerus hydrochaeris), — полуводное травоядное млекопитающее из подсемейства водосвинковых (Hydrochoerinae), один из двух (наряду с малой водосвинкой) ныне существующих видов рода водосвинки. Капибара — самый крупный среди современных грызунов.
            </div> <br>
            <div>
                Название животного берёт начало от слова kaapiûara, что на мёртвом языке тупи (родственном языку индейцев гуарани) буквально означает «поедатель тонкой травы» (kaá (трава) + píi (тонкий) + ú (есть) + ara (суффикс, аналогичный русскому суффиксу -тель)). В наиболее близкой к оригиналу форме capivara оно вошло в португальский язык и широко употребимо в Бразилии. Уже в форме capibara через испанский слово вошло в английский, русский, японский и ряд других языков. В испаноговорящих странах Латинской Америки также в ходу и другие названия, происходящие из языков местных индейцев: carpincho (Аргентина, Перу и др.), chigüiro (Венесуэла, Колумбия), jochi (Боливия), ñeque (Колумбия) и др.
            </div><br>
            <div>
                Научное название (как родовое, так и видовое) Hydrochoerus hydrochaeris переводится как «водяная свинья» (др.-греч. ὕδωρ — вода + χοῖρος — свинья), калька с которого послужила основой как для альтернативного русского наименования этого животного — водосвинка, — так и названий его на китайском (水豚), венгерском (Vízidisznó), исландском (Flóðsvín) и некоторых других языках, а также для вариантов, употребимых в Аргентине (chancho de agua и puerco de agua).
            </div>
        </div>

        <div class="image">
            <img src="''' + url_for('static', filename='kap.jpg') + '''">
        </div>

    </body>
</html>
'''

# -----------------------------------------------------------

@app.route('/lab2/a')
def a():
      return "без слэша"

@app.route('/lab2/a/')
def a2():
      return "со слэшем"

flower_list = ['роза','тюльпан', 'незабудка','ромашка']
@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
      if flower_id >= len(flower_list):
            return 'нет такого цветка', 404
      else:
            return "цветок:" + flower_list[flower_id]
@app.route('/lab2/add_flower/<name>')
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

@app.route('/lab2/add_flower/')
def no_name():
    return 'Вы не задали имя цветка', 400

@app.route('/lab2/kolvo_flowers')
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
@app.route('/lab2/example')
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

@app.route('/lab2/')
def lab2():
      return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
      phrase = "О <b> скольно </b> <u>нам</u> <i>открытий</i> чудных..."
      return render_template('filter.html', phrase = phrase)
# -----------------
@app.route('/lab2/calc/<int:a>/<int:b>')
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

@app.route('/lab2/calc/')
def calc_one():
    return redirect(url_for('calc', a=1, b=1))

@app.route('/lab2/calc/<int:a>')
def calc_two(a):
    return redirect(url_for('calc', a=a, b=1))

@app.route('/lab2/calc/<int:a>')
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
@app.route('/lab2/books')
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
@app.route('/lab2/berries')
def berries():
      return render_template('berries.html', lists=lists)

# -------------------------
@app.route('/')
def home():
    return render_template('menu.html')