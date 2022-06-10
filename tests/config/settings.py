import logging.config
from pathlib import Path

from config.logger import LOGGING_CONFIG
from pydantic import AnyHttpUrl, BaseSettings, DirectoryPath, Field, RedisDsn

logging.config.dictConfig(LOGGING_CONFIG)
ROOT_DIR = Path(__file__).parent.parent


class TestSettings(BaseSettings):

    super_user_login: str = Field(default="email", env="SUPER_USER_LOGIN")
    super_user_pass: str = Field(default="password", env="SUPER_USER_PASS")

    root_dir: DirectoryPath = ROOT_DIR
    testdata: DirectoryPath = ROOT_DIR / "testdata"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = TestSettings()
