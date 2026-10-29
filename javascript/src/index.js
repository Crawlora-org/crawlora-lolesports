import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class LoLEsportsClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-lolesports-js/0.1.0" });
    this["completedEvents"] = (...args) => this.request("lolesports-completed-events", ...args);
    this["event"] = (...args) => this.request("lolesports-event", ...args);
    this["gameDetails"] = (...args) => this.request("lolesports-game-details", ...args);
    this["gameWindow"] = (...args) => this.request("lolesports-game-window", ...args);
    this["gpr"] = (...args) => this.request("lolesports-gpr", ...args);
    this["leagues"] = (...args) => this.request("lolesports-leagues", ...args);
    this["live"] = (...args) => this.request("lolesports-live", ...args);
    this["news"] = (...args) => this.request("lolesports-news", ...args);
    this["schedule"] = (...args) => this.request("lolesports-schedule", ...args);
    this["seasons"] = (...args) => this.request("lolesports-seasons", ...args);
    this["standings"] = (...args) => this.request("lolesports-standings", ...args);
    this["teams"] = (...args) => this.request("lolesports-teams", ...args);
    this["tournaments"] = (...args) => this.request("lolesports-tournaments", ...args);
  }
}

export { LoLEsportsClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default LoLEsportsClient;
