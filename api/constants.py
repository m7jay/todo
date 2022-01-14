from django.db import models


class TodoStatus(models.TextChoices):
    TODO = "Todo", "Todo"
    IN_PROGRESS = "In Progress", "In Progress"
    DONE = "Done", "Done"
