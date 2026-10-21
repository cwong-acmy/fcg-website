# FCG 官网博客：交接说明（技术团队）

**日期：** 2026-10-21
**负责人：** Crystal Wong（Marketing）
**代码仓库：** `cwong-acmy/fcg-website`，分支 `codex/blog`（基于 `codex/drafts`，审查后合并回 `codex/drafts`）
**适用范围：** 官网改版项目（静态 HTML 站点）。目前线上的 fusionconnectgroup.com 仍是 Wix，**本次不涉及 Wix**。博客将随新官网一起上线。

---

## 1. 一句话总结

新官网增加了博客：每个页面的导航栏和页脚都有 Blog 入口，首页和产品页有文章推荐区，每篇文章有独立页面，手机端菜单已修好。所有博客内容来自一个数据文件 `blog/posts.json`，运行一条命令即可生成全部页面。

**需要你们做两件事：**
1. 审查、合并并部署本次改动（第 2 至第 6 节）。
2. 回复第 7 节的问题：**你们希望以后如何上传文章？**

---

## 2. 改了什么

| 改动 | 说明 |
|---|---|
| 导航栏、页脚统一 | 原来 11 个页面各自复制一份导航和页脚（`_shell/` 里的版本已过时）。现在以 `_shell/nav.html`、`_shell/footer.html` 为唯一来源，由脚本同步到各页面。导航栏在 About 后面新增 Blog（Products · Network · Developer · About · Blog），页脚 Company 栏新增 Blog。 |
| 手机端菜单修复 | 原来手机端的菜单按钮只跳转到页面内的 `#capabilities`，**手机用户无法访问其他页面**。现在点击会打开完整菜单（Products、Network、Company 三组，含 Blog），按 Esc 或点击链接即关闭。 |
| 博客首页 `blog.html` | 标题、订阅框、话题筛选（可分享链接，如 `blog.html?topic=ai`）、置顶文章、文章卡片网格。 |
| 文章页 `blog/<slug>.html` | 面包屑、标题、作者、配图、680px 阅读栏、产品 CTA 卡片、"Keep reading" 相关文章。由模板 `blog/_post.html` 生成。 |
| 首页 | 页脚上方新增 "Latest from the blog"（最新 3 篇）。 |
| 产品页（9 个：`corporate-booking-tool`、`ai-booking-tool`、`agreeease`、`atlas`、`glink`、`flink`、`addn`、`payment`、`developer`） | 在 Closing CTA 上方新增 "Related reading"，优先显示与该产品相关的文章，不足 3 篇时用最新文章补齐。 |
| SEO | canonical、Open Graph、BlogPosting 结构化数据（JSON-LD）、RSS（`blog/feed.xml`）。草稿文章自动加 `noindex`，且不进入 RSS。 |
| 无障碍与对比度 | 灰色日期文字、浅色模式下橙色 "LIVE.NETWORK" 标签的对比度已达标（WCAG AA）；页脚文字由 10.4px 改为 12px；按钮点击区域 44px；支持"减少动态效果"系统设置。 |

**刻意没有改动：** `components.html`（设计参考页）和 `nav-preview.html`（临时预览页）不参与同步；`about.html` 只同步导航和页脚，不加文章推荐区；`_shell/head.html` 未改动。

**页面正文未改动：** 11 个页面中，除导航、页脚、文章推荐区和 head 中新增的一行 CSS 引用外，其余内容与 `codex/drafts` 逐字节一致（已用脚本核对）。

---

## 3. 新增与修改的文件

**新增**
- `blog.html`：博客首页
- `blog/posts.json`：**全部文章数据（唯一需要日常编辑的文件）**
- `blog/_post.html`：文章页模板
- `blog/*.html`、`blog/feed.xml`：脚本生成，**请勿手动编辑**
- `_shell/blog-head.html`：博客页面共用的 head
- `tools/build-site.py`：构建脚本（仅用 Python 标准库，无需安装依赖）
- `assets/css/fcg-blog.css`、`assets/css/fcg-chrome.css`（后者复制自现有页面 head 中的内联样式）
- `assets/js/fcg-nav.js`（手机菜单、主题切换、当前页高亮）、`assets/js/fcg-blog.js`（话题筛选、订阅框）

**修改**
- 11 个页面：`index.html`、`about.html`、`addn.html`、`agreeease.html`、`ai-booking-tool.html`、`atlas.html`、`corporate-booking-tool.html`、`developer.html`、`flink.html`、`glink.html`、`payment.html`。只改动导航、页脚、博客推荐区，以及 head 中新增的一行 CSS 引用。
- `_shell/nav.html`、`_shell/footer.html`：更新为现有页面的最新版本，并加入 Blog 和手机菜单。**现在是构建来源**，里面的 `{{root}}` 由脚本替换。
- `assets/css/fcg-brand-theme.css`：新增手机菜单样式，以及浅色模式下 LIVE 标签的颜色变量 `--fcg-live-text`
- `.vercelignore`：新增 `HANDOVER-BLOG.md`（本文件不对外发布）

