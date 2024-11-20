team1_num = 5
team2_num = 6

print('В команде мастера кода участников: %s !' % team1_num)
print('В команде мастера кода участников: %s и %s !' % (team1_num ,team2_num))

score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} c!'.format(team1_time))


print(f'Команды решили {score_1} и {score_2} задач')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print('Победа команды Мастера кода')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print('Победа команды Волшебники Данных!')
else:
    print('Ничья')

task_total = score_1 + score_2
time_avg = (team1_time + team2_time)/(score_1 + score_2)

print(f'Сегодня было решено {task_total} задач, в среднем по {round(time_avg,1)} секунды на задачу!')