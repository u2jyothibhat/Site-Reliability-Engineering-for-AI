from pydantic import BaseModel, Field, ValidationError
from typing import Literal

class ClaimTriage(BaseModel):
    category: Literal["outpatient", "inpatient", "pharmacy", "dental", "other"]
    urgency: Literal["routine", "priority", "urgent"]
    missing_documents: list[str] = Field(default_factory=list)
    summary: str = Field(max_length=800)

def triage_claim(claim_text: str, request_id: str) -> ClaimTriage | None:
    raw = gateway.complete_json(
        route="claims-triage",
        schema=ClaimTriage.model_json_schema(),
        input=claim_text,
        request_id=request_id,
    )
    try:
        result = ClaimTriage.model_validate_json(raw)
    except ValidationError as err:
        metrics.counter("triage_schema_failures_total").inc()
        log.warning("schema validation failed", request_id=request_id,
                    errors=err.error_count())
        return None   # caller routes to manual triage queue
    return result