**说明：** `codex/blog` 分支只包含本次改动，可以直接审查整个分支的 diff。

---

## 4. 构建方法

需要 Python 3.9 或以上版本，无第三方依赖。

```bash
# 生成或更新所有页面
python3 tools/build-site.py

# 检查是否有页面未更新（适合放进 CI，未同步时返回 1）
python3 tools/build-site.py --check
```

脚本只替换以下标记之间的内容，页面其他部分不受影响：

| 标记 | 内容 |
|---|---|
| `<!-- SHARED:NAV -->` 至 `<!-- /SHARED:NAV -->` | 导航栏、手机菜单 |
| `<!-- SHARED:FOOTER -->` 至 `<!-- /SHARED:FOOTER -->` | 页脚 |
| `<!-- BLOG:LATEST -->`（首页）、`<!-- BLOG:RELATED -->`（产品页） | 文章推荐区 |
| `<!-- BLOG:TAGS -->`、`<!-- BLOG:CARDS -->`（`blog.html`） | 话题按钮、文章卡片 |

**规则：** 要改导航或页脚，请改 `_shell/nav.html` 或 `_shell/footer.html`，然后运行脚本。直接改页面里的导航，下次构建时会被覆盖。

**建议：** 在 CI 中加入 `python3 tools/build-site.py --check`，防止有人只改了数据却没有重新生成页面。

---

## 5. 发文流程（当前方案）

1. 编辑 `blog/posts.json`，新文章加在最前面（第一篇会自动成为置顶文章）。
2. 配图放在 `assets/images/` 下，路径不能含空格或引号。文件不存在时脚本会报错停止。
3. 运行 `python3 tools/build-site.py`。
4. 本地预览，然后提交并部署。

**字段说明**

| 字段 | 必填 | 说明 |
|---|---|---|
| `slug` | 是 | 网址名，只能用小写字母、数字、连字符。上线后不要改（会产生死链）。 |
| `title`、`excerpt` | 是 | 标题、摘要（摘要用于卡片、SEO 描述、RSS）。 |
| `topic` | 是 | 主话题：`product`、`engineering`、`ai`、`industry`、`company` 之一。 |
| `tags` | 是 | 筛选用话题，可多个，取值同上。 |
| `minutes` | 是 | 阅读时长（分钟）。 |
| `image` | 是 | 配图路径。图标类 SVG 请加 `"contain": true`，避免被裁切拉伸。 |
| `author`、`role` | 是 | 作者与职位。 |
| `products` | 否 | 关联产品页的文件名（不含 `.html`），例如 `["atlas"]`。文章会出现在这些产品页的 "Related reading" 中。 |
| `cta` | 是 | 文章底部的产品卡片：`title`、`text`、`href`、`label`。 |
| `draft` | 否 | `true` 时为草稿：页面显示草稿提示，加 `noindex`，不进 RSS。 |
| `date` | 否 | `YYYY-MM-DD`。正式发布时请填写。 |
| `body` | 是 | 正文 HTML（由团队编写，脚本不做过滤），可用 `<p>`、`<h2>`、`<ul>`、`<a>`。 |

**删除或改名文章时：** 脚本会提示旧页面成为孤立文件（orphan），请手动删除该文件。

**现状：** 目前 7 篇文章均为**占位内容**（`draft: true`），正式文章由 Marketing 提供。

---

## 6. 上线前检查清单

- [ ] 审查 `codex/blog` 分支 diff 后合并到 `codex/drafts`
- [ ] `python3 tools/build-site.py --check` 返回 0
- [ ] 桌面（1440px）与手机（375px）都检查：博客首页、任一文章页、首页、任一产品页
- [ ] 手机菜单能打开、关闭，链接全部可用
- [ ] 浅色、深色模式都正常
- [ ] 浏览器控制台无报错
- [ ] **部署（重要）：** Vercel 项目 `fcg-website` 已连接 GitHub，**生产分支是 `main`**，推送到 `main` 会立即自动部署到 fcg-website-one.vercel.app。目前线上版本是 2026-08-26 通过 Vercel CLI 从 `codex/drafts` 手动部署的，而 `main` 仍是 5 月的旧版本。**在 Marketing 确认上线之前，请勿推送或合并到 `main`**，否则会把旧版本或未完成的博客发布上线。
- [ ] 上线流程建议：`codex/blog` 审查后合并到 `codex/drafts`；正式文章到位并经 Marketing 确认后，再将 `codex/drafts` 合并到 `main` 触发生产部署。部署前请先运行 `python3 tools/build-site.py`。
- [ ] 预览：推送 `codex/blog` 已自动生成 Vercel 预览部署：https://fcg-website-git-codex-blog-crystalwong-accomycoms-projects.vercel.app （始终指向 `codex/blog` 的最新版本，需登录 Vercel 团队账号查看），不影响线上。
- [ ] 确认正式域名：`tools/build-site.py` 中的 `SITE` 目前为 `https://www.fusionconnectgroup.com`，用于 canonical、OG、RSS。如有不同请修改后重新构建。
- [ ] 订阅框目前**未接入任何服务**，提交后只显示"尚未开放、邮箱未保存"。接入邮件服务前请保持现状，不要显示虚假的"订阅成功"。
- [ ] 占位文章在正式文章到位前**不要**改成 `draft: false`

