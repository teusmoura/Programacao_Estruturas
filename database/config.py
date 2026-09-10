import os

MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "lojas_rede")


def get_mysql_config(
    database: str | None = None,
    incluir_banco: bool = True,
):
    """Retorna os parâmetros de conexão com o MySQL.

    Os valores podem ser sobrescritos por variáveis de ambiente,
    permitindo que o ambiente didático funcione sem editar arquivos do projeto.
    """
    config = {
        "host": MYSQL_HOST,
        "port": MYSQL_PORT,
        "user": MYSQL_USER,
        "password": MYSQL_PASSWORD,
        "use_pure": True,
    }
    if database:
        config["database"] = database
    elif incluir_banco and MYSQL_DATABASE:
        config["database"] = MYSQL_DATABASE
    return config
