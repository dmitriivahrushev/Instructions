# Загрузка данных в PostgreSQL из файлов через Airflow   
- Проверяем есть ли нужный провайдер  
~~~
airflow providers list
~~~
- Установка провайдера  
~~~
pip install apache-airflow-providers-postgres
~~~

### Пример простой таски которая загрузит данных из csv  
Импортируем: `from airflow.providers.postgres.hooks.postgres import PostgresHook`  
C помощью `copy_expert` выполняем SQL запрос.
~~~
def copy_to_postgres():
    hook = PostgresHook(postgres_conn_id=PG_CONNECT)
    conn = hook.get_conn()
    cur = conn.cursor()

    with open(PATH_TO_CSV, 'r') as f:
        cur.copy_expert("""COPY stage.raw_data (data) FROM STDIN WITH (FORMAT CSV, HEADER FALSE, DELIMITER ';', ENCODING 'utf-8'); """, f)
    
    conn.commit()
    cur.close()
    conn.close()
~~~