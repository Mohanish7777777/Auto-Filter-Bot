
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6285296811:AAEEUJZqjTDtolijNNxKFBjae3eI-FM9HXU")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "20244111"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "b76d27da2a4220fe109fe9ef0e866530")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQAeIqJFqWheltDVX1DoNbicb867l7-j-HkDiFpTMCDPkjfV45OVkeSUdlCSxYFZflbl_GOivdYVG-xWFEVVeKEpPxdGrE7SNpE0TDbsBR6Ko4judKhTEar4BI6g5vApZOyAdyeQGC6pSN6Ll0U8hutGFrfGc7dKz55oalzpExQgUfWY_ZV7v4Eyc_dqtWK6XjfwT-Mm-uaScaG7b_07VfWbcpkM7nokayc2wCM5oVI5Thzj6TnOwH1AW6CA2iyS_waNi8GjHJMEI0DeBOL7946G-lVWWXXXtF7Am9GwFBiEcUb2DdeDkSe7JmJWyR1tXGQZBIT_SXDy44HVH72eRPcIAAAAAUwsSyoA-yAQUlFG8xo_aEsaI63WbFE-FxGSFoRS_uXcYgCrhHEF-yjRCzcOTekcq9MchmYJCfriphCuSMnHFR5PrwUS6xcvTQxo_UXuUSJfxSvrEGNLxmW8un_8pYJvHoKS2oXsPqc-YSMZHEIEkrq4prtJ08HJrR-3vY8p07yicPyRUjTRzIftUlXj3sMFxRkRlz5RFYwepQ5KAAAAAVfRjOkA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001988479230")




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
