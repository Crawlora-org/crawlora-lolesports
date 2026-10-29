# Crawlora LoL Esports API client for Ruby (`crawlora-lolesports`)

This Ruby gem calls Crawlora's hosted LoL Esports API at `https://api.crawlora.net/api/v1`. It exposes 13 endpoints covering leagues, schedules, live and completed events, teams, players, and game details; it does not call or scrape LoL Esports directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-lolesports"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/lolesports"

client = Crawlora::Lolesports::Client.new
result = client.request("lolesports-completed-events", JSON.parse("{\"tournament_id\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 13 API operations.

```ruby
client = Crawlora::Lolesports::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported LoL Esports API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-lolesports/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-lolesports) for account setup, the API operation reference, and release history.
