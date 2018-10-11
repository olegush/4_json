# Prettify JSON

The script formats json data to redable view

# Quickstart

Script needs a file data.json , contained unfotmatted json data
for example:
```
[{"Id":"79742784-9ef3-4543-bc98-a219a8903c18","Number":1,"Cells":{"global_id":14371450,"Name":"��������� ���","IsNetObject":"��","OperatingCompany":"��������� ���","TypeService":"���������� ����������������� �������","AdmArea":"�������� ���������������� �����","District":"����� �������","Address":"����� ��������� �������, ��� 10","PublicPhone":[{"PublicPhone":"(495) 777-51-95"}],"WorkingHours":[{"Hours":"09:30-22:30","DayOfWeek":"�����������"},{"Hours":"09:30-22:30","DayOfWeek":"�������"},{"Hours":"09:30-22:30","DayOfWeek":"�����"},{"Hours":"09:30-22:30","DayOfWeek":"�������"},{"Hours":"09:30-22:30","DayOfWeek":"�������"},{"Hours":"09:30-22:30","DayOfWeek":"�������"},{"Hours":"09:30-22:30","DayOfWeek":"�����������"}],"ClarificationOfWorkingHours":null,"geoData":{"type":"Point","coordinates":[37.39703804817934,55.740999719549094]}}}, {"Id":"1bd07c21-05de-4015-b015-d22657168ded","Number":2,"Cells":{"global_id":14934782,"Name":"��������� � ���������","IsNetObject":"��","OperatingCompany":"���������","TypeService":"���������� ����������������� �������","AdmArea":"������-��������� ���������������� �����","District":"����� ��������","Address":"����� �������, ��� 6","PublicPhone":[{"PublicPhone":"(499) 909-40-08"}],"WorkingHours":[{"Hours":"10:00-22:00","DayOfWeek":"�����������"},{"Hours":"10:00-22:00","DayOfWeek":"�������"},{"Hours":"10:00-22:00","DayOfWeek":"�����"},{"Hours":"10:00-22:00","DayOfWeek":"�������"},{"Hours":"10:00-22:00","DayOfWeek":"�������"},{"Hours":"10:00-22:00","DayOfWeek":"�������"},{"Hours":"10:00-22:00","DayOfWeek":"�����������"}],"ClarificationOfWorkingHours":null,"geoData":{"type":"Point","coordinates":[37.593177064306758,55.897722369367969]}}}, {"Id":"a16c8154-09d8-4207-8e13-cb8db654e95c","Number":3,"Cells":{"global_id":14937274,"Name":"������-�","IsNetObject":"���","OperatingCompany":null,"TypeService":"���������� ����������������� �������","AdmArea":"������-��������� ���������������� �����","District":"����� ��������","Address":"������������ �����, ��� 72","PublicPhone":[{"PublicPhone":"(905) 791-87-13"}],"WorkingHours":[{"Hours":"09:00-22:00","DayOfWeek":"�����������"},{"Hours":"09:00-22:00","DayOfWeek":"�������"},{"Hours":"09:00-22:00","DayOfWeek":"�����"},{"Hours":"09:00-22:00","DayOfWeek":"�������"},{"Hours":"09:00-22:00","DayOfWeek":"�������"},{"Hours":"09:00-22:00","DayOfWeek":"�������"},{"Hours":"09:00-22:00","DayOfWeek":"�����������"}],"ClarificationOfWorkingHours":null,"geoData":{"type":"Point","coordinates":[37.588035999647531,55.89020100016689]}}}]

```

Run pprint_json.py

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py

[
    {
        "Cells": {
            "Address": "\u0443\u043b\u0438\u0446\u0430 \u0410\u043a\u0430\u0434\u0435\u043c\u0438\u043a\u0430 \u041f\u0430\u0432\u043b\u043e\u0432\u0430, \u0434\u043e\u043c 10",
            "AdmArea": "\u0417\u0430\u043f\u0430\u0434\u043d\u044b\u0439 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433",
            "ClarificationOfWorkingHours": null,
            "District": "\u0440\u0430\u0439\u043e\u043d \u041a\u0443\u043d\u0446\u0435\u0432\u043e",
            "IsNetObject": "\u0434\u0430",
            "Name": "\u0410\u0440\u043e\u043c\u0430\u0442\u043d\u044b\u0439 \u041c\u0438\u0440",
            "OperatingCompany": "\u0410\u0440\u043e\u043c\u0430\u0442\u043d\u044b\u0439 \u041c\u0438\u0440",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "TypeService": "\u0440\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u0440\u043e\u0434\u043e\u0432\u043e\u043b\u044c\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0442\u043e\u0432\u0430\u0440\u043e\u0432",
            "WorkingHours": [
                {
                    "DayOfWeek": "\u043f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "\u0432\u0442\u043e\u0440\u043d\u0438\u043a",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "\u0441\u0440\u0435\u0434\u0430",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "\u0447\u0435\u0442\u0432\u0435\u0440\u0433",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "\u043f\u044f\u0442\u043d\u0438\u0446\u0430",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "\u0441\u0443\u0431\u0431\u043e\u0442\u0430",
                    "Hours": "09:30-22:30"
                },
                {
                    "DayOfWeek": "\u0432\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435",
                    "Hours": "09:30-22:30"
                }
            ],
            "geoData": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "global_id": 14371450
        },
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1
    },


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
