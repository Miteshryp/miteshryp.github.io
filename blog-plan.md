
# Introductory Blogs
- The Anatomy of Compilers
    - Recent conversation with a friend: Doing automata theory for life
    - Start off by most people only taught automata theory
    - AST and beyond: Three Address Code
    - Basic Blocks: Control Flow and Data Flow
    - Abstract Interpretation: Using Discrete Mathematics
        - Constant Propagation Lattice

# Vectorization Optimizations
- Resources: 
    - https://johnnysswlab.com/vectorization-dependencies-and-outer-loop-vectorization-if-you-cant-beat-them-join-them/ (Outer-loop vectorization demonstration)


# ML Compilers

## H/w characteristics (More known stories)
- Conventional CPUs: Extremely low-latency, highly complex silicon dyes
- Scaling latency with complex chips turned out to be physically impossible by 2004 (dark silicon era)
- Vendors started introducing multiple cores: First genesis of commercial parallel programmable h/w
- Even with multiple cores, synchronization overheads and complex units on silicon made it extremely difficult to scale the number of cores
- GPU Era: 

## S/w charateristics
- Normal vs ML Compilers: Why do we need it
- Historical benchmark characteristics: Browser and internet traffic
    - Limited parallelism exposure at high-level code
    - Loop-level code semantics varied highly across benchmarks

- Frameworks like OpenMP aimed at exposing parallelism from high-level languages easily
- Pointer-chasing patterns: 
    - Inherently dependent algorithms
    - Reduces parallelism; Needs independent chains to process in parallel
    - Applications: Databases (parallelism is managable as a state machine), graph-algorithms (parallelism is managed by creating independent sub-graphs and traversing through them)
