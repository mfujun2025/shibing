# 柿饼资讯网（柿饼.cn / xn--9vvp51i.cn）

中文柿饼资讯网站：行业资讯、产地动态、市场行情、健康养生、美食食谱、柿饼知识六大栏目。

## 站点结构

```
/
├── index.html                 # 首页（Hero + 栏目速览 + 最新资讯 + 产地特写）
├── about.html                 # 关于本站 / 投稿合作 / 免责声明
├── category-{slug}.html       # 6 个栏目页：xingye/chandi/shichang/jiankang/meishi/zhishi
├── news/                      # 文章页（拼音 slug 命名）
│   ├── shibing-chanye-qushi.html
│   └── ...（共 12 篇首发文章）
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

1. 按 `seo-article-writer` 技能流程写正文，输出为 `news/<拼音slug>.html`，页面结构参考现有文章（含 JSON-LD 结构化数据、canonical、meta 描述）。
2. 在 `index.html` 的「最新资讯」区按时间倒序登记卡片，并在对应栏目页 `category-*.html` 登记。
3. 在 `sitemap.xml` 追加新 URL（`<lastmod>` 填文章日期）。
4. 提交推送，GitHub Actions 自动构建部署到 Pages。

## 部署

仓库：`https://github.com/mfujun2025/shibing`
托管：GitHub Pages（`.github/workflows/deploy.yml` 自动构建，推送到 `main` 即发布）。

### 首次配置自定义域名（柿饼.cn）

1. 仓库 Settings → Pages → Custom domain 填入：`xn--9vvp51i.cn`（GitHub Pages 的 CNAME 需用 ASCII punycode），等待签发 HTTPS。
2. 域名 DNS（在域名注册商处设置）：
   - 若域名托管支持 A 记录：解析到 GitHub Pages 当前 IP（`185.199.108.153` / `185.199.109.153` / `185.199.110.153` / `185.199.111.153`）。
   - 或 CNAME 指向 `mfujun2025.github.io`。
   - 也可改用 Cloudflare Pages：把仓库导入 Cloudflare，构建输出目录为根目录，再绑定 `柿饼.cn`。
3. 验证：浏览器访问 https://柿饼.cn 或 https://xn--9vvp51i.cn 返回 200 后即完成。

## 本地预览

直接用浏览器打开 `index.html` 即可（静态页面，无构建依赖；改 `scripts/build_site.py` 后运行 `python scripts/build_site.py` 重建全站）。

## 说明

- 图片素材全部为 AI 生成原创图，本站可自由商用。
- 健康/行情类内容为一般性资讯，站内已注明不构成医疗或投资建议。
- ICP 备案信息待主体办理后更新（footer 与页面中为占位文案）。
