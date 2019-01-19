# -*- coding: utf-8 -*-
import logging.config
from format.json_formatter import JSONFormatter


def base_code():

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    # write log to file
    handler = logging.FileHandler("log/base_code.log")
    handler.setLevel(logging.INFO)
    # write log to console
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.INFO)
    # set formatter
    handler.setFormatter(JSONFormatter())
    handler_console.setFormatter(JSONFormatter("pretty"))
    # add handler
    log.addHandler(handler)
    log.addHandler(handler_console)

    try:
        log.info("message1","ms2","ms3",[1,2,3])
        log.info([1,23,45])
        # log.info("message2", {"extra_info": " trace info"})
        # log.info({"message3": " log info"})
        a = 1 / 0
    except Exception:
        # log.error("occurred exception", exc_info=True)
        log.exception("报错了")
        # log.exception("occurred exception")
        # log.exception("occurred exception", {"exception_id":225462})



base_code()