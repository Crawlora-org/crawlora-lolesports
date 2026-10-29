from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelLolesportsTournamentsResponse = TypedDict('ModelLolesportsTournamentsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'league_id': NotRequired[str],
    'source_url': NotRequired[str],
    'tournaments': NotRequired[list[ModelLolesportsTournament]],
}, total=False)

ModelLolesportsTournament = TypedDict('ModelLolesportsTournament', {
    'end_date': NotRequired[str],
    'id': NotRequired[str],
    'slug': NotRequired[str],
    'start_date': NotRequired[str],
}, total=False)

ModelLolesportsTeamsResponse = TypedDict('ModelLolesportsTeamsResponse', {
    'fetched_at': NotRequired[str],
    'has_more': NotRequired[bool],
    'limit': NotRequired[int],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelLolesportsTeamDetail]],
    'total': NotRequired[int],
}, total=False)

ModelLolesportsTeamDetail = TypedDict('ModelLolesportsTeamDetail', {
    'code': NotRequired[str],
    'home_league': NotRequired[ModelLolesportsHomeLeague],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'players': NotRequired[list[ModelLolesportsPlayer]],
    'slug': NotRequired[str],
    'status': NotRequired[Literal['active', 'archived']],
}, total=False)

ModelLolesportsPlayer = TypedDict('ModelLolesportsPlayer', {
    'first_name': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'last_name': NotRequired[str],
    'role': NotRequired[Literal['top', 'jungle', 'mid', 'bottom', 'support', 'none']],
    'summoner_name': NotRequired[str],
}, total=False)

ModelLolesportsHomeLeague = TypedDict('ModelLolesportsHomeLeague', {
    'name': NotRequired[str],
    'region': NotRequired[str],
}, total=False)

ModelLolesportsStandingsResponse = TypedDict('ModelLolesportsStandingsResponse', {
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'stages': NotRequired[list[ModelLolesportsStandingStage]],
    'tournament_id': NotRequired[str],
}, total=False)

