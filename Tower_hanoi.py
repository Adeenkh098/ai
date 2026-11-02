from collections import deque

def get_valid_moves(state):
    moves = []
    for i in range(3):
        if not state[i]:
            continue  # peg i is empty
        disk = state[i][-1]  # top disk
        for j in range(3):
            if i == j:
                continue

            if not state[j] or state[j][-1] > disk:
                # Create new state
                new_state = list(list(peg) for peg in state)
                new_state[i].pop()
                new_state[j].append(disk)
                moves.append(tuple(tuple(peg) for peg in new_state))
    return moves

def solve_hanoi_bfs(n):
    # Initial state: all n disks on peg 0 (largest to smallest from bottom to top)
    initial_state = (tuple(range(n, 0, -1)), (), ())
    goal_state = ((), (), tuple(range(n, 0, -1)))
    
    queue = deque([(initial_state, [initial_state])])
    visited = {initial_state}
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path
        
        for next_state in get_valid_moves(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))


# Example usage for 3 disks:
solution_path = solve_hanoi_bfs(3)
print(f"Total steps: {len(solution_path) - 1}")
for step, st in enumerate(solution_path):
    print(f"Step {step}: {st}")