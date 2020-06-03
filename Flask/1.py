from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VOVA'

data = {}
data['user'] = {
    'name': 'Vova',
    'tel': '6666666666444',
    'adress_A': 'bla-bla',
    'adress_B': 'qwerty_12'
}
data['taxi'] = {
    'id_name': 'vovchi007'

}

class taxi_form(FlaskForm):
    id_name = StringField('name: ')
    submit = SubmitField('Ok')

class user_form(FlaskForm):
    name = StringField('name: ')
    tel = StringField('tel: ')
    adress_A = StringField('adress_A: ')
    adress_B = StringField('adress_B: ')
    submit = SubmitField('Ok')


@app.route('/api/<action>', methods = ['GET'])
def r(action):
    if (action == 'all'):
        return render_template("get_all.html", user=data['user'], taxi = data['taxi'])
    elif (action== 'taxi'):
        return render_template("taxi.html", form=taxi_form())
    elif (action == 'user'):
        return render_template("user.html", form=user_form())
    else:
        return render_template("404.html", x=action)


@app.route('/api/taxi', methods = ['POST'])
def get_taxi():
    form = taxi_form()
    if form.is_submitted():
        result = request.form
        data['taxi']['id_name'] = result['id_name']
        return redirect('all')
    return render_template('taxi.html', form=form)


@app.route('/api/user', methods = ['POST'])
def get_user():
    form = user_form()
    if form.is_submitted():
        result = request.form
        data['user']['name'] = result['name']
        data['user']['tel'] = result['tel']
        data['user']['adress_A'] = result['adress_A']
        data['user']['adress_B'] = result['adress_B']
        return redirect('all')
    return render_template('user.html', form=form)

if __name__ == '__main__':

   app.run()

