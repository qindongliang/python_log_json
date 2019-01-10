# -*- coding: utf-8 -*-
import logging
from logging.config import fileConfig


def base_configuration():
    fileConfig('log_conf.ini')
    log = logging.getLogger(__name__)

    try:
        log.info("message1")
        # log.info("message2", {"extra_info": " trace info"})
        # log.info({"message3": " log info"})
        a = 1 / 0
    except Exception:
        # log.error("occurred exception", exc_info=True)
        log.exception({"exception_id": 22000})
        # log.exception("occurred exception")
        # log.exception("occurred exception", {"exception_id":225462})

base_configuration()