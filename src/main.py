import tomllib as tomli
import huggingface_hub
import requests

def backend_factory() -> requests.Session:
    session = requests.Session()
    session.proxies = {"http": "socks5://127.0.0.1:1080", "https": "socks5://127.0.0.1:1080"}
    return session

with open("config.toml", "rb") as f:
    config = tomli.load(f)['SPACE']
    name, org, prefix, token = config.values()

huggingface_hub.configure_http_backend(backend_factory=backend_factory)
repo = huggingface_hub.Repository(local_dir=f"{prefix}/{name}", clone_from=f"{org}/{name}", repo_type='space', token=token)

