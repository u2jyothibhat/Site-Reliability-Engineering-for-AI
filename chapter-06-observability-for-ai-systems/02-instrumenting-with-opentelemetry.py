from opentelemetry import trace

tracer = trace.get_tracer("assistant")

def call_chat_model(client, model, messages, request_id):
    with tracer.start_as_current_span(f"chat {model}") as span:
        span.set_attribute("gen_ai.operation.name", "chat")
        span.set_attribute("gen_ai.request.model", model)
        span.set_attribute("app.request_id", request_id)
        response = client.chat(model=model, messages=messages)
        span.set_attribute("gen_ai.response.model", response.model)
        span.set_attribute("gen_ai.usage.input_tokens", response.usage.input_tokens)
        span.set_attribute("gen_ai.usage.output_tokens", response.usage.output_tokens)
        span.set_attribute("gen_ai.response.finish_reasons", [response.finish_reason])
        return response
