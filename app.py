from flask import Flask, render_template
from utils import *


app = Flask(__name__)


@app.route('/')
def index():
    """
    Представление выводит список всех кандидатов.
    :return: возвращает ссылки на кандидатов из шаблонизатора 'list.html'
    """
    data = load_candidates_from_json()
    return render_template('list.html', list_candidates=data)


@app.route('/candidate/<int:x>/')
def get_candidate(x):
    """
    Представление, которое выводит данные про кандидата.
    :param x: id кандидата.
    :return: возвращает кандидатов из шаблонизатора card.html
    """
    candidate = get_candidate_by_id(x)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_name(candidate_name):
    """
    Представление для поиска по совпадению.
    :param candidate_name: имя кандидата.
    :return: список кандидатов из шаблонизатора search.html.
    """
    candidate_list = get_candidates_by_name(candidate_name)
    count_name = len(candidate_list)
    return render_template('search.html', list_candidates=candidate_list, count=count_name)


@app.route('/skill/<skill_name>')
def skill(skill_name):
    """
    Представление для поиска по навыкам.
    :param skill_name: наименование навыка.
    :return: список кандидатов из шаблонизатора skill.html.
    """
    skill_list = get_candidates_by_skill(skill_name)
    count_skill = len(skill_list)
    return render_template('skill.html', skill_name=skill_name, list_skill=skill_list, count=count_skill)


if __name__ == '__main__':
    app.run(debug=True)