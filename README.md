# Codex Skills Pack

这个仓库打包了可直接安装到 Codex 的本地 Skills。

当前包含：

- `skill-finder`：从 GitHub、Web、X/Twitter 等来源查找、比较和推荐 Codex/AI Agent Skills。
- `knowledge-concept-distiller`：把博主、专家、课程、访谈、图文或视频文稿蒸馏成可复用的知识概念型 Skill。
- `methodology-allegory`：把抽象方法论、理论或概念改写成具有悬念和认知跃迁的寓言，让读者先形成直觉，再在故事接近结尾时获得专业概念名称。

## 一句话安装

在 Codex 或终端里执行：

```bash
curl -fsSL https://raw.githubusercontent.com/medgrey123-prog/skill-finder/main/install.sh | bash
```

安装路径保持稳定：

```text
${CODEX_HOME:-~/.codex}/skills/skill-finder
${CODEX_HOME:-~/.codex}/skills/knowledge-concept-distiller
${CODEX_HOME:-~/.codex}/skills/methodology-allegory
```

安装后重启 Codex，让新 Skill 被自动发现。

## 一句话调用

### Skill Finder

```text
Use $skill-finder to find the best skill for publishing a local project to GitHub.
```

### Knowledge Concept Distiller

```text
用 $knowledge-concept-distiller，帮我把这个博主的语料蒸馏成一个知识概念型 Skill。不要仿写文案风格，重点提炼知识地图、核心概念、观点、逻辑链、方法论和适用边界。
```

如果语料在文件夹里：

```text
用 $knowledge-concept-distiller，语料都在这个文件夹里：/你的/语料/路径。请先读取和盘点，再输出知识识别分析报告。
```

### Methodology Allegory

直接指定一个概念：

```text
用 $methodology-allegory，把“Jobs to Be Done”讲成一个寓言故事。不要一开始告诉我概念名称，让我先经历困惑、误判、发现规律和认知跃迁，最后再揭晓答案。
```

适合社交媒体版本：

```text
用 $methodology-allegory，把“选择过载”写成一个适合社交媒体发布的寓言。控制长度，但不要压成事件摘要，要保留异常、调查、失败、重复线索和最后的认知反转。
```

完整学习版本：

```text
用 $methodology-allegory，给我讲“网络效应”。先讲寓言，最后再揭晓专业概念，并解释核心问题、反直觉之处、关键机制、真实应用和故事隐喻。
```

## Skill: skill-finder

适合请求：

- “Find me the best Codex skill for publishing projects to GitHub.”
- “Compare available Karpathy-inspired skills.”
- “Is this GitHub skill maintained and worth installing?”

内容：

- `skill-finder/SKILL.md`
- `skill-finder/scripts/github_skill_search.py`
- `skill-finder/references/source-evaluation.md`

## Skill: knowledge-concept-distiller

适合请求：

- 想把一个博主的内容沉淀成知识库，而不是只模仿文案。
- 想提炼专家的概念、判断、方法论、案例拆解方式。
- 想生成一个后续可以继续调用的 Knowledge Skill Prompt。
- 想对大量视频文稿、图文笔记、课程文字稿做结构化蒸馏。

它会按 KCLM 四层执行：

1. **Knowledge Map**：知识地图，识别主题簇和知识边界。
2. **Concept System**：概念系统，提炼核心概念和定义。
3. **Logic Chains**：逻辑链，复原作者如何从现象推到结论。
4. **Method Library**：方法库，把知识转成可复用方法。

内容：

- `knowledge-concept-distiller/SKILL.md`
- `knowledge-concept-distiller/agents/openai.yaml`
- `knowledge-concept-distiller/references/workflow.md`
- `knowledge-concept-distiller/references/output-templates.md`
- `knowledge-concept-distiller/references/skill-prompt-template.md`

## Skill: methodology-allegory

适合请求：

- 想把品牌、营销、市场、商业、行为经济学或战略方法论讲成寓言。
- 不想先听定义，而是希望先通过故事形成直觉。
- 想把复杂概念改写成适合社交媒体阅读、但仍然具有完整故事性的内容。
- 希望读者经历“困惑 → 误判 → 发现规律 → 重新提问 → 概念揭晓”的理解过程。

核心原则：

1. **先隐藏概念**：故事前期不暴露专业名称。
2. **先制造异常**：主人公原有常识必须解释不了现实。
3. **允许犯错**：错误尝试必须合理，并对应真实的常见误区。
4. **重复埋线索**：不同事件由同一个底层机制驱动。
5. **改变问题**：认知跃迁通常来自重新提出问题，而不是突然得到答案。
6. **最后命名**：专业概念尽量推迟到故事最后 10%–15%。
7. **统一隐喻**：结尾继续使用故事原有的核心意象，不突然引入新的隐喻系统。

内容：

- `methodology-allegory/SKILL.md`
- `methodology-allegory/agents/openai.yaml`

## Requirements

- macOS or Linux shell for the one-line installer
- `unzip`
- `curl` or `python3`
- Codex skills directory at `${CODEX_HOME:-~/.codex}/skills`

`skill-finder` 的公开 GitHub 搜索不需要凭据，但可能触发 GitHub 速率限制。只有需要更高限制或私有仓库访问时才设置 `GITHUB_TOKEN`，不要把 token 提交到仓库。

## Troubleshooting

- 如果 Codex 安装后看不见 Skill，先重启 Codex。
- 如果 `unzip` 缺失，先安装 `unzip`，或手动把对应 skill 文件夹复制到 `~/.codex/skills/`。
- 如果安装脚本提示备份旧版本，这是正常更新行为。
- 如果网络无法下载 GitHub 压缩包，可以打开仓库页面，让 Codex 把对应 skill 文件夹复制到 `~/.codex/skills/`。
