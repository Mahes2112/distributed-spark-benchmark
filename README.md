![CI](https://github.com/Mahes2112/distributed-spark-benchmark/actions/workflows/ci.yml/badge.svg)
# Distributed Spark Benchmark
> Storage Format Optimization & Distributed Performance Study

---

## Overview

A structured distributed benchmarking study built using Apache Spark to analyze the performance impact of storage format, partitioning, and query optimization across datasets ranging from 10M to 100M rows.

**Areas of focus:**
- CSV vs Parquet storage format performance
- Partitioning strategies and partition pruning
- Predicate pushdown and column pruning
- Execution plan optimization via Catalyst
- I/O behavior and cost implications at scale

---

## Problem Statement

In distributed data systems, storage format and partitioning directly influence scan cost, I/O overhead, CPU utilization, shuffle behavior, and cluster efficiency. This project quantifies how these factors interact under realistic workloads and growing dataset sizes.

---

## Project Structure

```
distributed-spark-benchmark/
│
├── 01_Data_Load_and_Conversion.ipynb
├── 02_Optimization_Validation.ipynb
├── 03_Benchmark_Suite.ipynb
├── 04_Cost_And_IO_Analysis.ipynb
├── 05_Price_Optimization_Analysis.ipynb
├── 06_Scalability_Test.ipynb
├── 07_Engineering_Insights.ipynb
│
├── DataGenerator.py
├── tests/
│   └── test_spark_session.py
│
├── .github/workflows/ci.yml
├── requirements.txt
├── .flake8
└── README.md
```

---

## Methodology

**1. Data Generation** — Synthetic large-scale datasets with a controlled schema, simulating consistent workloads at 10M and 100M row scales.

**2. Format Conversion** — Data written in both CSV (row-based, text) and Parquet (columnar, compressed, metadata-aware), partitioned by year to enable pruning validation.

**3. Optimization Validation** — `.explain(True)` used to inspect logical, optimized logical, and physical plans. Verified partition pruning, predicate pushdown, and column pruning behavior.

**4. Benchmark Suite** — Measured execution time across filter + aggregation, full scan operations, and selective column reads under both formats.

**5. Scalability Analysis** — Compared performance scaling from 10M to 100M rows, observing I/O-bound vs compute-bound trends and performance growth characteristics.

---

## Why Apache Spark?

Spark was chosen for its distributed DAG-based execution, Catalyst optimizer, lazy evaluation, and wide production adoption. This study focuses on distributed execution behavior rather than single-node analytics.

---

## CSV vs Parquet — Engineering Perspective

| Property | CSV | Parquet |
|---|---|---|
| Storage model | Row-based | Columnar |
| Scan behavior | Full file scan required | Predicate pushdown |
| Schema | None embedded | Metadata-aware |
| Filtering | No metadata filtering | Partition & column pruning |
| Compression | None | Supported |
| Text parsing overhead | Yes | No |

---

## Key Findings

- Parquet significantly reduces scan time in selective queries.
- Partition pruning eliminates unnecessary directory scans entirely.
- Column pruning reduces memory pressure under aggregation workloads.
- CSV performance degrades linearly due to mandatory full scans.
- Parquet benefits compound as dataset size increases — the performance gap widens at 100M rows.
- I/O cost dominates overall performance at scale.
- Physical plan inspection confirms Catalyst optimizer effectiveness.

---

## Scalability Insights

CSV scales poorly with increasing dataset size due to its full scan requirement. Parquet demonstrates significantly better scalability under selective filters, with the performance gap widening as data grows. Partition effectiveness is sensitive to column cardinality and access pattern.

---

## Trade-Off Considerations

- Over-partitioning creates small file problems that degrade performance.
- Columnar storage increases write overhead but substantially improves read performance.
- Compression improves I/O efficiency but may increase CPU usage.
- Spark cluster configuration significantly affects observed scaling behavior.

---

## Testing & CI

Automated CI is configured via GitHub Actions and runs on every push.

**Pipeline steps:**
- Python and Java 17 setup (Spark-compatible)
- Dependency installation
- Code formatting validation (Black)
- Lint validation (Flake8)
- Spark session test via Pytest

This ensures reproducibility, environment validation, continuous quality enforcement, and Spark compatibility verification.

---

## Tooling

| Tool | Purpose |
|---|---|
| Apache Spark | Distributed processing engine |
| Parquet | Columnar format evaluation |
| Black | Code formatting enforcement |
| Flake8 | Lint validation |
| Pytest | Spark session testing |
| GitHub Actions | CI automation |

---

## How to Run Locally

```bash
pip install -r requirements.txt
pytest
```

To run the notebooks, open in Jupyter and execute cells sequentially starting from `01_Data_Load_and_Conversion.ipynb`.

---

## Future Improvements

- Streaming benchmark using Structured Streaming
- Executor memory tuning comparison
- Shuffle partition optimization experiments
- Dockerized reproducible environment
- Cloud cost modeling
- Cluster-mode benchmark validation

---

## Learning Outcomes

This project demonstrates practical understanding of distributed execution planning, storage format trade-offs, I/O cost analysis, partition strategy design, Catalyst optimization behavior, and CI/CD automation for data systems — including real-world toolchain debugging (Java 11 → 17 compatibility).
