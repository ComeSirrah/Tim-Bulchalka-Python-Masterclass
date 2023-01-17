text = "hello world"

sentence = []
output = []
for x in text.split():
    output.append(len(x))
print(output)


answer = [(x, len(x)) for x in text.split()]
print(answer)

inch_measurement = (3, 8, 20)

cm_measurement = [(n * 2.54) for n in inch_measurement]
cm_measurement2 = tuple([(n * 2.54) for n in inch_measurement])
print(cm_measurement)
print(cm_measurement2)
