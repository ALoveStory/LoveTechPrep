# -*- coding: utf-8 -*-
"""
sessions.py
-----------
Interview prep schedule (8 weeks, 56 days).
Driver assigns actual calendar dates based on START_DATE.
"""

SESSIONS = [

    # -----------------
    # WEEK 1: Sliding Window + Two Pointers
    # -----------------
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Warm-up","description":"Review Big-O basics."},
        {"start_hour":18,"start_minute":20,"duration_min":40,"title":"Grokking – Sliding Window Intro","description":"Maximum Sum Subarray of Size K."},
        {"start_hour":19,"start_minute":0,"duration_min":45,"title":"Practice","description":"Smallest Subarray with a Given Sum + LeetCode Minimum Size Subarray Sum."},
        {"start_hour":20,"start_minute":0,"duration_min":40,"title":"Reflection","description":"Summarize sliding window template & pitfalls."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":15,"title":"Quick Review","description":"Sliding window recap."},
        {"start_hour":18,"start_minute":15,"duration_min":45,"title":"Grokking – Sliding Window Deep Dive","description":"Longest Substring with K Distinct Characters + Fruits into Baskets."},
        {"start_hour":19,"start_minute":15,"duration_min":45,"title":"NeetCode Practice","description":"Permutation in String + LeetCode Longest Substring Without Repeating Characters."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Warm-up","description":"Array/sorting basics."},
        {"start_hour":18,"start_minute":20,"duration_min":40,"title":"Grokking – Two Pointers Intro","description":"Pair with Target Sum + Remove Duplicates from Sorted Array."},
        {"start_hour":19,"start_minute":0,"duration_min":45,"title":"NeetCode Practice","description":"3Sum (classic)."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":15,"title":"Quick Review","description":"Two pointers recap."},
        {"start_hour":18,"start_minute":15,"duration_min":45,"title":"Grokking – Reinforcement","description":"Squaring a Sorted Array."},
        {"start_hour":19,"start_minute":15,"duration_min":45,"title":"NeetCode + LeetCode","description":"Container With Most Water + Sort Colors (timed)."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":15,"title":"Pattern Recap","description":"Sliding Window + Two Pointers cheat sheet."},
        {"start_hour":18,"start_minute":15,"duration_min":45,"title":"Practice","description":"Move Zeroes + Longest Repeating Character Replacement (timed)."},
        {"start_hour":19,"start_minute":15,"duration_min":45,"title":"Reflection","description":"Update notes & review mistakes."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":30,"title":"Mock – Problem 1","description":"Sliding Window (timed)."},
        {"start_hour":18,"start_minute":40,"duration_min":30,"title":"Mock – Problem 2","description":"Two Pointers (timed)."},
        {"start_hour":19,"start_minute":20,"duration_min":40,"title":"Review","description":"Clean code rewrite + discussion."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":30,"title":"Review Tough Problems","description":"Redo 2 hardest from week."},
        {"start_hour":18,"start_minute":40,"duration_min":45,"title":"Cheat Sheet","description":"Finalize templates for Sliding Window + Two Pointers."},
    ]},

    # -----------------
    # WEEK 2: Fast & Slow Pointers + Merge Intervals
    # -----------------
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Warm-up","description":"Linked list basics."},
        {"start_hour":18,"start_minute":20,"duration_min":40,"title":"Grokking – Fast & Slow Intro","description":"Linked List Cycle + Happy Number."},
        {"start_hour":19,"start_minute":10,"duration_min":40,"title":"Practice","description":"LeetCode Linked List Cycle II."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Quick Review","description":"Cycle detection recap."},
        {"start_hour":18,"start_minute":20,"duration_min":40,"title":"Grokking – Fast & Slow","description":"Middle of Linked List + Palindrome Linked List."},
        {"start_hour":19,"start_minute":10,"duration_min":45,"title":"NeetCode Practice","description":"Detect Cycle II (review)."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Warm-up","description":"Intervals basics."},
        {"start_hour":18,"start_minute":20,"duration_min":40,"title":"Grokking – Merge Intervals Intro","description":"Merge Intervals + Insert Interval."},
        {"start_hour":19,"start_minute":10,"duration_min":45,"title":"LeetCode Practice","description":"Non-overlapping Intervals."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":15,"title":"Quick Review","description":"Intervals recap."},
        {"start_hour":18,"start_minute":15,"duration_min":45,"title":"Grokking – Reinforcement","description":"Interval List Intersections."},
        {"start_hour":19,"start_minute":15,"duration_min":45,"title":"NeetCode Practice","description":"Meeting Rooms II."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Pattern Recap","description":"Fast/Slow + Intervals cheat sheet."},
        {"start_hour":18,"start_minute":20,"duration_min":45,"title":"Practice","description":"LeetCode: Minimum Interval to Include Each Query."},
        {"start_hour":19,"start_minute":15,"duration_min":40,"title":"Reflection","description":"Summarize pitfalls."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":30,"title":"Mock – Problem 1","description":"Fast/Slow Pointers (timed)."},
        {"start_hour":18,"start_minute":40,"duration_min":30,"title":"Mock – Problem 2","description":"Merge Intervals (timed)."},
        {"start_hour":19,"start_minute":20,"duration_min":40,"title":"Review","description":"Discuss trade-offs."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":30,"title":"Review Tough Problems","description":"Redo 2 hardest from week."},
        {"start_hour":18,"start_minute":40,"duration_min":45,"title":"Cheat Sheet","description":"Finalize templates for Fast/Slow + Intervals."},
    ]},

    # -----------------
    # WEEK 3: Binary Search + Subsets
    # -----------------
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Warm-up","description":"Binary search basics."},
        {"start_hour":18,"start_minute":20,"duration_min":40,"title":"Grokking – Binary Search Intro","description":"Order-agnostic Binary Search + Search in Rotated Sorted Array."},
        {"start_hour":19,"start_minute":10,"duration_min":45,"title":"Practice","description":"First Bad Version, Find Peak Element (LeetCode)."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Quick Review","description":"Binary search template recall."},
        {"start_hour":18,"start_minute":20,"duration_min":45,"title":"Grokking – Binary Search Variants","description":"Ceiling of a Number + Next Letter."},
        {"start_hour":19,"start_minute":15,"duration_min":45,"title":"NeetCode Practice","description":"Search Insert Position + Find Minimum in Rotated Sorted Array."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Warm-up","description":"Subsets concept."},
        {"start_hour":18,"start_minute":20,"duration_min":40,"title":"Grokking – Subsets Intro","description":"Generate all subsets."},
        {"start_hour":19,"start_minute":10,"duration_min":45,"title":"Practice","description":"LeetCode: Subsets, Subsets II."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":15,"title":"Quick Review","description":"Recursive subset generation recap."},
        {"start_hour":18,"start_minute":15,"duration_min":45,"title":"Grokking – Permutations","description":"Permutations of array/string."},
        {"start_hour":19,"start_minute":15,"duration_min":45,"title":"NeetCode Practice","description":"Permutations + Combination Sum."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Pattern Recap","description":"Binary search + subsets cheat sheet."},
        {"start_hour":18,"start_minute":20,"duration_min":45,"title":"LeetCode Practice","description":"Letter Case Permutation, Generate Parentheses."},
        {"start_hour":19,"start_minute":15,"duration_min":40,"title":"Reflection","description":"Notes on recursion/backtracking patterns."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":30,"title":"Mock – Problem 1","description":"Binary Search (timed)."},
        {"start_hour":18,"start_minute":40,"duration_min":30,"title":"Mock – Problem 2","description":"Subsets/Permutations (timed)."},
        {"start_hour":19,"start_minute":20,"duration_min":40,"title":"Review","description":"Discuss recursive tree construction."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":30,"title":"Review Tough Problems","description":"Redo 2 hardest from week."},
        {"start_hour":18,"start_minute":40,"duration_min":45,"title":"Cheat Sheet","description":"Finalize templates for binary search + subsets."},
    ]},

    # -----------------
    # WEEK 4: BFS/DFS + Top-K Elements
    # -----------------
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Warm-up","description":"Tree traversal basics."},
        {"start_hour":18,"start_minute":20,"duration_min":40,"title":"Grokking – BFS Intro","description":"Binary Tree Level Order Traversal."},
        {"start_hour":19,"start_minute":10,"duration_min":45,"title":"Practice","description":"LeetCode: Minimum Depth of Binary Tree."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Quick Review","description":"BFS vs DFS comparison."},
        {"start_hour":18,"start_minute":20,"duration_min":45,"title":"Grokking – DFS Intro","description":"Path Sum + Tree Diameter."},
        {"start_hour":19,"start_minute":15,"duration_min":45,"title":"NeetCode Practice","description":"Number of Islands (DFS)."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Warm-up","description":"Heap refresher."},
        {"start_hour":18,"start_minute":20,"duration_min":40,"title":"Grokking – Top-K Elements","description":"Kth Largest Element + K Closest Points to Origin."},
        {"start_hour":19,"start_minute":10,"duration_min":45,"title":"LeetCode Practice","description":"Top K Frequent Elements."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":15,"title":"Quick Review","description":"Heap operations recap."},
        {"start_hour":18,"start_minute":15,"duration_min":45,"title":"Grokking – More Top-K","description":"Frequency Sort + Kth Smallest Number."},
        {"start_hour":19,"start_minute":15,"duration_min":45,"title":"NeetCode Practice","description":"Merge K Sorted Lists."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":20,"title":"Pattern Recap","description":"BFS, DFS, Top-K cheat sheet."},
        {"start_hour":18,"start_minute":20,"duration_min":45,"title":"LeetCode Practice","description":"Course Schedule (Topological Sort)."},
        {"start_hour":19,"start_minute":15,"duration_min":40,"title":"Reflection","description":"Summarize traversal patterns."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":30,"title":"Mock – Problem 1","description":"Graph traversal (timed)."},
        {"start_hour":18,"start_minute":40,"duration_min":30,"title":"Mock – Problem 2","description":"Heap/Top-K (timed)."},
        {"start_hour":19,"start_minute":20,"duration_min":40,"title":"Review","description":"Check performance trade-offs BFS vs DFS."},
    ]},
    { "blocks": [
        {"start_hour":18,"start_minute":0,"duration_min":30,"title":"Review Tough Problems","description":"Redo 2 hardest from week."},
        {"start_hour":18,"start_minute":40,"duration_min":45,"title":"Cheat Sheet","description":"Finalize templates for BFS/DFS + Top-K."},
    ]},

    # -----------------
    # WEEK 5: DP Basics (Fibonacci, Knapsack)
    # -----------------
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Warm-up",
         "description": "Intro to DP: memoization vs tabulation."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 40, "title": "Grokking – Fibonacci Numbers",
         "description": "Nth Fibonacci, Climbing Stairs."},
        {"start_hour": 19, "start_minute": 10, "duration_min": 45, "title": "Practice",
         "description": "House Robber (LeetCode)."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Quick Review",
         "description": "Overlapping subproblems & optimal substructure."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 45, "title": "Grokking – Fibonacci Variants",
         "description": "Minimum Jumps to Reach End + Min Cost Climbing Stairs."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 45, "title": "NeetCode Practice",
         "description": "Unique Paths, Decode Ways."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Warm-up",
         "description": "Knapsack basics."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 40, "title": "Grokking – 0/1 Knapsack Intro",
         "description": "Subset Sum Problem."},
        {"start_hour": 19, "start_minute": 10, "duration_min": 45, "title": "Practice",
         "description": "Partition Equal Subset Sum (LeetCode)."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 15, "title": "Quick Review",
         "description": "Knapsack DP state recap."},
        {"start_hour": 18, "start_minute": 15, "duration_min": 45, "title": "Grokking – More Knapsack",
         "description": "Target Sum, Count of Subset Sum."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 45, "title": "NeetCode Practice",
         "description": "Coin Change (minimum coins)."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Pattern Recap",
         "description": "Fibonacci & Knapsack cheat sheet."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 45, "title": "LeetCode Practice",
         "description": "Combination Sum IV, Min Path Sum."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 40, "title": "Reflection",
         "description": "Identify DP transition patterns."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 30, "title": "Mock – Problem 1",
         "description": "Fibonacci-type DP (timed)."},
        {"start_hour": 18, "start_minute": 40, "duration_min": 30, "title": "Mock – Problem 2",
         "description": "Knapsack-type DP (timed)."},
        {"start_hour": 19, "start_minute": 20, "duration_min": 40, "title": "Review",
         "description": "Refactor to bottom-up approaches."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 30, "title": "Review Tough Problems",
         "description": "Redo 2 hardest DP basics problems."},
        {"start_hour": 18, "start_minute": 40, "duration_min": 45, "title": "Cheat Sheet",
         "description": "Finalize templates for Fibonacci + Knapsack."},
    ]},

    # -----------------
    # WEEK 6: DP Advanced (LCS, Palindromes) + Backtracking
    # -----------------
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Warm-up",
         "description": "String DP refresher."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 40, "title": "Grokking – Longest Common Subsequence",
         "description": "LCS problem, Min Deletions to Make Palindrome."},
        {"start_hour": 19, "start_minute": 10, "duration_min": 45, "title": "Practice",
         "description": "Edit Distance (LeetCode)."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Quick Review",
         "description": "2D DP table construction."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 45, "title": "Grokking – Palindromic Substrings",
         "description": "Longest Palindromic Substring, Count Palindromic Substrings."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 45, "title": "NeetCode Practice",
         "description": "Longest Palindromic Subsequence (LPS)."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Warm-up",
         "description": "Backtracking intro."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 40, "title": "Grokking – Backtracking",
         "description": "N-Queens, Word Search."},
        {"start_hour": 19, "start_minute": 10, "duration_min": 45, "title": "Practice",
         "description": "LeetCode: Sudoku Solver."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 15, "title": "Quick Review",
         "description": "Recursion tree tracing."},
        {"start_hour": 18, "start_minute": 15, "duration_min": 45, "title": "Grokking – More Backtracking",
         "description": "Generate Parentheses, Combination Sum II."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 45, "title": "NeetCode Practice",
         "description": "Word Search II (Trie + Backtracking)."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Pattern Recap",
         "description": "DP Advanced + Backtracking cheat sheet."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 45, "title": "LeetCode Practice",
         "description": "Distinct Subsequences, Wildcard Matching."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 40, "title": "Reflection",
         "description": "Compare recursion vs DP approaches."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 30, "title": "Mock – Problem 1",
         "description": "LCS or Palindrome DP (timed)."},
        {"start_hour": 18, "start_minute": 40, "duration_min": 30, "title": "Mock – Problem 2",
         "description": "Backtracking (timed)."},
        {"start_hour": 19, "start_minute": 20, "duration_min": 40, "title": "Review",
         "description": "Compare brute force vs optimized solutions."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 30, "title": "Review Tough Problems",
         "description": "Redo 2 hardest from week."},
        {"start_hour": 18, "start_minute": 40, "duration_min": 45, "title": "Cheat Sheet",
         "description": "Finalize templates for LCS, Palindromes, Backtracking."},
    ]},

    # -----------------
    # WEEK 7: Mixed Review + Mock Interviews
    # -----------------
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Warm-up",
         "description": "Quick recall of core patterns (Sliding Window, Two Pointers)."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 40, "title": "Targeted Review",
         "description": "Revisit weakest pattern from Weeks 1–3."},
        {"start_hour": 19, "start_minute": 10, "duration_min": 45, "title": "Practice",
         "description": "2 LeetCode mediums from reviewed pattern."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Quick Review",
         "description": "Fast/Slow Pointers & Merge Intervals recap."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 45, "title": "Targeted Review",
         "description": "Revisit interval scheduling problems."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 45, "title": "Practice",
         "description": "Meeting Rooms II + Minimum Interval to Include Each Query."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Warm-up",
         "description": "Binary Search recap."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 45, "title": "Targeted Review",
         "description": "Binary search + subsets."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 45, "title": "Practice",
         "description": "Find Minimum in Rotated Array + Subsets II."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 15, "title": "Quick Review",
         "description": "BFS/DFS recap."},
        {"start_hour": 18, "start_minute": 15, "duration_min": 45, "title": "Targeted Review",
         "description": "Graph traversal patterns."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 45, "title": "Practice",
         "description": "Number of Islands + Course Schedule."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Warm-up",
         "description": "DP basics recap."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 45, "title": "Targeted Review",
         "description": "Knapsack & Fibonacci patterns."},
        {"start_hour": 19, "start_minute": 15, "duration_min": 45, "title": "Practice",
         "description": "House Robber II + Coin Change II."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 30, "title": "Mock – Problem 1",
         "description": "Array/Strings (timed)."},
        {"start_hour": 18, "start_minute": 40, "duration_min": 30, "title": "Mock – Problem 2",
         "description": "Graph/DFS (timed)."},
        {"start_hour": 19, "start_minute": 20, "duration_min": 40, "title": "Review",
         "description": "Discuss solutions & optimizations."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 30, "title": "Review Tough Problems",
         "description": "Redo 2 hardest from week."},
        {"start_hour": 18, "start_minute": 40, "duration_min": 45, "title": "Cheat Sheet",
         "description": "Update combined notes across all patterns."},
    ]},

        # -----------------
        # WEEK 8: Full Simulation + Polishing
        # -----------------
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 15, "title": "Warm-up",
         "description": "Light review of cheat sheet."},
        {"start_hour": 18, "start_minute": 15, "duration_min": 90, "title": "Full Mock Interview",
         "description": "1-hour problem + 30-min review."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 15, "title": "Warm-up",
         "description": "Array/string template recall."},
        {"start_hour": 18, "start_minute": 15, "duration_min": 90, "title": "Full Mock Interview",
         "description": "2 medium problems back-to-back."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Quick Review",
         "description": "Graphs recap."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 90, "title": "Full Mock Interview",
         "description": "Graph + BFS/DFS/Topological sort."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 15, "title": "Warm-up",
         "description": "DP template recall."},
        {"start_hour": 18, "start_minute": 15, "duration_min": 90, "title": "Full Mock Interview",
         "description": "DP heavy problem (timed)."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 20, "title": "Review",
         "description": "Weakest pattern drill (self-assessment)."},
        {"start_hour": 18, "start_minute": 20, "duration_min": 90, "title": "Mixed Set",
         "description": "3 timed problems from different categories."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 15, "title": "Warm-up",
         "description": "Behavioral prep (STAR method)."},
        {"start_hour": 18, "start_minute": 15, "duration_min": 90, "title": "Final Mock Interview",
         "description": "Simulate with peer or Interviewing.io."},
    ]},
    {"blocks": [
        {"start_hour": 18, "start_minute": 0, "duration_min": 45, "title": "Final Review",
         "description": "Redo toughest 2–3 problems from past 8 weeks."},
        {"start_hour": 18, "start_minute": 50, "duration_min": 40, "title": "Reflection",
         "description": "Finalize cheat sheet + confidence check."},
    ]}

]
