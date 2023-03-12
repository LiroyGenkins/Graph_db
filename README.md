# Graph_db_fastApi_rest
REST сервис для доступа к графовой БД Nebula

# Требования:
* Python 3.10
* Запущенная по адресу http://127.0.0.1:9669 Nebula Graph

# Установка и остановка сервиса
## Для запуска необходимо:
```
git clone https://github.com/LiroyGenkins/Graph_db_fastApi_rest.git
cd Graph_db_fastApi_rest  
setup.bat 
uvicorn main:app --reload
```
Сервис поднимется по адресу http://127.0.0.1:8000

## Остановка
Для остановки в открывшемся окне консоли достаточно нажать Ctrl+C

# API
В данном сервере имеется только один тип запросов `GET http://127.0.0.1:8000/[ПРОСТРАНСТВО]/name='[ФИО]`, которы возвращает все события в которых задействовано указанное имя.

Пример:
```
GET http://127.0.0.1:8000/test/name='Абахова Кира Егоровна'

{
    "_decode_type": "utf-8",
    "_resp": {
        "error_code": 0,
        "latency_in_us": 685668,
        "data": {
            "column_names": [
                "events"
            ],
            "rows": [
                {
                    "values": [
                        {
                            "field": 10,
                            "value": {
                                "src": {
                                    "field": 5,
                                    "value": "Абахова Кира Егоровна"
                                },
                                "dst": {
                                    "field": 5,
                                    "value": "Головатинский Геннадий Робертович"
                                },
                                "type": -1,
                                "name": "event",
                                "ranking": 0,
                                "props": {
                                    "event_id": {
                                        "field": 3,
                                        "value": 43828
                                    }
                                }
                            }
                        }
                    ]
                }
            ]
        },
        "space_name": "test",
        "error_msg": null,
        "plan_desc": null,
        "comment": null
    },
    "_data_set_wrapper": {
        "_decode_type": "utf-8",
        "_timezone_offset": 0,
        "_data_set": {
            "column_names": [
                "events"
            ],
            "rows": [
                {
                    "values": [
                        {
                            "field": 10,
                            "value": {
                                "src": {
                                    "field": 5,
                                    "value": "Абахова Кира Егоровна"
                                },
                                "dst": {
                                    "field": 5,
                                    "value": "Головатинский Геннадий Робертович"
                                },
                                "type": -1,
                                "name": "event",
                                "ranking": 0,
                                "props": {
                                    "event_id": {
                                        "field": 3,
                                        "value": 43828
                                    }
                                }
                            }
                        }
                    ]
                }
            ]
        },
        "_column_names": [
            "events"
        ],
        "_key_indexes": {
            "events": 0
        },
        "_pos": 0
    },
    "_all_latency": 692516,
    "_timezone_offset": 0
}
```
В файле test_main.http приведены ещё несколько примеров запросов.
