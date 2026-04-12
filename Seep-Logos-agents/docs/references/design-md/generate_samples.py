#!/usr/bin/env python3
"""
DESIGN.md → HTML サンプルページ 一括生成スクリプト
出力先: docs/references/design-md/samples/
"""

import os
import re
import html as html_module
from pathlib import Path

BASE = Path("/Users/matsuura-hisashi/com/Seep-Logos-agents/docs/references/design-md")
JAPAN_DIR = BASE / "japan"
INT_DIR = BASE / "international"
OUT_DIR = BASE / "samples"


# ─── 抽出ヘルパー ───────────────────────────────────────────────────────────────

def extract_brand_name(filename, content):
    m = re.search(r'^# DESIGN\.md — (.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r'^# Design System Inspired by (.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return filename.replace('_DESIGN.md', '').replace('_', ' ').title()


def extract_theme(content):
    """Section 1 の最初の段落・箇条書きを取得"""
    m = re.search(r'## 1\. Visual Theme.*?\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if not m:
        return ""
    block = m.group(1).strip()
    # 最初の段落だけ（長すぎる場合は 200 文字で切る）
    lines = [l for l in block.split('\n') if l.strip() and not l.startswith('#')]
    text = ' '.join(lines[:3])
    return text[:300] + ('...' if len(text) > 300 else '')


def get_section(content, num):
    """指定番号のセクションを抽出する"""
    m = re.search(rf'## {num}\b.*?\n(.*?)(?=\n## \d|\Z)', content, re.DOTALL)
    return m.group(1) if m else ""


def find_color_in(text, keywords, fallback=None):
    """テキスト内でキーワード近傍の最初の hex を返す"""
    for kw in keywords:
        pattern = rf'(?i){re.escape(kw)}[^\n#]*?(#[0-9a-fA-F]{{6}}|#[0-9a-fA-F]{{3}})\b'
        m = re.search(pattern, text)
        if m:
            return m.group(1)
        pattern2 = rf'(?i)(#[0-9a-fA-F]{{6}}|#[0-9a-fA-F]{{3}})[^\n]*?{re.escape(kw)}'
        m = re.search(pattern2, text)
        if m:
            return m.group(1)
    return fallback


def find_color(content, keywords, fallback=None):
    """Section 9 → Section 2 → 全体 の優先順位でカラー検索"""
    for sec in [get_section(content, 9), get_section(content, 2), content]:
        if not sec:
            continue
        result = find_color_in(sec, keywords)
        if result:
            return result
    return fallback


def all_hex_colors(content):
    return re.findall(r'#[0-9a-fA-F]{6}', content)


def extract_font(content):
    # 1. CSS font-family ブロック
    m = re.search(r'font-family\s*:\s*([^;`\n]+)', content)
    if m:
        raw = m.group(1).strip().rstrip(';').strip()
        first = raw.split(',')[0].strip().strip('"\'')
        return (first, raw)
    # 2. Agent Prompt Guide の "Font:" 行 (section 9)
    sec9 = get_section(content, 9)
    m = re.search(r'(?i)^(?:- )?(?:Primary\s+)?Font\s*:\s*(.+)$', sec9, re.MULTILINE)
    if m:
        raw = m.group(1).strip()
        first = raw.split(',')[0].strip().strip('"\'')
        return (first, raw)
    # 3. Section 3: "- **Headline**:" / "- **Primary**:" / "- **Body**:" から取得
    sec3 = get_section(content, 3)
    m = re.search(r'(?i)\*\*(?:Headline|Primary|Body[^*]*)\*\*\s*[:：]\s*[`"]?([^`"\n,]+)', sec3)
    if m:
        first = m.group(1).strip().strip('`\'"')
        # フォールバックを含む全行を取得
        line_m = re.search(rf'(?i)\*\*(?:Headline|Primary|Body)\*\*.*?fallback.*?`([^`]+)`', sec3, re.DOTALL)
        if line_m:
            fb = line_m.group(1)
            return (first, f"{first}, {fb}")
        return (first, f"{first}, sans-serif")
    return ("sans-serif", "sans-serif")


def extract_radius(content, keys, fallback="4px"):
    for key in keys:
        m = re.search(rf'(?i){re.escape(key)}[^\n]*?(\d+)px', content)
        if m:
            return m.group(1) + "px"
    return fallback


def hex_to_rgb(hex_color):
    h = hex_color.lstrip('#')
    if len(h) == 3:
        h = ''.join(c*2 for c in h)
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return r, g, b


def luminance(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    def srgb(c):
        c = c / 255
        return c/12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4
    return 0.2126*srgb(r) + 0.7152*srgb(g) + 0.0722*srgb(b)


def contrast_text(bg_hex):
    """背景色に対してテキストを白か黒か決定"""
    try:
        lum = luminance(bg_hex)
        return "#ffffff" if lum < 0.4 else "#111111"
    except:
        return "#ffffff"


def extract_all_colors(content):
    """カラーパレット全色を (name, hex) のリストで取得"""
    # `Name` (`#XXXXXX`): ... パターン
    pattern = r'\*\*([^*`\n]+)\*\*\s*\(`(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})`\)'
    matches = re.findall(pattern, content)
    seen = {}
    result = []
    for name, hex_val in matches:
        if hex_val not in seen:
            seen[hex_val] = True
            result.append((name.strip(), hex_val))
    # 少なすぎる場合は全 hex 拾う
    if len(result) < 3:
        for hex_val in all_hex_colors(content):
            if hex_val not in seen:
                seen[hex_val] = True
                result.append((hex_val, hex_val))
    return result[:20]  # 最大20色


# ─── HTML テンプレート ──────────────────────────────────────────────────────────

def make_color_swatches(colors, limit=16):
    items = []
    for name, hex_val in colors[:limit]:
        text_col = contrast_text(hex_val)
        safe_name = html_module.escape(name)
        items.append(f"""
        <div class="swatch" style="background:{hex_val};color:{text_col}">
          <span class="swatch-hex">{hex_val}</span>
          <span class="swatch-name">{safe_name}</span>
        </div>""")
    return '\n'.join(items)


def make_html(brand_name, theme, brand_color, bg_color, text_color,
              text_secondary, surface_color, border_color,
              btn_radius, card_radius, font_name, font_stack,
              all_colors, relative_path_to_index):

    brand_text = contrast_text(brand_color)
    bg_text = contrast_text(bg_color)
    surface_text = contrast_text(surface_color)

    swatches_html = make_color_swatches(all_colors)
    safe_name = html_module.escape(brand_name)
    safe_theme = html_module.escape(theme)
    safe_font = html_module.escape(font_name)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{safe_name} — Design Sample</title>
  <style>
    :root {{
      --brand:     {brand_color};
      --brand-text:{brand_text};
      --bg:        {bg_color};
      --text:      {text_color};
      --text-sec:  {text_secondary};
      --surface:   {surface_color};
      --border:    {border_color};
      --r-btn:     {btn_radius};
      --r-card:    {card_radius};
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background: var(--bg);
      color: var(--text);
      font-family: {font_stack}, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 16px;
      line-height: 1.6;
    }}

    /* ── Nav ── */
    .nav {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .nav-brand {{
      font-weight: 700;
      font-size: 18px;
      color: var(--brand);
    }}
    .nav-back {{
      font-size: 13px;
      color: var(--text-sec);
      text-decoration: none;
    }}
    .nav-back:hover {{ color: var(--brand); }}

    /* ── Layout ── */
    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 48px 24px 80px;
    }}
    .section {{
      margin-bottom: 56px;
    }}
    .section-title {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--text-sec);
      margin-bottom: 20px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }}

    /* ── Hero ── */
    .hero {{
      background: var(--brand);
      color: var(--brand-text);
      border-radius: var(--r-card);
      padding: 48px 40px;
      margin-bottom: 56px;
    }}
    .hero h1 {{
      font-size: 36px;
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 16px;
    }}
    .hero p {{
      font-size: 15px;
      line-height: 1.7;
      opacity: 0.85;
      max-width: 600px;
    }}

    /* ── Color Palette ── */
    .palette {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
      gap: 8px;
    }}
    .swatch {{
      border-radius: 8px;
      padding: 20px 12px 10px;
      min-height: 80px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
    }}
    .swatch-hex {{
      font-size: 12px;
      font-weight: 700;
      font-family: monospace;
      opacity: 0.9;
    }}
    .swatch-name {{
      font-size: 11px;
      opacity: 0.7;
      margin-top: 2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    /* ── Typography ── */
    .type-row {{
      display: flex;
      align-items: baseline;
      gap: 20px;
      padding: 16px 0;
      border-bottom: 1px solid var(--border);
    }}
    .type-meta {{
      width: 100px;
      flex-shrink: 0;
      font-size: 11px;
      color: var(--text-sec);
    }}
    .type-display  {{ font-size: 48px; font-weight: 700; line-height: 1.1; }}
    .type-h1       {{ font-size: 32px; font-weight: 700; line-height: 1.2; }}
    .type-h2       {{ font-size: 24px; font-weight: 600; line-height: 1.3; }}
    .type-h3       {{ font-size: 20px; font-weight: 600; line-height: 1.4; }}
    .type-body     {{ font-size: 16px; font-weight: 400; line-height: 1.6; }}
    .type-small    {{ font-size: 13px; font-weight: 400; color: var(--text-sec); }}
    .type-label    {{ font-size: 11px; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; }}

    /* ── Buttons ── */
    .btn-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 10px 20px;
      border-radius: var(--r-btn);
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: opacity 0.15s;
      font-family: inherit;
    }}
    .btn:hover {{ opacity: 0.85; }}
    .btn-primary {{
      background: var(--brand);
      color: var(--brand-text);
    }}
    .btn-secondary {{
      background: transparent;
      color: var(--text);
      border: 1.5px solid var(--border);
    }}
    .btn-surface {{
      background: var(--surface);
      color: var(--text);
      border: 1px solid var(--border);
    }}
    .btn-ghost {{
      background: transparent;
      color: var(--brand);
      text-decoration: underline;
      padding-left: 0;
      padding-right: 0;
    }}

    /* ── Input ── */
    .input-demo {{
      display: flex;
      flex-direction: column;
      gap: 16px;
      max-width: 480px;
    }}
    .input-label {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-sec);
      margin-bottom: 4px;
      display: block;
    }}
    .input {{
      width: 100%;
      padding: 10px 14px;
      background: var(--bg);
      color: var(--text);
      border: 1.5px solid var(--border);
      border-radius: var(--r-btn);
      font-size: 15px;
      font-family: inherit;
      outline: none;
      transition: border-color 0.15s;
    }}
    .input:focus {{
      border-color: var(--brand);
    }}
    .input-row {{
      display: flex;
      gap: 8px;
    }}
    .input-row .input {{ flex: 1; }}

    /* ── Cards ── */
    .card-row {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 16px;
    }}
    .card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r-card);
      padding: 24px;
    }}
    .card-label {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--brand);
      margin-bottom: 8px;
    }}
    .card h3 {{
      font-size: 18px;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .card p {{
      font-size: 14px;
      color: var(--text-sec);
      line-height: 1.6;
    }}
    .card-footer {{
      margin-top: 20px;
      display: flex;
      justify-content: flex-end;
    }}

    /* ── Font info ── */
    .font-info {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r-card);
      padding: 20px 24px;
      font-size: 13px;
      color: var(--text-sec);
    }}
    .font-info strong {{ color: var(--text); }}
  </style>
