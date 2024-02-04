# Мини-проект «Поварская книга»

Представляет собой небольшое веб-приложение на Django, предназначенное для учета продуктов и рецептов.

## Стек технологий

Python, Django

## Как запустить:

Клонируем себе репозиторий:

```
git clone git@github.com:AnastasDan/cookbook.git
```

Переходим в директорию:

```
cd cookbook
```

Cоздаем и активируем виртуальное окружение:

* Если у вас Linux/MacOS:

    ```
    python3 -m venv venv
    ```

    ```
    source venv/bin/activate
    ```

* Если у вас Windows:

    ```
    python -m venv venv
    ```

    ```
    source venv/Scripts/activate
    ```

Устанавливаем зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполняем миграции:

```
python manage.py migrate
```

Создаем суперпользователя:

```
python manage.py createsuperuser
```

Запускаем проект:

```
python manage.py runserver
```

## Для взаимодействия с функциями используем следующие ссылки:

### 1. **add_product_to_recipe**

Добавляет продукт с весом к указанному рецепту. Если продукт уже присутствует в рецепте, функция обновляет его вес.

**Параметры:**

  - `recipe_id` (id рецепта).
  - `product_id` (id продукта).
  - `weight` (Вес продукта в граммах).

**Пример использования:**

  ```
  http://127.0.0.1:8000/recipes/add_product_to_recipe/?recipe_id=1&product_id=2&weight=150
  ```

### 2. **cook_recipe**

Увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.

**Параметры:**

- `recipe_id` (id рецепта).

**Пример использования:**

  ```
  http://127.0.0.1:8000/recipes/cook_recipe/?recipe_id=1
  ```

### 3. **show_recipes_without_product**

Возвращает HTML-страницу с таблицей, в которой отображаются id и названия всех рецептов, в которых продукт отсутствует или присутствует в количестве менее 10 грамм.

**Параметры:**

- `product_id` (id продукта).

**Пример использования:**

```
http://127.0.0.1:8000/recipes/show_recipes_without_product/?product_id=3
```

## Автор мини-проекта

[Anastas Danielian](https://github.com/AnastasDan)