# Bibliographies · 参考文献编排

Keep actual references in `refs.bib`, with stable citation keys. Use DOI metadata
from `references` to locate a work, then read the relevant source before using it
to support a claim. Preserve titles, author names and identifiers.

The included layouts use BibTeX/natbib, driven by latexmk. For an existing
BibLaTeX project, retain its chosen backend; managed TinyTeX also includes Biber.
An externally connected installation may need that extra program. This module
reuses `tool-tex`; choosing it alongside `writing` creates one toolchain.

文献记录与文稿放在同一项目。已有引用体系继续使用；按照实际期刊要求调整样式。
元数据检索、阅读原文、正文引用和文献排版各有用途。引用实际阅读的来源。
