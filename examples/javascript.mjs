import { LoLEsportsClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new LoLEsportsClient({ apiKey });

  const schedule = await client.schedule({ hl: "en-US" });
  console.log("schedule", schedule);
  const leagues = await client.leagues({  });
  console.log("leagues", leagues);
