# Models have not been improving that much, their harness is doing all the work

**Binding Constraint thesis.**
Recent Model have seen poor or not much improvement in their weight capabilities/reasoning but most of the testbench score increase comes from the harness used along with the model.
Older and smaller models often rank better (way better) than their previous score without a harness and sometime better than newer models.
Paper: https://arxiv.org/pdf/2605.23950

Other papers related:
https://arxiv.org/abs/2603.28052
https://arxiv.org/abs/2606.09498 (crazy 132% gain on modifying their harness to their needs)

2. Real-World Head-to-Head Comparisons
When looking at these frameworks applied to older vs. newer models, the industry data heavily mirrors the arXiv literature:

| Baseline Model Pairings                                                                  | Harness Setup                                                       | Benchmark Performance / Cost Shift                                                                                                                                                       |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Older/Smaller Model:** Nemotron 3 Ultra  <br>**Newer Frontier Model:** Gemini/Opus 4.8 | Customized LangChain Harness vs. Generic New Model Scaffolding      | **Nemotron 3 Ultra surged to within 1 point** of the newer flagship model. It achieved this at **1/10th the token cost** ($4.48 vs $43.48) purely by swapping the framework scaffolding. |
| **Same Base Model:** (e.g., GPT-5.6 variant)                                             | Retained Reasoning & Context Compaction flags enabled vs. Stock API | On the tough `ARC-AGI-3` benchmark, toggling harness-level runtime controls **tripled the score** and **reduced output tokens by 6x** without altering a single base model weight.       |