PRICE_PER_MILLION = {
    # Illustrative numbers only. Load real prices from config and keep them current.
    "primary-large":   {"input": 2.50, "output": 10.00},
    "secondary-large": {"input": 3.00, "output": 15.00},
    "small-fast":      {"input": 0.15, "output": 0.60},
}

def call_cost(model: str, input_tokens: int, output_tokens: int,
              cached_input_tokens: int = 0, cache_discount: float = 0.9) -> float:
    p = PRICE_PER_MILLION[model]
    billable_input = (input_tokens - cached_input_tokens) \
        + cached_input_tokens * (1 - cache_discount)
    return (billable_input * p["input"] + output_tokens * p["output"]) / 1_000_000

# In the gateway, after each call:
cost = call_cost(target_model, usage.input_tokens, usage.output_tokens,
                 usage.cached_input_tokens)
metrics.counter("genai_cost_usd_total",
                labels={"service": app_id, "route": route, "model": target_model}
                ).inc(cost)
