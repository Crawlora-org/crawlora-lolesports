# Crawlora LoL Esports API client for Java

The official Java client for Crawlora's hosted LoL Esports API. It exposes 13 endpoints covering leagues, schedules, live and completed events, teams, players, and game details. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-lolesports</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-java-console) to get an API key.

```java
import net.crawlora.lolesports.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.leagues(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported LoL Esports API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-lolesports/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-lolesports)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-java-api-docs)
