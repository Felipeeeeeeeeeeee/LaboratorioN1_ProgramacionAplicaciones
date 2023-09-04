from flask import Blueprint, render_template, request, redirect, url_for
from models.prompt import Prompt
from models.word import Word
from utils.db import db
from utils.nlp import NLP

index = Blueprint('index', __name__)

# Routes
@index.route("/")
def home():
    return render_template('index.html')


@index.route("/new", methods=['POST'])
def add_prompt():
    if request.method == 'POST':
        content = request.form.get('content')
        new_prompt = Prompt(content=content)
        words_and_frequency = NLP(NLP(content).get_cleaned_words()).count_words()
        for word_tuple in words_and_frequency:
            word, count = word_tuple
            existing_word = Word.query.get(word)
            if existing_word:
                existing_word.count += count
            else:
                new_word = Word(id=word, count=count)
                db.session.add(new_word)
        db.session.add(new_prompt)
        db.session.commit()
        return redirect(url_for('index.home'))


@index.route("/prompts")
def show_prompts():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    prompts = Prompt.query.order_by(Prompt.id.desc()).paginate(page=page, per_page=per_page)
    return render_template('show_prompts.html', prompts=prompts)


@index.route("/words")
def show_words():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    words_pagination = Word.query.order_by(Word.count.desc()).paginate(page=page, per_page=per_page, error_out=False)
    return render_template('show_words.html', words_pagination=words_pagination)


@index.route("/prompts/details/<int:form_id>")
def details_of_prompt(form_id):
    prompt = Prompt.query.get(form_id)
    tokenized = NLP(prompt.content)
    num_nouns, num_verbs = tokenized.get_num_of_verbs_and_nouns()
    tokens = tokenized.get_word_labels()
    return render_template('show_details_of_prompt.html', num_nouns=num_nouns, num_verbs=num_verbs, tokens=tokens, timestamp=prompt.timestamp.strftime('%Y-%m-%d %H:%M:%S'))


@index.route("/prompts/delete/<int:form_id>")
def delete_prompt(form_id):
    prompt = Prompt.query.get(form_id)
    db.session.delete(prompt)
    db.session.commit()
    return redirect(url_for('index.show_prompts'))
