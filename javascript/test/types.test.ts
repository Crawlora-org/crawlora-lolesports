import { LoLEsportsClient } from "../src/index.js";

const client = new LoLEsportsClient({ apiKey: "test-key" });
void client.completedEvents({"tournament_id": "sample"});
void client.request("lolesports-completed-events", {"tournament_id": "sample"});
const streamResponse: Promise<Response> = client.request("lolesports-completed-events", {"tournament_id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("lolesports-completed-events", {"tournament_id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.completedEvents({"tournament_id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("lolesports-completed-events", {"hl": "cs-CZ", "tournament_id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("lolesports-completed-events", {"tournament_id": "sample"}, { responseType: "text" });
void rawText;


void client.gpr();
void client.request("lolesports-gpr");
// @ts-expect-error The selected operation requires its documented params.
void client.completedEvents();
