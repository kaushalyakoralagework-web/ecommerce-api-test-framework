import os
import yaml
from pathlib import Path
from typing import Any


class ConfigLoader:
    """
    Loads and manages environment configuration from environments.yaml.
    Supports environment switching via ENV environment variable.
    Usage: ENV=staging pytest
    """

    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self) -> None:
        # Resolve from this file's location — goes up from utils/ -> src/ -> project root
        project_root = Path(__file__).resolve().parent.parent.parent
        config_path = project_root / "config" / "environments.yaml"

        if not config_path.exists():
            # Fallback to working directory
            config_path = Path.cwd() / "config" / "environments.yaml"

        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found. Tried: {config_path}"
            )

        with open(config_path, "r") as f:
            self._config = yaml.safe_load(f)

    def _get_environment(self) -> str:
        return os.getenv("ENV", self._config.get("default_environment", "dev"))

    def _get_env_config(self) -> dict:
        env = self._get_environment()
        env_config = self._config.get("environments", {}).get(env)

        if env_config is None:
            raise ValueError(
                f"Environment '{env}' not found in configuration. "
                f"Available environments: {list(self._config.get('environments', {}).keys())}"
            )
        return env_config

    @property
    def base_url(self) -> str:
        return self._get_env_config()["base_url"]

    @property
    def timeout(self) -> int:
        return self._get_env_config()["timeout"]

    @property
    def retry_attempts(self) -> int:
        return self._get_env_config()["retry_attempts"]

    @property
    def verify_ssl(self) -> bool:
        return self._get_env_config()["verify_ssl"]

    @property
    def headers(self) -> dict:
        return self._get_env_config()["headers"]

    @property
    def environment(self) -> str:
        return self._get_environment()

    @property
    def ui_config(self) -> dict:
        return self._config.get("ui", {})

    @property
    def reporting_config(self) -> dict:
        return self._config.get("reporting", {})

    def get(self, key: str, default: Any = None) -> Any:
        return self._get_env_config().get(key, default)


config = ConfigLoader()