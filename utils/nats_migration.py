from datetime import timedelta
from nats.js.api import StorageType
from config_data.config import Config


async def create_stream(js, config: Config):
    try:
        await js.stream_info(config.delayed_consumer.stream)
    except Exception:
        print(f"Stream '{config.delayed_consumer.stream}' does not exist. Creating new stream.")
        await js.add_stream(
    name=config.delayed_consumer.stream,
    subjects=[config.delayed_consumer.subject],
    storage=StorageType.FILE,
)
