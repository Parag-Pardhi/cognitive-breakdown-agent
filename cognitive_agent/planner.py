from .models import Plan, Task

class Planner:
    """Break a goal into a dependency-aware execution plan."""

    def plan(self, goal: str) -> Plan:
        goal = goal.strip()
        if not goal:
            raise ValueError("goal cannot be empty")

        tasks = [
            Task(id="T1", title="Clarify requirements", objective=f"Define scope, users, constraints, and measurable outcomes for: {goal}", priority="critical", validation="Requirements and success criteria are explicit."),
            Task(id="T2", title="Design solution", objective="Choose architecture, interfaces, data flow, dependencies, and security boundaries.", priority="high", dependencies=["T1"], validation="Architecture can be explained with a component/data-flow diagram."),
            Task(id="T3", title="Implement core capability", objective="Build the smallest working implementation that satisfies the approved design.", priority="high", dependencies=["T2"], validation="Core workflow completes successfully with representative inputs."),
            Task(id="T4", title="Test and harden", objective="Add unit/integration tests, input validation, failure handling, logging, and security checks.", priority="high", dependencies=["T3"], validation="Tests pass and expected failure paths are covered."),
            Task(id="T5", title="Deploy and observe", objective="Package the application, document deployment, and add health checks/observability.", priority="medium", dependencies=["T4"], validation="A clean environment can deploy and expose a health check."),
        ]
        return Plan(
            goal=goal,
            assumptions=["The requester can provide required credentials and external dependencies.", "Production requirements may require additional domain-specific controls."],
            tasks=tasks,
            risks=["Unclear requirements can cause rework.", "External APIs or infrastructure may introduce availability and cost constraints.", "Security and privacy requirements must be reviewed before production deployment."],
            success_criteria=["Every task has an explicit validation check.", "Dependencies form an acyclic execution order.", "The resulting implementation is reproducible from documented setup steps."],
        )