---

## 7. 需要你们回复的问题：如何上传文章

目前的方式是编辑 JSON 再运行脚本，对技术团队可行，但 Marketing 无法自行发文。请评估并回复以下问题：

1. **谁来发文？** 由技术团队代发，还是 Marketing 自行发布？
2. **用什么方式上传？** 你们倾向哪种方案（或其他建议）：
   - **A.** 保持现状：编辑 `blog/posts.json`，通过 Git PR 提交，合并后自动部署。
   - **B.** 接入 Headless CMS（例如 Strapi、Sanity、Contentful 或 Decap CMS），Marketing 在后台写文章，构建时拉取内容。
   - **C.** 从飞书文档导出（Marketing 在飞书写稿），再由脚本或流程转换为 `posts.json`。
   - **D.** 其他方案，请说明。

   **Marketing 的初步建议（请技术团队评估后决定）：** Marketing 已有正式文章内容，希望能自行发布，因此倾向**基于 Git 的 CMS**。文章已存放在仓库中的 `blog/posts.json`，这类 CMS 只是提供一个网页编辑界面来修改这个文件，不需要数据库或服务器，每次保存都是一次 Git 提交，可随时回滚。

   | 方案 | 优点 | 需要注意 |
   |---|---|---|
   | **Pages CMS**（[pagescms.org](https://pagescms.org)，Marketing 首选） | 免费、托管版无需部署；用 GitHub 登录；只需在仓库加一个配置文件 `.pages.yml` | 尚未验证能否直接编辑 `posts.json` 这种"文章数组"格式；如不支持，可能需要把每篇文章拆成单独文件，并相应修改 `build-site.py` |
   | **Decap CMS** | 免费、开源、成熟 | 部署在 Vercel 时需要另外搭建 GitHub OAuth 登录服务 |
   | **TinaCMS** | 可视化实时编辑体验好 | 配置较多；超出小团队规模需付费 |
   | **Sanity / Contentful**（Headless CMS） | 适合多人协作、多语言 | 需要改造构建流程，构建时从 API 拉取内容 |

   **无论选哪个方案，都需要：**
   - 每位编辑都要有 GitHub 账号，并拥有 `cwong-acmy/fcg-website` 的访问权限（Headless CMS 方案除外）。
   - 部署时自动运行 `python3 tools/build-site.py`。目前 Vercel 直接发布静态文件、没有构建步骤，需要在 Vercel 项目设置中加入该构建命令，并确认构建环境有 Python 3。否则在 CMS 中保存的文章不会出现在网站上。

   请告诉我们：你们选择哪个方案、预计工作量，以及上述两点是否可行。

3. **正文格式：** 写手更习惯 Markdown 还是富文本编辑器？是否需要我们把 `body` 改为支持 Markdown？
4. **图片：** 文章配图存放在仓库里，还是使用 CDN 或对象存储（例如 OSS、S3）？是否需要自动压缩、生成 WebP？
5. **审核与预览：** 发布前是否需要预览链接（例如 Vercel Preview）和审批流程？由谁审批？
6. **定时发布：** 是否需要按日期自动上线？
7. **部署：** 目前推送 `main` 会触发生产部署，但线上内容来自 CLI 手动部署。是否统一为"`main` 即线上版本"、只通过 Git 部署？是否可以在 CI 中加入 `build-site.py --check`？
8. **订阅：** 邮件订阅建议接入哪个服务？由谁维护订阅名单？
9. **多语言：** 博客是否需要中文版本？如需要，网址结构如何规划（例如 `/zh/blog/`）？
10. **上线：** 新官网替换 Wix 时，旧网址的 301 重定向由谁负责？

请直接在群聊中回复，或联系 Crystal Wong（crystal.wong@accomy.com）。

---

## 8. 联系人

- **内容、设计、优先级：** Crystal Wong
- **技术细节：** 见本文件第 2 至第 5 节，以及 `codex/blog` 分支的提交说明
