### Курс "Python Developer. Basic" ###

### Домашнее задание № 13 ###

## GitLab pipelines ##

### Неудачные попытки: ###

* Сайт gitlab.com под моим аккаунтом не дал создать public репозиторий.
* Для запуска pipeline на сайте gitlab.com требуется подтверждение учетной записи с помощью зарубежной карточки или
  зарубежного телефона, которых у меня не было.
* GitLab в Docker-е я запустил, но GitLab Runner отказался устанавливаться в Docker из-за отсутствия доступа к
  gitlab-runner в репозитории GitLab.

Пришлось устанавливать GitLab и Runner в виртуальные машины (ВМ).

## Выполнил: ## 

1. Установил GitLab на одну ВМ (по инструкции).
2. Задал пароль пользователю GitLab:

```
gitlab-rake gitlab:password:reset
```

3. Установил GitLab Runner на другую ВМ (по инструкции). Использовал ручную установку, так как установка через GitLab
   репозиторий выдавала
   ошибку - не было доступа к gitlab-runner.
4. Зарегистрировал Runner в GitLab (по инструкции).
5. На ВМ с Runner настроил выполнение sudo без указания пароля:

```
$ sudo usermod -a -G sudo gitlab-runner
$ sudo visudo
```

В конец файла добавил строку:

```
gitlab-runner ALL=(ALL) NOPASSWD: ALL
```

6. В GitHub в директорию HomeWork13 скопировал файлы из директории HomeWork12, которые нужны для запуска тестов.
7. Скопировал файл requirements.txt и директорию HomeWork13 из GitHub в GitLab. В requirements.txt оставил только то,
   что нужно для запуска тестов.
8. В GitLab создал pipeline с тестированием.

### [.gitlab-ci.yml](./results/.gitlab-ci.yml) ###

9. В GitLab запустил pipeline автоматически в ветке main и вручную в MR.

### [Журнал запуска pipeline](./results/pipeline_log.txt) ###

### [Результат запуска pipeline](./results/Pipeline.jpg) ###


