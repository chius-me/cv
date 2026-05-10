# cv

Yao Chius 的简历，使用 [RenderCV](https://github.com/rendercv/rendercv) 生成。

## 文件

- `cv.yaml`: 简历内容和 RenderCV 样式配置。
- `rendercv_output/`: 运行 RenderCV 后生成的 PDF、HTML、Markdown 和 Typst 文件。

## 安装 RenderCV

推荐使用 `pipx`：

```bash
pipx install "rendercv[full]"
```

也可以使用 `pip`：

```bash
python -m pip install "rendercv[full]"
```

如果你使用 `uv`，也可以不安装到全局，直接运行：

```bash
uvx --from "rendercv[full]" rendercv render cv.yaml
```

## 生成简历

在仓库根目录运行：

```bash
rendercv render cv.yaml
```

默认输出会写入 `rendercv_output/`。

## 编辑内容

先从 `cv.yaml` 的占位信息开始替换：

- `cv.name`、`cv.email`、`cv.social_networks`: 个人信息和链接。
- `cv.sections.education`: 教育经历。
- `cv.sections.research_experience`: 科研经历。
- `cv.sections.publications`: 论文或报告。
- `cv.sections.projects`: 项目。
- `cv.sections.skills`: 技能。

这个示例偏学术 CV，用于熟悉 RenderCV 的 YAML 结构。真实投递前请删除占位内容并检查联系方式。
