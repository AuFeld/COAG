'''
Use models to map data to MongoDB
'''

from app.database.models import MongoDBModel
import pymongo


class MyModel(MongoDBModel):
    additional_field1: str
    optional_field2: int = 42

    class Meta:
        collection = "mymodel_collection"
        # to create indexes
        indexes = [
            pymongo.IndexModel(...),
            pymongo.IndexModel(...),
        ]

mymodel = MyModel(additional_field1="value")
mymodel.save()

assert mymodel.additional_field1 == "value"
assert mymodel.optional_field2 == 42
assert isinstance(mymodel.id, int)


'''
OR use TimeStamped model with creation datetime
'''

from app.database.models import MongoDBTimeStampedModel
import datetime

class MyTimeStampedModel(MongoDBTimeStampedModel):

    class Meta:
        collection = "timestamped_collection"
        # to create indexes
        indexes = [
            pymongo.IndexModel(...),
            pymongo.IndexModel(...),
        ]

mymodel = MyTimeStampedModel()
mymodel.save()

assert isinstance(mymodel.id, int)
assert isinstance(mymodel.created, datetime)