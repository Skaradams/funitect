import json
from django.db import models
from django.contrib.auth.models import User


__all__ = (
    'Game',
    'UserGame',
    'ElementKind',
    'Element',
    'ElementComment',
    'ElementSketch',
    'EventKind',
    'Event',
    'EventElement',
    'EventComment',
    'EventNotification',
    'EventCommentNotification',
    'ElementNotification',
    'ElementCommentNotification',
    'ElementSketchNotification',
)


"""
Game related models
"""


class Game(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class UserGame(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)


"""
Element related models
"""


class ElementKind(models.Model):
    name = models.CharField(max_length=256, unique=True)
    game = models.ForeignKey(Game)

    def __str__(self):
        return self.name


class Element(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    kind = models.ForeignKey(ElementKind)

    def __str__(self):
        return self.name


class ElementComment(models.Model):
    element = models.ForeignKey(Element)
    text = models.TextField()
    user = models.ForeignKey(User)


class ElementSketch(models.Model):
    element = models.ForeignKey(Element)
    src = models.CharField(max_length=256)
    user = models.ForeignKey(User)


"""
Event related models
"""


class EventKind(models.Model):
    game = models.ForeignKey(Game)
    sentence = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.sentence

    def save(self):
        try:
            json.loads(self.sentence)
        except Exception, e:
            raise ValueError('Sentence has to be in json format : %s' % str(e))
        super(EventKind, self).save()


class Event(models.Model):
    user = models.ForeignKey(User)
    kind = models.ForeignKey(EventKind)


class EventElement(models.Model):

    class Meta:
        unique_together = ('event', 'identity')

    event = models.ForeignKey(Event)
    element = models.ForeignKey(Element)
    identity = models.CharField(max_length=32)


class EventComment(models.Model):
    event = models.ForeignKey(Event)
    text = models.TextField()
    user = models.ForeignKey(User)


"""
Dashboard related models
"""


class EventNotification(models.Model):
    game = models.ForeignKey(Game)
    timestamp = models.IntegerField()
    event = models.ForeignKey(Event)


class EventCommentNotification(models.Model):
    game = models.ForeignKey(Game)
    timestamp = models.IntegerField()
    comment = models.ForeignKey(EventComment)


class ElementNotification(models.Model):
    game = models.ForeignKey(Game)
    timestamp = models.IntegerField()
    element = models.ForeignKey(Element)


class ElementCommentNotification(models.Model):
    game = models.ForeignKey(Game)
    timestamp = models.IntegerField()
    comment = models.ForeignKey(ElementComment)


class ElementSketchNotification(models.Model):
    game = models.ForeignKey(Game)
    timestamp = models.IntegerField()
    sketch = models.ForeignKey(ElementSketch)
