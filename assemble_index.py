#!/usr/bin/env python3
"""Assemble index.html from template and table partials."""
from pathlib import Path

ROOT = Path(__file__).parent
t1 = (ROOT / "partials/table1_body.html").read_text()
t2 = (ROOT / "partials/table2_body.html").read_text()

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="StyleInstructCaps — instruction-following speaking-style captioning benchmark for audio language models.">
  <title>StyleInstructCaps</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <nav class="site-nav" aria-label="Main">
    <div class="container inner">
      <a class="brand" href="#">StyleInstructCaps</a>
      <ul class="links">
        <li><a href="#overview">Overview</a></li>
        <li><a href="#figure">Figure</a></li>
        <li><a href="#benchmark">Benchmark</a></li>
        <li><a href="#results">Results</a></li>
      </ul>
    </div>
  </nav>

  <header class="hero">
    <div class="container">
      <h1>StyleInstructCaps</h1>
      <p class="tagline">Instruction-Following Speaking-Style Captioning for Audio Language Models</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="https://github.com/styleinstructcaps/StyleInstructCaps" target="_blank" rel="noopener noreferrer">GitHub</a>
        <a class="btn btn-secondary" href="https://huggingface.co/datasets/StyleInstructCaps/StyleInstructCapsDB" target="_blank" rel="noopener noreferrer">Hugging Face Dataset</a>
      </div>
    </div>
  </header>

  <main>
    <section id="overview">
      <div class="container">
        <h2>Overview</h2>
        <p class="lead">
          <strong>StyleInstructCaps</strong> is a large-scale benchmark for <em>instruction-following speaking-style captioning</em>
          with audio language models. We release <strong>StyleInstructCapsDB</strong> on Hugging Face — over one million
          utterances with rich style captions, six evaluation subsets, and an official toolkit spanning eight evaluation axes:
          metadata groundedness, hallucination, instruction following, speaker verification, speaker consistency,
          unseen-dataset generalization, out-of-domain prompts, and multi-model clustering analysis.
        </p>
        <p class="lead" style="margin-top: 1rem;">
          Audio is not redistributed; each row provides a <code>relative_audio_path</code> resolved against upstream corpora
          (Emilia, VoxCeleb, VCTK, EARS, Expresso, GigaSpeech). Evaluation uses Qwen3-32B as LLM-as-judge and e5-base-v2 for speaker metrics.
        </p>

        <div class="stats-grid">
          <div class="stat-card">
            <div class="value">1.05M+</div>
            <div class="label">Training utterances</div>
          </div>
          <div class="stat-card">
            <div class="value">6</div>
            <div class="label">Evaluation subsets</div>
          </div>
          <div class="stat-card">
            <div class="value">8</div>
            <div class="label">Evaluation axes</div>
          </div>
          <div class="stat-card">
            <div class="value">CC BY-NC 4.0</div>
            <div class="label">License</div>
          </div>
        </div>
      </div>
    </section>

    <section id="figure">
      <div class="container">
        <h2>Benchmark Overview</h2>
        <div class="figure-wrap">
          <img src="assets/StyleinstructCaps_fig_v2.png" alt="StyleInstructCaps benchmark overview figure">
          <a class="pdf-link" href="StyleinstructCaps_fig_v2.pdf">Open the figure as PDF</a>
          <p class="figure-caption">
            Overview of the StyleInstructCaps benchmark: dataset construction, instruction-following style captioning,
            and multi-axis evaluation on StyleInstructCaps-MetaSet and speaker-consistency splits.
          </p>
        </div>
      </div>
    </section>

    <section id="benchmark">
      <div class="container">
        <h2>Evaluation Toolkit</h2>
        <p class="lead">
          The <a href="https://github.com/styleinstructcaps/StyleInstructCaps">official evaluation repository</a>
          provides standalone scripts for all eight axes. Load subsets from
          <a href="https://huggingface.co/datasets/StyleInstructCaps/StyleInstructCapsDB">StyleInstructCaps/StyleInstructCapsDB</a>:
        </p>
        <div class="axes-table-wrap">
          <table class="axes-table">
            <thead>
              <tr>
                <th>Axis</th>
                <th>Metric</th>
                <th>Dataset config</th>
              </tr>
            </thead>
            <tbody>
              <tr><td>1</td><td>Metadata groundedness</td><td><code>StyleInstructCaps-MetaSet</code></td></tr>
              <tr><td>2</td><td>Hallucination</td><td><code>StyleInstructCaps-MetaSet</code></td></tr>
              <tr><td>3</td><td>Instruction following</td><td><code>StyleInstructCaps-MetaSet</code></td></tr>
              <tr><td>4</td><td>Speaker caption verification</td><td><code>VCTK_speaker_prompts</code></td></tr>
              <tr><td>5</td><td>Speaker consistency</td><td><code>VCTK_speaker_prompts</code></td></tr>
              <tr><td>6</td><td>Unseen eval (groundedness + hallucination + IF)</td><td><code>Gigaspeech_SpeechCraft_captions</code></td></tr>
              <tr><td>7</td><td>OOD prompt analysis (IF only)</td><td><code>VCTK_unseen_prompts</code></td></tr>
              <tr><td>8</td><td>Speaker description consistency (clustering plots)</td><td><code>VCTK_speaker_prompts</code> (multi-model)</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section id="results">
      <div class="container">
        <h2>Main Results</h2>

        <div class="table-section" id="table1">
          <h3>Table 1</h3>
          <p class="table-caption">
            Metadata groundedness, hallucination severity, and instruction-following performance evaluated on
            <em>StyleInstructCaps-MetaSet</em>. Blue shading indicates relative performance for scalar metrics.
          </p>
          <div class="table-scroll">
            <table class="results-table table-blue">
              <thead>
                <tr>
                  <th rowspan="2">Model</th>
                  <th colspan="2">LLM metadata groundedness</th>
                  <th colspan="3">LLM hallucination severity (%)</th>
                  <th colspan="2">Instruction following</th>
                </tr>
                <tr>
                  <th>Meta score ↑</th>
                  <th>Hall. ↓</th>
                  <th>Low</th>
                  <th>Mid</th>
                  <th>High</th>
                  <th>IFA score ↑</th>
                  <th>IFA rate (%) ↑</th>
                </tr>
              </thead>
              <tbody>
