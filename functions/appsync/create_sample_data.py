#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def lambda_handler(event, context):
    LOGGER.info(json.dumps(event, ensure_ascii=False))

    input = event.get("input")
    if input is None:
        return

    id = input.get("id")
    if id is None:
        return

    name = input.get("name")
    if name is None:
        return

    description = input.get("description")
    if description is None:
        return

    return {
        "id": id,
        "name": name,
        "description": description
    }
