<?php

declare(strict_types=1);

namespace Crawlora\Lolesports;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'lolesports';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 13;
    public const OPERATION_IDS = ["lolesports-completed-events", "lolesports-event", "lolesports-game-details", "lolesports-game-window", "lolesports-gpr", "lolesports-leagues", "lolesports-live", "lolesports-news", "lolesports-schedule", "lolesports-seasons", "lolesports-standings", "lolesports-teams", "lolesports-tournaments"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"lolesports-completed-events": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-completed-events", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric tournament id from lolesports-tournaments", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "115548681802226458"}], "path": "/lolesports/completed-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-event": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-event", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric match id from lolesports-schedule, lolesports-live or lolesports-standings", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "117133816701918802"}], "path": "/lolesports/event", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "match_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-game-details": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-game-details", "method": "GET", "params": [{"description": "Numeric game id from lolesports-event", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "117133816701918803"}, {"description": "RFC 3339 UTC timestamp whose seconds are divisible by 10; frames begin there", "in": "query", "name": "starting_time", "type": "string", "x-example": "2026-10-07T11:30:00.000Z"}, {"description": "Participant numbers 1 to 10 joined by underscores, for example 1_2_3", "in": "query", "name": "participant_ids", "type": "string", "x-example": "1_2"}], "path": "/lolesports/game-details", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"in": "query", "name": "starting_time", "type": "string"}, {"in": "query", "name": "participant_ids", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-game-window": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-game-window", "method": "GET", "params": [{"description": "Numeric game id from lolesports-event", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "117133816701918803"}, {"description": "RFC 3339 UTC timestamp whose seconds are divisible by 10; frames begin there", "in": "query", "name": "starting_time", "type": "string", "x-example": "2026-10-07T10:20:00.000Z"}], "path": "/lolesports/game-window", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"in": "query", "name": "starting_time", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-gpr": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-gpr", "method": "GET", "params": [{"description": "Ranking snapshot; one of current, 2025, 2024; defaults to current", "enum": ["current", "2025", "2024"], "in": "query", "name": "season", "type": "string"}, {"description": "Home league slug from the leagues list of the response, for example lck", "in": "query", "name": "league", "type": "string"}, {"description": "Number of teams to return, 1 to 200, best rank first; defaults to all", "in": "query", "maximum": 200, "minimum": 1, "name": "limit", "type": "integer"}, {"description": "Add each team's GPR history points", "in": "query", "name": "history", "type": "boolean"}], "path": "/lolesports/gpr", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["current", "2025", "2024"], "in": "query", "name": "season", "type": "string"}, {"in": "query", "name": "league", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "history", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "lolesports-leagues": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-leagues", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}], "path": "/lolesports/leagues", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-live": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-live", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}], "path": "/lolesports/live", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-news": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-news", "method": "GET", "params": [{"description": "Site language; one of cs-CZ, de-DE, el-GR, en-AU, en-GB, en-PH, en-SG, en-US, es-ES, es-MX, fr-FR, hu-HU, id-ID, it-IT, ja-JP, ko-KR, pl-PL, pt-BR, ro-RO, ru-RU, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "el-GR", "en-AU", "en-GB", "en-PH", "en-SG", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "id-ID", "it-IT", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "ro-RO", "ru-RU", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Number of newest articles to return, 1 to 100; defaults to all the page lists", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/lolesports/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "el-GR", "en-AU", "en-GB", "en-PH", "en-SG", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "id-ID", "it-IT", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "ro-RO", "ru-RU", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "lolesports-schedule": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-schedule", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric league id from lolesports-leagues, or up to 10 comma-separated ids to combine leagues; omit for all leagues", "in": "query", "name": "league_id", "type": "string", "x-example": "98767991302996019"}, {"description": "older_page_token or newer_page_token copied from a previous response", "in": "query", "name": "page_token", "type": "string"}], "path": "/lolesports/schedule", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "page_token", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-seasons": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-seasons", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric season id from an earlier lolesports-seasons response; omit for every season", "in": "query", "name": "season_id", "type": "string", "x-example": "115547545029543948"}, {"description": "Split region, case-insensitive; one of AMERICAS, BRAZIL, CHINA, COMMONWEALTH OF INDEPENDENT STATES, EMEA, EUROPE, GLOBAL, HONG KONG, MACAU, TAIWAN, INTERNATIONAL, JAPAN, KOREA, LATIN AMERICA, LATIN AMERICA NORTH, LATIN AMERICA SOUTH, NORTH AMERICA, OCEANIA, REGIONAL, SOUTHEAST ASIA, TURKEY, VIETNAM", "in": "query", "name": "region", "type": "string", "x-example": "KOREA"}, {"description": "Numeric league id from lolesports-leagues; keeps only that league's tournaments", "in": "query", "name": "league_id", "type": "string", "x-example": "98767991302996019"}], "path": "/lolesports/seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "season_id", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "league_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-standings": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-standings", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric tournament id from lolesports-tournaments", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "115548681802226458"}, {"description": "true adds each section's id and type (group or bracket) and bracket round names with their match ids; costs a second upstream call; false or omitted keeps the default response", "enum": [true, false], "in": "query", "name": "rounds", "type": "boolean"}], "path": "/lolesports/standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"enum": ["True", "False"], "in": "query", "name": "rounds", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "lolesports-teams": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-teams", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Exact team slug such as t1 or g2-esports; takes precedence over q", "in": "query", "name": "slug", "type": "string", "x-example": "t1"}, {"description": "Case-insensitive substring of team name, code or slug", "in": "query", "name": "q", "type": "string"}, {"description": "Team status filter: active or archived", "enum": ["active", "archived"], "in": "query", "name": "status", "type": "string"}, {"description": "1-based page number; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size 1 to 100; defaults to 25", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/lolesports/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "slug", "type": "string"}, {"in": "query", "name": "q", "type": "string"}, {"enum": ["active", "archived"], "in": "query", "name": "status", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "lolesports-tournaments": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-tournaments", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric league id from lolesports-leagues", "in": "query", "name": "league_id", "required": true, "type": "string", "x-example": "98767991302996019"}], "path": "/lolesports/tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "league_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-lolesports-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function completed_events(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-completed-events", $params, $responseType);
    }
    public function event(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-event", $params, $responseType);
    }
    public function game_details(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-game-details", $params, $responseType);
    }
    public function game_window(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-game-window", $params, $responseType);
    }
    public function gpr(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-gpr", $params, $responseType);
    }
    public function leagues(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-leagues", $params, $responseType);
    }
    public function live(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-live", $params, $responseType);
    }
    public function news(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-news", $params, $responseType);
    }
    public function schedule(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-schedule", $params, $responseType);
    }
    public function seasons(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-seasons", $params, $responseType);
    }
    public function standings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-standings", $params, $responseType);
    }
    public function teams(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-teams", $params, $responseType);
    }
    public function tournaments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("lolesports-tournaments", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
