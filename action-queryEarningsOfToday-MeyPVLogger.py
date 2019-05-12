#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import requests 
from threading import Thread

def query(hermes, url):
    r = requests.get(url)
    response = r.json()
    e = int(response['e'])

    result_sentence = "Heute wurden {:d} Kilo Watt Stunden produziert".format(e)

    hermes.publish_start_session_notification("", result_sentence)
    
    return True

def action_wrapper(hermes, intent_message):
    URL = 'http://192.168.2.106/php/getOverview.php'
    queryThread = Thread(target=query, args=[hermes, URL])
    queryThread.start()

    current_session_id = intent_message.session_id
    result_sentence = "Einen Moment bitte"

    hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("PM_SNIPS:queryEarningsOfToday", action_wrapper).start()
