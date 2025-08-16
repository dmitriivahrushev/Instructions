from pg_connect import Dbconfig, PosgresManager
from config import Config




if __name__ == '__main__':
    local_pg = Config.PostgresLocal
    
    config = Dbconfig(
        host=local_pg.host,
        database=local_pg.db_name,
        user=local_pg.user,
        password=local_pg.password,
        port=local_pg.port 
    )

    with PosgresManager(config) as db:
        select = db.execute_query("SELECT * FROM public.b")
        print(select)
