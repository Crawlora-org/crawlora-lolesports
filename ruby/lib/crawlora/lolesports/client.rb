require "json"
require "net/http"
require "uri"

module Crawlora
  module Lolesports
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"lolesports-completed-events": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-completed-events", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric tournament id from lolesports-tournaments", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "115548681802226458"}], "path": "/lolesports/completed-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-event": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-event", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric match id from lolesports-schedule, lolesports-live or lolesports-standings", "in": "query", "name": "match_id", "required": true, "type": "string", "x-example": "117133816701918802"}], "path": "/lolesports/event", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "match_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-game-details": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-game-details", "method": "GET", "params": [{"description": "Numeric game id from lolesports-event", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "117133816701918803"}, {"description": "RFC 3339 UTC timestamp whose seconds are divisible by 10; frames begin there", "in": "query", "name": "starting_time", "type": "string", "x-example": "2026-10-07T11:30:00.000Z"}, {"description": "Participant numbers 1 to 10 joined by underscores, for example 1_2_3", "in": "query", "name": "participant_ids", "type": "string", "x-example": "1_2"}], "path": "/lolesports/game-details", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"in": "query", "name": "starting_time", "type": "string"}, {"in": "query", "name": "participant_ids", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-game-window": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-game-window", "method": "GET", "params": [{"description": "Numeric game id from lolesports-event", "in": "query", "name": "game_id", "required": true, "type": "string", "x-example": "117133816701918803"}, {"description": "RFC 3339 UTC timestamp whose seconds are divisible by 10; frames begin there", "in": "query", "name": "starting_time", "type": "string", "x-example": "2026-10-07T10:20:00.000Z"}], "path": "/lolesports/game-window", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "game_id", "required": true, "type": "string"}, {"in": "query", "name": "starting_time", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-gpr": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-gpr", "method": "GET", "params": [{"description": "Ranking snapshot; one of current, 2025, 2024; defaults to current", "enum": ["current", "2025", "2024"], "in": "query", "name": "season", "type": "string"}, {"description": "Home league slug from the leagues list of the response, for example lck", "in": "query", "name": "league", "type": "string"}, {"description": "Number of teams to return, 1 to 200, best rank first; defaults to all", "in": "query", "maximum": 200, "minimum": 1, "name": "limit", "type": "integer"}, {"description": "Add each team's GPR history points", "in": "query", "name": "history", "type": "boolean"}], "path": "/lolesports/gpr", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["current", "2025", "2024"], "in": "query", "name": "season", "type": "string"}, {"in": "query", "name": "league", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "history", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "lolesports-leagues": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-leagues", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}], "path": "/lolesports/leagues", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-live": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-live", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}], "path": "/lolesports/live", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-news": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-news", "method": "GET", "params": [{"description": "Site language; one of cs-CZ, de-DE, el-GR, en-AU, en-GB, en-PH, en-SG, en-US, es-ES, es-MX, fr-FR, hu-HU, id-ID, it-IT, ja-JP, ko-KR, pl-PL, pt-BR, ro-RO, ru-RU, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "el-GR", "en-AU", "en-GB", "en-PH", "en-SG", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "id-ID", "it-IT", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "ro-RO", "ru-RU", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Number of newest articles to return, 1 to 100; defaults to all the page lists", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/lolesports/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "el-GR", "en-AU", "en-GB", "en-PH", "en-SG", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "id-ID", "it-IT", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "ro-RO", "ru-RU", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "lolesports-schedule": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-schedule", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric league id from lolesports-leagues, or up to 10 comma-separated ids to combine leagues; omit for all leagues", "in": "query", "name": "league_id", "type": "string", "x-example": "98767991302996019"}, {"description": "older_page_token or newer_page_token copied from a previous response", "in": "query", "name": "page_token", "type": "string"}], "path": "/lolesports/schedule", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "league_id", "type": "string"}, {"in": "query", "name": "page_token", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-seasons": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-seasons", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric season id from an earlier lolesports-seasons response; omit for every season", "in": "query", "name": "season_id", "type": "string", "x-example": "115547545029543948"}, {"description": "Split region, case-insensitive; one of AMERICAS, BRAZIL, CHINA, COMMONWEALTH OF INDEPENDENT STATES, EMEA, EUROPE, GLOBAL, HONG KONG, MACAU, TAIWAN, INTERNATIONAL, JAPAN, KOREA, LATIN AMERICA, LATIN AMERICA NORTH, LATIN AMERICA SOUTH, NORTH AMERICA, OCEANIA, REGIONAL, SOUTHEAST ASIA, TURKEY, VIETNAM", "in": "query", "name": "region", "type": "string", "x-example": "KOREA"}, {"description": "Numeric league id from lolesports-leagues; keeps only that league's tournaments", "in": "query", "name": "league_id", "type": "string", "x-example": "98767991302996019"}], "path": "/lolesports/seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "season_id", "type": "string"}, {"in": "query", "name": "region", "type": "string"}, {"in": "query", "name": "league_id", "type": "string"}], "security": ["ApiKeyAuth"]}, "lolesports-standings": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-standings", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric tournament id from lolesports-tournaments", "in": "query", "name": "tournament_id", "required": true, "type": "string", "x-example": "115548681802226458"}, {"description": "true adds each section's id and type (group or bracket) and bracket round names with their match ids; costs a second upstream call; false or omitted keeps the default response", "enum": [true, false], "in": "query", "name": "rounds", "type": "boolean"}], "path": "/lolesports/standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "tournament_id", "required": true, "type": "string"}, {"enum": ["True", "False"], "in": "query", "name": "rounds", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "lolesports-teams": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-teams", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Exact team slug such as t1 or g2-esports; takes precedence over q", "in": "query", "name": "slug", "type": "string", "x-example": "t1"}, {"description": "Case-insensitive substring of team name, code or slug", "in": "query", "name": "q", "type": "string"}, {"description": "Team status filter: active or archived", "enum": ["active", "archived"], "in": "query", "name": "status", "type": "string"}, {"description": "1-based page number; defaults to 1", "in": "query", "minimum": 1, "name": "page", "type": "integer"}, {"description": "Page size 1 to 100; defaults to 25", "in": "query", "maximum": 100, "minimum": 1, "name": "limit", "type": "integer"}], "path": "/lolesports/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "slug", "type": "string"}, {"in": "query", "name": "q", "type": "string"}, {"enum": ["active", "archived"], "in": "query", "name": "status", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "lolesports-tournaments": {"bodyParam": null, "bodyRequired": false, "id": "lolesports-tournaments", "method": "GET", "params": [{"description": "Language for names and labels; one of cs-CZ, de-DE, en-US, es-ES, es-MX, fr-FR, hu-HU, ja-JP, ko-KR, pl-PL, pt-BR, th-TH, tr-TR, vi-VN, zh-TW; defaults to en-US", "enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"description": "Numeric league id from lolesports-leagues", "in": "query", "name": "league_id", "required": true, "type": "string", "x-example": "98767991302996019"}], "path": "/lolesports/tournaments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["cs-CZ", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "hu-HU", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "th-TH", "tr-TR", "vi-VN", "zh-TW"], "in": "query", "name": "hl", "type": "string"}, {"in": "query", "name": "league_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["lolesports-completed-events", "lolesports-event", "lolesports-game-details", "lolesports-game-window", "lolesports-gpr", "lolesports-leagues", "lolesports-live", "lolesports-news", "lolesports-schedule", "lolesports-seasons", "lolesports-standings", "lolesports-teams", "lolesports-tournaments"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-lolesports-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('completed_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-completed-events', params, response_type: response_type)
      end
      define_method('event') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-event', params, response_type: response_type)
      end
      define_method('game_details') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-game-details', params, response_type: response_type)
      end
      define_method('game_window') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-game-window', params, response_type: response_type)
      end
      define_method('gpr') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-gpr', params, response_type: response_type)
      end
      define_method('leagues') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-leagues', params, response_type: response_type)
      end
      define_method('live') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-live', params, response_type: response_type)
      end
      define_method('news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-news', params, response_type: response_type)
      end
      define_method('schedule') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-schedule', params, response_type: response_type)
      end
      define_method('seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-seasons', params, response_type: response_type)
      end
      define_method('standings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-standings', params, response_type: response_type)
      end
      define_method('teams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-teams', params, response_type: response_type)
      end
      define_method('tournaments') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('lolesports-tournaments', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
