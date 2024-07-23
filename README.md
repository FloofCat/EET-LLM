# EET-LLM: Enhancing the Emotional, Empathetic and Task-Oriented Capabilities of a LLM

This repository is the official codebase for EET-LLM. We deal with the creation of an emotional, empathetic and task-oriented LLM that is favorable to make more human-centric responses and be more friendly to humans. We state the final task to be making the human emotionally happy. The working of the same can be viewed here.

> This repository is a consolidated structure of everything to do with Emotional and Empathetic LLMs. We cover all papers read, datasets, codebases discovered and more.

## List of Contents
- [EET-LLM](#eet-llm)
- [Presentation of EET-LLM @ CDAC](#presentation--cdac)
- [Literature Review](#literature-review)
  - [Papers and Publications](#papers-and-publications)
  - [Datasets](#datasets)
  - [Open-Source Code](#open-source-codes)
- [Citation](#citation)
- [Execution of EET-LLM](#execution-and-running)
- [Authors](#authors)
- [License](#license)

## EET-LLM
Here is a simplified workflow of this LLM.
![framework](https://github.com/user-attachments/assets/75007891-5912-415d-883f-ba0e1bbbaa4c)

You may also test out EET-LLM hosted via Streamlit: https://eet-llm.streamlit.app/

Any feedback and other improvements can be reported to the authors in the Issues section of this repo. If not, you may also send an email to the Authors (mentioned in the Authors section).

## Presentation @ CDAC
This work was also presented to several interns and faculties at the Centre for Development of Advanced Computing, Kolkata. This presentation was done by Advik Raj Basani.

[![Video Thumbnail](https://github.com/user-attachments/assets/d5006d98-4839-4a91-8b94-5789d4b9937f)](https://drive.google.com/file/d/1kjE41pco6gp6HdtIH6pXvRVaeHL1jbLH/view)

The same presentation can be found [here](https://drive.google.com/file/d/1f6vjsO0B6a6cC24xPqrHmi_2mSz7JRir/view?usp=sharing).

## Literature Review
### Papers and Publications
| **Year** | **Title** | **Paper** | **Institute** |
| --------- | --------- |:---------:| ---------- |
| 2023 | Emotional Intelligence of Large Language Models | [![arXiv](https://img.shields.io/badge/arXiv-2307.09042-b31b1b.svg)](https://arxiv.org/pdf/2307.09042) | Department of Psychology & Tsinghua Laboratory of Brain and Intelligence |
| 2024 | EmoLLMs: A Series of Emotional Large Language Models and Annotation Tools for Comprehensive Affective Analysis | [![arXiv](https://img.shields.io/badge/arXiv-2401.08508-b31b1b.svg)](https://arxiv.org/pdf/2401.08508) | The University of Manchester |
| 2023 | Large Language Models Understand and Can Be Enhanced by Emotional Stimuli | [![arXiv](https://img.shields.io/badge/arXiv-2307.11760-b31b1b.svg)](https://arxiv.org/pdf/2307.11760) | Microsoft, Institute of Software, CAS |
| 2023 | Towards Emotion-Based Synthetic Consciousness: Using LLMs to Estimate Emotion Probability Vectors | [![arXiv](https://img.shields.io/badge/arXiv-2310.10673-b31b1b.svg)](https://arxiv.org/pdf/2310.10673) | Warwick University |
| 2024 | Enhancing Emotional Generation Capability of Large Language Models via Emotional Chain-of-Thought | [![arXiv](https://img.shields.io/badge/arXiv-2401.06836-b31b1b.svg)](https://arxiv.org/pdf/2401.06836v2) | School of Computer Science and Technology, Harbin Institute of Technology, Shenzhen |
| 2024 | Enhancing Empathetic Response Generation by Augmenting LLMs with Small-scale Empathetic Models | [![arXiv](https://img.shields.io/badge/arXiv-rnx2--N7aojy-blue.svg)](https://openreview.net/pdf?id=rnx2-N7aojy) | Anonymous Review |
| 2023 | SoulChat: Improving LLMs’ Empathy, Listening, and Comfort Abilities through Fine-tuning with Multi-turn Empathy Conversations | [![ACL Anthology](https://img.shields.io/badge/ACL%20Anthology-2023.findings--emnlp.83-blue.svg)](https://aclanthology.org/2023.findings-emnlp.83.pdf) | Guangdong Provincial Key Laboratory of Human Digital Twin, School of EE. |
| 2022 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | [![arXiv](https://img.shields.io/badge/arXiv-2201.11903-b31b1b.svg)](https://arxiv.org/pdf/2201.11903) | Google Research, Brain Team |
| 2023 | METAAGENTS: SIMULATING INTERACTIONS OF HUMAN BEHAVIORS FOR LLM-BASED TASK-ORIENTED COORDINATION VIA COLLABORATIVE GENERATIVE AGENTS | [![arXiv](https://img.shields.io/badge/arXiv-2310.06500-b31b1b.svg)](https://arxiv.org/abs/2310.06500) | University of Cambridge |
| 2023 | Meta-control of Dialogue Systems Using Large Language Models | [![arXiv](https://img.shields.io/badge/arXiv-2312.13715-b31b1b.svg)](https://arxiv.org/pdf/2312.13715v1) | - |
| 2023 | PLUG-AND-PLAY POLICY PLANNER FOR LARGE LANGUAGE MODEL POWERED DIALOGUE AGENTS | [![arXiv](https://img.shields.io/badge/arXiv-2311.00262-b31b1b.svg)](https://arxiv.org/pdf/2311.00262) | NUS |
| 2023 | DiagGPT: An LLM-based Dialogue System with Automatic Topic Management for Goal-Oriented Dialogue | [![OpenReview](https://img.shields.io/badge/OpenReview-mlPpFzmUygY-blue.svg)](https://openreview.net/pdf?id=mlPpFzmUygY) | Anonymous Review |
| 2023 | Prompt-Based Monte-Carlo Tree Search for Goal-oriented Dialogue Policy Planning | [![ACL Anthology](https://img.shields.io/badge/ACL%20Anthology-2023.emnlp--main.439-blue.svg)](https://aclanthology.org/2023.emnlp-main.439.pdf) | Department of Computer Science, Columbia University, New York, NY |
| 2023 | ZERO-SHOT GOAL-DIRECTED DIALOGUE VIA RL ON IMAGINED CONVERSATIONS | [![arXiv](https://img.shields.io/badge/arXiv-2311.05584-b31b1b.svg)](https://arxiv.org/pdf/2311.05584) | UC Berkeley |
| 2023 | Enhancing Large Language Model Induced Task-Oriented Dialogue Systems Through Look-Forward Motivated Goals | [![arXiv](https://img.shields.io/badge/arXiv-2309.08949-b31b1b.svg)](https://arxiv.org/pdf/2309.08949) | NUS, NTU, UCSB, UCL |
| 2024 | Bridging Human and AI Decision-Making with LLMs: The RAGADA Approach | [![SciTePress](https://img.shields.io/badge/SciTePress-127050-blue.svg)](https://www.scitepress.org/Papers/2024/127050/127050.pdf) | Department of Computer Science and Engineering, Aalto University, Finland |
| 2024 | Personalized LLM Response Generation with Parameterized Memory Injection | [![arXiv](https://img.shields.io/badge/arXiv-2404.03565-b31b1b.svg)](https://arxiv.org/pdf/2404.03565v1) | Worcester Polytechnic Institute, Worcester, USA |
| 2023 | Large language models show human-like content biases in transmission chain experiments | [![PNAS](https://img.shields.io/badge/PNAS-2313790120-blue.svg)](https://www.pnas.org/doi/10.1073/pnas.2313790120) | Stanford University, Stanford, CA |
| 2023 | LLM-based Smart Reply (LSR): Enhancing Collaborative Performance with ChatGPT-mediated Smart Reply System | [![arXiv](https://img.shields.io/badge/arXiv-2306.11980v4-b31b1b.svg)](https://arxiv.org/pdf/2306.11980v4) | Clemson University, USA |
| 2023 | Translating Natural Language to Planning Goals with Large-Language Models | [![arXiv](https://img.shields.io/badge/arXiv-2302.05128-b31b1b.svg)](https://arxiv.org/pdf/2302.05128) | NUS |

### Datasets
| **Year** | **Title** | **Link** |
| --------- | --------- | ---------- |
| 2024 | Amazon Product Reviews | [Amazon Product Reviews](https://registry.opendata.aws/amazon-reviews/) |
| 2008 | IEMOCAP | [IEMOCAP](https://sail.usc.edu/iemocap/) |
| 2017 | DailyDialog | [DailyDialog](https://paperswithcode.com/dataset/dailydialog) |
| 2020 | EmpatheticDialogues | [EmpatheticDialogues](https://github.com/facebookresearch/EmpatheticDialogues) |
| 2022 | PENS | [PENS](https://msnews.github.io/pens_data.html) |
| 2023 | SoulChatCorpus | [SoulChatCorpus](https://github.com/scutcyr/SoulChat) |
| 2023 | MISC | [MISC](https://www.microsoft.com/en-us/download/details.aspx?id=55594) |
| 2022 | MultiESC | [MultiESC](https://github.com/lwgkzl/MultiESC) |
| 2022 | GLHG | [GLHG](https://arxiv.org/pdf/2204.12749) |
| 2022 | PsyQA | [PsyQA](https://paperswithcode.com/dataset/psyqa) |
| 2023 | efaqa | [efaqa](https://github.com/chatopera/efaqa-corpus-zh) |
| 2021 | GSM8K | [GSM8K](https://huggingface.co/datasets/openai/gsm8k) |
| 2021 | CSQA | [CSQA](https://paperswithcode.com/dataset/csqa) |
| 2021 | StrategyQA | [StrategyQA](https://huggingface.co/datasets/voidful/StrategyQA) |
| 2022 | SayCan | [SayCan](https://say-can.github.io) |
| 2021 | CraisglistBargain | [CraigslistBargain](https://paperswithcode.com/dataset/craigslistbargains) |
| 2022 | CIMA | [CIMA](https://github.com/kstats/CIMA) |
| 2021 | DialoGLUE | [DialoGLUE](https://github.com/alexa/dialoglue) |
| 2021 | PersuasionForGood | [PersuasionForGood](https://convokit.cornell.edu/documentation/persuasionforgood.html) |
| 2020 | MultiWoZ 2.1 | [MultiWoZ 2.1](https://paperswithcode.com/dataset/multiwoz) |
| 2021 | AmazonQA | [AmazonQA](https://github.com/amazonqa/amazonqa) |
| 2021 | ALFRED-L | [ALFRED-L](https://paperswithcode.com/dataset/alfred) |


### Open-Source Codes
| **Year** | **Paper** | **Code** |
| --------- | --------- | ---------- |
| 2023 | Emotional Intelligence of Large Language Models | [![GitHub](https://img.shields.io/badge/GitHub-emotional--intelligence-brightgreen)](https://emotional-intelligence.github.io/) |
| 2024 | EmoLLMs: A Series of Emotional Large Language Models and Annotation Tools for Comprehensive Affective Analysis | [![GitHub](https://img.shields.io/badge/GitHub-EmoLLMs-brightgreen)](https://github.com/lzw108/EmoLLMs) |
| 2023 | SoulChat: Improving LLMs’ Empathy, Listening, and Comfort Abilities through Fine-tuning with Multi-turn Empathy Conversations | [![GitHub](https://img.shields.io/badge/GitHub-SoulChat-brightgreen)](https://github.com/scutcyr/SoulChat) |
| 2023 | PLUG-AND-PLAY POLICY PLANNER FOR LARGE LANGUAGE MODEL POWERED DIALOGUE AGENTS | [![GitHub](https://img.shields.io/badge/GitHub-PPDPP-brightgreen)](https://github.com/dengyang17/PPDPP) |
| 2023 | Prompt-Based Monte-Carlo Tree Search for Goal-oriented Dialogue Policy Planning | [![GitHub](https://img.shields.io/badge/GitHub-GDPZero-brightgreen)](https://github.com/jasonyux/GDPZero) |
| 2023 | Enhancing Large Language Model Induced Task-Oriented Dialogue Systems Through Look-Forward Motivated Goals | [![GitHub](https://img.shields.io/badge/GitHub-ProToD-brightgreen)](https://github.com/zhiyuanhubj/ProToD) |


## Citation
If you found this project helpful, please kindly cite our work:
```
@misc{advikbibek24,
  author = {Advik Raj Basani, Bibekananda Kundu},
  title = {EET-LLM: A Emotional, Empathetic and Task-Oriented LLM},
  year = {2024},
  howpublished = {\url{https://github.com/BitC3t/EET-LLM}}
}
```

## Execution and Running
You may run this framework locally via the following command: 
```streamlit run frontend.py```

Other scripts in this repo deal with the several other components of the framework.

## Authors
This project was created by Advik Raj Basani (f20221155@goa.bits-pilani.ac.in), under the guidance of Dr. Bibekananda Kundu.

## License
This code is under the GNU-GPL v3.0.
