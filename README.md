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
