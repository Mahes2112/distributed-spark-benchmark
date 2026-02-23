<div align="center">

```
██████╗ ██╗███████╗████████╗██████╗ ██╗██████╗ ██╗   ██╗████████╗███████╗██████╗ 
██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗██║██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗
██║  ██║██║███████╗   ██║   ██████╔╝██║██████╔╝██║   ██║   ██║   █████╗  ██║  ██║
██║  ██║██║╚════██║   ██║   ██╔══██╗██║██╔══██╗██║   ██║   ██║   ██╔══╝  ██║  ██║
██████╔╝██║███████║   ██║   ██║  ██║██║██████╔╝╚██████╔╝   ██║   ███████╗██████╔╝
╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═════╝ 
                                                                                    
 ███████╗██████╗  █████╗ ██████╗ ██╗  ██╗    ██████╗ ███████╗███╗   ██╗ ██████╗██╗  ██╗
 ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔══██╗██╔════╝████╗  ██║██╔════╝██║  ██║
 ███████╗██████╔╝███████║██████╔╝█████╔╝     ██████╔╝█████╗  ██╔██╗ ██║██║     ███████║
 ╚════██║██╔═══╝ ██╔══██║██╔══██╗██╔═██╗     ██╔══██╗██╔══╝  ██║╚██╗██║██║     ██╔══██║
 ███████║██║     ██║  ██║██║  ██║██║  ██╗    ██████╔╝███████╗██║ ╚████║╚██████╗██║  ██║
 ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝
```

# ⚡ Distributed Spark Benchmark Project

### *Engineering-grade performance validation on Databricks Serverless*

