# Manuscript templates · 中英文文稿模板

List layouts with `seedenv templates`, optionally `--language zh`, `--form article`
or `--style compact`. `standard`, `compact` and `submission` describe layout
families, not current approval by a journal. Follow the actual submission rules.

Copy one template without preparing software:

```sh
seedenv manuscript standard-article-zh --output my-paper
```

Edit `my-paper/main.tex`; put figures under `figures/`. Add actual bibliography
records in `refs.bib` when needed. Existing output directories are never replaced.
The 22 choices share identical sources where appropriate. Keep a manuscript in
its existing format if a conversion would not help the author.

For compilation, connect an existing TeX or prepare `writing`, then run
`seedenv build my-paper/main.tex`. The PDF and source remain in the project,
while compiler intermediates go into its `build/` directory. Templates use
LuaLaTeX; the build command also accepts XeLaTeX for compatible manuscripts.

模板可以单独取得，不触发 Python 科研包或 TeX 下载。按文稿类型、语言、排版选择；
已有项目继续使用原文稿。模板中的示例文字、图框和作者信息需要按实际研究替换。
只有需要编译且没有合适环境时，才准备 `writing`。
