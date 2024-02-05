<!--
> A batteries-included Django starter project by Sameer Shahi Thakuri.
-->


zx

asgiref==3.5.0
black==22.1.0
certifi==2023.5.7
cffi==1.15.1
charset-normalizer==3.1.0
click==8.0.4
colorama==0.4.4
cryptography==40.0.2
defusedxml==0.7.1
dj-database-url==1.2.0
Django==4.0.3
django-ckeditor==6.1.0
django-js-asset==2.0.0
gunicorn==20.1.0
idna==3.4
marshmallow==3.15.0
mypy-extensions==0.4.3
oauthlib==3.2.2
packaging==21.3
pathspec==0.9.0
Pillow==9.0.1
platformdirs==2.5.1
psycopg2-binary==2.9.5
pycparser==2.21
PyJWT==2.7.0
pyparsing==3.0.7
python-dotenv==0.19.2
python3-openid==3.2.0
requests==2.31.0
requests-oauthlib==1.3.1
six==1.16.0
social-auth-app-django==5.0.0
social-auth-core==4.4.2
sqlparse==0.4.2
tomli==2.0.1
tzdata==2022.1
urllib3==2.0.2
validate-email==1.3




## 🚀 Features

- Django 4.0.3 & Python 3.9.6
- Install via [virtualenv](https://pypi.org/project/virtualenv/) or [Pipenv](https://pypi.org/project/pipenv/)
- Python Code Formatter : [black](https://pypi.org/project/black/)

## ![Homepage](homepage.png)

## Table of Contents

- **[Installation](#installation)**
  - [Pip](#pip)
  - [Pipenv](#pipenv)
- [Setup](#setup)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

---

## 📖 Installation

DPFP can be installed via Pip, Virtualenv or Pipenv depending upon your setup. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/Sam231221/DPFP-National-Hackathon.git
```

postgres://dpfp_user:IQtoyjyjfVYbnFZkWaoEJ4JGVnX0x9Er@dpg-chpfqn7dvk4goeo39mt0-a/dpfp

### using Venv

```
$ python3 -m venv Zvirtual
$ source venv Zvirtual/bin/activate
(djangoprostartertemplate) $ pip install -r requirements.txt
(djangoprostartertemplate) $ python manage.py migrate
(djangoprostartertemplate) $ python manage.py loaddata user.json
(djangoprostartertemplate) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### using Pipenv

```
$ pipenv install
$ pipenv shell
(djangoprostartertemplate) $ python manage.py migrate
(djangoprostartertemplate) $ python manage.py loaddata user.json
(djangoprostartertemplate) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

# Load the site at http://127.0.0.1:8000

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!.

## ⭐️ Support

Give a ⭐️ if this project helped you!

## License

[The MIT License](LICENSE)
