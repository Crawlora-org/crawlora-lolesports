import os

from crawlora_lolesports import LoLEsportsClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with LoLEsportsClient(api_key=api_key) as client:
    schedule = client.schedule(hl='en-US')
    print('schedule', schedule)
    leagues = client.leagues()
    print('leagues', leagues)
