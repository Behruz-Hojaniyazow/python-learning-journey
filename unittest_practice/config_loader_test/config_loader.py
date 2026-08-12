class ConfigLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def validate(self, config: dict) -> bool:
        required_keys = {"host", "port"}
        return required_keys.issubset(config.keys())

    def load_config(self):
        config = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or '=' not in line:
                        continue
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
        except FileNotFoundError:
            return {}

        if self.validate(config):
            return config
        return {}