import json
import requests
from .models import GithubRepo
from django.http import HttpResponse
from django.shortcuts import render


def search_github_repo(search_by_term, search_by_topic):
    """ This function is used to return 5 GitHub's repo's name and description,
    when provided the desired desired key-word - search_by_term - and the
    desired programming language - search_y_topic -

    The function returns two arrays:
    - _name_response - the 5 user/name repo info
    - _desc_response - the 5 repo description, respectively to _name_response order """

    _name_response = []
    _desc_response = []

    # Connecting with the github's API searching through the repositories by the provided term and topic
    search_by_term = search_by_term
    search_by_topic = search_by_topic
    _r = requests.get('https://api.github.com/search/repositories?q=' + search_by_term +
                      '+language:' + search_by_topic +
                      '&sort=stars&order=desc')

    # Loading the JSON response of the request if the request is okay (status_code=200)
    if _r.ok:
        _item = json.loads(_r.text)
        try:
            _name = _item['items'][0]['owner']['login'] + '/' + _item['items'][0]['name']
            _desc = _item['items'][0]['description']
        except IndexError:
            _name = 'NOT_FOUND'
            _desc = 'NOT_FOUND'
        _name_response.append(_name)
        _desc_response.append(_desc)

        try:
            _name = _item['items'][1]['owner']['login'] + '/' + _item['items'][1]['name']
            _desc = _item['items'][1]['description']
        except IndexError:
            _name = 'NOT_FOUND'
            _desc = 'NOT_FOUND'
        _name_response.append(_name)
        _desc_response.append(_desc)

        try:
            _name = _item['items'][2]['owner']['login'] + '/' + _item['items'][2]['name']
            _desc = _item['items'][2]['description']
        except IndexError:
            _name = 'NOT_FOUND'
            _desc = 'NOT_FOUND'
        _name_response.append(_name)
        _desc_response.append(_desc)

        try:
            _name = _item['items'][3]['owner']['login'] + '/' + _item['items'][3]['name']
            _desc = _item['items'][3]['description']
        except IndexError:
            _name = 'NOT_FOUND'
            _desc = 'NOT_FOUND'
        _name_response.append(_name)
        _desc_response.append(_desc)

        try:
            _name = _item['items'][4]['owner']['login'] + '/' + _item['items'][4]['name']
            _desc = _item['items'][4]['description']
        except IndexError:
            _name = 'NOT_FOUND'
            _desc = 'NOT_FOUND'
        _name_response.append(_name)
        _desc_response.append(_desc)

        return _name_response, _desc_response


def index(request):
    if request.method == 'POST':
        # Getting through the POST request the input box value, which is the search_by_term value
        search_by_term_inputbox = request.POST.get('search_by_term_inputbox')

        """ Invoking the search function for each programming language.
         Returning it zipped to pass as parameter as context to the view.
         Returning it zipped in a second variable to use as consumable parameter to the database insertion """
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

        # Defining context to be passed to the view
        context = {
            'python_return_list': python_return_list,
            'ruby_return_list': ruby_return_list,
            'java_return_list': java_return_list,
            'elixir_return_list': elixir_return_list,
            'c_return_list': c_return_list,
        }

        # Iterating through the list(zip) object to save each item to the database
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
        # Open the view as empty the first time, when the request isn't POST
        context = {
            'return_list': '',
        }
        return HttpResponse(render(request, 'main/index.html', context))