</head>
<body>

<nav class="nav">
  <span class="nav-brand">{safe_name}</span>
  <a class="nav-back" href="{relative_path_to_index}">← Index</a>
</nav>

<div class="container">

  <!-- Hero -->
  <div class="hero">
    <h1>{safe_name}</h1>
    <p>{safe_theme}</p>
  </div>

  <!-- Font Info -->
  <div class="section">
    <div class="section-title">Font</div>
    <div class="font-info">
      <strong>{safe_font}</strong>
      <span style="margin-left:12px;font-family:monospace;font-size:12px">{html_module.escape(font_stack)}</span>
    </div>
  </div>

  <!-- Color Palette -->
  <div class="section">
    <div class="section-title">Color Palette</div>
    <div class="palette">
      {swatches_html}
    </div>
  </div>

  <!-- Typography -->
  <div class="section">
    <div class="section-title">Typography</div>
    <div class="type-row"><span class="type-meta">Display</span><span class="type-display">Aa</span></div>
    <div class="type-row"><span class="type-meta">H1</span><span class="type-h1">見出しサンプル / Heading One</span></div>
    <div class="type-row"><span class="type-meta">H2</span><span class="type-h2">見出しサンプル / Heading Two</span></div>
    <div class="type-row"><span class="type-meta">H3</span><span class="type-h3">見出しサンプル / Heading Three</span></div>
    <div class="type-row"><span class="type-meta">Body</span><span class="type-body">本文テキストのサンプルです。The quick brown fox jumps over the lazy dog.</span></div>
    <div class="type-row"><span class="type-meta">Small</span><span class="type-small">補足テキスト・ラベルなど / Caption and auxiliary text</span></div>
    <div class="type-row"><span class="type-meta">Label</span><span class="type-label">Label / ラベル</span></div>
  </div>

  <!-- Buttons -->
  <div class="section">
    <div class="section-title">Buttons</div>
    <div class="btn-row">
      <button class="btn btn-primary">Primary Action</button>
      <button class="btn btn-secondary">Secondary</button>
      <button class="btn btn-surface">Surface</button>
      <button class="btn btn-ghost">Ghost Link</button>
    </div>
  </div>

  <!-- Inputs -->
  <div class="section">
    <div class="section-title">Inputs</div>
    <div class="input-demo">
      <div>
        <label class="input-label">メールアドレス</label>
        <input class="input" type="text" placeholder="hello@example.com">
      </div>
      <div class="input-row">
        <input class="input" type="text" placeholder="検索キーワード...">
        <button class="btn btn-primary">検索</button>
      </div>
    </div>
  </div>

  <!-- Cards -->
  <div class="section">
    <div class="section-title">Cards</div>
    <div class="card-row">
      <div class="card">
        <div class="card-label">Feature</div>
        <h3>カードタイトル</h3>
        <p>カードの本文テキストです。デザインシステムのコンポーネントサンプルとして表示しています。</p>
        <div class="card-footer">
          <button class="btn btn-primary" style="font-size:13px;padding:8px 16px">詳しく見る</button>
        </div>
      </div>
      <div class="card">
        <div class="card-label">Info</div>
        <h3>Second Card</h3>
        <p>Another card sample showing the same card component in a grid layout. Consistent styling throughout.</p>
        <div class="card-footer">
          <button class="btn btn-secondary" style="font-size:13px;padding:8px 16px">Learn More</button>
        </div>
      </div>
      <div class="card">
        <div class="card-label">Stats</div>
        <h3>Third Card</h3>
        <p>グリッドレイアウト内のカードコンポーネントのサンプルです。余白・角丸・ボーダーを確認できます。</p>
        <div class="card-footer">
          <button class="btn btn-ghost" style="font-size:13px">See all →</button>
        </div>
      </div>
    </div>
  </div>

