### Курс "Python Developer. Basic" ###

### Домашнее задание № 5 ###

## Docker контейнер c веб-приложением ##

### [app.py](app.py) ###

### [Dockerfile](Dockerfile) ###

### [requirements.txt](requirements.txt) ###

### Команды в терминале: ###

```
cd C:\Work\HomeWork05
docker build -t my-fastapi-app:1.0 .
docker run -d -p 8000:8000 --name fastapi-container my-fastapi-app:1.0
```
