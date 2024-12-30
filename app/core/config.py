from pydantic_settings import BaseSettings


class Settings(BaseSettings):
   # Base
   api_v1_prefix: str
   debug: bool
   project_name: str
   version: str
   description: str

   # Database
   db_async_connection_str: str
   
   db_async_test_connection_str: str = "postgresql+asyncpg://hero:heroPass123@localhost:5436/heroes_db_tests"
   
settings = Settings()