import random

def get_next_move(state, game):
    directions = {'up', 'down', 'left', 'right'}
    
    board_width = game.get('board', {}).get('width')
    assert board_width is not None, '.board.width not found'

    board_height = game.get('board', {}).get('height')
    assert board_height is not None, '.board.height not found'

    body = game.get('you', {}).get('body')
    assert body is not None, '.you.body not found'
    assert len(body) > 0, '.you.body is empty'

    head_x = body[0].get('x')
    assert head_x is not None, '.you.body[0].x not found'

    head_y = body[0].get('y')
    assert head_y is not None, '.you.body[0].y not found'

    snakes = game.get('board', {}).get('snakes')
    assert snakes is not None, '.board.snakes not found'

    '''
    collision with wall
    '''
    # right
    next_x = head_x + 1
    next_y = head_y
    if collides_with_wall(next_x, next_y, board_width, board_height):
        directions.discard('right')

    # left
    next_x = head_x - 1
    next_y = head_y
    if collides_with_wall(next_x, next_y, board_width, board_height):
        directions.discard('left')

    # down
    next_x = head_x
    next_y = head_y + 1
    if collides_with_wall(next_x, next_y, board_width, board_height):
        directions.discard('down')

    # up
    next_x = head_x
    next_y = head_y - 1
    if collides_with_wall(next_x, next_y, board_width, board_height):
        directions.discard('up')

    '''
    collision with self
    '''
    # right
    next_x = head_x + 1
    next_y = head_y
    if collides_with_body(next_x, next_y, body):
        directions.discard('right')

    # left
    next_x = head_x - 1
    next_y = head_y
    if collides_with_body(next_x, next_y, body):
        directions.discard('left')

    # down
    next_x = head_x
    next_y = head_y + 1
    if collides_with_body(next_x, next_y, body):
        directions.discard('down')

    # up
    next_x = head_x
    next_y = head_y - 1
    if collides_with_body(next_x, next_y, body):
        directions.discard('up')

    '''
    collision with other snakes
    '''
    for i, snake in enumerate(snakes):
        snake_body = snake.get('body')
        assert snake_body is not None, f'.board.snakes[{i}].body not found'
        # right
        next_x = head_x + 1
        next_y = head_y
        if collides_with_body(next_x, next_y, snake_body):
            directions.discard('right')
        # left
        next_x = head_x - 1
        next_y = head_y
        if collides_with_body(next_x, next_y, snake_body):
            directions.discard('left')
        # down
        next_x = head_x
        next_y = head_y + 1
        if collides_with_body(next_x, next_y, snake_body):
            directions.discard('down')
        # up
        next_x = head_x
        next_y = head_y - 1
        if collides_with_body(next_x, next_y, snake_body):
            directions.discard('up')

    # stuck in a corner
    if not directions:
        print('WARNING: Stuck!')
        direction = 'up'
    elif len(directions) == 1:
        direction = directions.pop()
    else:
        direction = choose_random_avoid_food_until_hungry(directions, head_x, head_y, game)

    return direction

def collides_with_wall(x, y, width, height):
    if x >= width or x < 0 or y >= height or y < 0:
        return True
    else:
        return False

def collides_with_body(x, y, body):
    for i, segment in enumerate(body):
        segment_x = segment.get('x')
        assert segment_x is not None, f'.you.body[{i}].x not found'
        segment_y = segment.get('y')
        assert segment_y is not None, f'.you.body[{i}].y not found'
        if x == segment_x and y == segment_y:
            return True
    return False

def collides_with_food(x, y, food):
    for i, bite in enumerate(food):
        bite_x = bite.get('x')
        assert bite_x is not None, f'.board.food[{i}].x not found'
        bite_y = bite.get('y')
        assert bite_y is not None, f'.board.food[{i}].y not found'
        if x == bite_x and y == bite_y:
            return True
    return False

def choose_random_direction(directions, x, y, game):
    return random.choice(list(directions))

