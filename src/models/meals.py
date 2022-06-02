from mongoengine import Document, StringField, FloatField


class Meals(Document):
    """
    Template for a mongoengine document, which represents a user's favorite meal.
    :param name: required string value
    :param description: optional string value, fewer than 240 characters
    :param price: optional float value
    :param image_url: optional string image url
    """

    name = StringField(required=True)
    description = StringField(max_length=240)
    price = FloatField()
    image_url = StringField()
