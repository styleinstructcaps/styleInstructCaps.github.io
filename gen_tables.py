#!/usr/bin/env python3
import os

def shade(val, col_vals, higher_better=True, color=(0, 102, 204)):
    if val is None:
        return ""
    nums = [v for v in col_vals if v is not None]
    if not nums:
        return ""
    lo, hi = min(nums), max(nums)
    if hi == lo:
        t = 1.0
    else:
        t = (val - lo) / (hi - lo) if higher_better else (hi - val) / (hi - lo)
    t = max(0, min(1, t))
    a = 0.12 + 0.48 * t
    return f' style="background:rgba({color[0]},{color[1]},{color[2]},{a:.3f})"'


def main():
    os.makedirs("partials", exist_ok=True)

    t1_rows = [
        ("Oracle Caption (PSC)", [9.93, 0.069, 99.5, 0.5, 0, None, None], "oracle"),
        ("Oracle caption (SIC-DB)", [9.93, 0.036, 99.8, 0.2, 0, 8.48, 71.3], "oracle"),
        ("Audio-Flamingo-3", [5.69, 6.07, 15.4, 20.7, 63.8, 8.21, 62.4], ""),
        ("Voxtral-Mini-3B", [7.56, 3.12, 48.6, 35.0, 16.4, 8.15, 68.0], ""),
        ("Voxtral-Small-24B", [7.20, 1.58, 73.5, 16.8, 9.68, 7.51, 67.8], ""),
        ("Qwen2-Audio-7B-Instruct", [5.73, 5.58, 19.1, 27.9, 53.0, 6.58, 53.6], ""),
        ("MERaLiON-AudioLLM", [6.57, 1.25, 81.8, 10.6, 7.60, 6.11, 27.7], ""),
        ("MOSS-Audio", [9.10, 4.54, 21.8, 45.4, 32.7, 8.82, 82.8], ""),
        ("Qwen3-Omni", [6.77, 2.85, 51.2, 30.6, 18.2, 7.99, 74.0], ""),
        ("Audio-Flamingo-next", [9.18, 4.82, 19.35, 38.94, 41.7, 7.59, 48.5], ""),
        ("SALMONN", [7.85, 3.63, 42.1, 28.3, 29.5, 7.50, 58.5], ""),
        ("SALMONN (PSC)", [9.24, 4.77, 21.2, 46.3, 32.5, 7.98, 52.9], "ours"),
        ("SALMONN (SIC-DB) - ST", [9.32, 3.88, 35.2, 37.3, 27.4, 8.37, 65.6], "ours"),
        ("SALMONN (SIC-DB) - MT", [9.32, 3.43, 41.3, 38.2, 20.5, 8.62, 75.0], "ours"),
    ]
    hb = [True, False, True, False, False, True, True]
    cols = list(zip(*[r[1] for r in t1_rows]))
    fmts = ["{:.2f}", "{:.2f}", "{:.1f}", "{:.1f}", "{:.1f}", "{:.2f}", "{:.1f}"]
    with open("partials/table1_body.html", "w") as f:
        for name, vals, cls in t1_rows:
            tr_cls = f' class="{cls}"' if cls else ""
            f.write(f"          <tr{tr_cls}>\n")
            f.write(f'            <th scope="row">{name}</th>\n')
            for i, v in enumerate(vals):
                if v is None:
                    f.write('            <td class="num">—</td>\n')
                else:
                    s = shade(v, cols[i], hb[i])
                    f.write(f'            <td class="num"{s}>{fmts[i].format(v)}</td>\n')
            f.write("          </tr>\n")

    t2_rows = [
        ("Audio-Flamingo-3", [0.009, 0.046, 0.100, 0.046, 0.476, 0.532, 0.011, 0.048, 0.121, 0.057, 0.463, 0.556], ""),
        ("Voxtral-Mini-3B", [0.033, 0.122, 0.152, 0.133, 0.399, 0.643, 0.003, 0.028, 0.103, 0.063, 0.486, 0.519], ""),
        ("Voxtral-Small-24B", [0.067, 0.182, 0.186, 0.157, 0.363, 0.674, 0.011, 0.052, 0.119, 0.076, 0.480, 0.532], ""),
        ("Qwen2-Audio-7B-Instruct", [-0.002, 0.010, 0.072, 0.026, 0.498, 0.499, -0.002, 0.007, 0.083, 0.025, 0.496, 0.498], ""),
        ("MERaLiON-AudioLLM", [0.081, 0.276, 0.213, 0.233, 0.428, 0.604, 0.039, 0.146, 0.167, 0.169, 0.476, 0.534], ""),
        ("MOSS-Audio", [0.191, 0.381, 0.347, 0.221, 0.282, 0.792, 0.076, 0.228, 0.186, 0.175, 0.319, 0.755], ""),
        ("Qwen3-Omni", [0.152, 0.297, 0.243, 0.204, 0.376, 0.630, 0.069, 0.216, 0.184, 0.165, 0.311, 0.734], ""),
        ("Audio-Flamingo-next", [0.113, 0.318, 0.242, 0.227, 0.348, 0.717, 0.086, 0.264, 0.187, 0.212, 0.385, 0.673], ""),
        ("SALMONN", [0.351, 0.598, 0.511, 0.290, 0.225, 0.854, 0.145, 0.324, 0.303, 0.205, 0.320, 0.749], ""),
        ("SALMONN (PSC)", [0.297, 0.541, 0.491, 0.271, 0.231, 0.861, 0.157, 0.340, 0.312, 0.209, 0.320, 0.711], "ours"),
        ("SALMONN (SIC-DB) - ST", [0.363, 0.577, 0.508, 0.284, 0.214, 0.876, 0.145, 0.324, 0.303, 0.205, 0.320, 0.749], "ours"),
        ("SALMONN (SIC-DB) - MT", [0.357, 0.590, 0.517, 0.279, 0.212, 0.876, 0.156, 0.341, 0.298, 0.222, 0.282, 0.795], "ours"),
    ]
    hb2 = [True, True, True, True, False, True] * 2
    cols2 = list(zip(*[r[1] for r in t2_rows]))
    with open("partials/table2_body.html", "w") as f:
        for name, vals, cls in t2_rows:
            tr_cls = f' class="{cls}"' if cls else ""
            f.write(f"          <tr{tr_cls}>\n")
            f.write(f'            <th scope="row">{name}</th>\n')
            for i, v in enumerate(vals):
                s = shade(v, cols2[i], hb2[i], color=(220, 53, 69))
                f.write(f'            <td class="num"{s}>{v:.3f}</td>\n')
            f.write("          </tr>\n")


if __name__ == "__main__":
    main()
