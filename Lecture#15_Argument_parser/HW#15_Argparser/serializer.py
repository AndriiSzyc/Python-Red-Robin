import datetime
import csv
import json


class Human:
    def __init__(self, name, surname, age, birth_date):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth_date = birth_date or datetime.datetime.now()


class HumanSerializer:
    def serialize(self, obj, format):
        if format == "JSON":
            return self._serialize_to_json(obj)
        elif format == "CSV":
            return self._serialize_to_csv(obj)
        else:
            raise ValueError(format)

    def _serialize_to_json(self, obj):
        format_date = obj.birth_date.strftime("%d-%m-%Y %H:%M:%S")
        myData = {
            "name": obj.name,
            "surname": obj.surname,
            "age": obj.age,
            "birth_date": format_date,
        }
        with open("file.json", "w") as jsonfile:
            json.dump(myData, jsonfile)

    def _serialize_to_csv(self, obj):
        format_date = obj.birth_date.strftime("%d-%m-%Y")
        myData = [
            ["name", "surname", "age", "birth_date"],
            [obj.name, obj.surname, obj.age, format_date],
        ]
        with open("file.csv", "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerows(myData)


obj = Human("Oleksiy", "Maksymiv", 30, datetime.date(1992, 11, 13))
print(obj.birth_date, type(obj.birth_date))
HumanSerializer().serialize(obj, "CSV")  # 1992-11-13 => 13-11-1992
HumanSerializer().serialize(obj, "JSON")  # 1992-11-13 => 1992-11-13 00:00:00
