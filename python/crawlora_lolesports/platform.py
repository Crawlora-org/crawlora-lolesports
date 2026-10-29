"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class LoLEsportsClient(CrawloraClient):
    """Synchronous LoL Esports API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-lolesports-python/0.1.0')
        super().__init__(*args, **kwargs)

    def completed_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-completed-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-event', params, response_type=response_type, timeout=timeout, headers=headers)

    def game_details(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-game-details', params, response_type=response_type, timeout=timeout, headers=headers)

    def game_window(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-game-window', params, response_type=response_type, timeout=timeout, headers=headers)

    def gpr(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-gpr', params, response_type=response_type, timeout=timeout, headers=headers)

    def leagues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-leagues', params, response_type=response_type, timeout=timeout, headers=headers)

    def live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-live', params, response_type=response_type, timeout=timeout, headers=headers)

    def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    def seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    def teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-teams', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('lolesports-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncLoLEsportsClient(AsyncCrawloraClient):
    """Asynchronous LoL Esports API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-lolesports-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def completed_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-completed-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def event(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-event', params, response_type=response_type, timeout=timeout, headers=headers)

    async def game_details(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-game-details', params, response_type=response_type, timeout=timeout, headers=headers)

    async def game_window(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-game-window', params, response_type=response_type, timeout=timeout, headers=headers)

    async def gpr(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-gpr', params, response_type=response_type, timeout=timeout, headers=headers)

    async def leagues(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-leagues', params, response_type=response_type, timeout=timeout, headers=headers)

    async def live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-live', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    async def seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-teams', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournaments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('lolesports-tournaments', params, response_type=response_type, timeout=timeout, headers=headers)
