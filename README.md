# Venera Source Hub

Venera 漫画源仓库模板，包含 `index.json`、JS 源、取证/生成/检查工具和 GitHub Actions。

添加到 Venera：
`https://raw.githubusercontent.com/ChopDream/venera-source-hub/main/index.json`

工具：
`python3 tools/venera_source.py check`
`python3 tools/venera_source.py check --urls`
`python3 tools/venera_source.py search https://漫画站.example 漫画关键词`
`python3 tools/venera_source.py scaffold https://漫画站.example --name 我的漫画站 --key mysite`
`python3 tools/venera_source.py inspect example.js`

search 会把实际抓到的首页、搜索页和报告保存到 evidence/；scaffold 只生成待验证模板，不猜测解析器。

## 已收录漫画源

| 名称 | key | 文件 | 版本 |
|---|---|---|---|
| 包子漫画 | baozi | baozi.js | 1.1.6 |
| 禁漫天堂 | jm | jm.js | 1.4.0 |

来源：`venera-app/venera-configs`（上游 commit d8a71168，2026-09-07）。此处为镜像收录并同步上游修复；每个源的 `url` 已指向本仓库，便于自更新。

`templates/example.js` 为空模板，不参与 `index.json`，仅作新建源时参考。

## 更新已有源

```bash
git clone --depth 1 https://github.com/venera-app/venera-configs.git /tmp/upstream
cp /tmp/upstream/baozi.js ./baozi.js
python3 tools/check.py
```

同步上游后需把源文件里的 `url` 改回本仓库地址，并同步 `index.json` 的 `version`。

## 修复记录

### 2026-10-03

| 源 | 版本 | 问题（实测） | 修复 |
|---|---|---|---|
| 包子漫画 | 1.1.6 → 1.1.7 | 默认域名 `bzmgcn.com`、`baozimhcn.com` 均 302 跳转到 `www.baozimh.com` 后返回 403，搜索/分类全失败 | 默认域名改为 `webmota.com`，并把可用域名排在前面（`webmota.com` / `kukuc.co` / `twmanga.com` / `dinnerku.com`，实测搜索 200 且 `div.comics-card` 命中 142 处） |
| 禁漫天堂 | 1.4.0 → 1.4.1 | 内置备用线路 4 个全部失效（`cdnsha.org` / `cdnaspa.cc` / `cdnntr.cc` DNS 解析失败，`cdntwice.org` 返回 404）；若在线线路列表拉取失败则完全不可用 | 备用线路更新为当前在线列表 `www.cdnhjk.net` / `www.cdngwc.cc` / `www.cdngwc.net` / `www.cdngwc.club`（实测搜索接口 200，解密成功，total=710） |
| 禁漫天堂 | 1.4.1 | `JM.apiDomains` 无初始值，关闭“启动时刷新域名”后 `baseUrl` 为 undefined | 增加 `static apiDomains` 初值，与备用线路一致 |
