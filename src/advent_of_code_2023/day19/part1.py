from advent_of_code_2023.utils import read_input


def accepts(workflows, workflow_name, part) -> bool:
    # print(workflow_name)
    if workflow_name == 'A':
        return True
    if workflow_name == 'R':
        return False
    for cond, direction in workflows[workflow_name]:
        if cond(part):
            return accepts(workflows, direction, part)
    raise AssertionError()

def solve(lines: list[str]) -> int:
    lines = [line.strip() for line in lines]
    sep = lines.index('')
    workflow_lines = lines[:sep]
    part_lines = lines[sep+1:]
    parts = []
    workflows = {}
    for workflow_line in workflow_lines:
        workflow_line = workflow_line.split("{")
        name = workflow_line[0]
        rules = []
        for check in workflow_line[1][:-1].split(","):
            if ':' in check:
                condstr, section = check.split(':')
                if '>' in condstr:
                    var, val = condstr.split(">")
                    val = int(val)
                    condition = lambda part, var=var, val=val: part[var] > val
                else:
                    var, val = condstr.split("<")
                    val = int(val)
                    condition = lambda part, var=var, val=val: part[var] < val
            else:
                condition = lambda _: True
                section = check
            rules.append((condition, section))
        workflows[name] = rules
    for part_line in part_lines:
        assignments = part_line[1:-1].split(',')
        part = {}
        for assignment in assignments:
            assignment = assignment.split('=')
            part[assignment[0]] = int(assignment[1])
        parts.append(part)

    return sum(sum(part.values()) for part in parts if accepts(workflows, 'in', part))


print(solve(read_input(day=19)))