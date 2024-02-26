from django import template
from datetime import datetime

register = template.Library()

@register.filter
def extract_pk_from_url(url):
    parts = url.split('/')
    pk = parts[-2]  # Assuming the pk is the second-to-last part of the URL
    return pk


@register.filter
def extract_last(url):
    parts = url.split('/')
    pk = parts[-1]  # Assuming the pk is the second-to-last part of the URL
    return pk


@register.filter
def calculate_age(value):
    today = datetime.today()
    birth_date = datetime.strptime(str(value), '%Y-%m-%d')
    age = today.year - birth_date.year

    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    return age
