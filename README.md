# Codex Skills Pack

这个仓库打包了可直接安装到 Codex 的本地 Skills。

当前包含：

- `skill-finder`：从 GitHub、Web、X/Twitter 等来源查找、比较和推荐 Codex/AI Agent Skills。
- `knowledge-concept-distiller`：把博主、专家、课程、访谈、图文或视频文稿蒸馏成可复用的知识概念型 Skill。
- `fashion-outfit-exploder`：把人物照片转换成固定 9:16 版式的穿搭拆解图，一人一图，自动拆出服装、鞋履、配饰、包袋和道具。

## 一句话安装

在 Codex 或终端里执行：

```bash
curl -fsSL https://raw.githubusercontent.com/medgrey123-prog/skill-finder/main/install.sh | bash
```

安装路径保持稳定：

```text
${CODEX_HOME:-~/.codex}/skills/skill-finder
${CODEX_HOME:-~/.codex}/skills/knowledge-concept-distiller
${CODEX_HOME:-~/.codex}/skills/fashion-outfit-exploder
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

### 服装搭配师一键炸图

上传人物照片后调用：

```text
用 $fashion-outfit-exploder，把这张人物照片生成 9:16 穿搭炸图。忽略原图版式，人物给正脸，服装、鞋子、配饰和道具全部拆开。
```

多人照片：

```text
用 $fashion-outfit-exploder，左右两个人分别输出，一人一张，全部保持 9:16 和正脸。
```

连续处理新照片：

```text
继续，和之前一样。
```

该 Skill 会默认执行：

- 忽略输入照片的背景、截图界面、水印和原始排版。
- 中央只保留一名完整全身、正脸人物。
- 画布固定为 9:16。
- 左右拆出服装、鞋履、帽子、眼镜、包袋、首饰、围巾、腰带、乐器及其他显著道具。
- 多人物照片按人物分别生成，不混用单品。
- 采用白底、细衬线法文标题和纤细横线的固定时尚编辑版式。

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

## Skill: fashion-outfit-exploder

适合请求：

- 上传一张人物穿搭照片，自动生成固定版式穿搭拆解图。
- 忽略原图的海报、截图或商品栏版式，重新生成统一模板。
- 把双人或多人合照拆成一人一张。
- 把低头、侧脸或手机挡脸的人物转换成自然正脸展示。
- 拆解连衣裙、叠穿造型、鞋履、包袋、首饰、帽子、眼镜和乐器道具。

内容：

- `fashion-outfit-exploder/SKILL.md`
- `fashion-outfit-exploder/agents/openai.yaml`
- `fashion-outfit-exploder/references/layout-spec.md`
- `fashion-outfit-exploder/references/prompt-template.md`
- `fashion-outfit-exploder/references/quality-checklist.md`
- `fashion-outfit-exploder/references/test-cases.md`

## Requirements

- macOS or Linux shell for the one-line installer
- `unzip`
- `curl` or `python3`
- Codex skills directory at `${CODEX_HOME:-~/.codex}/skills`
- 使用 `fashion-outfit-exploder` 时，当前运行环境需要具备图像理解和图像生成或编辑能力

`skill-finder` 的公开 GitHub 搜索不需要凭据，但可能触发 GitHub 速率限制。只有需要更高限制或私有仓库访问时才设置 `GITHUB_TOKEN`，不要把 token 提交到仓库。

## Troubleshooting

- 如果 Codex 安装后看不见 Skill，先重启 Codex。
- 如果 `unzip` 缺失，先安装 `unzip`，或手动把对应 skill 文件夹复制到 `~/.codex/skills/`。
- 如果安装脚本提示备份旧版本，这是正常更新行为。
- 如果网络无法下载 GitHub 压缩包，可以打开仓库页面，让 Codex 把对应 skill 文件夹复制到 `~/.codex/skills/`。
- 如果穿搭拆解图没有按要求输出，检查当前环境是否提供图像生成工具，并在指令中明确“一人一张、9:16、正脸、忽略原图版式”。