from django.test import TestCase
from .models import GithubRepo
import requests
from .views import search_github_repo


class GithubRepoTests(TestCase):
    """ The unit automated tests to the GitHubRepo functions """

    def create_github_repo_object(self, name="name", desc="desc"):
        """ Return a GitHubRepo object """

        github_repo = GithubRepo(name=name, desc=desc)
        return github_repo

    def test_github_repo_object_creation(self):
        """ Test GitHubRepo object instance """

        g = self.create_github_repo_object()
        self.assertTrue(isinstance(g, GithubRepo))

    def test_github_api_conn(self, search_by_term='test', search_by_topic='python'):
        """ Test the request HTTP status code, looking for a success. """

        _r = requests.get('https://api.github.com/search/repositories?q=' + search_by_term +
                          '+language:' + search_by_topic +
                          '&sort=stars&order=desc')
        self.assertEqual(_r.status_code, 200)
