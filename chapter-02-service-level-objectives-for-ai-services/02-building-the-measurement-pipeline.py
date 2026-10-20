from prometheus_client import CollectorRegistry, Counter, push_to_gateway

registry = CollectorRegistry()
evaluated = Counter("genai_quality_evaluated_total",
                    "Responses evaluated", ["service", "segment"],
                    registry=registry)
good = Counter("genai_quality_good_total",
               "Responses judged good", ["service", "segment"],
               registry=registry)

def record_results(results, service="card-assistant"):
    """results: iterable of dicts with 'segment', 'grounded', 'format_ok', 'pii_clean'."""
    for r in results:
        evaluated.labels(service, r["segment"]).inc()
        if r["grounded"] and r["format_ok"] and r["pii_clean"]:
            good.labels(service, r["segment"]).inc()
    push_to_gateway("pushgateway.monitoring:9091",
                    job="genai-quality-eval", registry=registry)
