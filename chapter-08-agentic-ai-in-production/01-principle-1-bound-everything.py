import time
from collections import Counter
from dataclasses import dataclass

@dataclass
class Budget:
    max_steps: int = 15
    max_tool_calls: int = 25
    max_tokens: int = 60_000
    max_seconds: int = 120
    max_repeat_calls: int = 3

class BudgetExceeded(Exception):
    pass

def run_agent(goal, tools, policy, budget=Budget()):
    state = {"goal": goal, "history": [], "tokens": 0, "tool_calls": 0}
    started = time.monotonic()
    call_signatures = Counter()

    for step in range(budget.max_steps):
        if time.monotonic() - started > budget.max_seconds:
            raise BudgetExceeded("time")
        decision = plan_next_step(state, tools)          # model call
        state["tokens"] += decision.usage.total_tokens
        if state["tokens"] > budget.max_tokens:
            raise BudgetExceeded("tokens")
        if decision.is_final:
            return decision.answer

        signature = (decision.tool, canonical(decision.arguments))
        call_signatures[signature] += 1
        if call_signatures[signature] > budget.max_repeat_calls:
            raise BudgetExceeded("loop_detected")

        policy.authorise(decision.tool, decision.arguments, goal.user)
        state["tool_calls"] += 1
        if state["tool_calls"] > budget.max_tool_calls:
            raise BudgetExceeded("tool_calls")

        result = execute_tool(decision.tool, decision.arguments,
                              idempotency_key=f"{goal.task_id}:{step}")
        state["history"].append((decision, result))

    raise BudgetExceeded("steps")
