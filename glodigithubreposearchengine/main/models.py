from django.db import models
from django.utils.translation import ugettext_lazy as _


class GithubRepo(models.Model):
    """ Creating the Github Repository model class to be added to the database. """
    name = models.CharField(_('Name'), max_length=200)
    description = models.CharField(_('Description'), max_length=10000)
