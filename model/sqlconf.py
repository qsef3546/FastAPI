from pydantic import PostgresDsn
from pydantic_core import MultiHostUrl
class Config:

    SCHEME = "postgresql"
    USERNAME = "postgres"
    PASSWORD = "admin1234!"
    HOST = "host.docker.internal"
    PORT = 5432
    PATH = "user"

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