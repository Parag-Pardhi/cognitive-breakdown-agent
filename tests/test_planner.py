from cognitive_agent import Planner

def test_plan_has_dependencies_in_order():
    plan = Planner().plan("Build a secure API")
    assert plan.goal == "Build a secure API"
    assert [task.id for task in plan.tasks] == ["T1", "T2", "T3", "T4", "T5"]
    assert plan.tasks[1].dependencies == ["T1"]
    assert plan.tasks[-1].dependencies == ["T4"]

def test_empty_goal_rejected():
    try:
        Planner().plan("   ")
    except ValueError:
        return
    assert False, "empty goal should raise ValueError"
