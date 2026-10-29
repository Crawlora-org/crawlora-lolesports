require_relative "lib/crawlora/lolesports/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-lolesports"
  spec.version = Crawlora::Lolesports::VERSION
  spec.summary = "LoL Esports API client for Crawlora (13 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted LoL Esports API. Covers leagues, schedules, live and completed events, teams, players, and game details across 13 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=lolesports-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-lolesports", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-lolesports/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
