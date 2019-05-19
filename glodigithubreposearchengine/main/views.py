import json
import requests
from .models import GithubRepo
from django.http import HttpResponse
from django.shortcuts import render

def search_github_repo(search_by_term, search_by_topic):

    _name_response = []
    _desc_response = []

    search_by_term = search_by_term
    search_by_topic = search_by_topic
    _r = requests.get('https://api.github.com/search/repositories?q=' + search_by_term +
                      '+language:' + search_by_topic +
                      '&sort=stars&order=desc')

    if _r.ok:
        _item = json.loads(_r.text)
        _name = _item['items'][0]['owner']['login'] + '/' + _item['items'][0]['name']
        _desc = _item['items'][0]['description']
        _name_response.append(_name)
        _desc_response.append(_desc)

        _name = _item['items'][1]['owner']['login'] + '/' + _item['items'][1]['name']
        _desc = _item['items'][1]['description']
        _name_response.append(_name)
        _desc_response.append(_desc)

        _name = _item['items'][2]['owner']['login'] + '/' + _item['items'][2]['name']
        _desc = _item['items'][2]['description']
        _name_response.append(_name)
        _desc_response.append(_desc)

        _name = _item['items'][3]['owner']['login'] + '/' + _item['items'][3]['name']
        _desc = _item['items'][3]['description']
        _name_response.append(_name)
        _desc_response.append(_desc)

        _name = _item['items'][4]['owner']['login'] + '/' + _item['items'][4]['name']
        _desc = _item['items'][4]['description']
        _name_response.append(_name)
        _desc_response.append(_desc)

        return _name_response, _desc_response


def index(request):
    if request.method == 'POST':
        search_by_term_inputbox = request.POST.get('search_by_term_inputbox')

        _name_list, _desc_list = search_github_repo(search_by_term_inputbox, 'python')
        python_return_list = zip(_name_list, _desc_list)
        python_return_list_d = zip(_name_list, _desc_list)

        _name_list, _desc_list = search_github_repo(search_by_term_inputbox, 'ruby')
        ruby_return_list = zip(_name_list, _desc_list)
        ruby_return_list_d = zip(_name_list, _desc_list)

        _name_list, _desc_list = search_github_repo(search_by_term_inputbox, 'java')
        java_return_list = zip(_name_list, _desc_list)
        java_return_list_d = zip(_name_list, _desc_list)

        _name_list, _desc_list = search_github_repo(search_by_term_inputbox, 'elixir')
        elixir_return_list = zip(_name_list, _desc_list)
        elixir_return_list_d = zip(_name_list, _desc_list)

        _name_list, _desc_list = search_github_repo(search_by_term_inputbox, 'c')
        c_return_list = zip(_name_list, _desc_list)
        c_return_list_d = zip(_name_list, _desc_list)

        context = {
            'python_return_list': python_return_list,
            'ruby_return_list': ruby_return_list,
            'java_return_list': java_return_list,
            'elixir_return_list': elixir_return_list,
            'c_return_list': c_return_list,
        }

        for l in list(python_return_list_d):
            desc = l[1]
            if desc is None:
                desc = 'No Description Provided'
            github_repo = GithubRepo(name=l[0], description=desc)
            github_repo.save()

        for l in list(ruby_return_list_d):
            desc = l[1]
            if desc is None:
                desc = 'No Description Provided'
            github_repo = GithubRepo(name=l[0], description=desc)
            github_repo.save()

        for l in list(java_return_list_d):
            desc = l[1]
            if desc is None:
                desc = 'No Description Provided'
            github_repo = GithubRepo(name=l[0], description=desc)
            github_repo.save()

        for l in list(elixir_return_list_d):
            desc = l[1]
            if desc is None:
                desc = 'No Description Provided'
            github_repo = GithubRepo(name=l[0], description=desc)
            github_repo.save()

        for l in list(c_return_list_d):
            desc = l[1]
            if desc is None:
                desc = 'No Description Provided'
            github_repo = GithubRepo(name=l[0], description=desc)
            github_repo.save()

        return HttpResponse(render(request, 'main/index.html', context))

    else:
        context = {
            'return_list': '',
        }
        return HttpResponse(render(request, 'main/index.html', context))
