from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
      return render_template('lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
      return render_template('lab4/div-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
      if x2 == '0':
            return render_template('lab4/div.html', error='На ноль делить нельзя!')
      x1 = int(x1)
      x2 = int(x2)
      result = x1 / x2
      return render_template('lab4/div.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/summa-form')
def summa_form():
      return render_template('lab4/summa-form.html')


@lab4.route('/lab4/summa', methods=['POST'])
def summa():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '' :
            x1 = 0
      if x2 == '':
            x2 = 0
      x1 = int(x1)
      x2 = int(x2)
      result = x1 + x2
      return render_template('lab4/summa.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/stepen-form')
def stepen_form():
      return render_template('lab4/stepen-form.html')


@lab4.route('/lab4/stepen', methods=['POST'])
def stepen():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '' or x2 == '':
        return render_template('lab4/stepen.html', error='Оба поля должны быть заполнены!')
      if x1 == '0' and x2 == '0':
        return render_template('lab4/stepen.html', error='Поля не должны быть равны нулю!')
      x1 = int(x1)
      x2 = int(x2)
      result = x1 ** x2
      return render_template('lab4/stepen.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/razn-form')
def razn_form():
      return render_template('lab4/razn-form.html')


@lab4.route('/lab4/razn', methods=['POST'])
def razn():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '' or x2 == '':
        return render_template('lab4/razn.html', error='Оба поля должны быть заполнены!')
      x1 = int(x1)
      x2 = int(x2)
      result = x1 - x2
      return render_template('lab4/razn.html', x1=x1, x2=x2, result=result)


@lab4.route('/lab4/mult-form')
def mult_form():
      return render_template('lab4/mult-form.html')


@lab4.route('/lab4/mult', methods=['POST'])
def mult():
      x1 = request.form.get('x1')
      x2 = request.form.get('x2')
      if x1 == '':
           x1 = 1
      if x2 == '':
           x2 = 1 
      x1 = int(x1)
      x2 = int(x2)
      result = x1 * x2
      return render_template('lab4/mult.html', x1=x1, x2=x2, result=result)


tree_count = 0
@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
      global tree_count
      if request.method == 'GET':
           return render_template('lab4/tree.html', tree_count=tree_count)
      operation = request.form.get('operation')
      
      if operation == 'cut':
           tree_count -= 1
      elif operation == 'plant':
           tree_count += 1
      return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Grey', 'gender': 'female'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Marley', 'gender': 'male'},
    {'login': 'stu', 'password': '321', 'name': 'Stu Snipe', 'gender': 'female'},
    {'login': 'mathew', 'password': '543', 'name': 'Mathew Snow', 'gender': 'male'},
]
@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            name = next(user['name'] for user in users if user['login'] == login)
        else:
            authorized = False
            login = ''
        name = ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)

    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Вы не ввели логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    if not password:
        error = 'Вы не ввели пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    
    for user in users:
         if login == user['login'] and password == user['password'] :
              session['login'] = login
              return redirect('login')
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)


@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('lab4/fridge.html')
    temperature = request.form.get('temperature')
    if not temperature:
        error = 'Ошибка: не задана температура'
        return render_template('lab4/fridge.html', error=error)
    temperature = int(temperature)
    snow = None
    if temperature < -12:
        phraze = 'Не удалось установить температуру — слишком низкое значение'
    elif temperature > -1:
        phraze = 'Не удалось установить температуру — слишком высокое значение'
    elif -12 <= temperature <= -9:
        phraze = f'Установлена температура: {temperature}°С'
        snow = 3  
    elif -8 <= temperature <= -5:
        phraze = f'Установлена температура: {temperature}°С'
        snow = 2 
    elif -4 <= temperature <= -1:
        phraze = f'Установлена температура: {temperature}°С'
        snow = 1 
    else:
        phraze = 'Неизвестная ошибка'
    return render_template('lab4/fridge.html', phraze=phraze, snow=snow)


seeds_list = {
    'barley': {'name': 'ячмень', 'price': 12345},
    'oats': {'name': 'овёс', 'price': 8522},
    'wheat': {'name': 'пшеница', 'price': 8722},
    'rye': {'name': 'рожь', 'price': 14111}
}

@lab4.route('/lab4/seed', methods=['GET', 'POST'])
def seed():
    if request.method == 'POST':
        seed = request.form.get('seed')
        weight = request.form.get('weight')
        if weight == '':
            phraze = "Ошибка: укажите вес заказа"
            return render_template('lab4/seed.html', phraze=phraze)
        try:
            weight = float(weight)
        except ValueError:
            phraze = "Ошибка: вес должен быть числом."
            return render_template('lab4/seed.html', phraze=phraze)
        if weight <= 0:
            phraze = "Ошибка: вес должен быть больше 0"
            return render_template('lab4/seed.html', phraze=phraze)
        if weight > 500:
            phraze = "Ошибка: такого объёма нет в наличии"
            return render_template('lab4/seed.html', phraze=phraze)
        seeds_name = seeds_list.get(seed)
        price_per_ton = seeds_name['price']
        seeds_name_ru = seeds_name['name']
        total_price = weight * price_per_ton
        discount_phraze = None
        if weight > 50:
            discount = 0.1 
            total_price *= (1 - discount)
            discount_phraze = "Применена скидка 10% за большой объём"
        phraze = f"Заказ успешно сформирован. Вы заказали {seeds_name_ru}. Вес: {weight} т. Сумма к оплате: {total_price:.2f} руб."
        return render_template('lab4/seed.html', phraze=phraze, discount=discount_phraze)
    return render_template('lab4/seed.html')