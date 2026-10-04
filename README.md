# Venera 漫画源仓库

在 Venera 的「仓库地址」中填入：

```text
https://raw.githubusercontent.com/ChopDream/venera-source-hub/main/index.json
```

## 收录源

| 名称 | 站点 | 可在「源设置」中切换 |
| --- | --- | --- |
| 包子漫画 | 包子漫画 | 主域名、简繁、图片资源站、图片质量 |
| 禁漫天堂 | 禁漫天堂 | 分流线路、图片线路、启动时刷新域名 |
| 紳士漫畫 | wn09.shop | 域名选择、自定义域名（默认 wn09.shop）、启动时刷新域名 |
| 拷贝漫画 | mangacopy.com | API 地址、CDN 线路、图片质量、搜索方式 |
| MYCOMIC | mycomic.com | 分类页按国家、题材、受众、年份筛选 |
| nhentai | nhentai.net | 搜索语言、排序等选项 |
| momon:GA | momon-ga.com | 图片线路（3 号线 / 2 号线）、搜索排序 |

## 使用

1. 复制上面的地址
2. Venera → 我的 → 漫画源 → 添加仓库 → 粘贴地址
3. 单个源的可调项：漫画源 → 该源 → 设置

> jsDelivr 镜像（`https://cdn.jsdelivr.net/gh/ChopDream/venera-source-hub@main/index.json`）对分支内容最长缓存 12 小时，更新源时优先用上面的 raw 地址。

## 工具

```bash
python3 tools/check.py                              # 校验索引与源文件
python3 tools/search.py <站点URL> <关键词>            # 抓取站点样本到 evidence/
python3 tools/scaffold.py <站点URL> <名称> <key>      # 生成新源模板
```

`check.py` 校验：索引与源文件元数据一致、key 不重复、class 声明符合 Venera 解析规则、JS 语法（`node --check`）。

## 来源

源文件取自 `venera-app/venera-configs`，镜像收录并同步修复。漫画内容与图片版权归各站点及原作者所有，本仓库仅提供客户端解析脚本。
