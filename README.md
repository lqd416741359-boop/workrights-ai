<div align="center">

![WorkRights AI 封面](assets/cover.png)

# WorkRights AI

**中国大陆劳动权益研究与维权准备 Skill**

![License](https://img.shields.io/badge/license-MIT-c59a55)
![Scope](https://img.shields.io/badge/scope-中国大陆劳动争议-b3262e)
![Language](https://img.shields.io/badge/language-中文-12304a)
![Status](https://img.shields.io/badge/status-v1.0-2f855a)

</div>

## 项目简介

WorkRights AI 用于协助劳动者梳理中国大陆劳动争议：整理事实与时间线、识别潜在争议点、检索并核验现行法律依据、建立证据清单、在条件充分时估算金额，并为协商、调解、仲裁或专业咨询准备结构化材料。

它不会冒充律师、法律援助机构或政府部门，也不会保证胜诉或赔偿结果。

## 能做什么

- 梳理劳动合同、解除或辞职、工资、加班、休假、社保等事实
- 区分已核实规则、事实推断、待核实问题和现实选择
- 优先查询国家法律法规数据库、政府、人社部门和法院等官方来源
- 识别可能遗漏但有事实基础的合法请求
- 建立“待证明事实—现有证据—缺失证据—控制方”的证据表
- 展示计算输入、公式、假设、结果范围和不确定因素
- 生成便于向律师、法律援助、工会或主管部门咨询的摘要

## 使用示例

```text
请用 $workrights-ai 帮我分析：我在上海工作三年，公司口头通知我明天不用来了，
没有给书面解除通知。我月工资为 12000 元，目前有哪些关键问题，需要保存什么证据？
```

Skill 会先补齐可能改变结论的关键事实，再进行法律检索与分析。涉及现行法律、期限、地方标准或金额时，应以分析当日的官方来源为准。

## 安装

将整个 `workrights-ai` 文件夹复制到 Codex 的 Skills 目录，保持目录结构不变，然后重新加载或重启 Codex。

```text
workrights-ai/
├── agents/openai.yaml
├── assets/
│   ├── cover.png
│   ├── social-preview.png
│   └── report-template.md
├── references/
├── scripts/claim_calculator.py
├── .gitignore
├── LICENSE
├── GITHUB_UPLOAD.md
├── README.md
└── SKILL.md
```

> 不同版本或安装方式的 Skills 路径可能不同，请以你当前 Codex 版本的官方说明为准。

## 资料核验原则

本 Skill 不内置固定不变的法条结论，而是在具体任务中核验现行规则。优先使用全国人大及国家法律法规数据库、中国政府网、人力资源和社会保障部、最高人民法院以及相关地方政府、人社部门和法院的公开资料。

尤其要注意司法解释、地方工资标准、仲裁时效和地方裁审口径可能变化；搜索摘要或非官方转载不能直接作为关键结论的依据。

## 金额计算脚本

`scripts/claim_calculator.py` 只负责十进制金额运算，不判断用户是否依法享有某项请求。计算前必须先核实适用规则与事实。

## 重要声明

本项目仅用于一般性法律信息研究、事实整理和维权准备，不构成法律意见，不建立律师—客户关系，也不能替代持证律师、法律援助机构、工会或有关主管部门针对具体案件提供的帮助。法律具有时效性和地域差异；在签署文件、辞职、放弃权利、和解或临近期限前，建议及时寻求专业协助。

## License

本项目采用 [MIT License](LICENSE)。封面图为本仓库配套制作，可随项目在 MIT License 条款下使用。

## GitHub 发布

仓库名称、简介、Topics、Social Preview 和逐步上传方法已经集中写在 [GITHUB_UPLOAD.md](GITHUB_UPLOAD.md)。
