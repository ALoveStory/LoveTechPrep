# sessions.py
# 8-week, multi-slot agenda aligned to HelloInterview sections + Alex Xu readings.
# Each day is ~3:00–5:30 PM America/Chicago (your generator sets start time).

weeks = [
    # -----------------------------------------
    # Week 1 — Bit.ly, Dropbox, Rate Limiter
    # -----------------------------------------
    [
        {
            "day": "Day 1 – Bit.ly (URL Shortener)",
            "slots": [
                ("In a Hurry: Delivery Framework checklist", 15),
                ("Question Breakdown: Bit.ly v1 full design", 50),
                ("Break", 15),
                ("Core Concepts: Unique ID generation, cache-aside", 30),
                ("Key Tech: DB vs KV store, cache placement", 25),
                ("Refactor: Bit.ly v2 (sharding, failure modes)", 15),
                ("Reading: Vol 1 Ch.7 (Unique ID) + Ch.8 (URL Shortener)", 20),
            ],
        },
        {
            "day": "Day 2 – Bit.ly Refactor + Consistency",
            "slots": [
                ("Review yesterday’s gaps", 10),
                ("Question Breakdown: Bit.ly v3 (QPS math, hot-key mitigation)", 45),
                ("Break", 15),
                ("Core Concepts: Consistent hashing & caching strategies", 30),
                ("Key Tech: Cache invalidation, distributed counters", 30),
                ("Artifacts: Trade-off table + diagram cleanup", 20),
                ("Reading: Vol 1 Ch.4 (Rate Limiter)", 20),
            ],
        },
        {
            "day": "Day 3 – Dropbox (File Storage & Sync)",
            "slots": [
                ("Question Breakdown: Dropbox v1 design", 50),
                ("Break", 15),
                ("Core Concepts: Chunking, deduplication, replication", 30),
                ("Key Tech: Object storage, metadata partitioning", 35),
                ("Refactor: Dropbox v2 (multi-region sync, conflict resolution)", 10),
                ("Reading: Vol 1 Ch.15 (Google Drive)", 20),
            ],
        },
        {
            "day": "Day 4 – Dropbox Refactor + CAP & Networking",
            "slots": [
                ("Review risks from v2", 10),
                ("Question Breakdown: Dropbox v3 (consistency, retries, idempotency)", 45),
                ("Break", 15),
                ("Core Concepts: CAP theorem, partitioning, request flows", 30),
                ("Key Tech: DB consistency models, failure handling", 40),
                ("Exercise: Failure drill (region outage, latency spike)", 10),
                ("Reading: Vol 1 Ch.6 (Key-Value Store)", 20),
            ],
        },
        {
            "day": "Day 5 – Rate Limiter (Protection & Fairness)",
            "slots": [
                ("Question Breakdown: Rate Limiter v1", 45),
                ("Break", 15),
                ("Core Concepts: Token bucket, leaky bucket, sliding window", 30),
                ("Key Tech: API gateway placement, distributed enforcement", 40),
                ("Refactor: Rate Limiter v2 (multi-DC, hot-user handling)", 10),
                ("Reading: Vol 1 Ch.4 (Rate Limiter)", 20),
            ],
        },
        {
            "day": "Day 6 – Cross-Design Trade-Offs & Speed Round",
            "slots": [
                ("Workshop: Trade-off matrix (Bit.ly, Dropbox, Rate Limiter)", 20),
                ("Speed redo: one design in 30–35 min", 45),
                ("Break", 15),
                ("Core Concepts: Compare sharding, replication, consistency models", 45),
                ("Key Tech: Cache vs storage trade-offs", 25),
                ("Reading Review: Vol 1 Ch.7, Ch.15, Ch.4 (compare approaches)", 20),
            ],
        },
        {
            "day": "Day 7 – Mock Interview (Bit.ly/Dropbox/Rate Limiter)",
            "slots": [
                ("Simulation: Full mock (clarify → HLD → trade-offs)", 50),
                ("Break", 15),
                ("Self-Critique: Identify gaps in numbers, trade-offs, clarity", 45),
                ("Patch Plan: Prep adjustments for Week 2", 30),
                ("Optional Reading: Vol 1 Ch.1–3 (Framework + Estimation)", 30),
            ],
        },
    ],

    # ----------------------------------------------------
    # Week 2 — Social & Real-Time (News Feed, WhatsApp, Ticketmaster)
    # ----------------------------------------------------
    [
        {
            "day": "Day 8 – FB News Feed (v1)",
            "slots": [
                ("Question Breakdown: News Feed v1 (personalization, freshness, ranking)", 50),
                ("Break", 15),
                ("Patterns: Fan-out vs fan-in", 30),
                ("Core Concepts: Cache invalidation, request flows", 25),
                ("Refactor: News Feed v2 (trade-off table)", 10),
                ("Reading: Vol 1 Ch.11 (News Feed System)", 20),
            ],
        },
        {
            "day": "Day 9 – FB News Feed Refactor",
            "slots": [
                ("Question Breakdown: News Feed v3 (push vs pull, freshness)", 45),
                ("Break", 15),
                ("Core Concepts: Scale estimation for feeds", 30),
                ("Patterns: Scaling reads vs writes", 30),
                ("Artifacts: Updated trade-off table", 20),
                ("Reading: Vol 1 Ch.2 (Back-of-the-Envelope Estimation)", 20),
            ],
        },
        {
            "day": "Day 10 – WhatsApp (v1)",
            "slots": [
                ("Question Breakdown: WhatsApp v1 (1:1, groups, presence)", 50),
                ("Break", 15),
                ("Core Concepts: Durability vs latency in messaging", 30),
                ("Key Tech: Redis pub/sub, Kafka queues", 25),
                ("Refactor: WhatsApp v2 (broker + delivery guarantees)", 10),
                ("Reading: Vol 1 Ch.12 (Chat System)", 20),
            ],
        },
        {
            "day": "Day 11 – WhatsApp Refactor + Real-Time",
            "slots": [
                ("Question Breakdown: WhatsApp v3 (WebSockets/long polling)", 45),
                ("Break", 15),
                ("Patterns: Managing long-running connections (real-time updates)", 30),
                ("Core Concepts: Consistency trade-offs across devices", 30),
                ("Key Tech: Handling millions of concurrent connections", 20),
                ("Reading: Vol 2 Ch.9 (S3-like Object Storage) – media handling", 20),
            ],
        },
        {
            "day": "Day 12 – Ticketmaster (High-Concurrency v1)",
            "slots": [
                ("Question Breakdown: Ticketmaster v1 (ticket sales, high load)", 50),
                ("Break", 15),
                ("Patterns: Dealing with contention, fairness", 30),
                ("Key Tech: Distributed locks, queueing (hot-spot control)", 25),
                ("Refactor: Ticketmaster v2 (hot-spot handling)", 10),
                ("Reading: Vol 2 Ch.7 (Hotel Reservation) + Optional Ch.10 (Leaderboard)", 20),
            ],
        },
        {
            "day": "Day 13 – Trade-Off Workshop (Social Systems)",
            "slots": [
                ("Workshop: Compare News Feed, WhatsApp, Ticketmaster", 30),
                ("Core Concepts: Latency vs throughput, consistency guarantees", 30),
                ("Break", 15),
                ("Key Tech: Cost vs scalability analysis", 30),
                ("Artifacts: Trade-off matrix build", 30),
                ("Reading: Vol 1 Ch.6 (Key-Value Store)", 15),
            ],
        },
        {
            "day": "Day 14 – Mock Interview (Social Systems)",
            "slots": [
                ("Simulation: Full interview on one system", 50),
                ("Break", 15),
                ("Self-Critique: Scaling, trade-offs, clarity", 45),
                ("Patch Plan: Prep for Week 3", 30),
                ("Optional Reading: Vol 1 Ch.3 (Framework for SDIs)", 20),
            ],
        },
    ],

    # ----------------------------------------------------
    # Week 3 — Uber, Ad Click Aggregator, LeetCode
    # ----------------------------------------------------
    [
        {
            "day": "Day 15 – Uber (Geospatial Matching v1)",
            "slots": [
                ("Question Breakdown: Uber v1 (matching, surge, location)", 50),
                ("Break", 15),
                ("Core Concepts: Partitioning, replication, consistent hashing", 30),
                ("Key Tech: Redis (hot queries), Kafka (events)", 25),
                ("Refactor: Uber v2 (latency vs consistency)", 10),
                ("Reading: Vol 2 Ch.1 (Proximity Service)", 20),
            ],
        },
        {
            "day": "Day 16 – Uber Refactor + Redis/Kafka",
            "slots": [
                ("Review Uber v2", 10),
                ("Key Tech Deep Dive: Redis (cache, pub/sub, leaderboards)", 45),
                ("Break", 15),
                ("Key Tech Deep Dive: Kafka (durability, consumer groups)", 45),
                ("Refactor: Uber v3 integrations", 25),
                ("Reading: Vol 1 Ch.6 (Key-Value Store)", 15),
            ],
        },
        {
            "day": "Day 17 – Ad Click Aggregator (v1)",
            "slots": [
                ("Question Breakdown: Aggregator v1 (billions/day)", 50),
                ("Break", 15),
                ("Patterns: Work distribution, scaling writes", 30),
                ("Key Tech: Flink for aggregation, Cassandra/DynamoDB for writes", 25),
                ("Refactor: Aggregator v2 trade-offs", 10),
                ("Reading: Vol 2 Ch.6 (Ad Click Event Aggregation)", 20),
            ],
        },
        {
            "day": "Day 18 – Cassandra vs DynamoDB Deep Dive",
            "slots": [
                ("Core Concepts: Partitioning/sharding strategies", 30),
                ("Core Concepts: Replication/consistency trade-offs", 30),
                ("Break", 15),
                ("Refactor: Aggregator with DB comparisons", 40),
                ("Artifacts: Pros/cons table", 25),
                ("Reading: Vendor docs/cheatsheets (optional)", 10),
            ],
        },
        {
            "day": "Day 19 – LeetCode (Online Judge v1)",
            "slots": [
                ("Question Breakdown: LeetCode v1 (sandbox, safety)", 50),
                ("Break", 15),
                ("Patterns: Job scheduling, retries, idempotency", 30),
                ("Key Tech: Kafka/SQS scheduler, Docker isolation", 25),
                ("Refactor: LeetCode v2 (results DB, quotas)", 10),
                ("Reading: Vol 2 Ch.4 (Distributed Message Queue)", 20),
            ],
        },
        {
            "day": "Day 20 – Tech Trade-Off Workshop",
            "slots": [
                ("Compare Redis vs Kafka vs Cassandra", 30),
                ("Apply choices across Uber, Aggregator, LeetCode", 40),
                ("Break", 15),
                ("Artifacts: Technology cheat sheet", 35),
                ("Reading Review: Vol 2 Ch.1, Ch.4, Ch.6; Vol 1 Ch.5–6 (Consistent Hashing/KV)", 20),
            ],
        },
        {
            "day": "Day 21 – Mock Interview (Uber/Aggregator/LeetCode)",
            "slots": [
                ("Simulation: Pick one system", 50),
                ("Break", 15),
                ("Self-Critique: Tech justification clarity", 45),
                ("Patch Plan: Prep for Week 4", 30),
                ("Optional Reading: Revisit weakest chapter", 20),
            ],
        },
    ],

    # ----------------------------------------------------
    # Week 4 — YouTube, Web Crawler, Google Docs
    # ----------------------------------------------------
    [
        {
            "day": "Day 22 – YouTube (Video Platform v1)",
            "slots": [
                ("Question Breakdown: YouTube v1 (upload, stream, CDN)", 50),
                ("Break", 15),
                ("Core Concepts: Request flow, consistency models", 30),
                ("Key Tech: CDN, chunking, adaptive bitrate", 25),
                ("Refactor: YouTube v2 (hot content, failover)", 10),
                ("Reading: Vol 1 Ch.14 (YouTube)", 20),
            ],
        },
        {
            "day": "Day 23 – YouTube Refactor",
            "slots": [
                ("Focus: Storage + transcoding pipeline", 45),
                ("Break", 15),
                ("Key Tech: Failure handling (node crash, CDN outage)", 40),
                ("Artifacts: SLOs + backpressure notes", 40),
                ("Reading: Related blog posts/notes (optional)", 10),
            ],
        },
        {
            "day": "Day 24 – Web Crawler (v1)",
            "slots": [
                ("Question Breakdown: Crawler v1 (politeness, dedupe, indexing)", 50),
                ("Break", 15),
                ("Core Concepts: URL frontier, dedup (Bloom/DB), robots.txt", 30),
                ("Patterns: Work distribution, backpressure", 25),
                ("Refactor: Crawler v2 (sharding frontier)", 10),
                ("Reading: Vol 1 Ch.9 (Web Crawler)", 20),
            ],
        },
        {
            "day": "Day 25 – Web Crawler Refactor",
            "slots": [
                ("Core Concepts: Frontier scaling across shards", 40),
                ("Key Tech: Distributed dedup strategies", 30),
                ("Break", 15),
                ("Failure handling: lost workers, retries, idempotency", 40),
                ("Artifacts: Fault tree", 25),
                ("Reading: Any gaps found in Ch.9", 10),
            ],
        },
        {
            "day": "Day 26 – Google Docs (Collab Editing v1)",
            "slots": [
                ("Question Breakdown: Docs v1 (real-time collab, versions)", 50),
                ("Break", 15),
                ("Core Concepts: OT vs CRDTs", 30),
                ("Key Tech: Presence, conflict resolution, storage model", 25),
                ("Refactor: Docs v2 (multi-region, offline merge)", 10),
                ("Reading: Vol 1 Ch.15 (Google Drive) for storage parallels", 20),
            ],
        },
        {
            "day": "Day 27 – Trade-Off Workshop (Media/Search/Docs)",
            "slots": [
                ("Latency vs throughput across YouTube/Crawler/Docs", 30),
                ("Consistency vs availability", 30),
                ("Break", 15),
                ("Cost vs complexity analysis", 30),
                ("Artifacts: Matrix notes", 30),
                ("Reading Review: Vol 1 Ch.14–15; Ch.9", 15),
            ],
        },
        {
            "day": "Day 28 – Mock Interview (YouTube/Crawler/Docs)",
            "slots": [
                ("Simulation: Choose one", 50),
                ("Break", 15),
                ("Self-Critique: Depth vs breadth balance", 45),
                ("Patch Plan: Prep for Week 5", 30),
                ("Optional Reading: Weakest area revisit", 20),
            ],
        },
    ],

    # ----------------------------------------------------
    # Week 5 — Search & Discovery (FB Search, Yelp, Strava)
    # ----------------------------------------------------
    [
        {
            "day": "Day 29 – FB Post Search (v1)",
            "slots": [
                ("Question Breakdown: FB Search v1 (indexing, ranking)", 50),
                ("Break", 15),
                ("Core Concepts: Inverted index, query planning", 30),
                ("Key Tech: Elasticsearch basics", 25),
                ("Refactor: Search v2 (sharding, caching)", 10),
                ("Reading: (Suggested) Vol 1 Ch.13 (Search Autocomplete) concepts", 20),
            ],
        },
        {
            "day": "Day 30 – FB Post Search Refactor",
            "slots": [
                ("Core Concepts: Indexing strategies (prefix, n-gram)", 40),
                ("Key Tech: Query optimization, tiered storage", 30),
                ("Break", 15),
                ("Failure handling: partial index loss, rebuild", 40),
                ("Artifacts: Recovery plan", 25),
                ("Reading: Elastic docs (optional)", 10),
            ],
        },
        {
            "day": "Day 31 – Yelp (Discovery v1)",
            "slots": [
                ("Question Breakdown: Yelp v1 (listings, reviews, photos)", 50),
                ("Break", 15),
                ("Core Concepts: Geo-indexing, ranking/relevance", 30),
                ("Key Tech: Maps/geo infra, caches", 25),
                ("Refactor: Yelp v2 (hot cities, pagination)", 10),
                ("Reading: Vol 2 Ch.3 (Google Maps) parallels", 20),
            ],
        },
        {
            "day": "Day 32 – Yelp Refactor",
            "slots": [
                ("Core Concepts: Scaling geo-search & filters", 40),
                ("Patterns: Caching for locality hotspots", 30),
                ("Break", 15),
                ("Failure handling: degraded search modes", 40),
                ("Artifacts: SLOs + fallbacks", 25),
                ("Reading: Any geo indexing notes", 10),
            ],
        },
        {
            "day": "Day 33 – Strava (Activity Feed v1)",
            "slots": [
                ("Question Breakdown: Strava v1 (tracking, feed, leaderboards)", 50),
                ("Break", 15),
                ("Patterns: Event logging, aggregations, leaderboards", 30),
                ("Key Tech: Redis sorted sets, streaming ingestion", 25),
                ("Refactor: Strava v2 (privacy, segments)", 10),
                ("Reading: Vol 2 Ch.10 (Real-Time Gaming Leaderboard)", 20),
            ],
        },
        {
            "day": "Day 34 – Trade-Off Workshop (Search/Discovery)",
            "slots": [
                ("Search vs discovery trade-offs", 30),
                ("Consistency vs performance (eventual results)", 30),
                ("Break", 15),
                ("Cost vs latency analysis", 30),
                ("Artifacts: Matrix wrap-up", 30),
                ("Reading Review: Vol 2 Ch.3, Ch.10; Vol 1 Ch.13 concepts", 15),
            ],
        },
        {
            "day": "Day 35 – Mock Interview (FB Search/Yelp/Strava)",
            "slots": [
                ("Simulation: Choose one", 50),
                ("Break", 15),
                ("Self-Critique: Indexing vs serving clarity", 45),
                ("Patch Plan: Prep for Week 6", 30),
                ("Optional Reading: Weakest topic revisit", 20),
            ],
        },
    ],

    # ----------------------------------------------------
    # Week 6 — Transactions & Commerce (Auction, Price Tracker, Payment)
    # ----------------------------------------------------
    [
        {
            "day": "Day 36 – Online Auction (v1)",
            "slots": [
                ("Question Breakdown: Auction v1 (bidding, concurrency)", 50),
                ("Break", 15),
                ("Core Concepts: Atomicity, idempotency, concurrency control", 30),
                ("Patterns: Dealing with contention (hot items)", 25),
                ("Refactor: Auction v2 (locks/queues)", 10),
                ("Reading: Vol 2 Ch.7 (Hotel Reservation) parallels", 20),
            ],
        },
        {
            "day": "Day 37 – Auction Refactor",
            "slots": [
                ("Core Concepts: Locking strategies (optimistic/pessimistic)", 40),
                ("Key Tech: Queues, outbox/inbox patterns", 30),
                ("Break", 15),
                ("Failure handling: over-sell, refunds, retries", 40),
                ("Artifacts: Compensating transactions plan", 25),
                ("Reading: Payment/locking blogposts (optional)", 10),
            ],
        },
        {
            "day": "Day 38 – Price Tracker (v1)",
            "slots": [
                ("Question Breakdown: Price Tracker v1 (scrape, alerts)", 50),
                ("Break", 15),
                ("Patterns: Polling vs streaming, dedup, backoff", 30),
                ("Key Tech: Notification pipeline (email/push)", 25),
                ("Refactor: Tracker v2 (freshness/cost trade-offs)", 10),
                ("Reading: Vol 2 Ch.5 (Metrics/Monitoring) concepts apply", 20),
            ],
        },
        {
            "day": "Day 39 – Price Tracker Refactor",
            "slots": [
                ("Core Concepts: Data freshness SLAs", 40),
                ("Key Tech: Queueing + retries + DLQs", 30),
                ("Break", 15),
                ("Failure handling: vendor anti-bot, throttling", 40),
                ("Artifacts: Alert SLOs", 25),
                ("Reading: Provider docs (optional)", 10),
            ],
        },
        {
            "day": "Day 40 – Payment System (v1)",
            "slots": [
                ("Question Breakdown: Payment v1 (auth, capture, refund)", 50),
                ("Break", 15),
                ("Core Concepts: Idempotency keys, 2PC vs saga", 30),
                ("Key Tech: PCI concerns, provider integration", 25),
                ("Refactor: Payment v2 (fraud/latency trade-offs)", 10),
                ("Reading: Vol 2 Ch.11 (Payment System) / Ch.12 (Digital Wallet)", 20),
            ],
        },
        {
            "day": "Day 41 – Trade-Off Workshop (Auction/Tracker/Payment)",
            "slots": [
                ("Atomicity vs availability", 30),
                ("Throughput vs latency under load", 30),
                ("Break", 15),
                ("Cost vs safety trade-offs", 30),
                ("Artifacts: Matrix wrap-up", 30),
                ("Reading Review: Vol 2 Ch.7, Ch.11–12", 15),
            ],
        },
        {
            "day": "Day 42 – Mock Interview (Commerce Systems)",
            "slots": [
                ("Simulation: Choose one", 50),
                ("Break", 15),
                ("Self-Critique: Transaction clarity", 45),
                ("Patch Plan: Prep for Week 7", 30),
                ("Optional Reading: Weakest concept revisit", 20),
            ],
        },
    ],

    # ----------------------------------------------------
    # Week 7 — Infra & Scale (Distributed Cache, Job Scheduler, Live Comments)
    # ----------------------------------------------------
    [
        {
            "day": "Day 43 – Distributed Cache (v1)",
            "slots": [
                ("Question Breakdown: Cache v1 (latency, scale)", 50),
                ("Break", 15),
                ("Core Concepts: Replication, eviction, consistency", 30),
                ("Key Tech: Redis cluster, TTL policies", 25),
                ("Refactor: Cache v2 (rehash, failure modes)", 10),
                ("Reading: Vol 1 Ch.5 (Consistent Hashing) + Ch.6 (KV Store)", 20),
            ],
        },
        {
            "day": "Day 44 – Distributed Cache Refactor",
            "slots": [
                ("Core Concepts: Consistent hashing deep dive", 40),
                ("Patterns: Cache invalidation strategies", 30),
                ("Break", 15),
                ("Failure handling: node loss, split brain", 40),
                ("Artifacts: Recovery & rebalancing plan", 25),
                ("Reading: Redis cluster docs (optional)", 10),
            ],
        },
        {
            "day": "Day 45 – Job Scheduler (v1)",
            "slots": [
                ("Question Breakdown: Scheduler v1 (cron, retries, priorities)", 50),
                ("Break", 15),
                ("Patterns: Distributed scheduling, backoff, idempotency", 30),
                ("Key Tech: Kafka/SQS + workers, visibility timeouts", 25),
                ("Refactor: Scheduler v2 (fairness, throughput)", 10),
                ("Reading: Vol 2 Ch.4 (Distributed Message Queue)", 20),
            ],
        },
        {
            "day": "Day 46 – Job Scheduler Refactor",
            "slots": [
                ("Core Concepts: Queue semantics (at-least-once, exactly-once-ish)", 40),
                ("Key Tech: Dead-letter queues, poison pill handling", 30),
                ("Break", 15),
                ("Failure handling: worker churn, clock skew", 40),
                ("Artifacts: SLA & capacity model", 25),
                ("Reading: MQ provider docs (optional)", 10),
            ],
        },
        {
            "day": "Day 47 – FB Live Comments (v1)",
            "slots": [
                ("Question Breakdown: Live Comments v1 (real-time scale)", 50),
                ("Break", 15),
                ("Patterns: Fan-out, windowing, backpressure", 30),
                ("Key Tech: WebSockets, partitioned streams", 25),
                ("Refactor: Comments v2 (hot shards, ordering)", 10),
                ("Reading: Vol 2 Ch.10 (Leaderboard) analogies", 20),
            ],
        },
        {
            "day": "Day 48 – Trade-Off Workshop (Infra)",
            "slots": [
                ("Latency vs consistency across Cache/Scheduler/Comments", 30),
                ("Scalability vs cost", 30),
                ("Break", 15),
                ("Failure mode analysis", 30),
                ("Artifacts: Matrix wrap-up", 30),
                ("Reading Review: Vol 1 Ch.5–6; Vol 2 Ch.4, Ch.10", 15),
            ],
        },
        {
            "day": "Day 49 – Mock Interview (Infra Systems)",
            "slots": [
                ("Simulation: Choose one", 50),
                ("Break", 15),
                ("Self-Critique: Infra clarity & trade-offs", 45),
                ("Patch Plan: Prep for Week 8", 30),
                ("Optional Reading: Weakest infra topic", 20),
            ],
        },
    ],

    # ----------------------------------------------------
    # Week 8 — Mastery & Mocks (Redo high-value systems)
    # ----------------------------------------------------
    [
        {
            "day": "Day 50 – Uber (Redo)",
            "slots": [
                ("Question Breakdown: Uber timed redesign", 50),
                ("Break", 15),
                ("Self-Critique: Latency vs consistency articulation", 40),
                ("Artifacts: Notes wrap-up", 30),
                ("Reading Review: Vol 2 Ch.1 highlights", 15),
            ],
        },
        {
            "day": "Day 51 – WhatsApp (Redo)",
            "slots": [
                ("Question Breakdown: WhatsApp timed redesign", 50),
                ("Break", 15),
                ("Self-Critique: Real-time connection scaling", 40),
                ("Artifacts: Notes wrap-up", 30),
                ("Reading Review: Vol 1 Ch.12 highlights", 15),
            ],
        },
        {
            "day": "Day 52 – YouTube (Redo)",
            "slots": [
                ("Question Breakdown: YouTube timed redesign", 50),
                ("Break", 15),
                ("Self-Critique: CDN + storage trade-offs", 40),
                ("Artifacts: Notes wrap-up", 30),
                ("Reading Review: Vol 1 Ch.14 highlights", 15),
            ],
        },
        {
            "day": "Day 53 – News Feed (Redo)",
            "slots": [
                ("Question Breakdown: News Feed timed redesign", 50),
                ("Break", 15),
                ("Self-Critique: Fan-out vs fan-in clarity", 40),
                ("Artifacts: Notes wrap-up", 30),
                ("Reading Review: Vol 1 Ch.11 highlights", 15),
            ],
        },
        {
            "day": "Day 54 – Mock Mix (Uber + WhatsApp)",
            "slots": [
                ("Quick Uber drill", 30),
                ("Quick WhatsApp drill", 30),
                ("Break", 15),
                ("Trade-off discussion practice", 40),
                ("Wrap-up notes", 35),
                ("Reading: Revisit weakest of the two", 15),
            ],
        },
        {
            "day": "Day 55 – Mock Mix (YouTube + News Feed)",
            "slots": [
                ("Quick YouTube drill", 30),
                ("Quick News Feed drill", 30),
                ("Break", 15),
                ("Trade-off discussion practice", 40),
                ("Wrap-up notes", 35),
                ("Reading: Revisit weakest of the two", 15),
            ],
        },
        {
            "day": "Day 56 – Final Mock Interview",
            "slots": [
                ("Simulation: Pick any system", 50),
                ("Break", 15),
                ("Final Self-Critique: Delivery + trade-offs", 45),
                ("Capstone notes & interview readiness checklist", 30),
                ("Reading: Skim framework & estimation (Vol 1 Ch.1–3)", 15),
            ],
        },
    ],
]