def choose_closest_food(directions, x, y, game):
    # find closest food
    food = game.get('board', {}).get('food')
    assert food is not None, '.board.food not found'
    shortest_distance = float('inf')
    closest_x = None
    closest_y = None
    for i, bite in enumerate(food):
        bite_x = bite.get('x')
        assert bite_x is not None, f'.board.food[{i}].x not found'
        bite_y = bite.get('y')
        assert bite_y is not None, f'.board.food[{i}].y not found'
        distance = ((bite_x - x) ** 2) + ((bite_y - y) ** 2)
        if distance < shortest_distance:
            shortest_distance = distance
            closest_x = bite_x
            closest_y = bite_y

    # same column
    if closest_x == x and closest_y > y and 'down' in directions:
        return 'down'
    if closest_x == x and closest_y < y and 'up' in directions:
        return 'up'
    
    # same row
    if closest_x > x and closest_y == y and 'right' in directions:
        return 'right'
    if closest_x < x and closest_y == y and 'left' in directions:
        return 'left'
    
    # top left
    if closest_x <= x and closest_y <= y and ('left' in directions or 'up' in directions):
        if ('left' in directions) and ('up' in directions):
            x_distance = abs(closest_x - x)
            y_distance = abs(closest_y - y)
            if x_distance < y_distance:
                return 'left'
            if y_distance < x_distance:
                return 'up'
            return random.choice(['left', 'up'])
        elif 'left' in directions:
            return 'left'
        elif 'up' in directions:
            return 'up'
    
    # top right
    if closest_x >= x and closest_y <= y and ('right' in directions or 'up' in directions):
        if ('right' in directions) and ('up' in directions):
            x_distance = abs(closest_x - x)
            y_distance = abs(closest_y - y)
            if x_distance < y_distance:
                return 'right'
            if y_distance < x_distance:
                return 'up'
            return random.choice(['right', 'up'])
        elif 'right' in directions:
            return 'right'
        elif 'up' in directions:
            return 'up'
    
    # bottom left
    if closest_x <= x and closest_y >= y and ('left' in directions or 'down' in directions):
        if ('left' in directions) and ('down' in directions):
            x_distance = abs(closest_x - x)
            y_distance = abs(closest_y - y)
            if x_distance < y_distance:
                return 'left'
            if y_distance < x_distance:
                return 'down'
            return random.choice(['left', 'down'])
        elif 'left' in directions:
            return 'left'
        elif 'down' in directions:
            return 'down'
    
    # bottom right
    if closest_x >= x and closest_y >= y and ('right' in directions or 'down' in directions):
        if ('right' in directions) and ('down' in directions):
            x_distance = abs(closest_x - x)
            y_distance = abs(closest_y - y)
            if x_distance < y_distance:
                return 'right'
            if y_distance < x_distance:
                return 'down'
            return random.choice(['right', 'down'])
        elif 'right' in directions:
            return 'right'
        elif 'down' in directions:
            return 'down'
    
    return random.choice(list(directions))

def choose_random_avoid_food(directions, x, y, game):
    food = game.get('board', {}).get('food')
    assert food is not None, '.board.food not found'

    avoid_directions = set()
    '''
    collision with food
    '''
    # right
    next_x = x + 1
    next_y = y
    if collides_with_food(next_x, next_y, food):
        avoid_directions.add('right')

    # left
    next_x = x - 1
    next_y = y
    if collides_with_food(next_x, next_y, food):
        avoid_directions.add('left')

    # down
    next_x = x
    next_y = y + 1
    if collides_with_food(next_x, next_y, food):
        avoid_directions.add('down')

    # up
    next_x = x
    next_y = y - 1
    if collides_with_food(next_x, next_y, food):
        avoid_directions.add('up')
    
    best_directions = directions - avoid_directions
    if not best_directions:
        return choose_random_direction(directions, x, y, game)
    elif len(best_directions) == 1:
        return best_directions.pop()
    else:
        return random.choice(list(best_directions))

def choose_random_until_hungry(directions, x, y, game):
    health = game.get('you', {}).get('health')
    assert health is not None, '.you.health not found'
    print(f'HEALTH: {health}')
    if health < 15:
        return choose_closest_food(directions, x, y, game)
    else:
        return choose_random_direction(directions, x, y, game)

def choose_random_avoid_food_until_hungry(directions, x, y, game):
    health = game.get('you', {}).get('health')
    assert health is not None, '.you.health not found'
    print(f'HEALTH: {health}')
    if health < 15:
        return choose_closest_food(directions, x, y, game)
    else:
        return choose_random_avoid_food(directions, x, y, game)

# def think():
#     inputs = [...]
#     output = brain.predict(inputs)
#     if output < 0.25:
#         return 'up'
#     elif output < 0.5:
#         return 'down'
#     elif output < 0.75:
#         return 'left'
#     else:
#         return 'right'
