# FCG 官网博客：交接说明（技术团队）

**日期：** 2026-10-21（2026-10-26 更新：Pages CMS、自动构建、Book a demo 表单、订阅、无障碍修复）
**负责人：** Crystal Wong（Marketing）
**代码仓库：** `cwong-acmy/fcg-website`，分支 `codex/blog`（基于 `codex/drafts`，审查后合并回 `codex/drafts`）
**适用范围：** 官网改版项目（静态 HTML 站点）。目前线上的 fusionconnectgroup.com 仍是 Wix，**本次不涉及 Wix**。博客将随新官网一起上线。

---

## 1. 一句话总结

新官网增加了博客：每个页面的导航栏和页脚都有 Blog 入口，首页和产品页有文章推荐区，每篇文章有独立页面，手机端菜单已修好。每篇文章是 `blog/posts/` 下的一个 JSON 文件，Marketing 用 Pages CMS 网页后台编辑，GitHub Action 自动生成全部页面。

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
- `blog/posts/<slug>.json`：**每篇文章一个文件（文件名即网址），Marketing 在 Pages CMS 中编辑**
- `.pages.yml`：Pages CMS 配置
- `.github/workflows/build-site.yml`：推送后自动运行构建并提交生成的页面
- `contact.html`：Book a demo 表单页
- `api/book-demo.js`、`api/subscribe.js`、`api/_lib.js`：表单后端（Vercel Functions），`tools/test-forms.js`：测试
- `db/fcg-website-leads.sql`：表单数据表（2026-10-26 已在 Supabase `accomy-projects` 执行，schema `fcg_website`）
- `favicon.svg`、`robots.txt`、`sitemap.xml`（后者由脚本生成）
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

## 5. 发文流程：Marketing 用 Pages CMS

