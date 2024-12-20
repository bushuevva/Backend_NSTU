from flask import Blueprint, render_template, abort, request, jsonify

lab7 = Blueprint('lab7', __name__)


@lab7.route('/lab7/')
def lab():
    return render_template('lab7/lab7.html')
films = [
    {
        "title": "Interstellaar",
        "title_ru": "Интерстеллар",
        "year": 2014,
        "description": "Когда засуха, пыльные бури и вымирание растений приводят человечество к продовольственному кризису, коллектив исследователей и учёных отправляется сквозь червоточину (которая предположительно соединяет области пространства-времени через большое расстояние) в путешествие, чтобы превзойти прежние ограничения для космических путешествий человека и найти планету с подходящими для человечества условиями."
    },
    {
        "title": "Shutter Island",
        "title_ru": "Остров проклятых",
        "year": 2009,
        "description": "Два американских судебных пристава отправляются на один из островов в штате Массачусетс, чтобы расследовать исчезновение пациентки клиники для умалишенных преступников. При проведении расследования им придется столкнуться с паутиной лжи, обрушившимся ураганом и смертельным бунтом обитателей клиники."
    },
    {
        "title": "I Am Legend",
        "title_ru": "Я – легенда",
        "year": 2007,
        "description": "Неизвестный вирус унёс жизни половины населения земного шара, а остальную половину превратил в вампиров. Единственный уцелевший человек с иммунитетом к заболеванию ночами держит осаду упырей, а днем пытается найти противоядие и докопаться до причин эпидемии."
    },
    {
        "title": "Legend",
        "title_ru": "Легенда",
        "year": 2015,
        "description": "Близнецы Реджи и Ронни Крэй — культовые фигуры преступного мира Великобритании 1960-х. Братья возглавляли самую влиятельную бандитскую группировку Ист-Энда. В их послужном списке были вооруженные грабежи, рэкет, поджоги, покушения, убийства и собственный ночной клуб, куда доезжали даже голливудские знаменитости. Среди их жертв — криминальные авторитеты Джек МакВитти и Джордж Корнелл."
    },
    {
        "title": "Intouchables",
        "title_ru": "1+1",
        "year": 2011,
        "description": "Пострадав в результате несчастного случая, богатый аристократ Филипп нанимает в помощники человека, который менее всего подходит для этой работы, – молодого жителя предместья Дрисса, только что освободившегося из тюрьмы. Несмотря на то, что Филипп прикован к инвалидному креслу, Дриссу удается привнести в размеренную жизнь аристократа дух приключений"
    }
]


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return jsonify(films)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    return jsonify(films[id])


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    del films[id]
    return '', 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    film = request.get_json()
    if film ['description'] == '':
        return jsonify({'description': 'Заполните описание'}), 400
    if not film.get('title'):
        film['title'] = film['title_ru']
    films[id] = film
    return jsonify(films[id])


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film:
        abort(400)
    if film.get('description', '') == '':
        return jsonify({'description': 'Заполните описание'}), 400
    if not film.get('title'):
        film['title'] = film['title_ru']
    films.append(film)
    return jsonify(film), 201