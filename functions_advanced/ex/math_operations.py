def math_operations(*args, a, s, d, m):
    for idx in range(len(args)):
        if idx % 4 == 0:
            a += args[idx]
        elif idx % 4 == 1:
            s -= args[idx]
        elif idx % 4 == 2:
            if args[idx] == 0:
                continue
            d /= args[idx]
        elif idx % 4 == 3:
            m *= args[idx]
    results = {
        "a": a,
        "s": s,
        "d": d,
        "m": m,
    }

    sorted_results = dict(sorted(results.items(), key=lambda x: ((-x[1]), x[0])))
    final_results = ""
    for key, value in sorted_results.items():
        final_results += f"{key}: {value:.1f}\n"
    return final_results


print(math_operations(6.0, a=0, s=0, d=5, m=0))