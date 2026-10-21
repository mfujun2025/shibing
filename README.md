# 柿饼资讯网（柿饼.cn / xn--9vvp51i.cn）

中文柿饼资讯网站：行业资讯、产地动态、市场行情、健康养生、美食食谱、柿饼知识六大栏目。

## 站点结构

```
/
├── index.html                 # 首页（Hero + 栏目速览 + 最新资讯 + 产地特写）
├── about.html                 # 关于本站 / 域名出售出租（柿饼.cn、柿饼.中国、富平柿饼.cn）/ 投稿合作 / 免责声明
├── category-{slug}.html       # 6 个栏目页：xingye/chandi/shichang/jiankang/meishi/zhishi
├── news/                      # 文章页（拼音 slug 命名，共 17 篇）
│   ├── shibing-chanye-qushi.html
│   └── ...（新增文章在 scripts/build_site.py 的 ARTICLES 中登记后重跑生成）
├── css/style.css              # 全站样式（柿红·柿叶绿·霜纸色）
├── images/                    # 图片素材（AI 生成原创，可商用）
├── favicon.svg
├── sitemap.xml                # 站点地图（新文章需同步追加）
├── robots.txt
├── 404.html
├── CNAME                      # 自定义域名（punycode：xn--9vvp51i.cn）
└── scripts/build_site.py      # 页面生成脚本（改数据后可重跑重建全站）
```

## 新增文章流程（沿用 SEO 发文工作流）

1. 按 `seo-article-writer` 技能流程写正文。
2. 在 `scripts/build_site.py` 的 `ARTICLES` 列表中追加文章数据（slug / cat / date / title / cover / summary / body），图片放到 `images/`。
3. 运行 `python scripts/build_site.py`，脚本会自动重建首页、栏目页、文章页并更新 `sitemap.xml`。
4. 提交推送，GitHub Pages 分支部署会自动发布。

## 部署

仓库：`https://github.com/mfujun2025/shibing`
访问地址：
- 自定义域名：`https://柿饼.cn`（即 `https://xn--9vvp51i.cn`，已配置 Cloudflare 代理）
- GitHub Pages：`https://mfujun2025.github.io/shibing/`

当前部署方式：GitHub Pages 分支部署（Settings → Pages → Deploy from branch → main 根目录），推送到 `main` 即自动发布；仓库内 `.github/workflows/deploy.yml` 为可选的 Actions 部署方案（推送该文件需要 PAT 具备 `workflow` 权限）。

### 自定义域名（柿饼.cn，已完成）

- 仓库根目录 `CNAME` 内容为 `xn--9vvp51i.cn`（GitHub Pages 需用 ASCII punycode）。
- DNS：A 记录指向 `185.199.108.153` / `185.199.109.153` / `185.199.110.153` / `185.199.111.153`，或 CNAME 指向 `mfujun2025.github.io`；当前由 Cloudflare 代理（橙色云朵）。
- HTTPS 已由 Cloudflare 提供。

## 本地预览

直接用浏览器打开 `index.html` 即可（静态页面，无构建依赖；改 `scripts/build_site.py` 后运行 `python scripts/build_site.py` 重建全站）。

## 说明

- 图片素材全部为 AI 生成原创图，本站可自由商用。
- 健康/行情类内容为一般性资讯，站内已注明不构成医疗或投资建议。
- ICP 备案信息待主体办理后更新（footer 与页面中为占位文案）。
