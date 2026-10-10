---
title: "Intro to ML Compilers"
date: 2026-10-09T01:25:49+05:30
tags: []
author: "mitesh"
draft: true
---


# Blog structure
- Need to decide on a story for this approach

## Idea 1: Start with architecture story
- Out of Order processors - good for general web-based workloads
- VLIW: Failed for generic workloads; Bet was that compilers will extract scheduling out of workloads
- AI workloads: highly deterministic in nature
- VLIW suddenly becomes important since compile-time performance extraction becomes important

## Idea 2: Compilers POV
- Conventional compiler structure
    - Language design: frontend
    - IR: Each language eventually lowered to its own IR for applying optimizations
    - LLVM-IR/GCC: Lowered to backend specific codes
- Conventional compilers challenges
    - Loop-level representations lost at LLVM level
    - IR for language specs were limited; Same infrastructure was being re-implemented for every langugage in the market (AST, local block level optimizations, etc)
- Workloads Specific challenges
    - Compile-time techniques historically failed due to lack of compile-time information
    - Compiler analyses had to deal with arbituary/unstructured control and data flow in programs
        - Analysis results suffer with precision issues
    - Alias analysis, Pointer analysis, etc became extremely complicated
- Advent of AI: Producer-Consumer workloads
    - Workloads have pre-defined structure; entire compute graph available at compile-time

```cpp
#include<iostream>
int main() {
    std::cout << "Hello sailor!" << std::endl;
}
```
