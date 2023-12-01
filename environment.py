from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError
from functools import lru_cache


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8')

    def __init__(self):
        try:
            super().__init__()
        except ValidationError as exception:
            print(f"{str(exception)}")
            exit(1)


class Variables(Settings):
    sender_email: str
    sender_password: str
    david_email: str
    brandon_email: str


@lru_cache
def get_variables() -> Variables:
    return Variables()


variables = get_variables()
