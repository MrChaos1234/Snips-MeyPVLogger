#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import requests 


def action_wrapper(hermes, intent_message):
    URL = "http://192.168.2.106/php/getOverview.php"
    r = requests.get(url = URL) 
    data = r.json() 
    e = data['e']  

    result_sentence = "Heute wurden {} Kilo Watt Stunden produziert".format(e)

    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("PM_SNIPS:queryEarningsOfToday", action_wrapper).start()