**界面：** [app.pagescms.org](https://app.pagescms.org)，用 GitHub 账号登录，选择 `cwong-acmy/fcg-website` 和分支。左侧 "Blog posts" 是文章列表，点 "Add an entry" 新建，表单字段见 `.pages.yml`（标题、摘要、草稿开关、日期、话题、关联产品页、封面图上传、作者、正文富文本编辑器）。封面图和正文图片上传到 `assets/images/blog/`。

**流程：**
1. Marketing 在 Pages CMS 中新建或编辑文章，点 Save。每次保存就是一次 Git 提交。
2. GitHub Action（`.github/workflows/build-site.yml`）自动运行 `python3 tools/build-site.py` 和表单测试，把生成的页面提交回同一分支。删除的文章，其页面也会被自动删除。
3. 部署流程拿到新提交后发布（见第 8 节）。

**规则（脚本会检查，不符合时 Action 失败，页面不更新）：**
- 文件名（网址）在第一次保存时由标题生成，之后改标题不会改网址。上线后不要改文件名。
- 关闭"草稿"即发布，发布的文章必须填日期。草稿自动 `noindex`，不进 RSS 和 sitemap。
- 排序：勾选 Featured 的置顶，其余按日期从新到旧。阅读时长按正文字数自动计算。
- 结尾 CTA 可不填，默认是 "Book a demo" 链接到 `contact.html`。

**手动方式（技术团队）：** 直接编辑 `blog/posts/*.json`，运行 `python3 tools/build-site.py`，提交。

**需要验证（Pages CMS 文档未明确，请在接入时测试）：** `filename: "{primary}.json"` 是否把标题转为小写连字符的文件名；图片字段保存的路径格式（脚本已兼容开头带 `/` 的路径）；`select` 多选在 JSON 中保存为数组。

**现状：** 7 篇文章仍是占位内容（`draft: true`）。

---

## 6. 表单：Book a demo 与博客订阅（参照 accomy.com 的做法）

**以前的问题：** 所有 "Book a demo" 按钮只跳到本页底部的 CTA 区，而 CTA 区的按钮又链接回自己，**网站没有任何表单**，只有 `hello@` 邮件链接。

**现在：**
- 新页面 `contact.html`：姓名、工作邮箱、公司、职位、公司类型、地区、感兴趣的产品（从产品页进入时自动选中，例如 `contact.html?product=atlas`）、留言。产品页、About、Payment 的 Book a demo / Schedule a call 按钮和页脚 Contact 都指向这里。
- 博客订阅框接入真实提交。
- 后端 `api/book-demo.js`、`api/subscribe.js`，与 accomy.com 相同的处理顺序：服务端校验（与表单相同的选项列表）、隐藏陷阱字段防机器人、每个 IP 10 分钟 8 次限流；**先写入 Supabase**（`fcg_website.leads` / `fcg_website.subscribers`），成功后才向访客显示成功；再尽力同步到飞书（多维表格一行 + 群聊卡片），飞书失败不影响访客。同一邮箱重复订阅不报错、不重复通知。
- **与 Accomy 数据分开：** 独立 schema、独立多维表格和群聊。

**环境变量（在部署平台设置，不要提交到仓库）：** `SUPABASE_URL`、`SUPABASE_SECRET_KEY`、`FCG_DB_SCHEMA`（默认 `fcg_website`）、`LARK_APP_ID`、`LARK_APP_SECRET`、`LARK_LEADS_BASE_APP_TOKEN`、`LARK_LEADS_DEMO_TABLE_ID`、`LARK_LEADS_SUBSCRIBERS_TABLE_ID`、`LARK_LEADS_CHAT_ID`。

**测试：** `node --test tools/test-forms.js`（Supabase 和飞书已模拟，不需要密钥）。

**订阅是单次确认（single opt-in）。** 正式群发邮件前需要加确认邮件（double opt-in）。

---

## 7. 无障碍与 SEO 修复（2026-10-26）

- 页脚版权文字对比度：浅色 2.59 → 5.19，深色 2.48 → 6.25；LIVE.NETWORK 标签 4.42 → 6.24（WCAG AA 要求 4.5）
- 手机端主题开关加了无障碍名称；每页新增 "Skip to content" 跳转链接
- 新增 favicon、`robots.txt`、`sitemap.xml`（脚本生成，只含已发布文章）
- 博客页、文章页、表单页 axe 扫描 0 个问题（1440px 与 375px）。产品页正文里原有的小字对比度问题（如 Atlas 的 `.url`、`.tag`）不在本次范围。

---

## 8. 需要技术团队处理

1. **预发布环境暴露了内部文件：** staging 用 nginx 直接发布仓库，`.vercelignore` 不起作用，`HANDOVER-BLOG.md`、`AGENTS.md`、`README.md`、`tools/`、`_shell/`、`blog/_post.html`、`components.html`、`nav-preview.html` 都能被公开访问。建议只发布网站需要的文件（HTML、`assets/`、`blog/`、`favicon.svg`、`robots.txt`、`sitemap.xml`），或在 nginx 中屏蔽：
   ```nginx
   location ~* (\.md$|^/tools/|^/_shell/|^/db/|^/blog/posts/|^/blog/_post\.html$|^/(components|nav-preview)\.html$|/\.) { return 404; }
   ```
2. **staging 加 noindex：** `add_header X-Robots-Tag "noindex" always;`（只加在 staging）。
3. **启用自动构建：** 合并后 Action 会在推送时运行。请确认仓库 Settings → Actions 允许 workflow 写入（Read and write permissions），以及受保护分支是否允许 Action 推送。
4. **表单后端运行在哪里：** `api/` 是 Vercel Functions，生产环境若在 Vercel 可直接使用。staging 是 nginx，无法运行 `api/`，所以 `/api/book-demo`、`/api/subscribe` 返回 nginx 404。未接通时表单会显示"未能发送，请发邮件到 hello@"，不会假装成功。
   - **预发布接口地址：** `https://fcg-website-git-codex-blog-crystalwong-accomycoms-projects.vercel.app`（`codex/blog` 分支的固定预览地址，9 个环境变量已在 Vercel Preview 环境设置好）。
   - **该地址有 Vercel 登录保护**，直接访问会 302 跳转到登录页。nginx 代理时需带上 bypass 请求头，密钥由 Crystal 私下提供：
   ```nginx
   location /api/ {
       proxy_pass https://fcg-website-git-codex-blog-crystalwong-accomycoms-projects.vercel.app;
       proxy_set_header Host fcg-website-git-codex-blog-crystalwong-accomycoms-projects.vercel.app;
       proxy_ssl_server_name on;
       proxy_set_header x-vercel-protection-bypass "<由 Crystal 私下提供>";
   }
   ```
   - 前端无需修改。注意：经代理后所有访客在 Vercel 看来是同一个 IP（nginx 服务器），所以"每 IP 10 分钟 8 次"的限流在 staging 上是所有测试人员共用的。
   - 另一种方案是改为 Supabase Edge Function，工作量更大。
5. **Supabase：** 已完成：`accomy-projects` 中的 `fcg_website` schema 已建好并开放，专用密钥已生成（值由 Crystal 私下提供）。飞书多维表格和群聊也已建好，端到端测试通过。注意：工作账号的 Supabase 是免费版，约一周无流量会暂停，暂停期间表单全部失败。建议付费版，或每周检查行数。
6. **Pages CMS 编辑权限：** 每位 Marketing 编辑需要 GitHub 账号和仓库写权限。是否保存即上线，还是先到分支审核再合并，请确认。
7. **上线前（独立审查 2026-10-26 提出）：**
   - 在 Vercel Firewall 为 `/api/*` 加限流规则（代码内的限流只在单个实例内有效，挡不住分布式刷量）。
   - 订阅名单正式群发前加确认邮件（double opt-in），否则任何人都能替别人订阅。
   - 如果分支受保护，需要允许 Action 推送，否则自动构建的提交会失败。
   - 用一篇文章测试 Pages CMS 富文本编辑器保存后，正文 HTML 是否被改写。
   - 每次 CMS 保存会部署两次（先是旧页面，再是 Action 重建后的页面）。可在 Vercel 设置 Ignored Build Step，只部署 Action 的提交。
   - 用真实群聊测试一次：留言中输入 `<at id=all></at>` 不应 @ 所有人（代码已去掉 `<` `>`）。
8. **部署（重要）：** Vercel 项目 `fcg-website` 的生产分支是 `main`，推送 `main` 会立即部署。**在 Marketing 确认前，请勿推送或合并到 `main`**。
9. **404 页面：** 已补官网风格的 `404.html`（任意层级的错误网址都能正常显示样式，已设 noindex，不进 sitemap）。请在 nginx 配置 `error_page 404 /404.html;`，并去掉把未知路径回落到首页的规则（如 `try_files ... /index.html`），否则错误网址会返回 200 和首页。Vercel 会自动使用 `404.html`。

---

## 9. 联系人

- **内容、设计、优先级：** Crystal Wong
- **技术细节：** 见本文件第 2 至第 5 节，以及 `codex/blog` 分支的提交说明