</div>
</body>
</html>"""


# ─── メイン処理 ────────────────────────────────────────────────────────────────

def process_file(md_path, out_path, index_rel):
    content = md_path.read_text(encoding='utf-8')

    brand_name = extract_brand_name(md_path.name, content)
    theme = extract_theme(content)

    # 色抽出
    brand_color = (
        find_color(content, ['Brand CTA', 'Primary Color', 'ブランドカラー', 'brand color', 'Primary Brand', 'Rausch Red', 'brand accent']) or
        find_color(content, ['Primary']) or
        '#007aff'
    )
    bg_color = (
        find_color(content, ['Background:', 'Page Background', 'ページ背景', 'bg:', 'background\n']) or
        find_color(content, ['background']) or
        '#ffffff'
    )
    text_color = (
        find_color(content, ['Text Color:', 'Text Primary', 'Primary Text', '本文テキスト', 'primary text', 'text\n']) or
        find_color(content, ['Text']) or
        '#111111'
    )
    text_secondary = (
        find_color(content, ['Text Secondary', 'Secondary Text', 'Secondary text', 'text-sec', 'Olive Gray', 'Stone Gray', '補足テキスト']) or
        find_color(content, ['secondary', 'Secondary']) or
        '#666666'
    )
    surface_color = (
        find_color(content, ['Card Surface', 'Surface:', 'Surface\n', 'Ivory', 'カード', 'surface']) or
        find_color(content, ['card', 'surface', 'panel']) or
        bg_color
    )
    border_color = (
        find_color(content, ['Border:', 'Border\n', 'Border Cream', 'border color', 'ボーダー', 'border\n']) or
        find_color(content, ['border', 'Border']) or
        '#e5e5e5'
    )

    # フォント
    font_name, font_stack = extract_font(content)

    # 角丸
    btn_radius = extract_radius(content, ['Button.*Radius', 'btn.*radius', 'Radius.*button', 'Border Radius.*button', 'button.*radius', 'radius.*btn'], '6px')
    card_radius = extract_radius(content, ['Card.*Radius', 'card.*radius', 'r-card', 'container.*radius', 'card.*border.*radius'], '12px')

    # 全色
    all_colors = extract_all_colors(content)
    if not all_colors:
        # fallback: 最低限の色をリストアップ
        all_colors = [(c, c) for c in [brand_color, bg_color, text_color, text_secondary, surface_color, border_color] if c]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    html = make_html(
        brand_name, theme, brand_color, bg_color, text_color,
        text_secondary, surface_color, border_color,
        btn_radius, card_radius, font_name, font_stack,
        all_colors, index_rel
    )
    out_path.write_text(html, encoding='utf-8')
    return brand_name


def generate_index(entries):
    """ギャラリーindex.html を生成"""
    japan_items = []
    intl_items = []

    for brand_name, rel_path, category in sorted(entries, key=lambda x: x[0]):
        safe = html_module.escape(brand_name)
        item = f'<a class="item" href="{rel_path}">{safe}</a>'
        if category == 'japan':
            japan_items.append(item)
        else:
            intl_items.append(item)

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Design Sample Index</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background:#f8f8f8; color:#111; margin:0; }}
    .header {{ background:#fff; border-bottom:1px solid #e5e5e5; padding:24px 32px; }}
    .header h1 {{ font-size:22px; font-weight:700; margin:0 0 4px; }}
    .header p {{ font-size:13px; color:#666; margin:0; }}
    .container {{ max-width:1100px; margin:0 auto; padding:40px 32px; }}
    h2 {{ font-size:13px; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:#999; margin:0 0 16px; padding-bottom:8px; border-bottom:1px solid #e5e5e5; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(160px, 1fr)); gap:8px; margin-bottom:48px; }}
    .item {{ display:block; background:#fff; border:1px solid #e5e5e5; border-radius:8px; padding:14px 16px; font-size:14px; font-weight:500; color:#111; text-decoration:none; transition:box-shadow 0.15s, transform 0.15s; }}
    .item:hover {{ box-shadow:0 4px 12px rgba(0,0,0,0.1); transform:translateY(-2px); }}
    .count {{ font-size:12px; color:#999; font-weight:400; }}
  </style>
</head>
<body>
<div class="header">
  <h1>Design Sample Index</h1>
  <p>DESIGN.md から生成したブランド別 HTML サンプル</p>
</div>
<div class="container">
  <h2>Japan <span class="count">({len(japan_items)})</span></h2>
  <div class="grid">{''.join(japan_items)}</div>
  <h2>International <span class="count">({len(intl_items)})</span></h2>
  <div class="grid">{''.join(intl_items)}</div>
</div>
</body>
</html>"""


def main():
    entries = []

    for category, src_dir in [('japan', JAPAN_DIR), ('international', INT_DIR)]:
        for md_file in sorted(src_dir.glob('*.md')):
            if md_file.name.startswith('_'):
                continue
            slug = md_file.stem.replace('_DESIGN', '')
            out_path = OUT_DIR / category / f"{slug}.html"
            index_rel = "../../index.html"
            brand_name = process_file(md_file, out_path, index_rel)
            rel = f"{category}/{slug}.html"
            entries.append((brand_name, rel, category))
            print(f"  ✓ {brand_name} → {rel}")

    index_html = generate_index(entries)
    (OUT_DIR / "index.html").write_text(index_html, encoding='utf-8')
    print(f"\n✓ index.html 生成完了")
    print(f"✓ 合計 {len(entries)} ファイル → {OUT_DIR}")


if __name__ == '__main__':
    main()
