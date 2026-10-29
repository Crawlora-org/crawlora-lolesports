# Crawlora LoL Esports API client for PHP (`crawlora/lolesports`)

This PHP package calls Crawlora's hosted LoL Esports API at `https://api.crawlora.net/api/v1`. It exposes 13 endpoints covering leagues, schedules, live and completed events, teams, players, and game details. It does not call or scrape LoL Esports directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/lolesports
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Lolesports\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("lolesports-completed-events", ['tournament_id' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 13 API operations.

## Supported LoL Esports API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-lolesports/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/lolesports/completed-events` | `lolesports-completed-events` | League of Legends Esports completed matches |
| `GET` | `/lolesports/event` | `lolesports-event` | League of Legends Esports match detail |
| `GET` | `/lolesports/game-details` | `lolesports-game-details` | League of Legends Esports player game details |
| `GET` | `/lolesports/game-window` | `lolesports-game-window` | League of Legends Esports live game window |
| `GET` | `/lolesports/gpr` | `lolesports-gpr` | League of Legends Global Power Rankings |
| `GET` | `/lolesports/leagues` | `lolesports-leagues` | League of Legends Esports leagues |
| `GET` | `/lolesports/live` | `lolesports-live` | League of Legends Esports live matches |
| `GET` | `/lolesports/news` | `lolesports-news` | League of Legends Esports news |
| `GET` | `/lolesports/schedule` | `lolesports-schedule` | League of Legends Esports schedule |
| `GET` | `/lolesports/seasons` | `lolesports-seasons` | League of Legends Esports seasons and splits |
| `GET` | `/lolesports/standings` | `lolesports-standings` | League of Legends Esports standings |
| `GET` | `/lolesports/teams` | `lolesports-teams` | League of Legends Esports teams and rosters |
| `GET` | `/lolesports/tournaments` | `lolesports-tournaments` | League of Legends Esports tournaments |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-lolesports). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-lolesports/blob/main/docs/usage.md).
