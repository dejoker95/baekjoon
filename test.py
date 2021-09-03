def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cam = -30001

    for r in routes:
        if cam < r[0]:
            answer += 1
            cam = r[1]
    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))