[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.x-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![Databricks](https://img.shields.io/badge/Databricks-Serverless-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://databricks.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Parquet](https://img.shields.io/badge/Apache-Parquet-50ABF1?style=for-the-badge&logo=apache&logoColor=white)](https://parquet.apache.org/)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

<br/>

> **100,000,000 rows. 5 notebooks. 1 mission — prove that format and architecture are everything.**

<br/>

```
┌─────────────────────────────────────────────────────────┐
│                  HEADLINE RESULTS                       │
│                                                         │
│   CSV  10M   ████████████████████████  ~86s  (baseline) │
│   PP   10M   ███  ~15s   🔥 5.7x faster                 │
│   PP  100M   ████████  ~30s  10x data → 2x time         │
│                                                         │
│   Partition Pruning → 1.35x for 10x data 🤯             │
└─────────────────────────────────────────────────────────┘
```

</div>

---

## 📖 Table of Contents

| # | Section |
|---|---------|
| 1 | [🎯 Project Overview](#-project-overview) |
| 2 | [🏗 Architecture](#-architecture) |
| 3 | [📁 Notebook Structure](#-notebook-structure) |
| 4 | [🔬 Optimization Proofs](#-optimization-proofs) |
| 5 | [📊 Benchmark Results](#-benchmark-results) |
| 6 | [📈 Scalability Analysis](#-scalability-analysis) |
| 7 | [⚙️ Tech Stack](#️-tech-stack) |
| 8 | [🚀 How to Run](#-how-to-run) |
| 9 | [🧠 Engineering Insights](#-engineering-insights) |
| 10 | [🎤 Interview Talking Points](#-interview-talking-points) |

---

## 🎯 Project Overview

This project builds and benchmarks a **production-style distributed Spark data processing pipeline** on Databricks Serverless. The goal is to rigorously compare three dataset formats and sizes across multiple workload types — and **prove** every optimization through physical plan analysis.

### What Makes This Different

This isn't a tutorial or a notebook experiment. Every decision here mirrors real production engineering:

- ✅ Used `count()` instead of `collect()` — avoids driver bottleneck
- ✅ Validated every optimization via `explain(True)` physical plans
- ✅ Tested 4 workload types from simple aggregation to double-shuffle stress tests
- ✅ Measured step-by-step timing inside every notebook
- ✅ Generated 100M rows via `crossJoin` replication — real distributed scale

### Datasets Used

| Dataset | Format | Rows | Partitioned By |
|---------|--------|------|----------------|
| `ecommerce_10M_55cols.csv` | CSV (raw) | 10,000,000 | None |
| `ecommerce_parquet` | Parquet | 10,000,000 | `year`, `month` |
| `ecommerce_100M_parquet` | Parquet | 100,000,000 | `year`, `month` |

---

## 🏗 Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                        DATA FLOW                                      │
│                                                                        │
│  ┌─────────┐     ┌──────────────┐     ┌────────────────────────────┐  │
│  │  VSCode │────▶│ Unity Volume │────▶│  Spark Distributed Engine  │  │
│  │ CSV Gen │     │  raw_data/   │     │   (Databricks Serverless)  │  │
│  └─────────┘     └──────────────┘     └────────────┬───────────────┘  │
│                                                     │                  │
│                    ┌────────────────────────────────┘                  │
│                    ▼                                                   │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │                  PARTITIONED DATA LAKE                           │  │
│  │                                                                  │  │
│  │  ecommerce_parquet/                                              │  │
│  │  ├── year=2022/                                                  │  │
│  │  │   ├── month=1/ ── part-00001.parquet                         │  │
│  │  │   └── month=2/ ── part-00001.parquet                         │  │
│  │  ├── year=2023/                                                  │  │
│  │  └── year=2024/  ◀── Partition Pruning skips others             │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│                    │                                                   │
│                    ▼                                                   │
│  ┌──────────────────────────────────────────────────────────────┐     │
│  │  ANALYTICAL QUERIES  →  Benchmark  →  Physical Plan Proof    │     │
│  └──────────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 📁 Notebook Structure

```
distributed-spark-benchmark/
│
├── 📘 01_Data_Load_and_Conversion.ipynb
│       Load CSV → Add partitions → Write 10M PP → CrossJoin → Write 100M PP
│
├── 📘 02_Optimization_Validation.ipynb
│       Prove partition pruning + column pruning via explain(True)
│
├── 📘 03_Benchmark_Suite.ipynb
│       4 workloads × 3 datasets = 12 timed comparisons
│
├── 📘 04_Scalability_Test.ipynb
│       10M vs 100M scaling factors + AQE partition tuning
│
├── 📘 05_Engineering_Insights.ipynb
│       Structured observations, architecture recap, interview prep
│
├── 📄 README.md
└── 📄 requirements.txt
```

### What Each Notebook Proves

| Notebook | Question Answered |
|----------|------------------|
| `01` | How was the data generated and stored? |
| `02` | Does Spark actually optimize Parquet queries? |
| `03` | How much faster is Parquet vs CSV across real workloads? |
| `04` | Does it scale near-linearly from 10M → 100M? |
| `05` | What are the engineering takeaways? |

---

## 🔬 Optimization Proofs

### 1️⃣ Partition Pruning

When you filter on a partition column, Spark skips entire folders on disk.

```python
# This triggers PartitionFilters in the physical plan
parquet_df.filter("year = 2024").explain(True)
```

**Physical Plan Output (key line):**
```
PartitionFilters: [isnotnull(year#13), (year#13 = 2024)]
```

> 💡 Spark **never reads** year=2022 or year=2023 folders. Pure IO elimination.

---

### 2️⃣ Column Pruning

Parquet stores data column-by-column. Selecting 2 of 55 columns means 53 columns are **never read from disk**.

```python
parquet_df.select("category", "final_price").explain(True)
```

**Physical Plan Output (key line):**
```
ReadSchema: struct<category:string, final_price:double>
```

> 💡 With 55 columns in the dataset, column pruning alone eliminates **~96% of IO**.

---

### 3️⃣ Combined — Maximum Optimization

```python
parquet_df \
    .filter("year = 2024")           # → Partition Pruning  (skip folders)
    .select("category", "final_price") # → Column Pruning (skip columns)
    .explain(True)
```

Both optimizations stack. This is Parquet's full power.

---

### 4️⃣ Shuffle Tuning

```python
# For 100M workloads — increase distributed parallelism
spark.conf.set("spark.sql.shuffle.partitions", 400)
```

> 💡 On Databricks Serverless, AQE (Adaptive Query Execution) auto-coalesces shuffle partitions at runtime — making manual tuning largely redundant, but understanding the setting is essential.

---

## 📊 Benchmark Results

### Task 1 — Filter + Multi-Column Aggregation

```
Filter: year >= 2023 AND month >= 6 AND discount > 500
GroupBy: city, category
Agg: sum(final_price), sum(quantity)

  CSV  10M   ████████████████████████████████████████  8.55s
  PP   10M   ████  1.17s  ✅ 7.3x faster
  PP  100M   ██████████  3.88s  (10x data, only 3.3x slower)
```

### Stress 1 — High-Cardinality GroupBy (4 dimensions)

```
GroupBy: city, category, payment_method, product_id

  CSV  10M   █████████████████████████████████████████  8.69s
  PP   10M   ████████  1.90s  ✅ 4.6x faster
  PP  100M   ████████████████████████████████████████  30.20s  ← shuffle bottleneck
```

> 💡 100M Stress1 takes 30s because `product_id` has millions of unique values — the shuffle layer becomes the bottleneck, not disk IO.

### Stress 2 — Window Function (Row Number per user)

```
Window: PARTITION BY user_id ORDER BY final_price DESC

  CSV  10M   █████████████████████████████  5.48s
  PP   10M   █████  1.04s  ✅ 5.3x faster
  PP  100M   ████████████████  3.33s  (AQE optimized!)
```

### Nuclear — Double Shuffle (Repartition → Window → GroupBy)

```
repartition(800) → row_number() → groupBy(3 dims)
Two full shuffle stages

  CSV  10M   ████████████████████████████████████████████  11.09s
  PP   10M   █████████████████  4.24s  ✅ 2.6x faster
  PP  100M   ████████████████████████████████████████████  29.51s
```

### Full Comparison Table

| Workload | CSV 10M | PP 10M | PP 100M | CSV→PP Speedup |
|----------|---------|--------|---------|----------------|
| Task1 Filter+Agg | 8.55s | 1.17s | 3.88s | **7.3x** |
| Stress1 HiCard GroupBy | 8.69s | 1.90s | 30.20s | **4.6x** |
| Stress2 Window Function | 5.48s | 1.04s | 3.33s | **5.3x** |
| Nuclear Double Shuffle | 11.09s | 4.24s | 29.51s | **2.6x** |

---

## 📈 Scalability Analysis

### The Numbers That Tell the Story

```
Data grew 10x (10M → 100M rows)
Expected linear time: 10x slower

Actual results:
────────────────────────────────────────────────
  Filter+Agg  (Partition Pruning active)  1.35x ← SUB-LINEAR 🤯
  Full Scan   (Columnar IO only)          3.54x ← Sub-linear
  Window Fn   (Sort + Shuffle)            3.21x ← Sub-linear
  HiCard GB   (Shuffle bottleneck)       ~16x   ← Super-linear*
────────────────────────────────────────────────
* product_id high cardinality causes shuffle explosion at 100M
```

### Why Partition Pruning Causes Sub-Linear Scaling

```
10M dataset:  year=2022 | year=2023 | year=2024
               ~~~~~~~~   ~~~~~~~~   ✅ SCANNED

100M dataset: year=2022 | year=2023 | year=2024
               ~~~~~~~~   ~~~~~~~~   ✅ SCANNED

→ Filter "year = 2024" reads the SAME partition size
  regardless of total table size!
  That's why 10x data → only 1.35x time.
```

### AQE — Shuffle Partition Tuning

```
Manual setting: spark.sql.shuffle.partitions = 200 → 5.18s
Manual setting: spark.sql.shuffle.partitions = 400 → 5.22s
                                                      ──────
                                        Difference:   0.04s ← negligible

→ Databricks Serverless AQE is auto-managing partitions at runtime.
  Manual tuning knowledge is still essential for interviews.
```

---

## ⚙️ Tech Stack

| Component | Technology |
|-----------|------------|
| Compute | Databricks Serverless (2XS cluster) |
| Processing Engine | Apache Spark with Photon Engine |
| Storage Format | Apache Parquet (partitioned by year/month) |
| Data Source | CSV (55 columns, 10M rows, 3.79 GB) |
| Storage Layer | Unity Catalog Volume (`/Volumes/workspace/default/raw_data/`) |
| Language | Python 3.10+ (PySpark) |
| Query Optimization | AQE, Partition Pruning, Column Pruning, Predicate Pushdown |

---

## 🚀 How to Run

### Prerequisites

```bash
# Databricks workspace with:
# - Unity Catalog enabled
# - Serverless compute available
# - Volume: /Volumes/workspace/default/raw_data/
```

### Step 1 — Upload CSV to Unity Volume

Upload your `ecommerce_10M_55cols.csv` to:
```
/Volumes/workspace/default/raw_data/
```

### Step 2 — Create Workspace Folder

In Databricks workspace, create folder:
```
Distributed_Spark_Benchmark/
```

### Step 3 — Create & Run Notebooks In Order

```
01_Data_Load_and_Conversion    ← Run first, creates all data
02_Optimization_Validation     ← Validates physical plans
03_Benchmark_Suite             ← Core performance comparison
04_Scalability_Test            ← 10M vs 100M analysis
05_Engineering_Insights        ← Summary and documentation
```

> ⚠️ **Important**: Run `01` completely before any other notebook. It creates the Parquet datasets that all other notebooks read.

### Step 4 — Verify Data Created

After running notebook 01, confirm these paths exist:
```
/Volumes/workspace/default/raw_data/ecommerce_parquet/
/Volumes/workspace/default/raw_data/ecommerce_100M_parquet/
```

### Expected Runtime Per Notebook

| Notebook | Estimated Time |
|----------|---------------|
| `01_Data_Load_and_Conversion` | ~8–12 min |
| `02_Optimization_Validation` | ~30–60 sec |
| `03_Benchmark_Suite` | ~3–5 min |
| `04_Scalability_Test` | ~3–5 min |
| `05_Engineering_Insights` | ~10 sec |

---

## 🧠 Engineering Insights

### Why CSV Is Slow

```
CSV problems:
  1. No schema metadata → inferSchema reads entire file
  2. Row-based → must decode all 55 columns even for 2-column query
  3. No partition structure → full scan on every filter
  4. No predicate pushdown → filter after reading, not before
  5. No encoding → larger file size → more IO
```

### Why Parquet Is Fast

```
Parquet advantages:
  1. Column-based → read only the columns you need
  2. Partition directories → skip entire year/month folders
  3. Encoded + compressed → smaller files → less IO
  4. Row group statistics → skip row groups that can't match filter
  5. Schema embedded → no inferSchema cost
```

### The collect() Problem

```python
# ❌ WRONG for benchmarking
df.filter(...).groupBy(...).collect()  # Pulls ALL data to driver → bottleneck

# ✅ CORRECT
df.filter(...).groupBy(...).count()    # Distributed → returns 1 number
```

### Why High-Cardinality Breaks Linear Scaling

```
Low cardinality:  groupBy("category")        → ~10 unique keys   → small shuffle
High cardinality: groupBy("product_id")      → ~millions of keys → massive shuffle

At 100M rows, the shuffle network transfer becomes the bottleneck.
This is why Stress1 at 100M takes 30s even with Parquet.
```

---

## 🎤 Interview Talking Points

<details>
<summary><strong>Q: What is predicate pushdown?</strong></summary>

Predicate pushdown moves filter conditions as close to the data source as possible — ideally into the file scan itself. In Parquet, this means filtering happens at the row group level before data is loaded into memory, drastically reducing the amount of data Spark ever processes.

</details>

<details>
<summary><strong>Q: How did you prove partition pruning?</strong></summary>

I used `explain(True)` on a filtered Parquet DataFrame and verified the physical plan showed `PartitionFilters: [(year = 2024)]`. This confirms Spark is physically skipping non-matching partition directories — not just filtering after reading.

</details>

<details>
<summary><strong>Q: Why did 10x more data not take 10x longer?</strong></summary>

Because partition pruning makes scaling sub-linear. When filtering on `year = 2024`, Spark reads only that partition folder. The total table size is irrelevant — the scan volume is determined by partition size, not table size. That's why 100M rows with pruning took only 1.35x longer than 10M.

</details>

<details>
<summary><strong>Q: What is AQE and what did you find?</strong></summary>

Adaptive Query Execution is Spark's runtime optimizer that adjusts query plans based on actual data statistics collected during execution. It can coalesce shuffle partitions, handle skew, and switch join strategies at runtime. In my tests, changing from 200 to 400 shuffle partitions made only 0.04s difference — proving AQE was managing partition count automatically on Databricks Serverless.

</details>

<details>
<summary><strong>Q: Why did you use count() instead of collect()?</strong></summary>

`collect()` transfers all result rows back to the driver node. For 100M rows, this creates a massive bottleneck — you'd be measuring network transfer to driver, not distributed compute performance. `count()` triggers full distributed execution but only returns a single integer, giving a true measure of the distributed processing time.

</details>

<details>
<summary><strong>Q: What caused the 30-second time on Stress1 100M?</strong></summary>

Stress1 groups by 4 dimensions including `product_id`, which has millions of unique values (high cardinality). At 100M rows, this generates an enormous shuffle — every unique combination must be moved across the network to the same executor. The bottleneck shifts from disk IO (where Parquet excels) to network shuffle, which scales with data volume regardless of format.

</details>

---

## 📊 Visual Performance Summary

```
                    PERFORMANCE HEATMAP
                    
              CSV 10M    PP 10M    PP 100M
              ────────   ──────    ───────
Task1          🔴 8.5s   🟢 1.2s   🟡 3.9s
Stress1        🔴 8.7s   🟢 1.9s   🔴 30.2s
Stress2        🟡 5.5s   🟢 1.0s   🟢 3.3s
Nuclear        🔴11.1s   🟡 4.2s   🔴 29.5s

🟢 < 2s (Fast)    🟡 2s–6s (Moderate)    🔴 > 6s (Slow)
```

---

## 📌 Key Takeaways

```
┌────────────────────────────────────────────────────────────────┐
│  1. FORMAT IS EVERYTHING                                        │
│     Parquet vs CSV = 5–7x improvement on identical hardware    │
│                                                                  │
│  2. PARTITION PRUNING BEATS SCALING                             │
│     10x data → 1.35x time when pruning is active               │
│                                                                  │
│  3. SHUFFLE IS THE REAL ENEMY                                   │
│     High-cardinality groupBy at scale → network becomes limit  │
│                                                                  │
│  4. AQE MAKES SERVERLESS SMART                                  │
│     Runtime optimization > manual tuning on Databricks          │
│                                                                  │
│  5. VALIDATE WITH PHYSICAL PLANS                                │
│     Never assume optimizations work — prove them with explain() │
└────────────────────────────────────────────────────────────────┘
```

---

<div align="center">

### Built with ⚡ on Databricks Serverless

*If this project helped you understand distributed data engineering — drop a ⭐*

[![GitHub stars](https://img.shields.io/github/stars/yourusername/distributed-spark-benchmark?style=social)](https://github.com/yourusername/distributed-spark-benchmark)

</div>
