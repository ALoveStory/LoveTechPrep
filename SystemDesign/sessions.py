# sessions.py
# 8-week plan: Weeks 1–2 Follow-Along, Weeks 3–8 Practice-First.
# Slots are labeled with HelloInterview sections, SDI chapters, and Optional DDIA.
# Your generator controls start time/duration sequencing.

weeks = [
    # ================================
    # WEEK 1 — Follow-Along Mode
    # ================================
    [
        {
            "day": "Day 1 – Bit.ly (URL Shortener)",
            "slots": [
                ("Watch + Read Along: HelloInterview Question Breakdown (Bit.ly v1)", 50),
                ("Concepts: Unique ID generation, cache-aside", 30),
                ("Reading: SDI Vol 1 Ch.8 (URL Shortener)", 25),
                ("Light Practice: Sketch Bit.ly from memory", 15),
                ("Optional Reading: DDIA Ch.3 (Storage & Retrieval → KV stores, indexes)", 30),
            ],
        },
        {
            "day": "Day 2 – Bit.ly Refactor",
            "slots": [
                ("Watch + Read Along: HI Bit.ly v2/v3 (sharding, hot-key mitigation)", 45),
                ("Concepts: Consistent hashing, cache invalidation, distributed counters", 30),
                ("Reading: SDI Vol 1 Ch.4 (Rate Limiter overlap: counters & consistency)", 25),
                ("Light Practice: Redraw Bit.ly with improvements", 20),
            ],
        },
        {
            "day": "Day 3 – Dropbox (File Storage & Sync)",
            "slots": [
                ("Watch + Read Along: HelloInterview Dropbox v1", 50),
                ("Concepts: Chunking, deduplication, replication, metadata partitioning", 30),
                ("Reading: SDI Vol 1 Ch.15 (Google Drive)", 25),
                ("Light Practice: Sketch sync flow & conflicts", 15),
                ("Optional Reading: DDIA Ch.5 (Replication → durability & sync)", 30),
            ],
        },
        {
            "day": "Day 4 – Dropbox Refactor",
            "slots": [
                ("Watch + Read Along: HI Dropbox v2/v3 (multi-region, CAP, retries)", 45),
                ("Concepts: CAP theorem, idempotency, request flows", 30),
                ("Reading: SDI Vol 1 Ch.15 revisit (multi-region trade-offs)", 25),
                ("Light Practice: Failover scenario drill", 20),
            ],
        },
        {
            "day": "Day 5 – Rate Limiter (Protection & Fairness)",
            "slots": [
                ("Watch + Read Along: HelloInterview Rate Limiter v1", 50),
                ("Concepts: Token bucket, leaky bucket, sliding window", 30),
                ("Reading: SDI Vol 1 Ch.4 (Rate Limiter)", 25),
                ("Light Practice: Draw request flow + hot-user handling", 15),
                ("Optional Reading: DDIA Ch.7 (Transactions → concurrency & fairness)", 30),
            ],
        },
        {
            "day": "Day 6 – Cross-Design Workshop",
            "slots": [
                ("Compare: Bit.ly vs Dropbox vs Rate Limiter (strengths/weaknesses)", 30),
                ("Concepts: Sharding vs replication trade-offs", 30),
                ("Reading Recap: SDI Vol 1 Ch.4, Ch.8, Ch.15 (common patterns)", 30),
                ("Exercise: 1-page trade-off matrix", 30),
            ],
        },
        {
            "day": "Day 7 – Guided Mock",
            "slots": [
                ("Simulation: Redo Bit.ly or Dropbox (notes allowed)", 45),
                ("Self-Critique: Delivery framework & clarity", 30),
                ("Reading: Skim relevant SDI chapter for phrasing", 30),
                ("Light Practice: List 3 improvements for Week 2", 15),
            ],
        },
    ],

    # ================================
    # WEEK 2 — Follow-Along Mode
    # ================================
    [
        {
            "day": "Day 8 – FB News Feed (v1)",
            "slots": [
                ("Watch + Read Along: HI News Feed v1 (personalization, freshness, ranking)", 50),
                ("Patterns: Fan-out vs fan-in", 30),
                ("Reading: SDI Vol 1 Ch.11 (News Feed System)", 25),
                ("Light Practice: Sketch push vs pull", 15),
                ("Optional Reading: DDIA Ch.6 (Partitioning → feed sharding, hot users)", 30),
            ],
        },
        {
            "day": "Day 9 – FB News Feed Refactor",
            "slots": [
                ("Watch + Read Along: HI News Feed v2/v3 (freshness, ranking refinements)", 45),
                ("Concepts: Scale estimation for feeds, caching invalidation", 30),
                ("Reading: SDI Vol 1 Ch.2 (Back-of-the-Envelope Estimation)", 25),
                ("Light Practice: Update trade-off table", 20),
            ],
        },
        {
            "day": "Day 10 – WhatsApp (Chat v1)",
            "slots": [
                ("Watch + Read Along: HI WhatsApp v1 (1:1, groups, presence)", 50),
                ("Concepts: Durability vs latency, delivery guarantees", 30),
                ("Key Tech: Redis pub/sub, Kafka queues (quick scan)", 20),
                ("Reading: SDI Vol 1 Ch.12 (Chat System)", 20),
                ("Optional Reading: DDIA Ch.8 (Trouble with Distributed Systems → timeouts/retries)", 30),
            ],
        },
        {
            "day": "Day 11 – WhatsApp Refactor + Real-Time",
            "slots": [
                ("Watch + Read Along: HI WhatsApp v2/v3 (WebSockets/long-polling)", 45),
                ("Patterns: Managing long-running connections (real-time updates)", 30),
                ("Concepts: Consistency across devices", 25),
                ("Light Practice: Connection scaling checklist", 20),
            ],
        },
        {
            "day": "Day 12 – Ticketmaster (High-Concurrency v1)",
            "slots": [
                ("Watch + Read Along: HI Ticketmaster v1 (flash sales, fairness)", 50),
                ("Patterns: Dealing with contention, fairness", 30),
                ("Reading: SDI Vol 2 Ch.7 (Hotel Reservation analog for contention)", 25),
                ("Light Practice: Hot-spot handling sketch", 15),
            ],
        },
        {
            "day": "Day 13 – Trade-Off Workshop (Social Systems)",
            "slots": [
                ("Compare: News Feed vs WhatsApp vs Ticketmaster", 30),
                ("Concepts: Latency vs throughput, consistency guarantees", 30),
                ("Reading Recap: SDI Vol 1 Ch.11, Ch.12; Vol 2 Ch.7", 30),
                ("Exercise: Social systems trade-off matrix", 30),
            ],
        },
        {
            "day": "Day 14 – Guided Mock (Social Systems)",
            "slots": [
                ("Simulation: Choose 1 (notes allowed)", 45),
                ("Self-Critique: Scaling & trade-offs clarity", 30),
                ("Reading: Skim relevant SDI chapter for vocabulary", 30),
                ("Light Practice: Plan focus for Week 3", 15),
            ],
        },
    ],

    # ================================
    # WEEK 3 — Practice-First Mode
    # ================================
    [
        {
            "day": "Day 15 – Uber (Geospatial Matching v1)",
            "slots": [
                ("Practice First: Attempt Uber v1 cold (matching, surge, location)", 50),
                ("Review: HI reference (compare & capture gaps)", 25),
                ("Concepts: Partitioning, replication, consistent hashing", 30),
                ("Reading: SDI Vol 2 Ch.1 (Proximity Service)", 25),
            ],
        },
        {
            "day": "Day 16 – Uber Refactor + Redis/Kafka",
            "slots": [
                ("Practice: Refactor Uber (latency vs consistency)", 40),
                ("Key Tech Deep Dive: Redis (cache, pub/sub, leaderboards)", 30),
                ("Key Tech Deep Dive: Kafka (durability, consumer groups)", 30),
                ("Light Practice: Re-sketch data flow", 20),
            ],
        },
        {
            "day": "Day 17 – Ad Click Aggregator (v1)",
            "slots": [
                ("Practice First: Attempt Aggregator v1 cold (billions/day)", 50),
                ("Review: HI reference (trade-offs & storage)", 25),
                ("Concepts/Patterns: Work distribution, scaling writes", 30),
                ("Reading: SDI Vol 2 Ch.6 (Ad Click Event Aggregation)", 25),
                ("Optional Reading: DDIA Ch.10 (Batch Processing)", 30),
            ],
        },
        {
            "day": "Day 18 – Cassandra vs DynamoDB Deep Dive",
            "slots": [
                ("Concepts: Partitioning/sharding strategies", 30),
                ("Concepts: Replication/consistency trade-offs", 30),
                ("Practice: Refactor Aggregator with DB comparisons", 40),
                ("Artifacts: Pros/cons table", 20),
            ],
        },
        {
            "day": "Day 19 – LeetCode (Online Judge v1)",
            "slots": [
                ("Practice First: Attempt Online Judge v1 cold", 50),
                ("Review: HI reference (isolation, quotas)", 25),
                ("Patterns: Job scheduling, retries, idempotency", 30),
                ("Reading: SDI Vol 2 Ch.4 (Distributed Message Queue)", 25),
                ("Optional Reading: DDIA Ch.11 (Stream Processing)", 30),
            ],
        },
        {
            "day": "Day 20 – Tech Trade-Off Workshop",
            "slots": [
                ("Compare: Redis vs Kafka vs Cassandra", 30),
                ("Apply choices across Uber/Aggregator/LeetCode", 40),
                ("Exercise: Technology cheat sheet", 40),
            ],
        },
        {
            "day": "Day 21 – Mock Interview (Week 3 set)",
            "slots": [
                ("Full Mock: Pick one system (cold)", 50),
                ("Self-Critique: Tech justification clarity", 30),
                ("Reading Recap: Skim SDI chapter of chosen system", 30),
            ],
        },
    ],

    # ================================
    # WEEK 4 — Practice-First Mode
    # ================================
    [
        {
            "day": "Day 22 – YouTube (Video Platform v1)",
            "slots": [
                ("Practice First: Attempt YouTube v1 cold (upload, stream, CDN)", 50),
                ("Review: HI reference (bitrate, hot content, CDN)", 25),
                ("Concepts: Request flow, consistency models", 30),
                ("Reading: SDI Vol 1 Ch.14 (YouTube)", 25),
            ],
        },
        {
            "day": "Day 23 – YouTube Refactor",
            "slots": [
                ("Practice: Storage + transcoding pipeline refactor", 40),
                ("Key Tech: Failure handling (node crash, CDN outage)", 30),
                ("Artifacts: SLOs + backpressure notes", 40),
            ],
        },
        {
            "day": "Day 24 – Web Crawler (v1)",
            "slots": [
                ("Practice First: Attempt Crawler v1 cold (politeness, dedupe, indexing)", 50),
                ("Review: HI reference (frontier, robots.txt, dedup)", 25),
                ("Concepts: URL frontier, Bloom vs DB dedup", 30),
                ("Reading: SDI Vol 1 Ch.9 (Web Crawler)", 25),
                ("Optional Reading: DDIA Ch.2 (Data Models & Query Languages)", 30),
            ],
        },
        {
            "day": "Day 25 – Web Crawler Refactor",
            "slots": [
                ("Concepts: Frontier scaling across shards", 35),
                ("Key Tech: Distributed dedup strategies", 30),
                ("Practice: Failure handling cases", 35),
                ("Artifacts: Fault tree", 20),
            ],
        },
        {
            "day": "Day 26 – Google Docs (Collab Editing v1)",
            "slots": [
                ("Practice First: Attempt Docs v1 cold (real-time collab, versions)", 50),
                ("Review: HI reference (presence, conflicts, storage)", 25),
                ("Concepts: OT vs CRDTs", 30),
                ("Reading: SDI Vol 1 Ch.15 (Google Drive) – storage parallels", 25),
                ("Optional Reading: DDIA Ch.9 (Consistency & Consensus)", 30),
            ],
        },
        {
            "day": "Day 27 – Trade-Off Workshop (Media/Search/Docs)",
            "slots": [
                ("Latency vs throughput across YouTube/Crawler/Docs", 30),
                ("Consistency vs availability", 30),
                ("Exercise: Cost vs complexity matrix", 40),
            ],
        },
        {
            "day": "Day 28 – Mock Interview (Week 4 set)",
            "slots": [
                ("Full Mock: Choose one (cold)", 50),
                ("Self-Critique: Depth vs breadth balance", 30),
                ("Reading Recap: Skim SDI chapter of chosen system", 30),
            ],
        },
    ],

    # ================================
    # WEEK 5 — Practice-First Mode
    # ================================
    [
        {
            "day": "Day 29 – FB Post Search (v1)",
            "slots": [
                ("Practice First: Attempt Search v1 cold (indexing, ranking)", 50),
                ("Review: HI reference (sharding, caching)", 25),
                ("Concepts: Inverted index, query planning", 30),
                ("Reading: (Closest) SDI Vol 1 Ch.13 (Autocomplete concepts)", 25),
                ("Optional Reading: DDIA Ch.4 (Encoding & Evolution)", 30),
            ],
        },
        {
            "day": "Day 30 – FB Post Search Refactor",
            "slots": [
                ("Concepts: Index strategies (prefix, n-gram), tiered storage", 35),
                ("Key Tech: Query optimization paths", 30),
                ("Practice: Failure handling & rebuild", 35),
                ("Artifacts: Recovery plan", 20),
            ],
        },
        {
            "day": "Day 31 – Yelp (Discovery v1)",
            "slots": [
                ("Practice First: Attempt Yelp v1 cold (listings, reviews, photos)", 50),
                ("Review: HI reference (ranking/relevance)", 25),
                ("Concepts: Geo-indexing & recommendations basics", 30),
                ("Reading: SDI Vol 2 Ch.3 (Maps/Geo parallels)", 25),
            ],
        },
        {
            "day": "Day 32 – Yelp Refactor",
            "slots": [
                ("Concepts: Scaling geo-search & filters", 35),
                ("Patterns: Caching for locality hotspots", 30),
                ("Practice: Degraded search modes", 35),
                ("Artifacts: SLOs + fallbacks", 20),
            ],
        },
        {
            "day": "Day 33 – Strava (Activity Feed v1)",
            "slots": [
                ("Practice First: Attempt Strava v1 cold (tracking, feed, leaderboards)", 50),
                ("Review: HI reference (privacy/segments)", 25),
                ("Patterns: Event logging & leaderboards", 30),
                ("Reading: SDI Vol 2 Ch.10 (Real-Time Gaming Leaderboard)", 25),
                ("Optional Reading: DDIA Ch.12 (Future of Data Systems)", 30),
            ],
        },
        {
            "day": "Day 34 – Trade-Off Workshop (Search/Discovery)",
            "slots": [
                ("Search vs discovery trade-offs", 30),
                ("Consistency vs performance (eventual results)", 30),
                ("Exercise: Cost vs latency matrix", 40),
            ],
        },
        {
            "day": "Day 35 – Mock Interview (Week 5 set)",
            "slots": [
                ("Full Mock: Choose one (cold)", 50),
                ("Self-Critique: Indexing vs serving clarity", 30),
                ("Reading Recap: Skim SDI chapter of chosen system", 30),
            ],
        },
    ],

    # ================================
    # WEEK 6 — Practice-First Mode
    # ================================
    [
        {
            "day": "Day 36 – Online Auction (v1)",
            "slots": [
                ("Practice First: Attempt Auction v1 cold (bidding, concurrency)", 50),
                ("Review: HI reference (locks/queues)", 25),
                ("Concepts: Atomicity, idempotency, concurrency control", 30),
                ("Reading: SDI Vol 2 Ch.7 (Hotel Reservation analogs)", 25),
                ("Optional Reading: DDIA Ch.9 (Consistency & Consensus)", 30),
            ],
        },
        {
            "day": "Day 37 – Auction Refactor",
            "slots": [
                ("Concepts: Locking strategies (optimistic/pessimistic)", 35),
                ("Key Tech: Queues, outbox/inbox patterns", 30),
                ("Practice: Failure handling (over-sell, refunds, retries)", 35),
                ("Artifacts: Compensating transactions plan", 20),
            ],
        },
        {
            "day": "Day 38 – Price Tracker (v1)",
            "slots": [
                ("Practice First: Attempt Price Tracker v1 cold (scrape, alerts)", 50),
                ("Review: HI reference (freshness/cost)", 25),
                ("Patterns: Polling vs streaming, backoff", 30),
                ("Reading: SDI Vol 2 Ch.5 (Metrics/Monitoring concepts apply)", 25),
            ],
        },
        {
            "day": "Day 39 – Price Tracker Refactor",
            "slots": [
                ("Concepts: Data freshness SLAs", 35),
                ("Key Tech: Queueing + retries + DLQs", 30),
                ("Practice: Anti-bot/throttling failure modes", 35),
                ("Artifacts: Alert SLOs", 20),
            ],
        },
        {
            "day": "Day 40 – Payment System (v1)",
            "slots": [
                ("Practice First: Attempt Payment v1 cold (auth, capture, refund)", 50),
                ("Review: HI reference (idempotency, retries, fraud)", 25),
                ("Concepts: 2PC vs saga, idempotency keys", 30),
                ("Reading: SDI Vol 2 Ch.11 (Payment System) / Ch.12 (Digital Wallet)", 25),
                ("Optional Reading: DDIA Ch.7 (Transactions)", 30),
            ],
        },
        {
            "day": "Day 41 – Trade-Off Workshop (Commerce)",
            "slots": [
                ("Atomicity vs availability", 30),
                ("Throughput vs latency under load", 30),
                ("Exercise: Cost vs safety matrix", 40),
            ],
        },
        {
            "day": "Day 42 – Mock Interview (Week 6 set)",
            "slots": [
                ("Full Mock: Choose one (cold)", 50),
                ("Self-Critique: Transaction clarity", 30),
                ("Reading Recap: Skim SDI chapter of chosen system", 30),
            ],
        },
    ],

    # ================================
    # WEEK 7 — Practice-First Mode
    # ================================
    [
        {
            "day": "Day 43 – Distributed Cache (v1)",
            "slots": [
                ("Practice First: Attempt Cache v1 cold (latency, scale)", 50),
                ("Review: HI reference (eviction, replication, rehash)", 25),
                ("Concepts: Replication, eviction, consistency", 30),
                ("Reading: SDI Vol 1 Ch.5 (Consistent Hashing) + Ch.6 (KV Store)", 25),
                ("Optional Reading: DDIA Ch.8 (Trouble with Distributed Systems)", 30),
            ],
        },
        {
            "day": "Day 44 – Distributed Cache Refactor",
            "slots": [
                ("Concepts: Consistent hashing deep dive", 35),
                ("Patterns: Cache invalidation strategies", 30),
                ("Practice: Failure handling (node loss, split brain)", 35),
                ("Artifacts: Recovery & rebalancing plan", 20),
            ],
        },
        {
            "day": "Day 45 – Job Scheduler (v1)",
            "slots": [
                ("Practice First: Attempt Scheduler v1 cold (cron, retries, priorities)", 50),
                ("Review: HI reference (fairness, throughput)", 25),
                ("Patterns: Distributed scheduling, backoff, idempotency", 30),
                ("Reading: SDI Vol 2 Ch.4 (Distributed Message Queue)", 25),
                ("Optional Reading: DDIA Ch.9 (Consensus → leader election/coordination)", 30),
            ],
        },
        {
            "day": "Day 46 – Job Scheduler Refactor",
            "slots": [
                ("Concepts: Queue semantics (at-least-once, exactly-once-ish)", 35),
                ("Key Tech: DLQs, poison pill handling", 30),
                ("Practice: Worker churn, clock skew cases", 35),
                ("Artifacts: SLA & capacity model", 20),
            ],
        },
        {
            "day": "Day 47 – FB Live Comments (v1)",
            "slots": [
                ("Practice First: Attempt Live Comments v1 cold (real-time scale)", 50),
                ("Review: HI reference (fan-out, ordering, hot shards)", 25),
                ("Patterns: Fan-out, windowing, backpressure", 30),
                ("Reading: SDI Vol 2 Ch.10 (Leaderboard analogies)", 25),
            ],
        },
        {
            "day": "Day 48 – Trade-Off Workshop (Infra)",
            "slots": [
                ("Latency vs consistency across Cache/Scheduler/Comments", 30),
                ("Scalability vs cost", 30),
                ("Exercise: Failure mode analysis matrix", 40),
            ],
        },
        {
            "day": "Day 49 – Mock Interview (Week 7 set)",
            "slots": [
                ("Full Mock: Choose one (cold)", 50),
                ("Self-Critique: Infra clarity & trade-offs", 30),
                ("Reading Recap: Skim SDI chapter of chosen system", 30),
            ],
        },
    ],

    # ================================
    # WEEK 8 — Practice-First Mode (Mastery & Mocks)
    # ================================
    [
        {
            "day": "Day 50 – Uber (Redo, timed)",
            "slots": [
                ("Timed Redesign: Uber (cold)", 50),
                ("Self-Critique: Latency vs consistency articulation", 30),
                ("Artifacts: Notes wrap-up", 30),
            ],
        },
        {
            "day": "Day 51 – WhatsApp (Redo, timed)",
            "slots": [
                ("Timed Redesign: WhatsApp (cold)", 50),
                ("Self-Critique: Real-time connection scaling", 30),
                ("Artifacts: Notes wrap-up", 30),
            ],
        },
        {
            "day": "Day 52 – YouTube (Redo, timed)",
            "slots": [
                ("Timed Redesign: YouTube (cold)", 50),
                ("Self-Critique: CDN + storage trade-offs", 30),
                ("Artifacts: Notes wrap-up", 30),
            ],
        },
        {
            "day": "Day 53 – News Feed (Redo, timed)",
            "slots": [
                ("Timed Redesign: News Feed (cold)", 50),
                ("Self-Critique: Fan-out vs fan-in clarity", 30),
                ("Artifacts: Notes wrap-up", 30),
            ],
        },
        {
            "day": "Day 54 – Mock Mix (Uber + WhatsApp)",
            "slots": [
                ("Quick Uber drill", 30),
                ("Quick WhatsApp drill", 30),
                ("Trade-off discussion practice", 40),
                ("Wrap-up notes", 30),
            ],
        },
        {
            "day": "Day 55 – Mock Mix (YouTube + News Feed)",
            "slots": [
                ("Quick YouTube drill", 30),
                ("Quick News Feed drill", 30),
                ("Trade-off discussion practice", 40),
                ("Wrap-up notes", 30),
                ("Optional Reading: DDIA Ch.1 (Reliable/Scalable/Maintainable) – capstone review", 30),
            ],
        },
        {
            "day": "Day 56 – Final Mock Interview",
            "slots": [
                ("Full Mock: Pick any system (cold)", 50),
                ("Final Self-Critique: Delivery + trade-offs", 30),
                ("Capstone notes & interview readiness checklist", 30),
            ],
        },
    ],
]
