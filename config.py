
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6202933813:AAHv2-YuEWOJCFqDAGsAoW8XGC_PMcK5BpM")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "20244111"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "b76d27da2a4220fe109fe9ef0e866530")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQBpcYRcF0DdLBWUdhRLmrhRAYZapU3oKzHBzfbRBqcbXcdALMbMTboNY9I1cLgscmOSSNw9jzthyTuzi6cPTA3CXiuOYRKFUMWIj6X9iCa7LeDdc7bA6sadItTDEe5dVrWjsTDBK4PMPo-yAQUlFG8xo_aEsaI63WbFE-FxGSFoRS_uXcYgCrhHEF-yjRCzcOTekcq9MchmYJCfriphCuSMnHFR5PrwUS6xcvTQxo_UXuUSJfxSvrEGNLxmW8un_8pYJvHoKS2oXsPqc-YSMZHEIEkrq4prtJ08HJrR-3vY8p07yicPyRUjTRzIftUlXj3sMFxRkRlz5RFYwepQ5KAAAAAVfRjOkA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1792384197")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
