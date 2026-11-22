# Scientific Python · 科研 Python 基础

Prepare `scientific-python` for a reusable NumPy, SciPy, SymPy, Matplotlib and
pandas environment. Select `numerical-computing`, `symbolic-mathematics` or
`scientific-plotting` alone for a smaller installation. Once the common base is
prepared or bound, those modules reuse it. Specialist dependencies stay optional.

Use `seedenv discover scientific-python --python /path/to/python` to inspect a
known interpreter, then bind `python-science` to that actual command. In Origo,
the host can supply its existing interpreters through `prepare-request`.
SeedEnv creates an isolated venv when a selected component has no binding.
The product's service interpreter supplies Python, not an implicit scientific
package inventory; installing the research base does not modify that service.

Use `seedenv entry python-science` and run the returned command with your script.
Keep the program, units, input data and results in the research project. Use the
full upstream APIs; the included fitting program is an editable starting point.
For a notebook, select its actual research interpreter as the kernel. Installing
Jupyter separately does not give every kernel the same packages.

The same preparation can be retried after interruption; completed components
and the unfinished Python destination are retained. An external interpreter is
connected in place. Prepare differing dependencies separately instead of changing
an environment used by an active calculation.

选择 `scientific-python` 准备通用计算基础；只需要数值计算、符号数学或绘图时，
可以分别选择对应模块。已有基础环境可直接绑定复用。研究代码和数据保存在项目中，
解释器和软件保留在用户研究空间。笔记本要选择实际具备所需软件的内核。

Upstream: https://scipy.org/ · https://numpy.org/doc/ · https://docs.sympy.org/
