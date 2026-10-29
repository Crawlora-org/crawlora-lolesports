package net.crawlora.lolesports;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the LoL Esports endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 13;
    public static final List<String> OPERATION_IDS = List.of(
            "lolesports-completed-events",
            "lolesports-event",
            "lolesports-game-details",
            "lolesports-game-window",
            "lolesports-gpr",
            "lolesports-leagues",
            "lolesports-live",
            "lolesports-news",
            "lolesports-schedule",
            "lolesports-seasons",
            "lolesports-standings",
            "lolesports-teams",
            "lolesports-tournaments"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("lolesports-completed-events", new Operation("lolesports-completed-events", "GET", "/lolesports/completed-events", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv")), Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("lolesports-event", new Operation("lolesports-event", "GET", "/lolesports/event", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv")), Map.entry("match_id", new Param("match_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("lolesports-game-details", new Operation("lolesports-game-details", "GET", "/lolesports/game-details", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv")), Map.entry("starting_time", new Param("starting_time", "query", false, "string", List.of(), "csv")), Map.entry("participant_ids", new Param("participant_ids", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("lolesports-game-window", new Operation("lolesports-game-window", "GET", "/lolesports/game-window", Map.ofEntries(Map.entry("game_id", new Param("game_id", "query", true, "string", List.of(), "csv")), Map.entry("starting_time", new Param("starting_time", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("lolesports-gpr", new Operation("lolesports-gpr", "GET", "/lolesports/gpr", Map.ofEntries(Map.entry("season", new Param("season", "query", false, "string", List.of("current", "2025", "2024"), "csv")), Map.entry("league", new Param("league", "query", false, "string", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv")), Map.entry("history", new Param("history", "query", false, "boolean", List.of(), "csv"))), List.of("application/json")));
        operations.put("lolesports-leagues", new Operation("lolesports-leagues", "GET", "/lolesports/leagues", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv"))), List.of("application/json")));
        operations.put("lolesports-live", new Operation("lolesports-live", "GET", "/lolesports/live", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv"))), List.of("application/json")));
        operations.put("lolesports-news", new Operation("lolesports-news", "GET", "/lolesports/news", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "el-GR", "en-AU", "en-GB", "en-PH", "en-SG", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "id-ID", "it-IT", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "ro-RO", "ru-RU", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("lolesports-schedule", new Operation("lolesports-schedule", "GET", "/lolesports/schedule", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of(), "csv")), Map.entry("page_token", new Param("page_token", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("lolesports-seasons", new Operation("lolesports-seasons", "GET", "/lolesports/seasons", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv")), Map.entry("season_id", new Param("season_id", "query", false, "string", List.of(), "csv")), Map.entry("region", new Param("region", "query", false, "string", List.of(), "csv")), Map.entry("league_id", new Param("league_id", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("lolesports-standings", new Operation("lolesports-standings", "GET", "/lolesports/standings", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv")), Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv")), Map.entry("rounds", new Param("rounds", "query", false, "boolean", List.of("True", "False"), "csv"))), List.of("application/json")));
        operations.put("lolesports-teams", new Operation("lolesports-teams", "GET", "/lolesports/teams", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv")), Map.entry("slug", new Param("slug", "query", false, "string", List.of(), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv")), Map.entry("status", new Param("status", "query", false, "string", List.of("active", "archived"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("limit", new Param("limit", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("lolesports-tournaments", new Operation("lolesports-tournaments", "GET", "/lolesports/tournaments", Map.ofEntries(Map.entry("hl", new Param("hl", "query", false, "string", List.of("cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"), "csv")), Map.entry("league_id", new Param("league_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown LoL Esports operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object completedEvents(Map<String, ?> params) { return request("lolesports-completed-events", params); }
    public Object event(Map<String, ?> params) { return request("lolesports-event", params); }
    public Object gameDetails(Map<String, ?> params) { return request("lolesports-game-details", params); }
    public Object gameWindow(Map<String, ?> params) { return request("lolesports-game-window", params); }
    public Object gpr(Map<String, ?> params) { return request("lolesports-gpr", params); }
    public Object leagues(Map<String, ?> params) { return request("lolesports-leagues", params); }
    public Object live(Map<String, ?> params) { return request("lolesports-live", params); }
    public Object news(Map<String, ?> params) { return request("lolesports-news", params); }
    public Object schedule(Map<String, ?> params) { return request("lolesports-schedule", params); }
    public Object seasons(Map<String, ?> params) { return request("lolesports-seasons", params); }
    public Object standings(Map<String, ?> params) { return request("lolesports-standings", params); }
    public Object teams(Map<String, ?> params) { return request("lolesports-teams", params); }
    public Object tournaments(Map<String, ?> params) { return request("lolesports-tournaments", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
