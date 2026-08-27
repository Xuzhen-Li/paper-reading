---
title: "<中文标题>"
en_title: "<English title>"
tags: [paper]
status: done
created: YYYY-MM-DD
note_depth: L3
first_author: ""
year: YYYY
journal: ""
doi: ""
source_pdf: "relative/path.pdf"
source_pdf_abs: "/absolute/path.pdf"
si_dir: "_figures/<slug>/si/"
si_inventory: "MOESM1 …; Tables …"
---

# <中文标题>

> **DOI**: [doi](https://doi.org/doi) · *Journal* year

## 速览卡

| 维度 | 内容 |
|------|------|
| 作者 | 并列第一作者、通讯、单位；作者贡献里谁做什么 |
| 一句话 | |
| 解决的问题 | |
| 物种/系统 | |
| 数据量级 | |
| 代码 | Code availability 有 GitHub/GitLab 全套脚本时必填：URL、许可、仓库里有什么；没有则删这一行 |
| 许可 | |

## 术语对照

| English | 笔记用语 |
|---------|----------|
| | |

## 📖 全文导读

按 Intro → 设计 → Fig 顺序 → 作者收束。方法段之后、第一张结果图之前，放 mermaid 流程图（样品 → 数据 → 分析 → 主结论），图下一行斜体写「笔记整理，不是原文图」。主图嵌在对应结果节。导读用完整中文句子（见 `references/fluency-zh.md`），不要电报体，不要为了短而压缩。译不准的术语留英文（如 `singleton`）。SI 路径只写 YAML，不要写进正文。

![Fig.1](_figures/<slug>/fig01.png)

## 数字速查

读完导读再查。

| 项 | 值 |
|----|----|

## 我的判断

亮点、混杂、作者未收住的局限，用段落写。不要贴核验标签。

### 可引用 / 不要当作

## 📜 原文摘抄

Intro / Results / Discussion，≥8 条。英文原文 + 中文紧译 + 出处。

> **EN**: "…"
> **中文**: …
> 出处：

## ✍️ 写作学习

原句列必须是 PDF/SI 里的英文原句，附出处。

| 原句 | 好在哪 | 可复用 |
|------|--------|--------|

## 关联

- Author et al. *Journal* year. [10.xxxx/xxxx](https://doi.org/10.xxxx/xxxx)。一句话为什么相关。有本地笔记时再加 `[slug](slug.md)`，不能只用本地链。
