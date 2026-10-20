fields @timestamp, served_model, status
| filter service = "card-assistant"
| stats count(*) as calls,
        sum(status >= 500) as errors
        by served_model
| sort calls desc
