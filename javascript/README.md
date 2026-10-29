# @crawlora-org/lolesports — LoL Esports API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted LoL Esports API.
It exposes 13 API endpoints for leagues, schedules, live and completed events, teams, players, and game details through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-javascript-homepage). It does not run a browser or scrape LoL Esports locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by LoL Esports or its owners.

## Install

```sh
npm install @crawlora-org/lolesports
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { LoLEsportsClient } from "@crawlora-org/lolesports";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new LoLEsportsClient({ apiKey });
const result1 = await client.schedule({ hl: "en-US" });
console.log(result1);
const result2 = await client.leagues({});
console.log(result2);
```

The client also exports `Client` as an alias for `LoLEsportsClient`. Operation
methods are available directly in camelCase and through the `lolesports`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-lolesports/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-lolesports/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported LoL Esports API endpoints

This package exposes each route below as a direct method and through the `lolesports` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-lolesports/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
