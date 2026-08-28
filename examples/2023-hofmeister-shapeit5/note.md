---
title: "SHAPEIT5：UKB 稀有变异单倍型定相；复合杂合 LoF 筛出 549 个基因"
en_title: "Accurate rare variant phasing of whole-genome and whole-exome sequencing data in the UK Biobank"
tags: [paper, SHAPEIT5, phasing, UKB, imputation, compound-heterozygote, Nature-Genetics, Delaneau]
status: done
created: 2026-08-24
updated: 2026-08-27
note_depth: L3
corresponding: "Olivier Delaneau（olivier.delaneau@unil.ch）"
first_author: "Robin J. Hofmeister*、Diogo M. Ribeiro*、Simone Rubinacci* (equal)"
year: 2023
journal: Nature Genetics
doi: 10.1038/s41588-023-01415-w
license: CC-BY-4.0
keywords: [SHAPEIT5, UKB, rare-variant, PBWT, switch-error, imputation, compound-het, LoF, Delaneau]
figures_note: "Local figure crops are not shipped. See the paper DOI."
figures_count: 7
code: "https://github.com/odelaneau/shapeit5 （MIT，全套脚本：phase_common / phase_rare / ligate / switch）；https://odelaneau.github.io/shapeit5 ；Zenodo 10.5281/zenodo.7828479 ；UKB RAP application 66995"
---

# SHAPEIT5：UKB 稀有变异单倍型定相；复合杂合 LoF 筛出 549 个基因

