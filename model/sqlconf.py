from pydantic import PostgresDsn
from pydantic_core import MultiHostUrl
class Config:

    SCHEME = "postgresql"
    USERNAME = "postgres"
    PASSWORD = "postgres"
    # HOST = "host.docker.internal"
    HOST = "postgres"
    PORT = 5432
    PATH = "postgres"

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme=self.SCHEME,
            username=self.USERNAME,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT,
            path=self.PATH,
        )
    
config = Config()