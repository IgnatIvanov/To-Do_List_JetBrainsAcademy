def select_dates(potential_dates):
    answer = ''
    for user in potential_dates:
        if user.get('age') > 30 and 'art' in user.get('hobbies') and user.get('city') == 'Berlin':
            if len(answer) > 1:
                answer += ', '

            answer += user.get('name')

    return answer