> **DOI**: [10.1038/s41588-023-01415-w](https://doi.org/10.1038/s41588-023-01415-w) · *Nat. Genet.* 55, 1243–1249（2023）· CC BY 4.0

## 分类


|     |                                                                                                                                      |
| --- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 系统  | UK Biobank：自报白人英国人（UKB 字段，再经 PCA 确认）的 WGS、WES，以及 Axiom 芯片                                                                            |
| 领域  | haplotype 定相、稀有变异、基因型 imputation、复合杂合（compound heterozygous）                                                                         |
| 方法  | 先用 SHAPEIT4 把常见位点定相，得到 haplotype scaffold；稀有位点用 PBWT 挑选 conditioning haplotypes，再按 Li–Stephens 做 imputation 式定相；singleton 按最短 IBD 赋值 |
| 数据  | WGS 150,119 人 / 603,925,301 位点；WES 452,644 人 / 26,199,614 位点；chr20 评测 n=147,754                                                      |
| 期刊  | *Nature Genetics* Technical Report（2023）                                                                                             |




## 速览卡


| 维度    | 内容                                                                                                                                                                                                                                                                                                                                      |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 作者    | Robin J. Hofmeister、Diogo M. Ribeiro、Simone Rubinacci 并列第一作者（按姓氏字母排）。通讯作者 Olivier Delaneau，洛桑大学计算生物学系（[olivier.delaneau@unil.ch](mailto:olivier.delaneau@unil.ch)）。作者贡献：Delaneau 与 Rubinacci 做方法；Hofmeister 在 UKB 上跑定相；Rubinacci 跑 imputation；Ribeiro 筛复合杂合；Delaneau 设计并监督。资助 SNSF PP00P3_176977。                                       |
| 一句话   | Delaneau 这一组先把常见位点定相，再把稀有杂合的相位挂到这套 haplotype scaffold 上。UKB 里 MAC 11–20 的 switch error rate（SER）相对 Beagle v.5.4 从 8.76% 降到 4.36%。同一批 haplotype 拿去当 reference panel，MAC 2–5 的 r² 大约高 0.05。WES 上 Supplementary Data 1 给出 549 个基因、779 条复合杂合 LoF 事件。                                                                                        |
| 解决的问题 | 十五万人规模的 WGS 里，大约 96% 的位点 MAF 不到 0.1%。全基因组平均 SER 几乎完全由常见杂合位点决定，稀有位点定错了也看不出来。要找复合杂合，又必须分清两个突变是 cis 还是 trans。                                                                                                                                                                                                                              |
| 材料    | UKB Research Analysis Platform，申请号 66995。评测只用自报、并且 PCA 确认过的白人英国人 trio 和 duo。                                                                                                                                                                                                                                                            |
| 数据量级  | WGS 上 MAC 11–20 的 SER 是 4.36%（Beagle 8.76%）。singleton 的 SER 大约 35%。复合杂合基因 549 个，相位置信度 >0.99 时还剩 441 个。                                                                                                                                                                                                                                  |
| 代码    | GitHub 全套脚本：[odelaneau/shapeit5](https://github.com/odelaneau/shapeit5)（MIT）。Code availability 写明含 `phase_common`、`phase_rare`；仓库里还有 `ligate`、`switch`。文档站 [https://odelaneau.github.io/shapeit5](https://odelaneau.github.io/shapeit5) ；Zenodo [10.5281/zenodo.7828479](https://doi.org/10.5281/zenodo.7828479)。UKB 作业走 RAP 申请号 66995。 |
| 许可    | 论文 CC BY 4.0。软件 MIT。定相后的 panel 只能通过 RAP 取。                                                                                                                                                                                                                                                                                              |




## 术语对照


| English                 | 笔记怎么写                                                          |
| ----------------------- | -------------------------------------------------------------- |
| haplotype phasing       | 把 haplotype 定相 / 统计定相                                          |
| switch error rate (SER) | switch error rate（SER）：相邻两个杂合位点之间相位翻错的比例                       |
| haplotype scaffold      | haplotype scaffold：先把常见位点定相，稀有位点再往这套 haplotype 上挂              |
| genotype imputation     | imputation（基因型填补）                                              |
| singleton (MAC = 1)     | **singleton**：整份队列里次要等位只出现一次                                   |
| MAC / MAF               | 次要等位基因计数 / 频率，正文里多用缩写                                          |
| forcing homozygosity    | forcing homozygosity：conditioning 样本若是杂合，两条 haplotype 都写成带次要等位 |
| conditioning haplotypes | conditioning haplotypes                                        |
| IBD                     | IBD（同源相同）                                                      |
| compound heterozygous   | 复合杂合（compound heterozygous）                                    |
| LoF                     | LoF（功能丧失：终止获得、移码、必需剪接）                                         |




## 📖 全文导读

以前做全基因组关联，主要靠 SNP 芯片。芯片上大多是常见位点；当时的统计定相方法，也是为这些常见位点写的，已经可以处理几十万人的数据。UK Biobank 后来放出 150,119 人的全基因组测序。和他们自己用的 Axiom 芯片比，位点数量高了大约三个数量级，其中大约 96% 的位点 MAF 不到 0.1%。如果还拿全基因组一条平均的 switch error rate（SER）来打分，这个分数几乎完全由常见杂合位点决定。稀有位点上就算相位估错了，也很难把这条平均拉下来。可是要识别复合杂合（compound heterozygous）事件，就必须知道两个杂合的 LoF 突变是分别落在父亲和母亲传来的两条 haplotype 上（trans），还是落在同一条上（cis）。相位一错，本来同在一条 haplotype 上的两个突变，会被当成两条拷贝都坏了。

通讯作者是洛桑大学计算生物学系的 Olivier Delaneau。方法上这一组从 SHAPEIT、SHAPEIT2 走到 SHAPEIT4：常见位点用 Gibbs 抽样，用 Li–Stephens 模型，再用 PBWT（positional Burrows–Wheeler transform）挑 informative haplotype。同一组的 Impute5 把 Li–Stephens 模型的 haploid 写法做成 imputation 引擎。GLIMPSE（2021）拿它做低覆盖测序的 imputation。2023 年 6 月 29 日，同一期 *Nature Genetics* 还发了 Rubinacci、Hofmeister、Sousa da Mota、Delaneau 的 GLIMPSE2，用的还是这 150,119 套 UKB 基因组（[10.1038/s41588-023-01438-3](https://doi.org/10.1038/s41588-023-01438-3)）。SHAPEIT5 负责把 haplotype 定相，GLIMPSE2 负责低覆盖 imputation，两篇是同一套工具的两半。作者贡献写得很清楚：Delaneau 和 Rubinacci 做方法，Hofmeister 跑 UKB 定相，Rubinacci 跑 imputation，Ribeiro 筛复合杂合。三位并列第一作者按姓氏字母排。资助是瑞士国家科学基金会 PP00P3_176977。

直接对照是 Browning 组的 Beagle v.5.4。Beagle 已经把常见位点和稀有位点拆开：先得到一套 haplotype scaffold，再用 imputation 的办法把稀有杂合挂上去。SHAPEIT5 也是这样拆的。它多出来的一步，是给每一个稀有杂合单独挑一套 conditioning haplotypes。挑的时候有两个要求：这些 haplotype 在本地和靶样本 IBD，并且这套里必须有人带着次要等位。没有次要等位，模型就分不清两种相位。

_Fig.1 SHAPEIT5 四步. See [DOI 10.1038/s41588-023-01415-w](https://doi.org/10.1038/s41588-023-01415-w)._

*Fig. 1。灰色条带是已经定相的常见位点，也就是后面稀有位点要挂上去的 haplotype scaffold。每一个稀有杂合只从本地 IBD 更长、并且带着次要等位的邻居 haplotype 上估计相位。singleton 在整份队列里没有第二个次要等位，找不到这样的邻居，就把次要等位派给 IBD 共享段最短的那条 haplotype。最右边一列才是复合杂合：两个 LoF 必须分别落在父亲和母亲传来的两条 haplotype 上。*

常见位点的阈值是 MAF ≥ 0.1%，用的是改过的 SHAPEIT4。SHAPEIT5 把 PBWT 按默认 4 cM 切成区段，方便并行。稀有位点（MAF < 0.1%）只保存带着次要等位的基因型，矩阵和它的转置一起放。每个稀有杂合只看一小撮 conditioning haplotypes。第二趟 PBWT 只扫携带者。如果邻居自己也是杂合，两条 haplotype 各带哪个等位还不知道。作者把次要等位同时写进两条 haplotype，Beagle v.5.4 也这么做，他们把这一步叫 forcing homozygosity。

稀有位点的定相写成 imputation 的形式，copying 模型来自 Impute5 那套 haploid Li–Stephens。两侧最近常见位点上的 copying 概率先取平均，再乘成两种相位的后验，范围 0.5–1，同时当作相位置信度。

_Supplementary Fig.1 相位后验怎么算. See [DOI 10.1038/s41588-023-01415-w](https://doi.org/10.1038/s41588-023-01415-w)._

*Supplementary Fig. 1。示范里 h1 带 1、h2 带 0 的联合概率是 0.998。forcing homozygosity 发生在把基因型 1 拆进等位 0/1 的那一步，不是事后贴的标签。*

singleton（MAC = 1）的 conditioning 集合里没有次要等位，imputation 模型转不起来。作者改用 Viterbi，分别找出两条靶 haplotype 各自最长的 IBD 共享段。共享段越短，最近共同祖先越老，新突变越可能落在这条线上，于是把次要等位派给最短匹配的那条。

Supplementary Table 1 把四套数据写全。Axiom 芯片质控后是 670,741 位点 × 486,442 人。WES 与未定相的芯片合并后是 26,199,614 位点 × 452,644 人，其中稀有 25,222,097、常见 977,517。合并是为了把基因间区的常见位点补进 haplotype scaffold；同一位点芯片和 WES 都有时留芯片。全基因组是 603,925,301 位点 × 150,119 人。chr20 评测是 13,780,190 位点 × 147,754 人（同时有芯片）。自报白人英国人 trio：芯片 897，WES 719，WGS 31。duo：芯片 4,373，WES 表上 3,104（Methods 写 3,014），WGS 432。WGS 切成平均大约 4.5 Mb 的重叠区段，缓冲 250 kb。

评测用孟德尔逻辑还原子代的真 haplotype，父母的基因组不进定相队列。SER 按相邻两个杂合位点之间有没有翻错来算，并且按 MAC 分箱，避免稀有位点被常见杂合稀释。

看全位点 SER、只看常见位点、或者换样本数，WGS 上和 Beagle 差得不大。Supplementary Fig. 2 把这件事画成样本数曲线：全位点 duo+trio、只 trio、常见位点三条蓝黑线几乎贴着走，Axiom 坐标那条 SHAPEIT5 才明显更低。芯片数据单独定相（5,000 到 480,000 人）两家差不多，最大样本上 SER 低于 0.2%，这时 switch error 和分型错误已经分不开。

_Supplementary Fig.2 全位点 SER 随样本数. See [DOI 10.1038/s41588-023-01415-w](https://doi.org/10.1038/s41588-023-01415-w)._

*Supplementary Fig. 2。a–c 的纵轴已经压到 1% 以下，两家差距很小。d 的 Axiom 切片上 SHAPEIT5 从大约 1.7% 降到大约 0.2%，Beagle 起点更高。*

真正分开的是按 MAC 切开的稀有箱子。

_Fig.2 按 MAC 的 SER 与 imputation r². See [DOI 10.1038/s41588-023-01415-w](https://doi.org/10.1038/s41588-023-01415-w)._

*Fig. 2。a、b 的蓝线在稀有 MAC 上低于黑线。c、d 的 imputation 差距挤在 MAC < 500；HRC 灰线（n=27,165）掉得更明显。*

正文印出来的数字是：WGS 上 MAC 11–20，SER 4.36% 对 Beagle 8.76%，少 50.2%。WES 同一档 2.93% 对 5.18%，少 42.67%。作者把各箱汇总成稀有位点少 20–50% 的 switch error。这个差在至少大约 50,000 人的队列里才站得住（Supplementary Fig. 4）。Source Data Fig. 2a 把 WGS 更稀的箱子也写出来了：MAC 2–5 为 9.33% 对 14.61%，singleton 35.26% 对 50.71%。摘要里「1/100,000 的位点 SER 低于 5%」更贴 MAC 11–20 的 4.36%，贴不到 singleton，也贴不到未过滤的 MAC 2–5。

singleton 要单独看。duo 里 47.36% 的子代 singleton 能被已经分型的那一方父母托住，52.64% 托不住。按无遗传偏好折，大约 5.26% 不是从父母来的。trio 里 4.52% 父母都不带次要等位。大约 95% 仍是遗传来的，能定相。

_Extended Data Fig.3 singleton 能否定相. See [DOI 10.1038/s41588-023-01415-w](https://doi.org/10.1038/s41588-023-01415-w)._

*Extended Data Fig. 3。a 里 p=0/0 约占 52%。b 里双亲都是 0/0 的柱子大约 5%。c、d 的错误柱在 35% 上下，对 50% 的二项检验 p 到了 10⁻¹⁵ 以下。*

WGS 上 singleton 的 SER 是 35.1%（duo）和 36.6%（trio），WES 是 35.2%。相对抛硬币有统计差，离能当诊断证据还远。作者自己写 moderate accuracy。复合杂合分析把 singleton 全部丢掉。

imputation 用来在全体样本上复查相位，不限于有父母的那一小撮。抽出 1,000 个无关英国人当靶，芯片位点填回去，WGS / WES 高覆盖当真值。reference panel 是剩下的 146,754 套 WGS 或 446,470 套 WES。UKB WGS 面板整体压过 HRC。MAC < 500 时，SHAPEIT5 定相的面板压过 Beagle 定相的同一批 UKB。MAC 2–5 的平方 Pearson 大约高 0.05。作者按 Pritchard & Przeworski 换算，说这等于这些位点的有效样本量多 5%，只来自 reference panel 的相位。singleton 的 imputation 也是 SHAPEIT5 面板更好，绝对精度仍然低。

稀有杂合（MAF < 0.1%）带 0.5–1 的置信度，singleton 固定 0.5。阈值 0.99 时，WGS 的 SER 上限大约 2%，WES 大约 1%。

_Extended Data Fig.5 置信度过滤. See [DOI 10.1038/s41588-023-01415-w](https://doi.org/10.1038/s41588-023-01415-w)._

*Extended Data Fig. 5。0.99 的深蓝线把 SER 压到文中说的大约 2% / 1%。WGS 的 MAC 2–5 大约扔掉 23% 杂合，WES 同一档扔掉一半以上，和正文「留下 >75% 与 >40%」对得上。*

算力写在 Supplementary Table 2–3。按 2022 年 10 月 RAP 按需实例：chr20 WGS n=147,754，Beagle £57.82、墙钟 28:55、内存 501 GB；SHAPEIT5 £65.16、墙钟 61:17，但区段并行后每份工作大约 9:20，常见位点每大约 4 Mb 区段均 9.31 GB，稀有 22.7 GB。外推全基因组按需 £2,890 / £3,258，竞价实例 £578 / £651.6。讨论里写全套 WGS+WES 定相低于 £4,000。SHAPEIT5 能切区段，不一定非要按需实例。

复合杂合用的是 WES 上的相位。队列是 374,826 个自报白人英国人，父母已经排除。高置信 LoF（终止获得、移码、必需剪接，LOFTEE 高置信）383,637 个，覆盖 17,689 个蛋白编码基因。每个基因平均 22.3 个 LoF，每人平均 7.8 个。2,150 个基因（12%）至少有一人带两个及以上 LoF。Supplementary Data 1 的 `LoF_compound_het_per_gene` 表有 17,689 行，其中 `num_inds_2_mut > 0` 的正好 2,150 个，`num_ch_events > 0` 的正好 549 个，事件合计 779。事件明细 779 行、549 个基因。个体 ID 被去掉，独特人数无法从表格重算。正文结果节写 766 人；讨论写 816 人、约 0.22% 队列。置信度 >0.99 时还剩 441 个基因（80%）和 614 次事件（79%）。

事件数最多的几个基因是 OBSCN（12）、HMCN2（11）、SPTBN5（11）、MUC4（9），都是大基因或黏蛋白，常见于纯合 LoF 耐受名单。CUBN 只有 5 次事件，但 184 人带着 ≥2 个 LoF、期望 92，观察远低于期望。

_Fig.3 复合杂合与必需基因. See [DOI 10.1038/s41588-023-01415-w](https://doi.org/10.1038/s41588-023-01415-w)._

*Fig. 3。把相位随机打乱以后，基因数抬到 1,792。蓝点在必需基因列表上全是负的 log₂(OR)，橙点贴零。LoF 的观察/期望中位贴着 0，错义 0.8，同义 1.4。*

549 个基因相对「同一人至少两个 LoF」的 2,150 个背景，在多份必需基因名单上耗竭（OR 0.1–0.48，P < 9.7×10⁻³），在非必需和纯合 LoF 耐受名单上富集（OR 1.2–2.7）。背景已经要求同一人有两个 LoF，耗竭对齐的是两条拷贝同时被打掉。UKB 以健康人为主，这个方向作者认为该出现。Beagle 定相得到 673 个基因、962 次事件，必需基因也耗竭，幅度更浅。随机相位 1,792 个基因、17,241 次事件，耗竭消失。按位点独立估算期望次数，LoF 观察明显低于期望；同义中位比值 1.4；错义均 0.8。

UKB 入组平均年龄 56 岁，罕见重症遗传病不该大量进队列。仍有 52 个基因至少出现在一份必需名单里。作者给了三条出路：效应没那么重（一例 ADAM19 敲除伴肺栓塞）；补偿突变（一例写成 CFFTR，应是 CFTR）；相位或 LoF 注释假阳性。

他们把这件事看成生物库尺度筛复合杂合的证明，也当成相位本身的生物学核对。往后可以把 LoF 和错义或调控位点一起筛，burden test 可以带上相位，新测的同人群基因组可以借这套面板贴极稀有位点。Genomics England 那种诊断场景被点名，singleton 的精度仍是限制。同日的 GLIMPSE2 则回答另一半问题：这 150,119 套 haplotype 能不能当低覆盖 imputation 的 reference panel。

补充材料见论文 SI（MOESM1 PDF：Suppl. Figs. 1–4 与 Tables 1–3；MOESM3 xlsx：Supplementary Data 1；MOESM4 xlsx：Fig. 2 source data）。PDF 不进本仓库。

## 数字速查


| 项                          | 值                                                                                                                                                                                               | 出处                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| WGS 全队列                    | 150,119 人；603,925,301 位点（常见 20,662,402，稀有 583,262,899）                                                                                                                                          | Methods；Suppl. Table 1 |
| chr20 评测定相                 | 147,754 人；13,780,190 位点（稀有 13,304,181，常见 476,009）                                                                                                                                               | Suppl. Table 1         |
| WES+芯片                     | 452,644 人；26,199,614 位点（稀有 25,222,097，常见 977,517）                                                                                                                                               | Suppl. Table 1         |
| 芯片质控                       | 670,741 位点 × 486,442 人                                                                                                                                                                          | Suppl. Table 1         |
| 白人英国人 trio / duo           | 芯片 897 / 4,373；WES 719 / 3,104（Methods 写 duo 3,014）；WGS 31 / 432                                                                                                                                | Suppl. Table 1；Methods |
| WGS MAC 11–20 SER          | SHAPEIT5 4.36%；Beagle 8.76%（−50.2%）                                                                                                                                                             | Fig. 2 正文              |
| WES MAC 11–20 SER          | 2.93% vs 5.18%（−42.67%）                                                                                                                                                                         | Fig. 2 正文              |
| WGS MAC 2–5 SER（source）    | SHAPEIT5 9.33%；Beagle 14.61%                                                                                                                                                                    | Source Data Fig. 2a    |
| WGS singleton SER（source）  | SHAPEIT5 35.26%；Beagle 50.71%                                                                                                                                                                   | Source Data Fig. 2a    |
| singleton SER（正文）          | WGS 35.1% / 36.6%；WES 35.2%                                                                                                                                                                     | Results；ED Fig. 3      |
| singleton 非遗传估计            | duo 折 5.26%；trio 孟德尔不一致 4.52%                                                                                                                                                                   | Results；ED Fig. 3      |
| imputation 靶 / panel       | 靶 1,000 英国人；WGS 面板 146,754；WES 面板 446,470                                                                                                                                                       | Fig. 2c,d              |
| MAC 2–5 Δr²                | 约 0.05；作者换算为有效样本量 +5%                                                                                                                                                                           | Results                |
| 置信度 0.99                   | WGS SER 上限约 2%，WES 约 1%；MAC 2–5 保留 >75% / >40%                                                                                                                                                  | Results；ED Fig. 5      |
| chr20 费用（按需 / 竞价, 2022-10） | Beagle £57.82 / £11.56；SHAPEIT5 £65.16 / £13.03                                                                                                                                                 | Suppl. Table 2         |
| 全基因组外推                     | Beagle £2,890 / £578；SHAPEIT5 £3,258 / £651.6                                                                                                                                                   | Suppl. Table 2         |
| chr20 墙钟 / 内存              | Beagle 28:55、501 GB；SHAPEIT5 61:17，并行每份约 9:20，区段均 9.31 / 22.7 GB                                                                                                                                | Suppl. Table 2–3       |
| 复合杂合队列                     | 374,826 人；383,637 高置信 LoF；17,689 基因                                                                                                                                                             | Results                |
| 人均 / 基因均 LoF               | 7.8 / 22.3                                                                                                                                                                                      | Results；ED Fig. 6      |
| Data 1 重算                  | 17,689 基因；2,150 个 `num_inds_2_mut>0`；549 个 `num_ch_events>0`；事件和 779                                                                                                                            | Suppl. Data 1          |
| 复合杂合人数                     | 结果节 766 人；讨论 816 人；Data 1 无个体 ID                                                                                                                                                                | Results vs Discussion  |
| 高置信相位 >0.99                | 441 基因（80%）；614 事件（79%）                                                                                                                                                                         | Results                |
| Beagle 对照                  | 673 基因；962 事件                                                                                                                                                                                   | Results                |
| 随机相位                       | 1,792 基因；17,241 事件                                                                                                                                                                              | Fig. 3a                |
| 观察/期望                      | LoF 明显低于 1；错义均 0.8；同义中位 1.4                                                                                                                                                                     | Fig. 3d                |
| 仍落在必需名单                    | 52 个基因                                                                                                                                                                                          | Discussion             |
| Data 1 事件最多                | OBSCN 12；HMCN2 11；SPTBN5 11；MUC4 9                                                                                                                                                              | Suppl. Data 1          |
| 软件                         | GitHub 全套脚本 [https://github.com/odelaneau/shapeit5（MIT）：phase_common](https://github.com/odelaneau/shapeit5（MIT）：phase_common) / phase_rare / ligate / switch；文档站；Zenodo 10.5281/zenodo.7828479 | Code availability      |




## 我的判断

全基因组一条平均的 SER 和 Beagle 几乎贴在一起，Supplementary Fig. 2 把这一点画死了。两家真正分开的地方是按 MAC 切开的稀有箱子：MAC 11–20 的 4.36% 对 8.76% 印在 Fig. 2 上，Source Data 里 MAC 2–5 是 9.33% 对 14.61%，imputation 的 r² 在 MAC < 500 同向。Beagle 已经把常见位点和稀有位点拆开。SHAPEIT5 多出来的，是给每一个稀有位点单独挑一套既 IBD、又带着次要等位的 conditioning haplotypes。样本少于大约 5 万人时，文中说两家差不显著，别把 UKB 的减幅抄到几千人的队列上。

混杂很硬。真值只来自自报白人英国人 trio / duo，WGS trio 只有 31 个。Axiom 坐标上的 SER 优势，芯片单独定相时又消失，说明优势绑在测序稀有位点上；芯片常见位点上两家打平。WES 的 haplotype scaffold 吃进了芯片常见位点，外显子上的稀有定相带着芯片做成的那套 haplotype。forcing homozygosity 把邻居杂合当成两条都带次要等位，相位依赖邻居，邻居自己也在被估。最大样本上芯片 SER < 0.2% 时，作者承认 switch error 和分型错误分不开，trio 真值也会被父母分型错误弄脏（ED Fig. 2）。

singleton 模型有方向（相对 50% 有二项差），SER 仍在 35% 上下。复合杂合分析把 singleton 全部丢掉，是对的。摘要里「1/100,000 的位点 SER 低于 5%」更贴 MAC 11–20 的印刷数字。

复合杂合用来核对相位有没有生物学方向。Data 1 把 549 / 2,150 / 779 钉死了。个体 ID 被去掉，讨论里的 816 人无法从表格复核；0.22% 跟着 816 走。引用人数时以结果节 766 / 779 为准，讨论的 816 并排注上。事件堆在 OBSCN、黏蛋白这类大基因上，和「非必需 / LoF 耐受」名单同向，549 不宜直接抄进体内验证的非必需目录。UKB 平均入组年龄 56 岁、入组偏健康，耗竭一部分是队列过滤器。52 个仍撞上必需名单的基因，作者自己列了注释错误和相位错误。

Beagle 也能筛出耗竭，只是更浅。复合杂合名单的增量不能全部记成 SHAPEIT5 独有。Delaneau 组自己的读法，是把 SHAPEIT5 和同日的 GLIMPSE2 配成一套：一边把稀有相位估稳，一边让 150,119 套 haplotype 真正能当低覆盖 imputation 的 reference panel。

### 可引用 / 不要当作

可引用：UKB 规模下，SHAPEIT5 相对 Beagle v.5.4 降低稀有位点 SER（WGS MAC 11–20：4.36% vs 8.76%；MAC 2–5 source：9.33% vs 14.61%）；同一批 UKB 面板用 SHAPEIT5 定相，MAC 2–5 的 imputation r² 大约高 0.05；置信度 0.99 可把留下的位点 SER 压到约 2% / 1%，WES 极稀有位点要扔掉一半以上；WES 上 549 个基因出现 LoF 复合杂合，Data 1 与正文一致，相对随机相位和同义对照呈必需基因耗竭。

不要当作：任意队列、任意祖先的通用 SER；singleton 已经能用于诊断或 burden test；549 个基因等于体内验证的非必需基因目录；讨论里的 816 人与结果节 766 人可以混用；没有芯片 haplotype scaffold 的纯 WES 也能复现同一精度；SHAPEIT5 可以脱离同组 GLIMPSE2 / Impute5 单独理解成一套新的群体遗传学理论。

## 📜 原文摘抄

> **EN**: "We demonstrate that SHAPEIT5 phases rare variants with low switch error rates of below 5% for variants present in just 1 sample out of 100,000."
> **中文**: 作者称 SHAPEIT5 能把仅在 100,000 人中出现 1 次的稀有变异定相到 SER 低于 5%。
> 出处：Abstract，p.1243

> **EN**: "As an example, the WGS data for 150,119 UKB samples comprise three orders of magnitude more variants than the Axiom array data, around 96% of them having a minor allele frequency (MAF) below 0.1%."
> **中文**: 150,119 人的 UKB WGS 位点数比 Axiom 芯片高三个数量级，约 96% 的位点 MAF < 0.1%。
> 出处：Introduction，p.1243

> **EN**: "When the conditioning sample is heterozygous, the allele carried by each of its two haplotypes is unknown. In this case, our model assumes that both haplotypes carry the minor allele as done in Beagle v.5.4."
> **中文**: 邻居若是杂合，两条 haplotype 各带哪个等位未知；模型假定两条都带次要等位，与 Beagle v.5.4 相同。
> 出处：Results Overview / Fig. 1 正文，p.1244

> **EN**: "SHAPEIT5 and Beagle v.5.4 phase rare variants in the WGS data (MAC between 11 and 20) with SER of 4.36% and 8.76%, respectively, which is a 50.2% drop."
> **中文**: WGS 上 MAC 11–20 的 SER 为 4.36% 对 8.76%，下降 50.2%。
> 出处：Results，Phasing performance，p.1245

> **EN**: "In the WES dataset, the same variant category is phased by SHAPEIT5 with a switch error rate of 2.93% compared with 5.18% with Beagle v.5.4 (42.67% reduction)."
> **中文**: WES 同一 MAC 档为 2.93% 对 5.18%，降 42.67%。
> 出处：Results，p.1245

> **EN**: "For instance, imputation using the WGS or WES reference panel phased with SHAPEIT5 provides an increase of squared Pearson coefficient of around 0.05 for variants with a MAC between 2 and 5. In an association study, this corresponds to an increase of 5% in effective sample size when testing these variants for association, due only to better reference panel phasing."
> **中文**: MAC 2–5 的平方 Pearson 大约高 0.05；作者将其换算为这些位点关联检验的有效样本量增加 5%，只来自 reference panel 的相位。
> 出处：Results，imputation，p.1245

> **EN**: "From those 2,150 genes, we found 549 (26%) genes with one or more individuals with compound heterozygous LoF variants (Fig. 3a), for a total of 779 gene-individual events (766 distinct individuals; Extended Data Fig. 7 and Supplementary Data 1)."
> **中文**: 2,150 个基因里有 549 个（26%）出现复合杂合 LoF，共 779 次基因–个体事件、766 个不同个体。
> 出处：Results，compound heterozygotes，p.1246

> **EN**: "The minor allele of singletons is then assigned to the target haplotype with the shortest shared segment."
> **中文**: singleton 的次要等位被派给共享片段最短的那条靶 haplotype。
> 出处：Methods，Singleton phasing

> **EN**: "To phase WES data, we first merged it with the unphased SNP array data. The aim of this was to increase the number of common variants that are phased in the first step of SHAPEIT5 … which improves the quality of the haplotype scaffold onto which rare variants are phased, in particular at intergenic regions."
> **中文**: WES 先与未定相芯片合并，为的是增加第一步常见位点，改善稀有位点所挂的 haplotype scaffold，尤其在基因间区。
> 出处：Methods，UKB WES dataset

> **EN**: "O.D. and S.R. developed the method. R.J.H. performed the phasing experiments. S.R. performed the imputation experiments. D.M.R. performed compound heterozygous analyses. … O.D. designed and supervised the study."
> **中文**: Delaneau 与 Rubinacci 做方法；Hofmeister 跑定相；Rubinacci 跑 imputation；Ribeiro 筛复合杂合；Delaneau 设计并监督。
> 出处：Author contributions

> **EN**: "Here, we show that high-quality phasing of rare variants with SHAPEIT5 allows compound heterozygosity to be studied at the biobank-scale level … we found 549 genes predicted to be fully knocked out across 816 UKB individuals out of the 374,826 individuals considered in this study."
> **中文**: 讨论把完全敲除写成 549 个基因、816 人 / 374,826；与结果节 766 人不一致。
> 出处：Discussion，p.1248



## ✍️ 写作学习


| 原句                                                                                                                                                                                                                            | 好在哪                                                     | 可复用                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------ |
| "In an association study, this corresponds to an increase of 5% in effective sample size when testing these variants for association, due only to better reference panel phasing."                                            | 把 Δr² ≈ 0.05 直接换成下游有效样本量，读者不用自己做换算。                     | 定相 / imputation 论文里，先给相关，再写「等于少了多少人」。出处：Results，p.1245 |
| "When the conditioning sample is heterozygous, the allele carried by each of its two haplotypes is unknown. In this case, our model assumes that both haplotypes carry the minor allele as done in Beagle v.5.4."             | 把与对照方法共享的假设说清楚，后面增益才落在「按位点挑选 conditioning haplotypes」上。 | 算法文不要假装每一步都是新的。出处：p.1244                               |
| "Finally, as a control, we attributed the phase of variants randomly, which led to 1,792 compound heterozygous genes and 17,241 events (Fig. 3a), which did not display depletion in essential genes, as expected (Fig. 3b)." | 用乱相位阴性对照证明耗竭来自相位，而不是 LoF 注释本身。                          | 筛 cis/trans 时必须有乱相位对照。出处：p.1247                        |




## 关联

- Rubinacci, Hofmeister, Sousa da Mota, Delaneau. *Nat. Genet.* 55, 1088–1090（2023）。[10.1038/s41588-023-01438-3](https://doi.org/10.1038/s41588-023-01438-3)。同日 GLIMPSE2：同一套 150,119 haplotype 当低覆盖 imputation 的 reference panel。
- Delaneau et al. *Nat. Commun.* 10, 5436（2019）。[10.1038/s41467-019-13225-y](https://doi.org/10.1038/s41467-019-13225-y)。SHAPEIT4，本文常见位点 haplotype scaffold 的前身。
- Rubinacci, Delaneau, Marchini. *PLoS Genet.* 16, e1009049（2020）。[10.1371/journal.pgen.1009049](https://doi.org/10.1371/journal.pgen.1009049)。Impute5，稀有位点 copying 模型的直接来源。
- Rubinacci, Ribeiro, Hofmeister, Delaneau. *Nat. Genet.* 53, 120–126（2021）。[10.1038/s41588-020-00756-0](https://doi.org/10.1038/s41588-020-00756-0)。GLIMPSE v1。
- Browning, Tian, Zhou, Browning. *Am. J. Hum. Genet.* 108, 1880–1890（2021）。[10.1016/j.ajhg.2021.08.005](https://doi.org/10.1016/j.ajhg.2021.08.005)。Beagle v.5.4 two-stage 定相，本文的直接对照。
- Browning & Browning. *Am. J. Hum. Genet.* 110, 161–165（2023）。[10.1016/j.ajhg.2022.11.008](https://doi.org/10.1016/j.ajhg.2022.11.008)。同一组用 Beagle 定相了 150,119 套 UKB 基因组。
- Halldorsson et al. *Nature* 607, 732–740（2022）。[10.1038/s41586-022-04965-x](https://doi.org/10.1038/s41586-022-04965-x)。UKB 150,119 WGS 数据发布。
- McCarthy et al. *Nat. Genet.* 48, 1279–1283（2016）。[10.1038/ng.3643](https://doi.org/10.1038/ng.3643)。HRC 参考面板，Fig. 2c 灰线。
- Sulem et al. *Nat. Genet.* 47, 448–452（2015）。[10.1038/ng.3243](https://doi.org/10.1038/ng.3243)。早期完整敲除目录，讨论里拿 0.22% 对照。
- Karczewski et al. *Nature* 581, 434–443（2020）。[10.1038/s41586-020-2308-7](https://doi.org/10.1038/s41586-020-2308-7)。gnomAD 约束 / 纯合 LoF 耐受名单。
- Durbin. *Bioinformatics* 30, 1266–1272（2014）。[10.1093/bioinformatics/btu014](https://doi.org/10.1093/bioinformatics/btu014)。PBWT。
- Li & Stephens. *Genetics* 165, 2213–2233（2003）。[10.1093/genetics/165.4.2213](https://doi.org/10.1093/genetics/165.4.2213)。copying 模型。
- Schloissnig et al. *Nature*（2025）。[10.1038/s41586-025-09290-7](https://doi.org/10.1038/s41586-025-09290-7)。本地笔记：[2025-schloissnig-korbel-1019-human-long-read-sv-nature](2025-schloissnig-korbel-1019-human-long-read-sv-nature.md)。长读 SV 目录用 SHAPEIT5 定相 164,571 个主位点。
- Wang et al. *Nature*（2026）。[10.1038/s41586-026-10315-y](https://doi.org/10.1038/s41586-026-10315-y)。本地笔记：[2026-wang-yang-1000-chinese-pangenome-nature](2026-wang-yang-1000-chinese-pangenome-nature.md)。华人泛基因组也做 imputation 面板；稀有等位频率和定相是同一类下游。
- Sousa da Mota et al. *Nat. Commun.*（2023）。[10.1038/s41467-023-39202-0](https://doi.org/10.1038/s41467-023-39202-0)。本地笔记：[2023-mota-imputation-ancient-human-nat-commun](2023-mota-imputation-ancient-human-nat-commun.md)。古 DNA imputation（Sousa da Mota 亦出现在 GLIMPSE2）；reference panel 的相位误差会进 GLIMPSE 一类工具。

