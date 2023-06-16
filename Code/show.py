import json
import matplotlib.pyplot as plt
import statistics as stat

with open('result_genetic_10.json', 'r') as fp:
    d = json.load(fp)
    for key, values in d.items():
        minimun = min([values[str(i)]['best_fit'] for i in range(3)])
        is_cubic = False
        if minimun == 0 or minimun == 0.0:
            is_cubic = True
        print('Case: ', key, ', Is Cubic: ', is_cubic)

with open('result_genetic_10.json', 'r') as fp:
    d = json.load(fp)
    sum_lines = []    
    for key, values in d.items():
        minimun = min([values[str(i)]['best_fit'] for i in range(3)])
        is_cubic = False
        if minimun == 0 or minimun == 0.0:
            is_cubic = True
            for i in range(3):
                line = values[str(i)]['line']
                sum_lines.append(len(line))                
                plt.plot(line)
    plt.show()
print(stat.mean(sum_lines))
print(stat.stdev(sum_lines))