#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    LOGGER.info(json.dumps(event, ensure_ascii=False))

    id = event.get("id")
    if id is None:
        return

    return {
        "id": id,
        "name": "Sample Name",
        "description": "You are Done! Welcome to AppSync!"
    }
