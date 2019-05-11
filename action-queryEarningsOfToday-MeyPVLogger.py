#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes


def action_wrapper(hermes, intent_message):
    result_sentence = "Dies ist ein Test"

    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("PM_SNIPS:queryEarningsOfToday", action_wrapper).start()
