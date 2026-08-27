# Banned phrases

If any of these appear in a note body, delete the span and rewrite the content (limits belong in 局限性, as data).

## Process / self-audit (hard fail)

- `AI 初判`、`待人核`、`[AI 初判·待人核]`、`总体可信度（AI`
- `## 自检`、`笔记自检`、`合格自检`、`Target 420`、`L2 合格`
- `生成过程`、`提取行数`、`凑字`、`Ask 模式`、`作为 AI`、`我无法访问 PDF`
- `下面我将`、`接下来分析` (narrating the model)

## Chinese slop (rewrite)

- `具有重要意义`、`填补空白`、`提供理论基础`、`具有广阔应用前景`
- `值得注意的是`、`不难发现`、`综上所述`、`如上所述`
- `为后续研究提供参考`、`具有指导意义`
- Dense `首先` / `其次` / `再次` / `最后` in one section
- `在此基础上`、`进一步地`、`本文拟`
- Straw 翻案腔: `你以为……其实……`、`说到底`、`答案恰恰相反` (a data contrast is fine)
- Insight signposts: `一文读懂`、`更微妙的是`、`还有一层`、`只说对了一半`。钩子样张反例：`AI_lib/articles/古人类演化/ccr5-hiv.md`（「听起来，是否带着一种跨越时空的奇妙巧合？」这类开篇）

A factual sequence (不含 A 时…加入 A 后…) is allowed. A numbered essay skeleton is not.
