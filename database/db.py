from mongoengine import connect
from mongoengine import Document
from mongoengine import IntField
from mongoengine import StringField
from mongoengine import BinaryField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import DateField

from config import settings


connect(settings.DB_NAME, host=settings.DB_HOST, port=settings.DB_PORT)


class Student(Document):
    student_id = IntField(required=True, unique=True)
    full_name = StringField(required=True)
    topic = StringField(required=True)
    potok = StringField(required=True)
    date = DateField(required=True)
    juries = ListField(ReferenceField('Jury'))

class Jury(Document):
    jury_id = IntField(required=True, unique=True)
    full_name = StringField(required=True)
    signature = BinaryField()
    students = ListField(ReferenceField(Student))
