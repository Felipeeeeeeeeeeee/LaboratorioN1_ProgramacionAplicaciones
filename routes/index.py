from flask import Blueprint, render_template, request, redirect, url_for
from models.form import Form
from utils.db import db
from utils.nlp import NLP

index = Blueprint('index', __name__)

# Routes

@index.route("/")
def home():
    return render_template('index.html')


@index.route("/new", methods=['POST'])
def add_form():
    if request.method == 'POST':
        content = request.form.get('content')
        new_form = Form(content=content)
        db.session.add(new_form)
        db.session.commit()
        return redirect(url_for('index.home'))


@index.route("/forms")
def show_forms():
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Número de formularios por página

    forms = Form.query.order_by(Form.id.desc()).paginate(page=page, per_page=per_page)

    return render_template('show_forms.html', forms=forms)


@index.route("/forms/details/<int:form_id>")
def details_of_form(form_id):
    form = Form.query.get(form_id)
    tokenizado = NLP(form.content)
    num_nouns, num_verbs = tokenizado.get_num_of_verbs_and_nouns()
    tokens = tokenizado.get_word_labels()
    print(tokens)
    return render_template('show_details_of_form.html', num_nouns=num_nouns, num_verbs=num_verbs, tokens=tokens)


@index.route("/forms/delete/<int:form_id>")
def delete_form(form_id):
    form = Form.query.get(form_id)
    db.session.delete(form)
    db.session.commit()
    return redirect(url_for('index.show_forms'))
