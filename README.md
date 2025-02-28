### Hexlet tests and linter status:
[![Actions Status](https://github.com/RustemYeldessov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/RustemYeldessov/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/f600ac56e652872bb201/maintainability)](https://codeclimate.com/github/RustemYeldessov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f600ac56e652872bb201/test_coverage)](https://codeclimate.com/github/RustemYeldessov/python-project-50/test_coverage)



# Проект: Сравнение файлов (JSON/YAML)

## Описание

Этот проект предоставляет утилиту для сравнения файлов в форматах JSON и YAML. Программа анализирует различия между двумя файлами и выводит результат в удобочитаемом формате.

## Возможности

- Сравнение файлов в форматах JSON и YAML

- Поддержка нескольких форматов вывода (stylish, plain, JSON)

- Обнаружение добавленных, удалённых и изменённых ключей

## Установка

1. Клонируйте репозиторий:

    В терминале выполните команду:
    ```bash
    git clone https://github.com/RustemYeldessov/python-project-49.git

2. Перейдите в директорию проекта:

    ```bash
   cd python-project-49

3. Установите зависимости:

    ```bash
    make install

4. Установите пакет глобально:

    ```bash
    pip install .

## Примеры работы
### Входные файлы:

**file1.json**

    {
      "host": "hexlet.io",
      "timeout": 50,
      "proxy": "123.234.53.22",
      "follow": false
    }

**file2.json**

    {
      "timeout": 20,
      "verbose": true,
      "host": "hexlet.io"
    }

**Вывод:**

    {
      - follow: false
        host: hexlet.io
      - proxy: 123.234.53.22
      - timeout: 50
      + timeout: 20
      + verbose: true
    }

## Использование

### Основная команда

    uv run gendiff tests/fixtures/file3.json tests/fixtures/file4.json

Пример запуска команды: https://asciinema.org/a/toPgRsXcfvqpLTbzndwupJ3he


Программа сравнит два файла форматов JSON или YAML, выведя различия в стандартном формате.

## Опции

    gendiff -h

Выведет справку по использованию утилиты:

Пример запуска команды: https://asciinema.org/a/i6VWNYmCSo5RWDylFMj2a448Y


### Форматы вывода

Программа поддерживает несколько форматов вывода:

- stylish (по умолчанию) — древовидный формат

- plain — текстовое описание изменений

- json — формат JSON

**Формат plain**

    uv run gendiff -f plain tests/fixtures/file3.json tests/fixtures/file4.json

Пример запуска команды: https://asciinema.org/a/ABfHxgknyolsYDoPe2OqvqqR4

**Формат JSON**

    uv run gendiff -f json tests/fixtures/file3.json tests/fixtures/file4.json

Пример запуска команды: https://asciinema.org/a/RJSH67RqMCiiK2CVnMjslpESs

## Тестирование

Запуск тестов:

    make test-coverage

