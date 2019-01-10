# python_log_json
一个将Python的log给转成json格式的工具包

## 背景

将日志转成json格式，有很多便利之处，最常见的的就是对接各种日志分析系统，如开源的ELK，将数据导入之后就能
快速的进行查询和分析，方便做各种统计，监控或报警等。

## 使用方式

（1）完全基于代码配置，向控制台和log文件同时记录日志

```python
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
        log.info("message1")
        # log.info("message2", {"extra_info": " trace info"})
        # log.info({"message3": " log info"})
        a = 1 / 0
    except Exception:
        # log.error("occurred exception", exc_info=True)
        log.exception({"exception_id": 22000})
        # log.exception("occurred exception")
        # log.exception("occurred exception", {"exception_id":225462})
```

（2）完全基于配置文件，向控制台和log文件同时记录日志

配置文件如下：
```ini
[loggers]
keys=root

[handlers]
keys=console,file

[formatters]
keys=json,json_pretty

[logger_root]
level=DEBUG
;handlers=console,file,rotate
handlers=console,file

[handler_console]
class=StreamHandler
level=INFO
formatter=json_pretty
args=(sys.stderr,)


[handler_file]
class=FileHandler
level=INFO
formatter=json
args=('log/base_conf.log','a','utf-8')

[handler_rotate]
class=handlers.TimedRotatingFileHandler
level=INFO
formatter=json
args=('log/rotate.log', 'D',1,0,'utf-8')

[formatter_json]
class=format.json_formatter.JSONFormatter

[formatter_json_pretty]
format=pretty
class=format.json_formatter.JSONFormatter
```

测试代码：

```python
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
```


其中定制的json组件，支持美化输出，在调试的过程中可以选择开启，上面的代码中有示例。

一个带有异常信息的json日志如下：
```json
{
 "name": "__main__",
 "args": [],
 "levelname": "ERROR",
 "levelno": 40,
 "pathname": "C:/texx.py",
 "lineno": 17,
 "funcName": "base_configuration",
 "thread": 10608,
 "threadName": "MainThread",
 "processName": "MainProcess",
 "process": 11916,
 "@timestamp": "2019-01-10T12:50:20.392Z",
 "host_name": "your-PC",
 "host_ip": "192.168.10.789",
 "message": {
  "exception_id": 22000
 },
 "exc_info": "Traceback (most recent call last):\n  File \"C:/txxx.py\", line 14, in base_configuration\n    a = 1 / 0\nZeroDivisionError: division by zero"
}
```
