# Ошибка кодировок PostgreSQL
При загрузке файла в базу возникает ошибка:
~~~
ERROR: character with byte sequence 0x98 in encoding "WIN1251" has no equivalent in encoding "UTF8"
~~~

## Решение

### Если используешь графический интерфейс Dbeaver:
1. Открой файл в WPS Office
2. Сохрани его в формате:  
   **CSV UTF-8 (Comma delimited) (.csv)**

### Если используешь `psql`:
1. Проверь текущие кодировки на стороне сервера и клиента:
   ```sql
   SHOW server_encoding;
   SHOW client_encoding;

2. Если кодировки отличаются, установи клиентскую в UTF-8:
   ```sql
   SET client_encoding = 'UTF8';

3. После этого можно повторно загрузить файл — ошибка должна исчезнуть.
