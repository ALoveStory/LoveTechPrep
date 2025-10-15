# sessions.py

weeks = [
    # ------------------------
    # Week 1 – Bit.ly, Dropbox, Rate Limiter
    # ------------------------
    [
        {
            "day": "Day 1 – Bit.ly (URL Shortener)",
            "slots": [
                ("Warm-up & framework checklist", 15),
                ("Bit.ly v1 full design", 50),
                ("Break", 15),
                ("Targeted concepts (ID generation, DB vs KV store, cache placement)", 30),
                ("Bit.ly v2 refactor (sharding, cache hit path, failure modes)", 25),
                ("Journal: 3 gaps to fix tomorrow", 15),
            ],
        },
        {
            "day": "Day 2 – Bit.ly Refactor + Consistency/Caching",
            "slots": [
                ("Review yesterday’s gaps", 10),
                ("Bit.ly v3 (QPS math, hot-key mitigation, consistent hashing)", 45),
                ("Break", 15),
                ("Concepts sprint: caching strategies + consistency trade-offs", 30),
                ("Trade-off table + failure plan", 30),
                ("Snapshot notes & diagram cleanup", 20),
            ],
        },
        {
            "day": "Day 3 – Dropbox (File Storage & Sync)",
            "slots": [
                ("Problem framing (functional & non-functional)", 10),
                ("Dropbox v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: object storage + metadata partitioning", 30),
                ("Dropbox v2 (chunking, dedupe, conflict resolution, multi-region)", 35),
                ("Risks list (hot files, large folders, backfill)", 10),
            ],
        },
        {
            "day": "Day 4 – Dropbox Refactor + CAP & Networking",
            "slots": [
                ("Review risks", 10),
                ("Dropbox v3 (sync consistency, retries, idempotency)", 45),
                ("Break", 15),
                ("Concepts sprint: CAP theorem + request flow", 30),
                ("Failure drill (region outage, shard loss, latency spike)", 40),
                ("Update diagrams & notes", 10),
            ],
        },
        {
            "day": "Day 5 – Rate Limiter (Protection & Fairness)",
            "slots": [
                ("Define requirements (per-IP, per-key, sliding window)", 10),
                ("Rate Limiter v1 (algo choice, API gateway placement)", 45),
                ("Break", 15),
                ("Concepts sprint: token vs leaky bucket, fixed vs sliding windows", 30),
                ("Rate Limiter v2 (multi-DC, hot users, failures)", 40),
                ("Quick trade-off table (accuracy, memory, throughput)", 10),
            ],
        },
        {
            "day": "Day 6 – Cross-Design Trade-offs & Speed Round",
            "slots": [
                ("Build trade-off matrix (Bit.ly, Dropbox, Rate Limiter)", 20),
                ("Speed redo of Bit.ly or Dropbox", 45),
                ("Break", 15),
                ("Edge-case lab (geo-replication, cache stampede, write spikes)", 45),
                ("Write 60-second opening script", 25),
            ],
        },
        {
            "day": "Day 7 – Mock Interview (Bit.ly/Dropbox/Rate Limiter)",
            "slots": [
                ("Pick one design problem", 10),
                ("Full mock (clarify → HLD → deep dive → trade-offs)", 50),
                ("Break", 15),
                ("Self-critique (unclear parts, missing numbers, weak trade-offs)", 45),
                ("Patch plan for Week 2 (top 3 focus areas)", 30),
            ],
        },
    ],

    # ------------------------
    # Week 2 – News Feed, WhatsApp, Ticketmaster
    # ------------------------
    [
        {
            "day": "Day 8 – FB News Feed",
            "slots": [
                ("Warm-up & requirements", 15),
                ("News Feed v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: fan-out vs fan-in, caching invalidation", 30),
                ("News Feed v2 trade-off table", 25),
                ("Wrap-up notes", 15),
            ],
        },
        {
            "day": "Day 9 – FB News Feed Refactor",
            "slots": [
                ("Review yesterday’s design", 10),
                ("Push vs pull model deep dive", 45),
                ("Break", 15),
                ("Add ranking + freshness trade-offs", 30),
                ("News Feed v3 improvements", 40),
                ("Write summary notes", 10),
            ],
        },
        {
            "day": "Day 10 – WhatsApp (Chat System)",
            "slots": [
                ("Requirements (1:1 chat, groups, presence)", 15),
                ("WhatsApp v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: durability vs latency (queues, pub/sub)", 30),
                ("WhatsApp v2 with message broker (Kafka/Redis)", 30),
                ("Wrap-up notes", 10),
            ],
        },
        {
            "day": "Day 11 – WhatsApp Refactor + Real-Time",
            "slots": [
                ("Review yesterday’s design", 10),
                ("Add WebSockets/long-polling", 45),
                ("Break", 15),
                ("Scaling millions of connections", 30),
                ("WhatsApp v3 refinements", 40),
                ("Wrap-up notes", 10),
            ],
        },
        {
            "day": "Day 12 – Ticketmaster (High-Concurrency)",
            "slots": [
                ("Requirements (ticket sales, high load)", 15),
                ("Ticketmaster v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: distributed locks, consistency", 30),
                ("Ticketmaster v2 hot spot handling", 30),
                ("Notes wrap-up", 10),
            ],
        },
        {
            "day": "Day 13 – Trade-Off Workshop (News Feed, WhatsApp, Ticketmaster)",
            "slots": [
                ("Compare designs on latency vs throughput", 30),
                ("Consistency guarantees trade-offs", 30),
                ("Break", 15),
                ("Cost vs scalability analysis", 30),
                ("Trade-off matrix build", 30),
            ],
        },
        {
            "day": "Day 14 – Mock Interview (Social Systems)",
            "slots": [
                ("Pick one design (News Feed/WhatsApp/Ticketmaster)", 10),
                ("Full mock design interview", 50),
                ("Break", 15),
                ("Self-critique (trade-offs clarity)", 45),
                ("Refactor notes for Week 3", 30),
            ],
        },
    ],

    # ------------------------
    # Week 3 – Uber, Ad Click Aggregator, LeetCode
    # ------------------------
    [
        {
            "day": "Day 15 – Uber (Geospatial Matching)",
            "slots": [
                ("Requirements (drivers, riders, surge)", 15),
                ("Uber v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: Redis cache for hot queries, Kafka for events", 30),
                ("Uber v2 trade-offs (consistency vs latency)", 30),
                ("Notes wrap-up", 10),
            ],
        },
        {
            "day": "Day 16 – Uber Refactor + Redis/Kafka",
            "slots": [
                ("Review yesterday’s design", 10),
                ("Redis deep dive (caching, pub/sub, leaderboards)", 45),
                ("Break", 15),
                ("Kafka deep dive (event streaming, durability, consumer groups)", 45),
                ("Uber v3 refinements", 35),
            ],
        },
        {
            "day": "Day 17 – Ad Click Aggregator",
            "slots": [
                ("Requirements (billions of events/day)", 15),
                ("Aggregator v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: Flink for aggregation, Cassandra/DynamoDB for writes", 30),
                ("Aggregator v2 trade-offs", 30),
                ("Notes wrap-up", 10),
            ],
        },
        {
            "day": "Day 18 – Cassandra vs DynamoDB Deep Dive",
            "slots": [
                ("Partitioning/sharding review", 30),
                ("Replication/consistency trade-offs", 30),
                ("Break", 15),
                ("Refactor Aggregator design with DB comparisons", 40),
                ("Wrap-up", 20),
            ],
        },
        {
            "day": "Day 19 – LeetCode (Online Judge)",
            "slots": [
                ("Requirements (sandbox, safe code execution)", 15),
                ("LeetCode v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: Job scheduler with Kafka, Docker isolation", 30),
                ("LeetCode v2 improvements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 20 – Tech Trade-Off Workshop",
            "slots": [
                ("Redis vs Kafka vs Cassandra overview", 30),
                ("Apply to Uber, Aggregator, LeetCode", 40),
                ("Break", 15),
                ("Build technology cheat sheet", 35),
                ("Wrap-up", 30),
            ],
        },
        {
            "day": "Day 21 – Mock Interview (Uber/Aggregator/LeetCode)",
            "slots": [
                ("Pick one design", 10),
                ("Full mock (end-to-end design)", 50),
                ("Break", 15),
                ("Self-critique (tech justification clarity)", 45),
                ("Patch plan for Week 4", 30),
            ],
        },
    ],

    # ------------------------
    # Week 4 – YouTube, Web Crawler, Google Docs
    # ------------------------
    [
        {
            "day": "Day 22 – YouTube (Video Platform)",
            "slots": [
                ("Requirements (upload, stream, CDN)", 15),
                ("YouTube v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: CDN, chunking, adaptive bitrate", 30),
                ("YouTube v2 refinements", 30),
                ("Notes wrap-up", 10),
            ],
        },
        {
            "day": "Day 23 – YouTube Refactor",
            "slots": [
                ("Review design", 10),
                ("Focus on storage + transcoding", 45),
                ("Break", 15),
                ("Refactor with failure handling (node crash, CDN outage)", 40),
                ("Wrap-up", 40),
            ],
        },
        {
            "day": "Day 24 – Web Crawler",
            "slots": [
                ("Requirements (crawl, index, politeness)", 15),
                ("Crawler v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: URL frontier, deduplication, robots.txt", 30),
                ("Crawler v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 25 – Web Crawler Refactor",
            "slots": [
                ("Scaling frontier across shards", 40),
                ("Distributed deduplication strategies", 30),
                ("Break", 15),
                ("Failure handling (lost workers)", 40),
                ("Wrap-up", 25),
            ],
        },
        {
            "day": "Day 26 – Google Docs (Collab Editing)",
            "slots": [
                ("Requirements (real-time collab, versioning)", 15),
                ("Docs v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: OT vs CRDTs", 30),
                ("Docs v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 27 – Trade-Off Workshop (YouTube, Crawler, Docs)",
            "slots": [
                ("Latency vs throughput trade-offs", 30),
                ("Consistency vs availability", 30),
                ("Break", 15),
                ("Cost vs complexity analysis", 30),
                ("Matrix notes", 30),
            ],
        },
        {
            "day": "Day 28 – Mock Interview (YouTube/Crawler/Docs)",
            "slots": [
                ("Pick one design", 10),
                ("Full mock", 50),
                ("Break", 15),
                ("Self-critique", 45),
                ("Week 5 prep notes", 30),
            ],
        },
    ],

    # ------------------------
    # Week 5 – Search & Discovery (FB Search, Yelp, Strava)
    # ------------------------
    [
        {
            "day": "Day 29 – FB Post Search",
            "slots": [
                ("Requirements (search, ranking)", 15),
                ("FB Search v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: inverted index, sharding", 30),
                ("FB Search v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 30 – FB Post Search Refactor",
            "slots": [
                ("Indexing strategies", 40),
                ("Query optimization", 30),
                ("Break", 15),
                ("Failure handling", 40),
                ("Notes wrap-up", 25),
            ],
        },
        {
            "day": "Day 31 – Yelp (Discovery Service)",
            "slots": [
                ("Requirements (business listings, reviews)", 15),
                ("Yelp v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: geo-indexing, recommendations", 30),
                ("Yelp v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 32 – Yelp Refactor",
            "slots": [
                ("Scaling geo-search", 40),
                ("Caching strategies for hot cities", 30),
                ("Break", 15),
                ("Failure handling", 40),
                ("Wrap-up", 25),
            ],
        },
        {
            "day": "Day 33 – Strava (Activity Feed)",
            "slots": [
                ("Requirements (fitness tracking, feed)", 15),
                ("Strava v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: event logging, leaderboard", 30),
                ("Strava v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 34 – Trade-Off Workshop (Search/Discovery Systems)",
            "slots": [
                ("Search vs discovery trade-offs", 30),
                ("Consistency vs performance", 30),
                ("Break", 15),
                ("Cost vs latency analysis", 30),
                ("Matrix wrap-up", 30),
            ],
        },
        {
            "day": "Day 35 – Mock Interview (FB Search/Yelp/Strava)",
            "slots": [
                ("Pick one design", 10),
                ("Full mock", 50),
                ("Break", 15),
                ("Self-critique", 45),
                ("Week 6 prep notes", 30),
            ],
        },
    ],

    # ------------------------
    # Week 6 – Transactions & Commerce
    # ------------------------
    [
        {
            "day": "Day 36 – Online Auction System",
            "slots": [
                ("Requirements (bidding, concurrency)", 15),
                ("Auction v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: optimistic locks, queues", 30),
                ("Auction v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 37 – Auction Refactor",
            "slots": [
                ("Locking strategies", 40),
                ("Failure handling", 30),
                ("Break", 15),
                ("Scaling hot items", 40),
                ("Wrap-up", 25),
            ],
        },
        {
            "day": "Day 38 – Price Tracker",
            "slots": [
                ("Requirements (web scraping, alerts)", 15),
                ("Price Tracker v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: polling vs streaming, notifications", 30),
                ("Price Tracker v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 39 – Price Tracker Refactor",
            "slots": [
                ("Notification pipeline deep dive", 40),
                ("Data freshness trade-offs", 30),
                ("Break", 15),
                ("Failure handling", 40),
                ("Wrap-up", 25),
            ],
        },
        {
            "day": "Day 40 – Payment System",
            "slots": [
                ("Requirements (transactions, fraud detection)", 15),
                ("Payment v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: idempotency, 2PC, retries", 30),
                ("Payment v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 41 – Trade-Off Workshop (Auction/Price/Payment)",
            "slots": [
                ("Atomicity vs availability", 30),
                ("Throughput vs latency", 30),
                ("Break", 15),
                ("Cost vs safety trade-offs", 30),
                ("Matrix wrap-up", 30),
            ],
        },
        {
            "day": "Day 42 – Mock Interview (Auction/Price/Payment)",
            "slots": [
                ("Pick one design", 10),
                ("Full mock", 50),
                ("Break", 15),
                ("Self-critique", 45),
                ("Week 7 prep notes", 30),
            ],
        },
    ],

    # ------------------------
    # Week 7 – Infra & Scale
    # ------------------------
    [
        {
            "day": "Day 43 – Distributed Cache",
            "slots": [
                ("Requirements (latency, scale)", 15),
                ("Cache v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: eviction, consistency, replication", 30),
                ("Cache v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 44 – Distributed Cache Refactor",
            "slots": [
                ("Consistent hashing deep dive", 40),
                ("Cache invalidation strategies", 30),
                ("Break", 15),
                ("Failure handling", 40),
                ("Wrap-up", 25),
            ],
        },
        {
            "day": "Day 45 – Job Scheduler",
            "slots": [
                ("Requirements (scheduling, retries)", 15),
                ("Scheduler v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: queues, distributed scheduling", 30),
                ("Scheduler v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 46 – Job Scheduler Refactor",
            "slots": [
                ("Queueing deep dive (Kafka, SQS)", 40),
                ("Scalability trade-offs", 30),
                ("Break", 15),
                ("Failure handling", 40),
                ("Wrap-up", 25),
            ],
        },
        {
            "day": "Day 47 – FB Live Comments",
            "slots": [
                ("Requirements (real-time, millions of comments)", 15),
                ("FB Live Comments v1 design", 50),
                ("Break", 15),
                ("Concepts sprint: fan-out, sharding, WebSockets", 30),
                ("Live Comments v2 refinements", 30),
                ("Wrap-up", 10),
            ],
        },
        {
            "day": "Day 48 – Trade-Off Workshop (Cache, Scheduler, Comments)",
            "slots": [
                ("Latency vs consistency", 30),
                ("Scalability vs cost", 30),
                ("Break", 15),
                ("Failure mode analysis", 30),
                ("Matrix wrap-up", 30),
            ],
        },
        {
            "day": "Day 49 – Mock Interview (Infra Systems)",
            "slots": [
                ("Pick one design", 10),
                ("Full mock", 50),
                ("Break", 15),
                ("Self-critique", 45),
                ("Week 8 prep notes", 30),
            ],
        },
    ],

    # ------------------------
    # Week 8 – Mastery & Mocks
    # ------------------------
    [
        {
            "day": "Day 50 – Uber (Redo)",
            "slots": [
                ("Warm-up & requirements", 15),
                ("Uber timed design (redo)", 50),
                ("Break", 15),
                ("Self-critique", 40),
                ("Notes wrap-up", 30),
            ],
        },
        {
            "day": "Day 51 – WhatsApp (Redo)",
            "slots": [
                ("Warm-up & requirements", 15),
                ("WhatsApp timed design (redo)", 50),
                ("Break", 15),
                ("Self-critique", 40),
                ("Notes wrap-up", 30),
            ],
        },
        {
            "day": "Day 52 – YouTube (Redo)",
            "slots": [
                ("Warm-up & requirements", 15),
                ("YouTube timed design (redo)", 50),
                ("Break", 15),
                ("Self-critique", 40),
                ("Notes wrap-up", 30),
            ],
        },
        {
            "day": "Day 53 – FB News Feed (Redo)",
            "slots": [
                ("Warm-up & requirements", 15),
                ("News Feed timed design (redo)", 50),
                ("Break", 15),
                ("Self-critique", 40),
                ("Notes wrap-up", 30),
            ],
        },
        {
            "day": "Day 54 – Mock Mix (Uber + WhatsApp)",
            "slots": [
                ("Quick Uber design drill", 30),
                ("Quick WhatsApp design drill", 30),
                ("Break", 15),
                ("Trade-off discussion practice", 40),
                ("Wrap-up notes", 35),
            ],
        },
        {
            "day": "Day 55 – Mock Mix (YouTube + News Feed)",
            "slots": [
                ("Quick YouTube design drill", 30),
                ("Quick News Feed design drill", 30),
                ("Break", 15),
                ("Trade-off discussion practice", 40),
                ("Wrap-up notes", 35),
            ],
        },
        {
            "day": "Day 56 – Final Mock Interview",
            "slots": [
                ("Pick any system", 10),
                ("Full mock under pressure", 50),
                ("Break", 15),
                ("Final self-critique", 45),
                ("Capstone notes & prep for real interviews", 30),
            ],
        },
    ],
]
