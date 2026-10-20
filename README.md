# Site Reliability Engineering for AI — Code Listings

Companion code for the book **Site Reliability Engineering for AI: Reliable Cloud and Data Platforms with AIOps, Generative AI and Agentic Systems on AWS, Azure and Google Cloud** by **Jyothi Kodenkiri**, the second book in the *AI and Cloud Technology* series.

Every code listing printed in the book is here, organised by chapter, so you can copy, run and adapt it without retyping.

## Contents

| Folder | What's inside |
|---|---|
| `chapter-02-…` | SLO recording and burn-rate alerting rules (Prometheus), quality-evaluation metrics in Python |
| `chapter-03-…` | Terraform for a GPU inference node pool on GKE |
| `chapter-04-…` | dbt data tests, a data contract, retrieval with embedding-version and access filters |
| `chapter-05-…` | vLLM deployment on Kubernetes, KEDA autoscaling on queue depth, a fallback model-gateway router |
| `chapter-06-…` | OpenTelemetry GenAI spans, an example trace, a population stability index (PSI) drift function |
| `chapter-07-…` | A prompt manifest, structured-output validation with Pydantic |
| `chapter-08-…` | A bounded agent loop with step, token, time and loop-detection budgets |
| `chapter-09-…` | Seasonal anomaly query, read-only investigation tools for an operations assistant |
| `chapter-11-…` | Gateway fault-injection rule with automatic expiry |
| `chapter-12-…` | An evaluation case, a GitHub Actions evaluation gate |
| `chapter-15-…` | Cost-per-request metering, a cost anomaly alert |
| `appendix-d-cloud-recipes` | AWS, Azure and Google Cloud recipes: throttling alerts, private endpoints, GPU metrics, an OpenTelemetry Collector, log queries |

A full list of every file with the section it comes from is in [LISTINGS.md](LISTINGS.md).

## Using the code

The listings are deliberately short. They show the shape of a solution rather than a production-ready implementation, and some refer to helper functions or resources (for example `call_model`, `metrics`, or a Terraform `var`) that you will supply from your own environment. Before using any of it in production:

- Replace names, regions, thresholds and tags with your own standards.
- Check cloud resource arguments and metric names against the provider's current documentation and your Terraform provider version.
- Review everything against your organisation's security, data-protection and change-management controls.
- Treat any prices in the examples as placeholders.

## Errata and updates

Cloud and AI services change quickly. If you find something that no longer works, please open an issue in this repository. Updates to the code will be made here.

## Licence

The code in this repository is released under the MIT Licence (see [LICENSE](LICENSE)). The book text and figures remain © 2026 Jyothi Kodenkiri, all rights reserved.
