# PySpark_test
___
### Описание
Метод "get_joined_dataframes(df1, df2, df1_2)", в файле "get_data.py",
позволяет объединить два других датафрейма (продукты и их категории) в один
по названию продукта и именованию категории.
___

### Схема данных
Все 3 датафрейма (две родительские таблицы, 
одна связная дочерняя, т.к. связь М:М).

#### Продукт
* id - уникальный идентификатор (PK); 
* name - название продукта.

#### Категория
* id - уникальный идентификатор (PK);
* name - название категории.

#### Продукт_Категория
* id - уникальный идентификатор (PK);
* id_product - id продукта (FK);
* id_category - id категории (FK).
___

### Как это работает
На вход подается все 3 датафрейма. С помощью "LEFT_JOIN" мы присоединяем
к датафрейму продукт остальные датафреймы. 

Сначала, присоединяем Продукт_Категория.
Затем, Категория. 

После этого делаем "SELECT" по названиям продукта и категории и получаем нужный результат.
___

### Вьюшка
В подкаталоге "data" есть небольшие тестовые "csv" файлы.

Предварительно установив "PySpark", можно запустить "main.py" и проверить 
работоспособность метода "get_joined_dataframes(df1, df2, df1_2)"