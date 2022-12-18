import json
import os


def load_candidates_from_json():
    """
    Функция читает список кaндидатов, из файла 'candidates.json'.
    :return: возвращает список всех кандидатов.
    """
    with open(os.path.join('candidates.json'), 'rt', encoding='utf-8') as f:
        return json.load(f)


list_candidates = load_candidates_from_json()


def get_candidate_by_id(candidate_id):
    """
    Функция проходит по списку кандидатов возвращая кандидата по id.
    :param candidate_id: получает имя и фамилию кандидата.
    :return: возвращает одного кандидата по его id.
    """
    for candidate in list_candidates:
        if candidate['id'] == candidate_id:
            return candidate
        else:
            continue


def get_candidates_by_name(candidate_name):
    """
    Функция проходит по списку кандидатов возвращая кандидата по имени.
    :param candidate_name: имя кандидата.
    :return: возвращает кандидатов по имени
    """
    name_candidate = []
    for candidate in list_candidates:
        if candidate_name.lower() in candidate['name'].lower():
            name_candidate.append(candidate)
            return name_candidate
        else:
            continue


def get_candidates_by_skill(skill_name):
    """
    Функция проходит по списку кандидатов возвращая кандидата по наличию введенного навыка.
    :param skill_name: введенный навык пользователем.
    :return: возвращает кандидата по скиллам.
    """
    candidates = []
    for candidate in list_candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates