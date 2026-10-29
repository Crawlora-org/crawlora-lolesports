# LoL Esports clients for Crawlora

Official Crawlora client packages for the hosted LoL Esports API. Access 13 API endpoints covering leagues, schedules, live and completed events, teams, players, and game details from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape LoL Esports locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by LoL Esports or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/lolesports`](javascript/README.md)
- Python: [`crawlora-lolesports`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-lolesports`](go.mod)
- Ruby: [`crawlora-lolesports`](ruby/README.md)
- Java: [`net.crawlora:crawlora-lolesports:0.1.0`](java/README.md)
- PHP: [`crawlora/lolesports`](php/README.md)
- Rust: [`crawlora-lolesports`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 13 selected public LoL Esports API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
