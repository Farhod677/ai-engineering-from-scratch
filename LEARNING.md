# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission
I want to ship an AI product, change careers, understand the tools I already use daily, and do research (all of the options). By the end, I want to build some kind of AI SaaS.

## Placement
- Date: 2026-11-02
- Score: self-selected
- Entry point: Phase 0: Setup & Tooling
- Pace: ~3–4 hours/week
- Previous placement quiz: 10/10 (2/2 in each area). Chose to complete the full curriculum from Phase 0.

## Path
| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Do | 16 |
| 1 | Math Foundations | Do | 23 |
| 2 | ML Fundamentals | Do | 26 |
| 3 | Deep Learning Core | Do | 15 |
| 4 | Computer Vision | Do | 27 |
| 5 | NLP | Do | 30 |
| 6 | Speech & Audio | Do | 18 |
| 7 | Transformers Deep Dive | Do | 14 |
| 8 | Generative AI | Do | 14 |
| 9 | Reinforcement Learning | Do | 13 |
| 10 | LLMs from Scratch | Do | 26 |
| 11 | LLM Engineering | Do | 19 |
| 12 | Multimodal AI | Do | 65 |
| 13 | Tools & Protocols | Do | 76 |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 34 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

Your personalized path: ~1,170 hours across 20 phases. Estimates come from the individual phase headings in ROADMAP.md and include 620 hours for Capstone Projects. At 3–4 hours/week, the full path is approximately 292–390 weeks; individual lessons and artifacts provide milestones along the way.

## Progress log
| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-11-02 | 00-setup-and-tooling/01-dev-environment | 2/3 | Created and activated .venv with Python 3.14.6; installed NumPy and verified dot product 14. Understands interpreter isolation and PATH; review system foundation before runtimes. Beginner preflight passed 2/2; GPU access was discussed, not tested. |

| 2026-11-02 | 00-setup-and-tooling/02-git-and-collaboration | 3/3 | Warm-up 2/2; correctly predicted staging snapshots and branch behavior. Staged and committed LEARNING.md on my-progress, pushed to own fork, and verified existing checkpoint ignore rules. Understands that ignore rules do not remove tracked history. |

| 2026-11-03 | 00-setup-and-tooling/03-gpu-setup-and-cloud | 2/3 | Warm-up 2/2; verified M1 Pro GPU (14 cores), 16 GiB unified memory, and PyTorch 2.15.0 MPS access. Ran identity matmul on mps:0; warmed 4000x4000 benchmark medians: CPU 0.0686s, MPS 0.0353s (1.94x). Learned dispatch overhead, batching, synchronization, identity multiplication, and fp16 weight estimates; initially assumed GPU always wins and overhead per matrix increases with batching. Missed NVIDIA status command; review nvidia-smi. |

| 2026-11-03 | 00-setup-and-tooling/04-apis-and-keys | 3/3 | Warm-up 1/2; confused VRAM with swap, then reviewed dedicated versus unified memory. Completed live raw HTTP request using learning-artifacts/00-04-apis-and-keys/first_request.py; reported 21 input tokens, 52 output tokens, and end_turn. Understands backend key storage, explicit .env loading, headers/body, JSON encoding, SDK request construction and parsing, and 401 versus 429. Initially mistook a nonempty environment variable for a valid key; corrected after feedback. SDK comparison discussed, not run. |

| 2026-11-03 | 00-setup-and-tooling/05-jupyter-notebooks | 3/3 | Warm-up 2/2. Ran notebook cells; screenshot confirmed edited assignment left kernel value unchanged. Reported 100 after restart and run all. Initially confused editing with execution and expected variables to survive restart; later correctly explained that deleting a cell leaves its variables in memory. Reported list timing 3.11 ms versus NumPy 30.6 us (about 102x faster), and a single-run %%time result with sum 333328333350000. Correctly chose notebooks for exploration and scripts for scheduled jobs. |

| 2026-11-03 | 00-setup-and-tooling/06-python-environments | 3/3 | Warm-up 2/2. Reported matching project Python and pip paths; created and activated learning-artifacts/00-06-python-environments/isolated-env, confirmed NumPy absent before installation, then reported NumPy 2.5.4 installed inside its site-packages. Saved requirements.txt containing numpy==2.5.4. Correctly explained package isolation and activation; initially thought numpy>=2.5 guaranteed identical versions, then distinguished ranges from exact pins. Conda tracking and NVIDIA build/driver compatibility discussed; uv, Conda, and setup script not run. |

## Review queue

- 00-setup-and-tooling/01-dev-environment — Review bottom-up environment setup: system foundation, package managers, language runtimes, AI libraries. Quiz: 2/3 (67%).
- 00-setup-and-tooling/03-gpu-setup-and-cloud — Review NVIDIA hardware status via nvidia-smi versus PyTorch runtime availability checks; reinforce dispatch overhead per matrix when batching. Quiz: 2/3 (67%).
