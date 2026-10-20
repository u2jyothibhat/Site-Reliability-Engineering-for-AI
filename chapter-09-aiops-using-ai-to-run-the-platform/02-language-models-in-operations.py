TOOLS = [
    {
        "name": "query_metrics",
        "description": "Run a read-only PromQL query over a time range. "
                       "Returns time series. Use for rates, latencies, saturation.",
        "parameters": {"promql": "string", "start": "RFC3339", "end": "RFC3339"},
    },
    {
        "name": "search_logs",
        "description": "Search structured logs for a service and time range. "
                       "Returns up to 200 log events, most recent first.",
        "parameters": {"service": "string", "query": "string",
                       "start": "RFC3339", "end": "RFC3339"},
    },
    {
        "name": "list_changes",
        "description": "List deploys, config changes, flag flips, model and prompt "
                       "version changes for services in a time range.",
        "parameters": {"services": "list[string]", "start": "RFC3339", "end": "RFC3339"},
    },
    {
        "name": "get_dependencies",
        "description": "Return upstream and downstream dependencies of a service.",
        "parameters": {"service": "string"},
    },
    {
        "name": "find_similar_incidents",
        "description": "Retrieve past incidents with similar symptoms, with their "
                       "causes and resolutions.",
        "parameters": {"symptoms": "string", "limit": "integer"},
    },
]
