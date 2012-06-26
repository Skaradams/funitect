from django.db import models
from django.contrib.auth.models import User


__all__ = (
    'Game',
    'UserGame',
    'ElementKind',
    'Element',
    'EventKind',
    'Event',
    'EventElement',
    'Comment'
)


class Game(models.Model):
    name = models.CharField(max_length=256)


class UserGame(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)


class ElementKind(models.Model):
    name = models.CharField(max_length=256)
    game = models.ForeignKey(Game)


class Element(models.Model):
    name = models.CharField(max_length=256)
    kind = models.ForeignKey(ElementKind)


class EventKind(models.Model):
    game = models.ForeignKey(Game)
    sentence = models.CharField(max_length=256)


class Event(models.Model):
    kind = models.ForeignKey(EventKind)


class EventElement(models.Model):
    event = models.ForeignKey(Event)
    element = models.ForeignKey(Element)
    identity = models.CharField(max_length=32)


class Comment(models.Model):
    event = models.ForeignKey(Event)
    text = models.TextField()
