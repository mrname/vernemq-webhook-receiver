from django.db import models


class MQTTAction(models.Model):
    '''
    Basically a catch-all model. This is used to store the data on any possible
    webhook action received
    '''
    client_id = models.CharField(max_length=255, db_index=True)
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    peer_addr = models.CharField(max_length=255, blank=True, null=True)
    peer_port = models.IntegerField(blank=True, null=True)
    qos = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    mountpoint = models.CharField(max_length=255, blank=True, null=True)
    clean_session = models.NullBooleanField()
    retain = models.NullBooleanField()


class TopicSubscription(models.Model):
    action = models.ForeignKey(MQTTAction, related_name='topics')
    topic = models.CharField(max_length=255)
    qos = models.IntegerField()
