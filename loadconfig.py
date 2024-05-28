class Config:
    """
    Impostare qui le credenziali di MySQL e Redis, e l'attivazione o meno della cache
    """

    def __init__(self):
        # Attiva o disattiva il caching
        self.enable_caching = True

        # default db settings
        self.db_config = dict(
            host="localhost",
            user="root",
            port=3306,
            password="PASSWORD_MYSQL",
            db="company",
        )

        # default redis settings
        self.cache_config = dict(host="127.0.0.1", port=6379, password="PASSWORD_REDIS")

        # Quanti impiegati mettere nel DB?
        self.how_many_employees = 1000

    def get_db_config(self):
        return self.db_config

    def get_cache_config(self):
        return self.cache_config
