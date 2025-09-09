from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    chuck_api_url: str = "https://api.chucknorris.io/jokes/random"

    # HTTP client configuration
    http_connect_timeout: float = 5.0
    http_read_timeout: float = 5.0
    http_write_timeout: float = 5.0
    http_pool_timeout: float = 5.0

    http_max_keepalive_connections: int = 20
    http_max_connections: int = 100
