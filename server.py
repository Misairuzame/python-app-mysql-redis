from flask import Flask, render_template

from database import Database
from loadconfig import Config
from rediscache import Cache

app = Flask(__name__)

# initialize the db
db = Database()

# initialize the redis cache
cache = Cache()

config = Config()

# Attiva o meno l'uso della cache
IS_CACHING_ENABLED = config.enable_caching


@app.get("/")
def list_employees():
    def db_query():
        if IS_CACHING_ENABLED:
            emps = cache.get_conn().get("listemp")
            if not emps:
                # Cache miss
                emps = str(db.list_employees())
                # write into the cache
                cache.get_conn().set("listemp", str(emps))
                emps = eval(emps)
                print("N impiegati presi dal DB:", len(emps))
            else:
                # Cache hit
                emps = eval(emps)
                print("N impiegati presi dalla chace: ", len(emps))
        else:
            emps = str(db.list_employees())
            emps = eval(emps)
            print("N impiegati presi dal DB:", len(emps))

        return emps

    # query db or cache to get the list of the employees
    res = db_query()
    return render_template(
        "employees.html",
        result=res,
    )


if __name__ == "__main__":
    app.run()
