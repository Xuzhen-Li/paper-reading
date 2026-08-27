# Terminology (Chinese notes)

Keep one rendering per English term for the whole note. Do not rotate synonyms for style.

## 总原则

Settled, accurate Chinese first (塌缩区域、定相、共线性). If there is **no** settled Chinese, keep the English and gloss once in a complete Chinese sentence (`doubled monoploid`、`gamete binning`、`haplotig`、`PAP`). Do not invent a compact calque.

One term, one rendering for the whole note. The ledger holds **scientific terms, names, symbols, and units only**. Do not turn ordinary Chinese (丢进、齐活、随机派) into a substitution table; those are paragraph-rewrite problems (`zh-polish-order.md`).

## When to keep English

If there is **no settled, accurate Chinese** (or the Chinese would just be English words glued together: 单例变异、单倍型骨架、强制纯合), **keep the English** and gloss once in ordinary Chinese. Do not invent a compact calque to look bilingual.

Examples that stay English unless the field already has a stable term:

| English | In the note |
|---------|-------------|
| singleton (MAC = 1) | `singleton`（整份队列里次要等位只出现一次） |
| haplotype scaffold | `haplotype scaffold`（先把常见位点定相，后面稀有位点往这套 haplotype 上挂） |
| forcing homozygosity | `forcing homozygosity`（conditioning 样本若是杂合，两条 haplotype 都写成带次要等位） |
| conditioning haplotypes | `conditioning haplotypes` |
| switch error rate | `switch error rate`（SER；相邻两个杂合位点之间相位翻错的比例） |
| doubleton | `doubleton` |

Settled Chinese that *is* worth using: phasing → 定相；MAF / MAC 可保留缩写；复合杂合（compound heterozygous）医学遗传里已常用，可写中文，第一次括注英文。haplotype **stays English** in the whole note (do not rotate 单倍型). Do not glue haplotype onto the next noun (不要写单倍型骨架、条件单倍型)；那种地方直接留 `haplotype scaffold` / `conditioning haplotypes`.

Do **not** use 单点 for singleton (that is point mutation talk). Do **not** use 单倍体 or 单倍型 for haplotype. 单倍体 is reserved for haploid (单倍体配子、单倍体基因组大小).

## Ledger (extend per paper)

| English | Use in the note | Do not use |
|---------|-----------------|------------|
| phasing | 定相；需要时写 haplotype phasing | 排相位、分相（易与化学相混） |
| haplotype | haplotype（全篇统一英文） | 单倍型、单倍体 |
| switch error rate (SER) | switch error rate（SER） | 切换率、跳变率 |
| haplotype scaffold | haplotype scaffold + 一句中文解释 | 单倍型骨架（英文词硬拼） |
| genotype imputation | imputation，或 基因型填补 | 插补（易与 missing-data 插补混） |
| compound heterozygous | 复合杂合（compound heterozygous） | 化合物杂合 |
| singleton (MAC = 1) | **singleton** | 单点、单例变异 |
| doubleton | doubleton | 双点、双例变异 |
| MAC / MAF | MAC / MAF；首次可写次要等位基因计数 / 频率 | 最小等位频率 |
| forcing homozygosity | forcing homozygosity | 强制纯合（除非后文已解释过） |
| conditioning haplotypes | conditioning haplotypes | 条件单倍型、调节单倍型 |
| IBD | IBD（同源相同） | 血缘相同 |
| PBWT | PBWT；首次写 positional Burrows–Wheeler transform | 位置BWT 单独出现 |
| Li and Stephens | Li–Stephens 模型 | LS 模型（除非已定义） |
| LoF | LoF；首次可写功能丧失 | 失活突变（过宽） |
| burden test | burden test，或 基因负担检验 | 负荷测试 |
| reference panel | reference panel，或 参考面板 | 参照盘 |
| white British | 自报白人英国人（UKB 字段，PCA 确认） | 白英国人 |
| chunk / buffer | 染色体区段 / 重叠缓冲 | 块（可作括注） |

If unsure, add a row in `## 术语对照` with the **English** in the 笔记用语 column.

## Ledger — 基因组组装 / 多倍体

| English | Use in the note | Do not use |
|---------|-----------------|------------|
| collapsed contig / region | 塌缩 contig、塌缩区域 | 塌掉 |
| read binning | 把读段按 haplotype 分开 / 归到某条 haplotype | 分箱、箱子、分箱重组装 |
| trio binning / gamete binning | 方法名留英文；首次各用一句中文解释 | 把方法名译成「三联分箱」「配子分箱」 |
| phased / phasing | 已定相 / 定相 | 排相位、分相 |
| haplotype-resolved assembly | haplotype 解析组装 | 单倍型解析组装 |
| doubled monoploid (DM) | `doubled monoploid`（DM，单倍体加倍得到的纯合系） | 加倍单倍体裸用 |
| haplotig / diplotig / triplotig / tetraplotig | 留英文；首次：初始组装里塌缩成 1 / 2 / 3 / 4 套 haplotype 的 contig | 单倍 contig、双倍 contig |
| PAP (presence/absence pattern) | `PAP`；首次：某个窗口在 717 个花粉核上有没有覆盖，连成的有无向量 | 有无模式裸用 |
| coverage marker | coverage marker（50 kb 窗口的覆盖） | |
| pseudo-heterozygous | 伪杂合 | |
| double reduction | double reduction（四倍体减数分裂里两条同源染色体进入同一配子） | 双减数（除非后文已解释） |
| crossover | 交叉（crossover） | |
| ARG | ARG（ancestral recombination graph，祖先重组图） | 祖源重组图（易读成 ancestry） |
| archaic introgression | 古人类渗入；首次括注 archaic introgression | 古代渗入（过宽） |
| ghost ancestry | ghost ancestry（未测序的古人类祖源） | 鬼魂祖先 |
| super-archaic | super-archaic（比尼安德特/丹尼索瓦更深的分化） | 超古代 |
| ILS | ILS（不完全谱系排序） | |
| SINGER / Relate | 方法名留英文 | |
| hmmix / Sprime / IBDmix | 方法名留英文 | |

New-domain papers: append a subsection here. Do not invent a one-off rendering only inside the note.

## 速览卡

Must include **作者**：并列第一作者、通讯作者、单位、作者贡献里谁做什么。Do not leave authors only in YAML.

If Code availability lists GitHub/GitLab (or Zenodo) **with a full set of scripts** (tools + pipeline to rerun the paper, not a binary-only dump), must include **代码**：URL、许可、仓库里有什么。Do not bury this only in YAML `code:`.

## Chinese must be Chinese

Do not compress a clause into an English compound. 「芯片时代的单倍型定相已经能扛几十万人」is a calque. Write who did what to whom, with a verb: 以前用 SNP 芯片做关联研究时，统计方法已经可以把几十万人的常见位点定相。

Do not shrink 导读 to hit a line or character target. Length follows the paper.

## 写作学习

The **原句** column must be a verbatim English sentence from the PDF or SI, with a locator.
