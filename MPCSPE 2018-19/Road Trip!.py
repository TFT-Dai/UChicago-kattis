#https://uchicago.kattis.com/problems/roadtrip2

N, R, H, M, S = list(map(int, input().split()))
cities = []
for i in range(N):
    cities.append({'s': 0, 't': 0, 'v': -1})
time = [[-1] * N for i in range(N)]
for city in cities:
    num, city['s'], city['t'] = list(input().split())
    city['t'] = int(city['t'])
for i in range(R):
    a, b, d = list(map(int, input().split()))
    time[a][b] = time[b][a] = d
T = cities[S]['t']
cities[S]['v'] = T
route = [S]
while T < M:
    new = -1
    new_t = 2 ** 32
    for i in range(N):
        flag1 = time[S][i] == -1
        flag2 = cities[i]['v'] != -1 and T + time[S][i] < H + cities[i]['v']
        flag3 = T + time[S][i] + cities[i]['t'] > M
        if not (flag1 or flag2 or flag3):
            if time[S][i] < new_t:
                new = i
                new_t = time[S][i]
    if new == -1:
        break
    T += new_t + cities[new]['t']
    cities[new]['v'] = T
    S = new
    route.append(new)
for i in range(len(route) - 1):
    print(cities[route[i]]['s'], end=' ')
print(cities[route[len(route) - 1]]['s'])
print(T)
