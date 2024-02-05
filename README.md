### Hexlet tests and linter status:
[![Actions Status](https://github.com/mishablokhin/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mishablokhin/python-project-49/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/c106a2f3749f6b9153b9/maintainability)](https://codeclimate.com/github/mishablokhin/python-project-49/maintainability)

### Описание проекта
Проект **Brain Games** написан в рамках курса Python-разработчик на Hexlet. 
Проект представляет собой набор из 5 консольных игр:
1. Brain Even - игра на проверку чисел на чётность или нечётность
1. Brain Calc - игра на решение задач на сложение или умножение
1. Brain GCD - игра на определение наибольшего общего делителя для двух чисел
1. Brain Prime - игра на определение является ли число простым
1. Brain Progression - игра на заполнение арифметической прогрессии пропущенными числами

**Все игры следуют общим правилам:**
- Числа для игр генерируются случайным образом.
- Для победы необходимо правильно дать ответ на три вопроса.
- В случае, если пользователь даст неправильный ответ, игра завершается.

### Работа с приложением
- Установка приложения в систему для текущего пользователя:
```
make package-install
```
- Удаление приложения из системы
```
make package-uninstall
```
Запуск игр из терминала после установки пакета:
```
brain-even
brain-calc
brain-gcd
brain-prime
brain-progression
```
### Аскинемы с примерами работы разных игр
asciinema record: brain-even

[![asciicast](https://asciinema.org/a/mXTH0pF3IYMauUxhcijz0sPax.svg)](https://asciinema.org/a/mXTH0pF3IYMauUxhcijz0sPax)

asciinema record: brain-calc

[![asciicast](https://asciinema.org/a/FxOGrkS8hQiZ6AxyajMpRMbej.svg)](https://asciinema.org/a/FxOGrkS8hQiZ6AxyajMpRMbej)

asciinema record: brain-gcd

[![asciicast](https://asciinema.org/a/CGqXXNjjptf8BiyHS6lCAhBaI.svg)](https://asciinema.org/a/CGqXXNjjptf8BiyHS6lCAhBaI)

asciinema record: brain-progression

[![asciicast](https://asciinema.org/a/ypTtodWMv2VVAOD1pb2pxzWxP.svg)](https://asciinema.org/a/ypTtodWMv2VVAOD1pb2pxzWxP)

asciinema record: brain-prime

[![asciicast](https://asciinema.org/a/Qgztv11NFdFodOeC4W0J8BPAf.svg)](https://asciinema.org/a/Qgztv11NFdFodOeC4W0J8BPAf)
