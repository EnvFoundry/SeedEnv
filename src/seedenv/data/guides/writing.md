# Research writing · 研究写作

LaTeX 论文编译与文献引用。

1. 优先连接已有 TeX 工具链；Origo 可以按需准备 research-tex。用 latexmk 驱动编译并读取编译输出。
2. 中文文稿使用合适的 XeLaTeX/LuaLaTeX 与中文字体；保留 .tex、.bib、图表和目标模板。
3. 公式、图表与参考文献保持来自实际研究产物，文稿组织由研究问题决定。

查看组件与准备方式：`seedenv show writing`。准备后用 `seedenv entry COMPONENT` 获取实际命令。通过该解释器或程序使用完整上游接口。

上游文档：

- https://www.tug.org/texlive/
- https://yihui.org/tinytex/
