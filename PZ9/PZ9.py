
#Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15',
# отражающая средние температуры по месяцам в году. Преобразовать информацию из строки в словарь,
# с использованием функции найти среднюю и минимальные температуры, результаты вывести на экран.
import statistics

def analyze_temperatures(temperature_string):
    parts = temperature_string.split(' -')
    year = int(parts[0].replace('год', ''))
    temperatures = [int(temp) for temp in parts[1].split()]

    average_temperature = statistics.mean(temperatures)
    min_temperature = min(temperatures)

    result = {
        'year': year,
        'temperatures': temperatures,
        'average_temperature': average_temperature,
        'min_temperature': min_temperature
    }
    return result
temperature_string = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
analysis_result = analyze_temperatures(temperature_string)

print(f"Год: {analysis_result['year']}")
print(f"Температуры по месяцам: {analysis_result['temperatures']}")
print(f"Средняя температура: {analysis_result['average_temperature']}")
print(f"Минимальная температура: {analysis_result['min_temperature']}")
