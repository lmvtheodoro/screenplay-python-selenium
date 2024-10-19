import os
import json

class UrlManagerConfig:
    def __init__(self):
        env = os.getenv("Env", "Sandbox").lower()

        with open('src/data/urls.json') as json_file:
            self.urls = json.load(json_file)

        self.base_url = self.urls.get(env, {}).get("baseUrl", "")
        
        if not self.base_url:
            raise ValueError(f"Base URL not found for environment: {env}")