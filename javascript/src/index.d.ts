import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class LoLEsportsClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  completedEvents(params: OperationParamsMap["lolesports-completed-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  event(params: OperationParamsMap["lolesports-event"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  gameDetails(params: OperationParamsMap["lolesports-game-details"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  gameWindow(params: OperationParamsMap["lolesports-game-window"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  gpr(params?: OperationParamsMap["lolesports-gpr"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  leagues(params?: OperationParamsMap["lolesports-leagues"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  live(params?: OperationParamsMap["lolesports-live"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  news(params?: OperationParamsMap["lolesports-news"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  schedule(params?: OperationParamsMap["lolesports-schedule"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  seasons(params?: OperationParamsMap["lolesports-seasons"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  standings(params: OperationParamsMap["lolesports-standings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teams(params?: OperationParamsMap["lolesports-teams"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournaments(params: OperationParamsMap["lolesports-tournaments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  completedEvents(params: OperationParamsMap["lolesports-completed-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  event(params: OperationParamsMap["lolesports-event"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  gameDetails(params: OperationParamsMap["lolesports-game-details"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  gameWindow(params: OperationParamsMap["lolesports-game-window"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  gpr(params?: OperationParamsMap["lolesports-gpr"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  leagues(params?: OperationParamsMap["lolesports-leagues"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  live(params?: OperationParamsMap["lolesports-live"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  news(params?: OperationParamsMap["lolesports-news"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  schedule(params?: OperationParamsMap["lolesports-schedule"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  seasons(params?: OperationParamsMap["lolesports-seasons"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  standings(params: OperationParamsMap["lolesports-standings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teams(params?: OperationParamsMap["lolesports-teams"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournaments(params: OperationParamsMap["lolesports-tournaments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  completedEvents(...args: OperationRequestArgs<"lolesports-completed-events">): Promise<OperationResponseMap["lolesports-completed-events"]>;
  event(...args: OperationRequestArgs<"lolesports-event">): Promise<OperationResponseMap["lolesports-event"]>;
  gameDetails(...args: OperationRequestArgs<"lolesports-game-details">): Promise<OperationResponseMap["lolesports-game-details"]>;
  gameWindow(...args: OperationRequestArgs<"lolesports-game-window">): Promise<OperationResponseMap["lolesports-game-window"]>;
  gpr(...args: OperationRequestArgs<"lolesports-gpr">): Promise<OperationResponseMap["lolesports-gpr"]>;
  leagues(...args: OperationRequestArgs<"lolesports-leagues">): Promise<OperationResponseMap["lolesports-leagues"]>;
  live(...args: OperationRequestArgs<"lolesports-live">): Promise<OperationResponseMap["lolesports-live"]>;
  news(...args: OperationRequestArgs<"lolesports-news">): Promise<OperationResponseMap["lolesports-news"]>;
  schedule(...args: OperationRequestArgs<"lolesports-schedule">): Promise<OperationResponseMap["lolesports-schedule"]>;
  seasons(...args: OperationRequestArgs<"lolesports-seasons">): Promise<OperationResponseMap["lolesports-seasons"]>;
  standings(...args: OperationRequestArgs<"lolesports-standings">): Promise<OperationResponseMap["lolesports-standings"]>;
  teams(...args: OperationRequestArgs<"lolesports-teams">): Promise<OperationResponseMap["lolesports-teams"]>;
  tournaments(...args: OperationRequestArgs<"lolesports-tournaments">): Promise<OperationResponseMap["lolesports-tournaments"]>;
}
export { LoLEsportsClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default LoLEsportsClient;
