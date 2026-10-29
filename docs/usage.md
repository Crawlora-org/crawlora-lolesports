# LoL Esports API endpoint reference and client usage

This reference lists all 13 public LoL Esports API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/lolesports`, `crawlora-lolesports`, and `crawlora-lolesports` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape LoL Esports locally; Crawlora is independent from and not endorsed by LoL Esports or its owners.

The package tracks the public API contract revision `sha256:dfc04699ee510a4e612c84eca40523396769018af312af081351eac0c0e4fa43` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `lolesports`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `completedEvents` | `completed_events` | `lolesports.completed_events` | `GET /lolesports/completed-events` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`), `tournament_id` (query, required) | League of Legends Esports completed matches |
| `event` | `event` | `lolesports.event` | `GET /lolesports/event` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`), `match_id` (query, required) | League of Legends Esports match detail |
| `gameDetails` | `game_details` | `lolesports.game_details` | `GET /lolesports/game-details` | `game_id` (query, required), `starting_time` (query, optional), `participant_ids` (query, optional) | League of Legends Esports player game details |
| `gameWindow` | `game_window` | `lolesports.game_window` | `GET /lolesports/game-window` | `game_id` (query, required), `starting_time` (query, optional) | League of Legends Esports live game window |
| `gpr` | `gpr` | `lolesports.gpr` | `GET /lolesports/gpr` | `season` (query, optional; values: `current`, `2025`, `2024`), `league` (query, optional), `limit` (query, optional), `history` (query, optional) | League of Legends Global Power Rankings |
| `leagues` | `leagues` | `lolesports.leagues` | `GET /lolesports/leagues` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`) | League of Legends Esports leagues |
| `live` | `live` | `lolesports.live` | `GET /lolesports/live` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`) | League of Legends Esports live matches |
| `news` | `news` | `lolesports.news` | `GET /lolesports/news` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `el-GR`, `en-AU`, `en-GB`, `en-PH`, `en-SG`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `id-ID`, `it-IT`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `ro-RO`, `ru-RU`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`), `limit` (query, optional) | League of Legends Esports news |
| `schedule` | `schedule` | `lolesports.schedule` | `GET /lolesports/schedule` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`), `league_id` (query, optional), `page_token` (query, optional) | League of Legends Esports schedule |
| `seasons` | `seasons` | `lolesports.seasons` | `GET /lolesports/seasons` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`), `season_id` (query, optional), `region` (query, optional), `league_id` (query, optional) | League of Legends Esports seasons and splits |
| `standings` | `standings` | `lolesports.standings` | `GET /lolesports/standings` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`), `tournament_id` (query, required), `rounds` (query, optional; values: `True`, `False`) | League of Legends Esports standings |
| `teams` | `teams` | `lolesports.teams` | `GET /lolesports/teams` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`), `slug` (query, optional), `q` (query, optional), `status` (query, optional; values: `active`, `archived`), `page` (query, optional), `limit` (query, optional) | League of Legends Esports teams and rosters |
| `tournaments` | `tournaments` | `lolesports.tournaments` | `GET /lolesports/tournaments` | `hl` (query, optional; values: `cs-CZ`, `de-DE`, `en-US`, `es-ES`, `es-MX`, `fr-FR`, `hu-HU`, `ja-JP`, `ko-KR`, `pl-PL`, `pt-BR`, `th-TH`, `tr-TR`, `vi-VN`, `zh-TW`), `league_id` (query, required) | League of Legends Esports tournaments |

## Client forms

- JavaScript: import `LoLEsportsClient` (also exported as `Client`) from `@crawlora-org/lolesports`; use `new LoLEsportsClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `LoLEsportsClient` (also exported as `Client`) from `crawlora_lolesports`; use `with LoLEsportsClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncLoLEsportsClient`, used with `async with` and `await`.
- Rust: add `crawlora-lolesports` with Cargo; import `Client` and the generated operation parameter struct, then call `client.lolesports.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-lolesports/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
