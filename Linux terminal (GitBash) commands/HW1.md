## HW1 : Linux terminal (GitBash) commands

**№** | **Задание** | **Команда**
--- | --- | ---
1 | Посмотреть где я | `pwd`
2 | Создать папку | `mkdir HW1`
3 | Зайти в папку | `cd HW1`
4 | Создать 3 папки | `mkdir oneFolder twoFolder threeFolder`
5 | Зайти в любоую папку | `cd oneFolder`
6 | Создать 5 файлов (3 txt, 2 json) | `touch oneTxt.txt secondTxt.txt thirdTxt.txt oneJson.json secondJson.json`
7 | Создать 3 папки | `mkdir txtFolder jsonFolder anotherFiles`
8 | Вывести список содержимого папки | `ls -la`
9 | + Открыть любой txt файл | `vim oneTxt.txt`
10 | + написать туда что-нибудь, любой текст | `i`
11 | + сохранить и выйти | `Esc :wq`
12 | Выйти из папки на уровень выше | `cd ..`
13 | Переместить любые 2 файла, которые вы создали, в любую другую папку | `mv oneJson.json secondJson.json jsonFolder/`
14 | Скопировать любые 2 файла, которые вы создали, в любую другую папку | `cp oneTxt.txt secondTxt.txt txtFolder/`
15 | Найти файл по имени | `find -name secondTxt.txt`
16 | Просмотреть содержимое в реальном времени (команда grep) изучите как она работает | `tail -f name.log \| grep --line-buffered pattern`
17 | Вывести несколько первых строк из текстового файла | `head -n3 oneTxt.txt`
18 | Вывести несколько последних строк из текстового файла | `tail -n3 oneTxt.txt`
19 | Просмотреть содержимое длинного файла (команда less) изучите как она работает | `less oneTxt.txt`
20 | Вывести дату и время | `date`

------------------------------

**Задания\***
1. Отправить http запрос на сервер `http://162.55.220.72:5005/terminal-hw-request`:

`curl http://162.55.220.72:5005/terminal-hw-request`

`curl http://162.55.220.72:5005/get_method?name=Natalia&age=43`

2. Написать скрипт который выполнит автоматически пункты 3, 4, 5, 6, 7, 8, 13 

`touch myScript.sh`

`vim myscript.sh`
```
#!/bin/bash
cd HW1
mkdir oneFolder twoFolder threeFolder
cd oneFolder
touch oneTxt.txt secondTxt.txt thirdTxt.txt oneJson.json secondJson.json
mkdir txtFolder jsonFolder anotherFiles
ls -la
mv oneJson.json secondJson.json jsonFolder/
```
`chmod +x ./myscript.sh`

`./myscript.sh`

------------------------------
#### Полезности

`open ./` - откроет текущую папку в проводнике (Linux)

`clear` - очистка экрана

[Grep](https://losst.ru/gerp-poisk-vnutri-fajlov-v-linux)

[Перенаправить вывод tail -f через grep в файл](https://dgrafov.blogspot.com/2015/06/tail-f-grep.html)

[10 команд curl (Client URL), которые вам следует знать](https://vc.ru/dev/155069-10-komand-curl-kotorye-vam-sleduet-znat)

[Bash-скрипты](https://habr.com/ru/company/ruvds/blog/325522/)

