import time

ROUTES = {
    "assistant-default": [
        {"provider": "azure-openai", "model": "primary-large", "timeout_s": 20},
        {"provider": "bedrock", "model": "secondary-large", "timeout_s": 20},
        {"provider": "self-hosted", "model": "assistant-8b-v4", "timeout_s": 15},
    ]
}

class AllRoutesFailed(Exception):
    pass

def complete(route_name, messages, request_id):
    errors = []
    for target in ROUTES[route_name]:
        if circuit_open(target):
            errors.append((target["model"], "circuit_open"))
            continue
        start = time.monotonic()
        try:
            response = call_model(target, messages, timeout=target["timeout_s"],
                                  idempotency_key=request_id)
            record_success(target, time.monotonic() - start, response.usage)
            response.served_by = target["model"]
            return response
        except (TimeoutError, ProviderUnavailable, RateLimited) as exc:
            record_failure(target, type(exc).__name__)
            errors.append((target["model"], type(exc).__name__))
    raise AllRoutesFailed(errors)