TABLE1_BODY
              </tbody>
            </table>
          </div>
        </div>

        <div class="table-section" id="table2">
          <h3>Table 2</h3>
          <p class="table-caption">
            Speaker-style consistency evaluation using clustering and verification metrics on the ID-balanced and UD-VCTK sets.
            Darker shading indicates better performance per column. Higher is better for ARI, NMI, Purity, InterSep, and AUC;
            lower is better for EER.
          </p>
          <div class="table-scroll">
            <table class="results-table table-red">
              <thead>
                <tr>
                  <th rowspan="2">Model</th>
                  <th colspan="6">ID-balanced</th>
                  <th colspan="6">UD-VCTK</th>
                </tr>
                <tr>
                  <th>ARI ↑</th>
                  <th>NMI ↑</th>
                  <th>Purity ↑</th>
                  <th>InterSep ↑</th>
                  <th>EER ↓</th>
                  <th>AUC ↑</th>
                  <th>ARI ↑</th>
                  <th>NMI ↑</th>
                  <th>Purity ↑</th>
                  <th>InterSep ↑</th>
                  <th>EER ↓</th>
                  <th>AUC ↑</th>
                </tr>
              </thead>
              <tbody>
TABLE2_BODY
              </tbody>
            </table>
          </div>
        </div>

        <div class="table-section" id="table3">
          <h3>Table 3</h3>
          <p class="table-caption">
            Speaker description verification results on VCTK (10 prompts per speaker). Higher AUC is better; lower EER and minDCF are better.
          </p>
          <div class="table-scroll">
            <table class="results-table">
              <thead>
                <tr>
                  <th>Model</th>
                  <th>EER ↓</th>
                  <th>AUC ↑</th>
                  <th>minDCF ↓</th>
                </tr>
              </thead>
              <tbody>
                <tr><th scope="row">Audio-Flamingo-3</th><td class="num">0.462917</td><td class="num">0.556000</td><td class="num">0.025563</td></tr>
                <tr><th scope="row">Voxtral-Mini-3B</th><td class="num">0.485625</td><td class="num">0.519186</td><td class="num">0.009994</td></tr>
                <tr><th scope="row">Voxtral-Small-24B</th><td class="num">0.479792</td><td class="num">0.531450</td><td class="num">0.010206</td></tr>
                <tr><th scope="row">Qwen2-Audio-7B-Instruct</th><td class="num">0.496250</td><td class="num">0.497724</td><td class="num">0.048633</td></tr>
                <tr><th scope="row">MERaLiON-AudioLLM</th><td class="num">0.476250</td><td class="num">0.534108</td><td class="num">0.023596</td></tr>
                <tr><th scope="row">MOSS-Audio</th><td class="num">0.319375</td><td class="num">0.755114</td><td class="num">0.010185</td></tr>
                <tr><th scope="row">Qwen3-Omni</th><td class="num">0.311250</td><td class="num">0.734208</td><td class="num">0.010396</td></tr>
                <tr><th scope="row">Audio-Flamingo-next</th><td class="num">0.384583</td><td class="num">0.673539</td><td class="num">0.031281</td></tr>
                <tr><th scope="row">SALMONN</th><td class="num">0.320417</td><td class="num">0.749198</td><td class="num">0.009960</td></tr>
                <tr class="ours"><th scope="row">SALMONN (PSC)</th><td class="num">0.281667</td><td class="num">0.795312</td><td class="num">0.010169</td></tr>
                <tr class="ours"><th scope="row">SALMONN (SIC-DB) - ST</th><td class="num">0.264375</td><td class="num">0.831516</td><td class="num">0.009898</td></tr>
                <tr class="ours"><th scope="row">SALMONN (SIC-DB) - MT</th><td class="num">0.281667</td><td class="num">0.795312</td><td class="num">0.010169</td></tr>
              </tbody>
            </table>
          </div>
        </div>

        <div class="table-section" id="speakerConsistencyFigure">
          <h3>Speaker description consistency (Axis 8)</h3>
          <p class="table-caption">
            t-SNE visualization for multi-model speaker clustering on VCTK. This axis evaluates whether speaker descriptions remain consistent across prompts and examples.
          </p>
          <div class="figure-wrap">
            <img src="assets/tsne_all_speakers_doublecol_12.png" alt="t-SNE plot: all speakers (double column)">
            <a class="pdf-link" href="tsne_all_speakers_doublecol_12.pdf">Open the plot as PDF</a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>
        StyleInstructCaps &middot;
        <a href="https://huggingface.co/datasets/StyleInstructCaps/StyleInstructCapsDB">Dataset</a> &middot;
        <a href="https://github.com/styleinstructcaps/StyleInstructCaps">Code</a>
      </p>
      <p>Released under <a href="https://creativecommons.org/licenses/by-nc/4.0/">CC BY-NC 4.0</a>.</p>
      <p style="margin-top: 12px; font-size: 12px; opacity: 0.85;">
        Website design inspired by
        <a href="https://speechparaling-bench.github.io">SpeechParaling-Bench</a> and
        <a href="https://plnguyen2908.github.io/AV-SpeakerBench-project-page/">AV-SpeakerBench</a>.
      </p>
    </div>
  </footer>
</body>
</html>
"""

out = HTML.replace("TABLE1_BODY", t1.rstrip()).replace("TABLE2_BODY", t2.rstrip())
(ROOT / "index.html").write_text(out)
print("Wrote index.html", len(out), "bytes")
