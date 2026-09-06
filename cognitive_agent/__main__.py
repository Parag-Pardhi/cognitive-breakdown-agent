import argparse
import json
from .planner import Planner

def main() -> None:
    parser = argparse.ArgumentParser(description="Cognitive Breakdown Agent")
    parser.add_argument("goal", help="Complex goal to decompose")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()
    plan = Planner().plan(args.goal)
    if args.format == "json":
        print(plan.model_dump_json(indent=2))
    else:
        print(f"# {plan.goal}\n")
        for task in plan.tasks:
            deps = ", ".join(task.dependencies) or "none"
            print(f"## {task.id}: {task.title} ({task.priority})")
            print(task.objective)
            print(f"Dependencies: {deps}")
            print(f"Validation: {task.validation}\n")
        print("## Risks")
        for risk in plan.risks:
            print(f"- {risk}")

if __name__ == "__main__":
    main()