ModelLolesportsStandingStage = TypedDict('ModelLolesportsStandingStage', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'sections': NotRequired[list[ModelLolesportsStandingSection]],
    'slug': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelLolesportsStandingSection = TypedDict('ModelLolesportsStandingSection', {
    'id': NotRequired[str],
    'matches': NotRequired[list[ModelLolesportsStandingMatch]],
    'name': NotRequired[str],
    'rankings': NotRequired[list[ModelLolesportsRanking]],
    'rounds': NotRequired[list[ModelLolesportsStandingRound]],
    'type': NotRequired[Literal['group', 'bracket']],
}, total=False)

ModelLolesportsStandingRound = TypedDict('ModelLolesportsStandingRound', {
    'match_ids': NotRequired[list[str]],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelLolesportsRanking = TypedDict('ModelLolesportsRanking', {
    'ordinal': NotRequired[int],
    'teams': NotRequired[list[ModelLolesportsTeam]],
}, total=False)

ModelLolesportsTeam = TypedDict('ModelLolesportsTeam', {
    'code': NotRequired[str],
    'game_wins': NotRequired[int],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'outcome': NotRequired[Literal['win', 'loss']],
    'record': NotRequired[ModelLolesportsRecord],
    'slug': NotRequired[str],
}, total=False)

ModelLolesportsRecord = TypedDict('ModelLolesportsRecord', {
    'losses': NotRequired[int],
    'wins': NotRequired[int],
}, total=False)

ModelLolesportsStandingMatch = TypedDict('ModelLolesportsStandingMatch', {
    'flags': NotRequired[list[str]],
    'id': NotRequired[str],
    'previous_match_ids': NotRequired[list[str]],
    'state': NotRequired[str],
    'teams': NotRequired[list[ModelLolesportsTeam]],
}, total=False)

ModelLolesportsSeasonsResponse = TypedDict('ModelLolesportsSeasonsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'league_id': NotRequired[str],
    'region': NotRequired[str],
    'season_id': NotRequired[str],
    'seasons': NotRequired[list[ModelLolesportsSeason]],
    'source_url': NotRequired[str],
}, total=False)

ModelLolesportsSeason = TypedDict('ModelLolesportsSeason', {
    'end_time': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'split_count': NotRequired[int],
    'splits': NotRequired[list[ModelLolesportsSplit]],
    'start_time': NotRequired[str],
}, total=False)

ModelLolesportsSplit = TypedDict('ModelLolesportsSplit', {
    'description': NotRequired[str],
    'end_time': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'region': NotRequired[str],
    'slug': NotRequired[str],
    'start_time': NotRequired[str],
    'tournaments': NotRequired[list[ModelLolesportsSplitTournament]],
}, total=False)

ModelLolesportsSplitTournament = TypedDict('ModelLolesportsSplitTournament', {
    'id': NotRequired[str],
    'league': NotRequired[ModelLolesportsSeasonLeague],
    'name': NotRequired[str],
}, total=False)

ModelLolesportsSeasonLeague = TypedDict('ModelLolesportsSeasonLeague', {
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelLolesportsScheduleResponse = TypedDict('ModelLolesportsScheduleResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelLolesportsEvent]],
    'fetched_at': NotRequired[str],
    'newer_page_token': NotRequired[str],
    'older_page_token': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelLolesportsEvent = TypedDict('ModelLolesportsEvent', {
    'block_name': NotRequired[str],
    'games': NotRequired[list[ModelLolesportsGameVods]],
    'league': NotRequired[ModelLolesportsEventLeague],
    'match': NotRequired[ModelLolesportsMatch],
    'start_time': NotRequired[str],
    'state': NotRequired[Literal['unstarted', 'inProgress', 'completed']],
    'type': NotRequired[str],
}, total=False)

ModelLolesportsMatch = TypedDict('ModelLolesportsMatch', {
    'flags': NotRequired[list[str]],
    'id': NotRequired[str],
    'strategy': NotRequired[ModelLolesportsStrategy],
    'teams': NotRequired[list[ModelLolesportsTeam]],
}, total=False)

ModelLolesportsStrategy = TypedDict('ModelLolesportsStrategy', {
    'count': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelLolesportsEventLeague = TypedDict('ModelLolesportsEventLeague', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelLolesportsGameVods = TypedDict('ModelLolesportsGameVods', {
    'id': NotRequired[str],
    'vods': NotRequired[list[ModelLolesportsVod]],
}, total=False)

ModelLolesportsVod = TypedDict('ModelLolesportsVod', {
    'end_millis': NotRequired[int],
    'first_frame_time': NotRequired[str],
    'id': NotRequired[str],
    'locale': NotRequired[str],
    'locale_name': NotRequired[str],
    'offset': NotRequired[int],
    'parameter': NotRequired[str],
    'provider': NotRequired[str],
    'start_millis': NotRequired[int],
}, total=False)

ModelLolesportsNewsResponse = TypedDict('ModelLolesportsNewsResponse', {
    'articles': NotRequired[list[ModelLolesportsNewsArticle]],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'hl': NotRequired[str],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelLolesportsNewsArticle = TypedDict('ModelLolesportsNewsArticle', {
    'authors': NotRequired[list[str]],
    'description': NotRequired[str],
    'external': NotRequired[bool],
    'external_url': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'path': NotRequired[str],
    'published_at': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelLolesportsLiveResponse = TypedDict('ModelLolesportsLiveResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelLolesportsEvent]],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelLolesportsLeaguesResponse = TypedDict('ModelLolesportsLeaguesResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'leagues': NotRequired[list[ModelLolesportsLeague]],
    'source_url': NotRequired[str],
}, total=False)

ModelLolesportsLeague = TypedDict('ModelLolesportsLeague', {
    'display_status': NotRequired[Literal['force_selected', 'selected', 'not_selected', 'hidden']],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
    'priority': NotRequired[int],
    'region': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelLolesportsGprresponse = TypedDict('ModelLolesportsGprresponse', {
    'count': NotRequired[int],
    'end_date': NotRequired[str],
    'fetched_at': NotRequired[str],
    'leagues': NotRequired[list[ModelLolesportsGprleague]],
    'season': NotRequired[Literal['current', '2025', '2024']],
    'seasons': NotRequired[list[ModelLolesportsGprseasonLink]],
    'source_url': NotRequired[str],
    'start_date': NotRequired[str],
    'teams': NotRequired[list[ModelLolesportsGprteam]],
    'total': NotRequired[int],
}, total=False)

ModelLolesportsGprteam = TypedDict('ModelLolesportsGprteam', {
    'average_opponent_gpr': NotRequired[int],
    'date_calculated': NotRequired[str],
    'elo': NotRequired[int],
    'game_record': NotRequired[ModelLolesportsGprrecord],
    'history': NotRequired[list[ModelLolesportsGprpoint]],
    'match_record': NotRequired[ModelLolesportsGprrecord],
    'previous_rank': NotRequired[int],
    'previous_score': NotRequired[int],
    'rank': NotRequired[int],
    'rank_change': NotRequired[int],
    'score': NotRequired[int],
    'team': NotRequired[ModelLolesportsGprteamRef],
    'tournaments': NotRequired[list[ModelLolesportsGprtournament]],
}, total=False)

ModelLolesportsGprtournament = TypedDict('ModelLolesportsGprtournament', {
    'end_time': NotRequired[str],
    'id': NotRequired[str],
    'league': NotRequired[str],
    'losses': NotRequired[int],
    'name': NotRequired[str],
    'placement': NotRequired[int],
    'region_slug': NotRequired[str],
    'slug': NotRequired[str],
    'start_time': NotRequired[str],
    'state': NotRequired[str],
    'wins': NotRequired[int],
}, total=False)

ModelLolesportsGprteamRef = TypedDict('ModelLolesportsGprteamRef', {
    'code': NotRequired[str],
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'league': NotRequired[str],
    'league_id': NotRequired[str],
    'league_slug': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelLolesportsGprrecord = TypedDict('ModelLolesportsGprrecord', {
    'losses': NotRequired[int],
    'wins': NotRequired[int],
}, total=False)

ModelLolesportsGprpoint = TypedDict('ModelLolesportsGprpoint', {
    'date': NotRequired[str],
    'elo': NotRequired[int],
    'rank': NotRequired[int],
    'score': NotRequired[int],
}, total=False)

ModelLolesportsGprseasonLink = TypedDict('ModelLolesportsGprseasonLink', {
    'kind': NotRequired[Literal['current', 'worlds']],
    'season': NotRequired[str],
    'url': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelLolesportsGprleague = TypedDict('ModelLolesportsGprleague', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'teams': NotRequired[int],
}, total=False)

ModelLolesportsGameWindowResponse = TypedDict('ModelLolesportsGameWindowResponse', {
    'blue': NotRequired[ModelLolesportsTeamMetadata],
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'frames': NotRequired[list[ModelLolesportsWindowFrame]],
    'game_id': NotRequired[str],
    'match_id': NotRequired[str],
    'patch': NotRequired[str],
    'red': NotRequired[ModelLolesportsTeamMetadata],
    'source_url': NotRequired[str],
}, total=False)

ModelLolesportsTeamMetadata = TypedDict('ModelLolesportsTeamMetadata', {
    'participants': NotRequired[list[ModelLolesportsParticipantMetadata]],
    'team_id': NotRequired[str],
}, total=False)

ModelLolesportsParticipantMetadata = TypedDict('ModelLolesportsParticipantMetadata', {
    'champion_id': NotRequired[str],
    'participant_id': NotRequired[int],
    'player_id': NotRequired[str],
    'role': NotRequired[Literal['top', 'jungle', 'mid', 'bottom', 'support']],
    'summoner_name': NotRequired[str],
}, total=False)

ModelLolesportsWindowFrame = TypedDict('ModelLolesportsWindowFrame', {
    'blue': NotRequired[ModelLolesportsTeamTotals],
    'game_state': NotRequired[Literal['in_game', 'paused', 'finished']],
    'red': NotRequired[ModelLolesportsTeamTotals],
    'timestamp': NotRequired[str],
}, total=False)

ModelLolesportsTeamTotals = TypedDict('ModelLolesportsTeamTotals', {
    'barons': NotRequired[int],
    'dragons': NotRequired[list[str]],
    'inhibitors': NotRequired[int],
    'participants': NotRequired[list[ModelLolesportsWindowParticipant]],
    'total_gold': NotRequired[int],
    'total_kills': NotRequired[int],
    'towers': NotRequired[int],
}, total=False)

ModelLolesportsWindowParticipant = TypedDict('ModelLolesportsWindowParticipant', {
    'assists': NotRequired[int],
    'creep_score': NotRequired[int],
    'current_health': NotRequired[int],
    'deaths': NotRequired[int],
    'kills': NotRequired[int],
    'level': NotRequired[int],
    'max_health': NotRequired[int],
    'participant_id': NotRequired[int],
    'total_gold': NotRequired[int],
}, total=False)

ModelLolesportsGameDetailsResponse = TypedDict('ModelLolesportsGameDetailsResponse', {
    'count': NotRequired[int],
    'fetched_at': NotRequired[str],
    'frames': NotRequired[list[ModelLolesportsDetailsFrame]],
    'game_id': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelLolesportsDetailsFrame = TypedDict('ModelLolesportsDetailsFrame', {
    'participants': NotRequired[list[ModelLolesportsDetailsParticipant]],
    'timestamp': NotRequired[str],
}, total=False)

ModelLolesportsDetailsParticipant = TypedDict('ModelLolesportsDetailsParticipant', {
    'ability_power': NotRequired[int],
    'armor': NotRequired[int],
    'assists': NotRequired[int],
    'attack_damage': NotRequired[int],
    'attack_speed': NotRequired[int],
    'champion_damage_share': NotRequired[float],
    'creep_score': NotRequired[int],
    'critical_chance': NotRequired[float],
    'deaths': NotRequired[int],
    'items': NotRequired[list[int]],
    'kill_participation': NotRequired[float],
    'kills': NotRequired[int],
    'level': NotRequired[int],
    'life_steal': NotRequired[int],
    'magic_resistance': NotRequired[int],
    'participant_id': NotRequired[int],
    'rune_ids': NotRequired[list[int]],
    'rune_style_id': NotRequired[int],
    'rune_sub_style_id': NotRequired[int],
    'skill_order': NotRequired[list[str]],
    'tenacity': NotRequired[float],
    'total_gold_earned': NotRequired[int],
    'wards_destroyed': NotRequired[int],
    'wards_placed': NotRequired[int],
}, total=False)

ModelLolesportsEventDetailResponse = TypedDict('ModelLolesportsEventDetailResponse', {
    'fetched_at': NotRequired[str],
    'games': NotRequired[list[ModelLolesportsGame]],
    'id': NotRequired[str],
    'league': NotRequired[ModelLolesportsEventLeague],
    'source_url': NotRequired[str],
    'strategy': NotRequired[ModelLolesportsStrategy],
    'streams': NotRequired[list[ModelLolesportsStream]],
    'teams': NotRequired[list[ModelLolesportsTeam]],
    'tournament_id': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelLolesportsStream = TypedDict('ModelLolesportsStream', {
    'locale': NotRequired[str],
    'parameter': NotRequired[str],
    'provider': NotRequired[str],
}, total=False)

ModelLolesportsGame = TypedDict('ModelLolesportsGame', {
    'id': NotRequired[str],
    'number': NotRequired[int],
    'sides': NotRequired[list[ModelLolesportsGameSide]],
    'state': NotRequired[Literal['unneeded', 'unstarted', 'inProgress', 'completed']],
    'vods': NotRequired[list[ModelLolesportsVod]],
}, total=False)

ModelLolesportsGameSide = TypedDict('ModelLolesportsGameSide', {
    'side': NotRequired[Literal['blue', 'red']],
    'team_id': NotRequired[str],
}, total=False)

ModelLolesportsCompletedEventsResponse = TypedDict('ModelLolesportsCompletedEventsResponse', {
    'count': NotRequired[int],
    'events': NotRequired[list[ModelLolesportsEvent]],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'tournament_id': NotRequired[str],
}, total=False)

LolesportsCompletedEventsResponse = Any
LolesportsCompletedEventsParams = TypedDict('LolesportsCompletedEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'tournament_id': Required[str],
}, total=False)

LolesportsEventResponse = Any
LolesportsEventParams = TypedDict('LolesportsEventParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'match_id': Required[str],
}, total=False)

LolesportsGameDetailsResponse = Any
LolesportsGameDetailsParams = TypedDict('LolesportsGameDetailsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
    'starting_time': NotRequired[str],
    'participant_ids': NotRequired[str],
}, total=False)

LolesportsGameWindowResponse = Any
LolesportsGameWindowParams = TypedDict('LolesportsGameWindowParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'game_id': Required[str],
    'starting_time': NotRequired[str],
}, total=False)

LolesportsGprResponse = Any
LolesportsGprParams = TypedDict('LolesportsGprParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'season': NotRequired[Literal['current', '2025', '2024']],
    'league': NotRequired[str],
    'limit': NotRequired[int],
    'history': NotRequired[bool],
}, total=False)

LolesportsLeaguesResponse = Any
LolesportsLeaguesParams = TypedDict('LolesportsLeaguesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
}, total=False)

LolesportsLiveResponse = Any
LolesportsLiveParams = TypedDict('LolesportsLiveParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
}, total=False)

LolesportsNewsResponse = Any
LolesportsNewsParams = TypedDict('LolesportsNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'el-GR', 'en-AU', 'en-GB', 'en-PH', 'en-SG', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'ro-RO', 'ru-RU', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'limit': NotRequired[int],
}, total=False)

LolesportsScheduleResponse = Any
LolesportsScheduleParams = TypedDict('LolesportsScheduleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'league_id': NotRequired[str],
    'page_token': NotRequired[str],
}, total=False)

LolesportsSeasonsResponse = Any
LolesportsSeasonsParams = TypedDict('LolesportsSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'season_id': NotRequired[str],
    'region': NotRequired[str],
    'league_id': NotRequired[str],
}, total=False)

LolesportsStandingsResponse = Any
LolesportsStandingsParams = TypedDict('LolesportsStandingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'tournament_id': Required[str],
    'rounds': NotRequired[Literal['True', 'False']],
}, total=False)

LolesportsTeamsResponse = Any
LolesportsTeamsParams = TypedDict('LolesportsTeamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'slug': NotRequired[str],
    'q': NotRequired[str],
    'status': NotRequired[Literal['active', 'archived']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

LolesportsTournamentsResponse = Any
LolesportsTournamentsParams = TypedDict('LolesportsTournamentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'league_id': Required[str],
}, total=False)

class LolesportsGroup:
    @overload
    def completed_events(self, **params: Unpack[LolesportsCompletedEventsStreamParams]) -> BinaryIO: ...
    @overload
    def completed_events(self, **params: Unpack[LolesportsCompletedEventsTextResponseParams]) -> str: ...
    @overload
    def completed_events(self, **params: Unpack[LolesportsCompletedEventsDefaultParams]) -> LolesportsCompletedEventsResponse: ...
    @overload
    def event(self, **params: Unpack[LolesportsEventStreamParams]) -> BinaryIO: ...
    @overload
    def event(self, **params: Unpack[LolesportsEventTextResponseParams]) -> str: ...
    @overload
    def event(self, **params: Unpack[LolesportsEventDefaultParams]) -> LolesportsEventResponse: ...
    @overload
    def game_details(self, **params: Unpack[LolesportsGameDetailsStreamParams]) -> BinaryIO: ...
    @overload
    def game_details(self, **params: Unpack[LolesportsGameDetailsTextResponseParams]) -> str: ...
    @overload
    def game_details(self, **params: Unpack[LolesportsGameDetailsDefaultParams]) -> LolesportsGameDetailsResponse: ...
    @overload
    def game_window(self, **params: Unpack[LolesportsGameWindowStreamParams]) -> BinaryIO: ...
    @overload
    def game_window(self, **params: Unpack[LolesportsGameWindowTextResponseParams]) -> str: ...
    @overload
    def game_window(self, **params: Unpack[LolesportsGameWindowDefaultParams]) -> LolesportsGameWindowResponse: ...
    @overload
    def gpr(self, **params: Unpack[LolesportsGprStreamParams]) -> BinaryIO: ...
    @overload
    def gpr(self, **params: Unpack[LolesportsGprTextResponseParams]) -> str: ...
    @overload
    def gpr(self, **params: Unpack[LolesportsGprDefaultParams]) -> LolesportsGprResponse: ...
    @overload
    def leagues(self, **params: Unpack[LolesportsLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    def leagues(self, **params: Unpack[LolesportsLeaguesTextResponseParams]) -> str: ...
    @overload
    def leagues(self, **params: Unpack[LolesportsLeaguesDefaultParams]) -> LolesportsLeaguesResponse: ...
    @overload
    def live(self, **params: Unpack[LolesportsLiveStreamParams]) -> BinaryIO: ...
    @overload
    def live(self, **params: Unpack[LolesportsLiveTextResponseParams]) -> str: ...
    @overload
    def live(self, **params: Unpack[LolesportsLiveDefaultParams]) -> LolesportsLiveResponse: ...
    @overload
    def news(self, **params: Unpack[LolesportsNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[LolesportsNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[LolesportsNewsDefaultParams]) -> LolesportsNewsResponse: ...
    @overload
    def schedule(self, **params: Unpack[LolesportsScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def schedule(self, **params: Unpack[LolesportsScheduleTextResponseParams]) -> str: ...
    @overload
    def schedule(self, **params: Unpack[LolesportsScheduleDefaultParams]) -> LolesportsScheduleResponse: ...
    @overload
    def seasons(self, **params: Unpack[LolesportsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def seasons(self, **params: Unpack[LolesportsSeasonsTextResponseParams]) -> str: ...
    @overload
    def seasons(self, **params: Unpack[LolesportsSeasonsDefaultParams]) -> LolesportsSeasonsResponse: ...
    @overload
    def standings(self, **params: Unpack[LolesportsStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def standings(self, **params: Unpack[LolesportsStandingsTextResponseParams]) -> str: ...
    @overload
    def standings(self, **params: Unpack[LolesportsStandingsDefaultParams]) -> LolesportsStandingsResponse: ...
    @overload
    def teams(self, **params: Unpack[LolesportsTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def teams(self, **params: Unpack[LolesportsTeamsTextResponseParams]) -> str: ...
    @overload
    def teams(self, **params: Unpack[LolesportsTeamsDefaultParams]) -> LolesportsTeamsResponse: ...
    @overload
    def tournaments(self, **params: Unpack[LolesportsTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments(self, **params: Unpack[LolesportsTournamentsTextResponseParams]) -> str: ...
    @overload
    def tournaments(self, **params: Unpack[LolesportsTournamentsDefaultParams]) -> LolesportsTournamentsResponse: ...

OperationId = Literal[
    'lolesports-completed-events',
    'lolesports-event',
    'lolesports-game-details',
    'lolesports-game-window',
    'lolesports-gpr',
    'lolesports-leagues',
    'lolesports-live',
    'lolesports-news',
    'lolesports-schedule',
    'lolesports-seasons',
    'lolesports-standings',
    'lolesports-teams',
    'lolesports-tournaments',
]

class CrawloraClient:
    lolesports: LolesportsGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-completed-events'],
        params: LolesportsCompletedEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsCompletedEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-event'],
        params: LolesportsEventParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsEventResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-game-details'],
        params: LolesportsGameDetailsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsGameDetailsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-game-window'],
        params: LolesportsGameWindowParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsGameWindowResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-gpr'],
        params: LolesportsGprParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsGprResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-leagues'],
        params: LolesportsLeaguesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsLeaguesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-live'],
        params: LolesportsLiveParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsLiveResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-news'],
        params: LolesportsNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-schedule'],
        params: LolesportsScheduleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsScheduleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-seasons'],
        params: LolesportsSeasonsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsSeasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-standings'],
        params: LolesportsStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsStandingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-teams'],
        params: LolesportsTeamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsTeamsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['lolesports-tournaments'],
        params: LolesportsTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsTournamentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-completed-events'],
        params: LolesportsCompletedEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsCompletedEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-event'],
        params: LolesportsEventParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsEventResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-game-details'],
        params: LolesportsGameDetailsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsGameDetailsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-game-window'],
        params: LolesportsGameWindowParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsGameWindowResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-gpr'],
        params: LolesportsGprParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsGprResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-leagues'],
        params: LolesportsLeaguesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsLeaguesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-live'],
        params: LolesportsLiveParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsLiveResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-news'],
        params: LolesportsNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-schedule'],
        params: LolesportsScheduleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsScheduleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-seasons'],
        params: LolesportsSeasonsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsSeasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-standings'],
        params: LolesportsStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsStandingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-teams'],
        params: LolesportsTeamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsTeamsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['lolesports-tournaments'],
        params: LolesportsTournamentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> LolesportsTournamentsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class LoLEsportsClient(CrawloraClient):
    def __enter__(self) -> LoLEsportsClient: ...
    @overload
    def completed_events(self, **params: Unpack[LolesportsCompletedEventsStreamParams]) -> BinaryIO: ...
    @overload
    def completed_events(self, **params: Unpack[LolesportsCompletedEventsTextResponseParams]) -> str: ...
    @overload
    def completed_events(self, **params: Unpack[LolesportsCompletedEventsDefaultParams]) -> LolesportsCompletedEventsResponse: ...
    @overload
    def event(self, **params: Unpack[LolesportsEventStreamParams]) -> BinaryIO: ...
    @overload
    def event(self, **params: Unpack[LolesportsEventTextResponseParams]) -> str: ...
    @overload
    def event(self, **params: Unpack[LolesportsEventDefaultParams]) -> LolesportsEventResponse: ...
    @overload
    def game_details(self, **params: Unpack[LolesportsGameDetailsStreamParams]) -> BinaryIO: ...
    @overload
    def game_details(self, **params: Unpack[LolesportsGameDetailsTextResponseParams]) -> str: ...
    @overload
    def game_details(self, **params: Unpack[LolesportsGameDetailsDefaultParams]) -> LolesportsGameDetailsResponse: ...
    @overload
    def game_window(self, **params: Unpack[LolesportsGameWindowStreamParams]) -> BinaryIO: ...
    @overload
    def game_window(self, **params: Unpack[LolesportsGameWindowTextResponseParams]) -> str: ...
    @overload
    def game_window(self, **params: Unpack[LolesportsGameWindowDefaultParams]) -> LolesportsGameWindowResponse: ...
    @overload
    def gpr(self, **params: Unpack[LolesportsGprStreamParams]) -> BinaryIO: ...
    @overload
    def gpr(self, **params: Unpack[LolesportsGprTextResponseParams]) -> str: ...
    @overload
    def gpr(self, **params: Unpack[LolesportsGprDefaultParams]) -> LolesportsGprResponse: ...
    @overload
    def leagues(self, **params: Unpack[LolesportsLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    def leagues(self, **params: Unpack[LolesportsLeaguesTextResponseParams]) -> str: ...
    @overload
    def leagues(self, **params: Unpack[LolesportsLeaguesDefaultParams]) -> LolesportsLeaguesResponse: ...
    @overload
    def live(self, **params: Unpack[LolesportsLiveStreamParams]) -> BinaryIO: ...
    @overload
    def live(self, **params: Unpack[LolesportsLiveTextResponseParams]) -> str: ...
    @overload
    def live(self, **params: Unpack[LolesportsLiveDefaultParams]) -> LolesportsLiveResponse: ...
    @overload
    def news(self, **params: Unpack[LolesportsNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[LolesportsNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[LolesportsNewsDefaultParams]) -> LolesportsNewsResponse: ...
    @overload
    def schedule(self, **params: Unpack[LolesportsScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def schedule(self, **params: Unpack[LolesportsScheduleTextResponseParams]) -> str: ...
    @overload
    def schedule(self, **params: Unpack[LolesportsScheduleDefaultParams]) -> LolesportsScheduleResponse: ...
    @overload
    def seasons(self, **params: Unpack[LolesportsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def seasons(self, **params: Unpack[LolesportsSeasonsTextResponseParams]) -> str: ...
    @overload
    def seasons(self, **params: Unpack[LolesportsSeasonsDefaultParams]) -> LolesportsSeasonsResponse: ...
    @overload
    def standings(self, **params: Unpack[LolesportsStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def standings(self, **params: Unpack[LolesportsStandingsTextResponseParams]) -> str: ...
    @overload
    def standings(self, **params: Unpack[LolesportsStandingsDefaultParams]) -> LolesportsStandingsResponse: ...
    @overload
    def teams(self, **params: Unpack[LolesportsTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def teams(self, **params: Unpack[LolesportsTeamsTextResponseParams]) -> str: ...
    @overload
    def teams(self, **params: Unpack[LolesportsTeamsDefaultParams]) -> LolesportsTeamsResponse: ...
    @overload
    def tournaments(self, **params: Unpack[LolesportsTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    def tournaments(self, **params: Unpack[LolesportsTournamentsTextResponseParams]) -> str: ...
    @overload
    def tournaments(self, **params: Unpack[LolesportsTournamentsDefaultParams]) -> LolesportsTournamentsResponse: ...

class AsyncLoLEsportsClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncLoLEsportsClient: ...
    lolesports: _AsyncLolesportsGroup
    @overload
    async def completed_events(self, **params: Unpack[LolesportsCompletedEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def completed_events(self, **params: Unpack[LolesportsCompletedEventsTextResponseParams]) -> str: ...
    @overload
    async def completed_events(self, **params: Unpack[LolesportsCompletedEventsDefaultParams]) -> LolesportsCompletedEventsResponse: ...
    @overload
    async def event(self, **params: Unpack[LolesportsEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[LolesportsEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[LolesportsEventDefaultParams]) -> LolesportsEventResponse: ...
    @overload
    async def game_details(self, **params: Unpack[LolesportsGameDetailsStreamParams]) -> BinaryIO: ...
    @overload
    async def game_details(self, **params: Unpack[LolesportsGameDetailsTextResponseParams]) -> str: ...
    @overload
    async def game_details(self, **params: Unpack[LolesportsGameDetailsDefaultParams]) -> LolesportsGameDetailsResponse: ...
    @overload
    async def game_window(self, **params: Unpack[LolesportsGameWindowStreamParams]) -> BinaryIO: ...
    @overload
    async def game_window(self, **params: Unpack[LolesportsGameWindowTextResponseParams]) -> str: ...
    @overload
    async def game_window(self, **params: Unpack[LolesportsGameWindowDefaultParams]) -> LolesportsGameWindowResponse: ...
    @overload
    async def gpr(self, **params: Unpack[LolesportsGprStreamParams]) -> BinaryIO: ...
    @overload
    async def gpr(self, **params: Unpack[LolesportsGprTextResponseParams]) -> str: ...
    @overload
    async def gpr(self, **params: Unpack[LolesportsGprDefaultParams]) -> LolesportsGprResponse: ...
    @overload
    async def leagues(self, **params: Unpack[LolesportsLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[LolesportsLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[LolesportsLeaguesDefaultParams]) -> LolesportsLeaguesResponse: ...
    @overload
    async def live(self, **params: Unpack[LolesportsLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def live(self, **params: Unpack[LolesportsLiveTextResponseParams]) -> str: ...
    @overload
    async def live(self, **params: Unpack[LolesportsLiveDefaultParams]) -> LolesportsLiveResponse: ...
    @overload
    async def news(self, **params: Unpack[LolesportsNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[LolesportsNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[LolesportsNewsDefaultParams]) -> LolesportsNewsResponse: ...
    @overload
    async def schedule(self, **params: Unpack[LolesportsScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def schedule(self, **params: Unpack[LolesportsScheduleTextResponseParams]) -> str: ...
    @overload
    async def schedule(self, **params: Unpack[LolesportsScheduleDefaultParams]) -> LolesportsScheduleResponse: ...
    @overload
    async def seasons(self, **params: Unpack[LolesportsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def seasons(self, **params: Unpack[LolesportsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def seasons(self, **params: Unpack[LolesportsSeasonsDefaultParams]) -> LolesportsSeasonsResponse: ...
    @overload
    async def standings(self, **params: Unpack[LolesportsStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[LolesportsStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[LolesportsStandingsDefaultParams]) -> LolesportsStandingsResponse: ...
    @overload
    async def teams(self, **params: Unpack[LolesportsTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def teams(self, **params: Unpack[LolesportsTeamsTextResponseParams]) -> str: ...
    @overload
    async def teams(self, **params: Unpack[LolesportsTeamsDefaultParams]) -> LolesportsTeamsResponse: ...
    @overload
    async def tournaments(self, **params: Unpack[LolesportsTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments(self, **params: Unpack[LolesportsTournamentsTextResponseParams]) -> str: ...
    @overload
    async def tournaments(self, **params: Unpack[LolesportsTournamentsDefaultParams]) -> LolesportsTournamentsResponse: ...

class _AsyncLolesportsGroup:
    @overload
    async def completed_events(self, **params: Unpack[LolesportsCompletedEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def completed_events(self, **params: Unpack[LolesportsCompletedEventsTextResponseParams]) -> str: ...
    @overload
    async def completed_events(self, **params: Unpack[LolesportsCompletedEventsDefaultParams]) -> LolesportsCompletedEventsResponse: ...
    @overload
    async def event(self, **params: Unpack[LolesportsEventStreamParams]) -> BinaryIO: ...
    @overload
    async def event(self, **params: Unpack[LolesportsEventTextResponseParams]) -> str: ...
    @overload
    async def event(self, **params: Unpack[LolesportsEventDefaultParams]) -> LolesportsEventResponse: ...
    @overload
    async def game_details(self, **params: Unpack[LolesportsGameDetailsStreamParams]) -> BinaryIO: ...
    @overload
    async def game_details(self, **params: Unpack[LolesportsGameDetailsTextResponseParams]) -> str: ...
    @overload
    async def game_details(self, **params: Unpack[LolesportsGameDetailsDefaultParams]) -> LolesportsGameDetailsResponse: ...
    @overload
    async def game_window(self, **params: Unpack[LolesportsGameWindowStreamParams]) -> BinaryIO: ...
    @overload
    async def game_window(self, **params: Unpack[LolesportsGameWindowTextResponseParams]) -> str: ...
    @overload
    async def game_window(self, **params: Unpack[LolesportsGameWindowDefaultParams]) -> LolesportsGameWindowResponse: ...
    @overload
    async def gpr(self, **params: Unpack[LolesportsGprStreamParams]) -> BinaryIO: ...
    @overload
    async def gpr(self, **params: Unpack[LolesportsGprTextResponseParams]) -> str: ...
    @overload
    async def gpr(self, **params: Unpack[LolesportsGprDefaultParams]) -> LolesportsGprResponse: ...
    @overload
    async def leagues(self, **params: Unpack[LolesportsLeaguesStreamParams]) -> BinaryIO: ...
    @overload
    async def leagues(self, **params: Unpack[LolesportsLeaguesTextResponseParams]) -> str: ...
    @overload
    async def leagues(self, **params: Unpack[LolesportsLeaguesDefaultParams]) -> LolesportsLeaguesResponse: ...
    @overload
    async def live(self, **params: Unpack[LolesportsLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def live(self, **params: Unpack[LolesportsLiveTextResponseParams]) -> str: ...
    @overload
    async def live(self, **params: Unpack[LolesportsLiveDefaultParams]) -> LolesportsLiveResponse: ...
    @overload
    async def news(self, **params: Unpack[LolesportsNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[LolesportsNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[LolesportsNewsDefaultParams]) -> LolesportsNewsResponse: ...
    @overload
    async def schedule(self, **params: Unpack[LolesportsScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def schedule(self, **params: Unpack[LolesportsScheduleTextResponseParams]) -> str: ...
    @overload
    async def schedule(self, **params: Unpack[LolesportsScheduleDefaultParams]) -> LolesportsScheduleResponse: ...
    @overload
    async def seasons(self, **params: Unpack[LolesportsSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def seasons(self, **params: Unpack[LolesportsSeasonsTextResponseParams]) -> str: ...
    @overload
    async def seasons(self, **params: Unpack[LolesportsSeasonsDefaultParams]) -> LolesportsSeasonsResponse: ...
    @overload
    async def standings(self, **params: Unpack[LolesportsStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def standings(self, **params: Unpack[LolesportsStandingsTextResponseParams]) -> str: ...
    @overload
    async def standings(self, **params: Unpack[LolesportsStandingsDefaultParams]) -> LolesportsStandingsResponse: ...
    @overload
    async def teams(self, **params: Unpack[LolesportsTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def teams(self, **params: Unpack[LolesportsTeamsTextResponseParams]) -> str: ...
    @overload
    async def teams(self, **params: Unpack[LolesportsTeamsDefaultParams]) -> LolesportsTeamsResponse: ...
    @overload
    async def tournaments(self, **params: Unpack[LolesportsTournamentsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournaments(self, **params: Unpack[LolesportsTournamentsTextResponseParams]) -> str: ...
    @overload
    async def tournaments(self, **params: Unpack[LolesportsTournamentsDefaultParams]) -> LolesportsTournamentsResponse: ...

LolesportsCompletedEventsDefaultParams = TypedDict('LolesportsCompletedEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'tournament_id': Required[str],
}, total=False)

LolesportsCompletedEventsTextResponseParams = TypedDict('LolesportsCompletedEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'tournament_id': Required[str],
}, total=False)

LolesportsCompletedEventsStreamParams = TypedDict('LolesportsCompletedEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'tournament_id': Required[str],
}, total=False)

LolesportsEventDefaultParams = TypedDict('LolesportsEventDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'match_id': Required[str],
}, total=False)

LolesportsEventTextResponseParams = TypedDict('LolesportsEventTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'match_id': Required[str],
}, total=False)

LolesportsEventStreamParams = TypedDict('LolesportsEventStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'match_id': Required[str],
}, total=False)

LolesportsGameDetailsDefaultParams = TypedDict('LolesportsGameDetailsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
    'starting_time': NotRequired[str],
    'participant_ids': NotRequired[str],
}, total=False)

LolesportsGameDetailsTextResponseParams = TypedDict('LolesportsGameDetailsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
    'starting_time': NotRequired[str],
    'participant_ids': NotRequired[str],
}, total=False)

LolesportsGameDetailsStreamParams = TypedDict('LolesportsGameDetailsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
    'starting_time': NotRequired[str],
    'participant_ids': NotRequired[str],
}, total=False)

LolesportsGameWindowDefaultParams = TypedDict('LolesportsGameWindowDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'game_id': Required[str],
    'starting_time': NotRequired[str],
}, total=False)

LolesportsGameWindowTextResponseParams = TypedDict('LolesportsGameWindowTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'game_id': Required[str],
    'starting_time': NotRequired[str],
}, total=False)

LolesportsGameWindowStreamParams = TypedDict('LolesportsGameWindowStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'game_id': Required[str],
    'starting_time': NotRequired[str],
}, total=False)

LolesportsGprDefaultParams = TypedDict('LolesportsGprDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'season': NotRequired[Literal['current', '2025', '2024']],
    'league': NotRequired[str],
    'limit': NotRequired[int],
    'history': NotRequired[bool],
}, total=False)

LolesportsGprTextResponseParams = TypedDict('LolesportsGprTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'season': NotRequired[Literal['current', '2025', '2024']],
    'league': NotRequired[str],
    'limit': NotRequired[int],
    'history': NotRequired[bool],
}, total=False)

LolesportsGprStreamParams = TypedDict('LolesportsGprStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'season': NotRequired[Literal['current', '2025', '2024']],
    'league': NotRequired[str],
    'limit': NotRequired[int],
    'history': NotRequired[bool],
}, total=False)

LolesportsLeaguesDefaultParams = TypedDict('LolesportsLeaguesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
}, total=False)

LolesportsLeaguesTextResponseParams = TypedDict('LolesportsLeaguesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
}, total=False)

LolesportsLeaguesStreamParams = TypedDict('LolesportsLeaguesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
}, total=False)

LolesportsLiveDefaultParams = TypedDict('LolesportsLiveDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
}, total=False)

LolesportsLiveTextResponseParams = TypedDict('LolesportsLiveTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
}, total=False)

LolesportsLiveStreamParams = TypedDict('LolesportsLiveStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
}, total=False)

LolesportsNewsDefaultParams = TypedDict('LolesportsNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'el-GR', 'en-AU', 'en-GB', 'en-PH', 'en-SG', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'ro-RO', 'ru-RU', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'limit': NotRequired[int],
}, total=False)

LolesportsNewsTextResponseParams = TypedDict('LolesportsNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'el-GR', 'en-AU', 'en-GB', 'en-PH', 'en-SG', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'ro-RO', 'ru-RU', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'limit': NotRequired[int],
}, total=False)

LolesportsNewsStreamParams = TypedDict('LolesportsNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'el-GR', 'en-AU', 'en-GB', 'en-PH', 'en-SG', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'id-ID', 'it-IT', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'ro-RO', 'ru-RU', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'limit': NotRequired[int],
}, total=False)

LolesportsScheduleDefaultParams = TypedDict('LolesportsScheduleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'league_id': NotRequired[str],
    'page_token': NotRequired[str],
}, total=False)

LolesportsScheduleTextResponseParams = TypedDict('LolesportsScheduleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'league_id': NotRequired[str],
    'page_token': NotRequired[str],
}, total=False)

LolesportsScheduleStreamParams = TypedDict('LolesportsScheduleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'league_id': NotRequired[str],
    'page_token': NotRequired[str],
}, total=False)

LolesportsSeasonsDefaultParams = TypedDict('LolesportsSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'season_id': NotRequired[str],
    'region': NotRequired[str],
    'league_id': NotRequired[str],
}, total=False)

LolesportsSeasonsTextResponseParams = TypedDict('LolesportsSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'season_id': NotRequired[str],
    'region': NotRequired[str],
    'league_id': NotRequired[str],
}, total=False)

LolesportsSeasonsStreamParams = TypedDict('LolesportsSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'season_id': NotRequired[str],
    'region': NotRequired[str],
    'league_id': NotRequired[str],
}, total=False)

LolesportsStandingsDefaultParams = TypedDict('LolesportsStandingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'tournament_id': Required[str],
    'rounds': NotRequired[Literal['True', 'False']],
}, total=False)

LolesportsStandingsTextResponseParams = TypedDict('LolesportsStandingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'tournament_id': Required[str],
    'rounds': NotRequired[Literal['True', 'False']],
}, total=False)

LolesportsStandingsStreamParams = TypedDict('LolesportsStandingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'tournament_id': Required[str],
    'rounds': NotRequired[Literal['True', 'False']],
}, total=False)

LolesportsTeamsDefaultParams = TypedDict('LolesportsTeamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'slug': NotRequired[str],
    'q': NotRequired[str],
    'status': NotRequired[Literal['active', 'archived']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

LolesportsTeamsTextResponseParams = TypedDict('LolesportsTeamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'slug': NotRequired[str],
    'q': NotRequired[str],
    'status': NotRequired[Literal['active', 'archived']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

LolesportsTeamsStreamParams = TypedDict('LolesportsTeamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'slug': NotRequired[str],
    'q': NotRequired[str],
    'status': NotRequired[Literal['active', 'archived']],
    'page': NotRequired[int],
    'limit': NotRequired[int],
}, total=False)

LolesportsTournamentsDefaultParams = TypedDict('LolesportsTournamentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'league_id': Required[str],
}, total=False)

LolesportsTournamentsTextResponseParams = TypedDict('LolesportsTournamentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'league_id': Required[str],
}, total=False)

LolesportsTournamentsStreamParams = TypedDict('LolesportsTournamentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'hl': NotRequired[Literal['cs-CZ', 'de-DE', 'en-US', 'es-ES', 'es-MX', 'fr-FR', 'hu-HU', 'ja-JP', 'ko-KR', 'pl-PL', 'pt-BR', 'th-TH', 'tr-TR', 'vi-VN', 'zh-TW']],
    'league_id': Required[str],
}, total=False)
