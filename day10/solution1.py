signals = list(map(lambda x: x.split(" "), open("input.txt").read().split("\n")))
cycle_count = 0
x = 1
signal_strength_sum = 0
markers = [20, 60, 100, 140, 180, 220]

for signal in signals:
    if cycle_count in markers:
        signal_strength_sum += cycle_count * x
        markers.remove(cycle_count) # remove marker to avoid double counting

    if signal[0] == "noop":
        cycle_count += 1
    elif signal[0] == "addx":
        for _ in range(2):
            cycle_count += 1
            if cycle_count in markers:
                signal_strength_sum += cycle_count * x
                markers.remove(cycle_count) # remove marker to avoid double counting
        x += int(signal[1])


print(signal_strength_sum)
