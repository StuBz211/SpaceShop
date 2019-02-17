
### SPACE STUFF SHOP  

## Installation & setup

1. скопировать репозиторий: `git clone https://github.com/StuBz211/SpaceShop.git`.
2. установить [pyenv](https://github.com/yyuu/pyenv#installation).
3. установить [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv#installation).
4. Установить python 3.6: `pyenv install 3.6`.
5. создать виртуальное окружение `python3 -m venv env`.
6. активировать виртуальное окружение `source env\(Scripts|bin)\activate`.
7 `python -m pip install --updage pip` обновим pip до последней версии
8. `pip install -r requirements.txt` установим необходимые библиотеки
Теперь можно работать с менеджером django запускать сервер/миграции, вы великолепны!

`python manager.py makemigrations {app_name}` создание миграции бд.

`python manager.py migrations` устновка миграций 

`python manager.py content` создать тестовые модели из таблиц [categories.csv](/shop/contents/categories.csv) и [products.csv](/shop/contents/products.csv)