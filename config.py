import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self) -> None:
        # Aapki personal details yahan set hain
        self.API_ID: str = os.environ.get("API_ID", "28906864")
        self.API_HASH: str = os.environ.get("API_HASH", "62cfe849259339c73b6226e4a0599ed5")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "8255597786:AAE0qEuDheFJPiVItN3mPob95kGXodhtgeg")
        self.SESSION: str = os.environ.get("SESSION", "BQG5FXAAC33sudBT0lawN-jr7IKmVU3wtvjaPGv1B32qeEIq8nqPONwADKlcr-ONGFRn92LRDTBMx5sO1ga5yeFpORyhBXJ073unGd8wkCTXHzGeZwfPEiiECZ1wGzVwlwUAFDcyPuKlaMTRUbFVlk8zbSKqLS99AP9ycp0VCPcSr5G81S51_bIDyvL4vzjL_M5MIlQ6A4yrEQvQV3G8Rp6v5XAcJj4VHK2oOuA-7pfOM-podPw2WfvWg3GiAPOCQL23spMbWVHQKEdq_WyU8PEB_bm2f8vScsrgNeNSl2uaPNNqxI7l8YD7eU4ikgTZouGB0RGzFfTXblmBuLPXskSaKZoCtgAAAAHaWwCuAA")
        
        # SUDOERS mein apni Telegram ID yahan likhein (Space dekar)
        # Udaharan: "12345678 87654321"
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "7958364334").split() if id.isnumeric()
        ]

        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)

        # Basic Settings
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "! /").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)

config = Config()
