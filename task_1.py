string = '1h 45m,360s,25m,30m 120s,2h 60s'
result_in_seconds = 0
time_values = list(map(lambda i: i.split(' '), string.split(',')))

for time_value in time_values:
    for value in time_value:
        if 'h' in value:
            result_in_seconds += int(value[:-1]) * 3600
        elif 'm' in value:
            result_in_seconds += int(value[:-1]) * 60
        else:
            result_in_seconds += int(value[:-1])

result_in_minutes = result_in_seconds // 60
print(result_in_minutes)


# # alternative way to solve the task
# string = '1h 45m,360s,25m,30m 120s,2h 60s'
# result_in_seconds = 0
# time_map = {
#     'h': 3600,
#     'm': 60,
#     's': 1
# }

# time_values = list(map(lambda i: i.split(' '), string.split(',')))

# for time_value in time_values:
#     result_in_seconds += sum(map(lambda i: int(i[:-1]) * time_map[i[-1]], time_value))

# print(result_in_seconds // 60)