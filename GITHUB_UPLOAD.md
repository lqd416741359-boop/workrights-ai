# GitHub 上传设置

这份文件集中保存仓库发布时需要填写的内容。上传仓库文件时，请上传 `workrights-ai` 文件夹内的全部内容，包括以点开头的 `.gitignore`；不要把外面的 ZIP 上传到仓库。

## 1. 新建仓库

在 GitHub 右上角选择 **New repository**，使用以下设置：

- **Repository name：** `workrights-ai`
- **Description：** `中国大陆劳动权益研究与维权准备 Skill：梳理事实、核验法律依据、规划证据并估算合法请求。`
- **Visibility：** `Public`
- **Add a README file：** 不勾选
- **Add .gitignore：** 选择 `None`
- **Choose a license：** 选择 `None`

原因：本文件夹已经包含 `README.md`、`.gitignore` 和 `LICENSE`，GitHub 不需要再次生成。

## 2. 上传文件

仓库创建后选择 **Add file → Upload files**：

1. 打开本地 `workrights-ai` 文件夹。
2. 全选文件夹里面的全部内容，而不是上传外层文件夹本身。
3. 将全部内容拖到 GitHub 上传区域。
4. 确认页面中包含 `agents`、`assets`、`references`、`scripts`、`SKILL.md`、`README.md`、`LICENSE`、`.gitignore` 和本文件。
5. Commit message 填写：`Initial release of WorkRights AI`
6. 选择 **Commit changes**。

## 3. About 简介

在仓库首页右侧 **About** 区域点击齿轮，填写：

- **Description：** `中国大陆劳动权益研究与维权准备 Skill：梳理事实、核验法律依据、规划证据并估算合法请求。`
- **Website：** 留空
- **Use your GitHub Pages website：** 不勾选
- **Releases：** 可保留默认设置
- **Packages：** 可保留默认设置

## 4. Topics 标签

在 About 设置中加入以下 Topics：

```text
codex-skill
ai-skill
employment-law
labor-law
legal-research
china
prc
worker-rights
```

## 5. Social Preview 封面

README 顶部会自动显示 `assets/cover.png`。

如需在分享 GitHub 仓库链接时显示专用封面：

1. 打开仓库的 **Settings**。
2. 进入 **General**。
3. 找到 **Social preview**。
4. 上传 `assets/social-preview.png`。
5. 保存设置。

`social-preview.png` 只需要保留在仓库中一份，不要重复上传或改名。

## 6. 推荐仓库标题与版本

- 仓库名称：`workrights-ai`
- README 主标题：`WorkRights AI`
- 首个 Release 标签：`v1.0.0`
- Release 标题：`WorkRights AI v1.0.0`
- Release 简介：`首个公开版本：支持中国大陆劳动争议事实梳理、法律研究、证据规划、金额估算和咨询摘要准备。`

第一次上传时不必立即创建 Release；仓库文件确认无误后再创建即可。

## 7. 上传后检查

- README 顶部封面是否正常显示
- 中文是否没有乱码
- `SKILL.md` 是否位于仓库根目录
- `agents/openai.yaml` 是否存在
- `assets/cover.png` 与 `assets/social-preview.png` 是否能打开
- `LICENSE` 是否显示为 MIT License
- 仓库中是否没有 ZIP、临时文件或重复嵌套的 `workrights-ai/workrights-ai` 目录
