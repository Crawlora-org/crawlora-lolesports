"""Typed LoL Esports client for the Crawlora hosted API."""

from .platform import LoLEsportsClient, AsyncLoLEsportsClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = LoLEsportsClient
AsyncClient = AsyncLoLEsportsClient
__version__ = '0.1.0'
DISPLAY_NAME = 'LoL Esports'
PLATFORM = 'lolesports'
CONTRACT_REVISION = 'sha256:dfc04699ee510a4e612c84eca40523396769018af312af081351eac0c0e4fa43'

__all__ = [
    "LoLEsportsClient", "AsyncLoLEsportsClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
