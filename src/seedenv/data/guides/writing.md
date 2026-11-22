# Scientific Writing · 科研写作与编译

Use `writing-methods` for composition and `writing-templates` for editable
English/Chinese layouts. Reading guidance and copying templates need no TeX.
Continue the author's existing manuscript and format when suitable.

Reuse an installed TeX first: `seedenv bind tool-tex -- /path/to/latexmk`.
The toolchain needs latexmk, LuaLaTeX, XeLaTeX, pdfLaTeX, BibTeX and the Chinese
classes/fonts used by the supplied layouts. Binding does not modify that install.
`seedenv prepare writing` connects a suitable PATH installation or prepares
TinyTeX locally. A new installation includes the template packages, BibLaTeX and
Biber. Unix execution hosts need Perl. No compiler is downloaded at application
startup. Software stays in the selected user's persistent SeedEnv directory.

```sh
seedenv manuscript standard-article-en --output paper
seedenv build paper/main.tex --output paper/paper.pdf
```

Keep actual figures, bibliography and editable sources together. Compilation uses
the registered toolchain; intermediate files stay under `paper/build/`. Resolve a
missing package in an existing installation through its upstream manager.

In a product, execute preparation on the host that owns the manuscript. Use the
returned `command`, `commands` and optional `environment` to register the toolchain.
`seedenv build` and `seedenv run` apply those bindings directly.

已有 TeX 优先连接；缺少时按需准备，后续会话复用。编译器、宏包与字体属于软件环境，
正文、文献与图表属于研究项目。写作方法与模板分别选择，不强制安装全部研究软件。

Upstream: https://github.com/rstudio/tinytex-releases · https://www.tug.org/texlive/
