# pattern-AA Designer仕様書
## Webデザイナー Round 2 成果物

作成日: 2026-04-04
担当: Webデザイナー（web-designer）
参照: web/templates/instructions/pattern-AA/director.md / web/templates/DESIGN.md

---

## 1. カラー定義

すべての値は `web/templates/DESIGN.md` の Studio Defaults から取得する。

### CSS変数定義

```css
:root {
  /* ── Studio Defaults (DESIGN.md Section 2 準拠) ── */
  --bg:              #080810;   /* Deep night. Hero背景・ページ最暗部 */
  --surface:         #0f0f17;   /* Section背景。Signal・Gateセクションに使用 */
  --surface-cont:    #1a1a2a;   /* カード・パネル。Echo内のフォーカスブロックに使用 */
  --text:            #e8e3da;   /* Primary text. 温かみのある白 */
  --text-dim:        #888899;   /* Secondary. Signal断片テキスト・メタ情報 */
  --text-muted:      #555566;   /* Muted. 非アクティブ状態 */

  /* ── IP-Specific Accent (テンプレート仮設定) ── */
  --accent:          #a0a0b0;   /* ニュートラル青灰色。IP導入時に上書き必須 */
  --accent-glow:     rgba(160, 160, 176, 0.30); /* accentの30%不透明度 */
}
```

### 各カラーの割り当て理由

| 変数 | 割り当てセクション | 理由 |
|---|---|---|
| `--bg` | Hero・body | 「虚空」の表現。DESIGN.md: "Deep night. Blue-black void. The base of all immersion." |
| `--surface` | Signal・Gate背景 | bgより1段浮いた表面。「兆し」と「閾」のセクションに適合 |
| `--surface-cont` | Echo フォーカスブロック | コンテンツが近づいてくる感覚。Echo の「共鳴」にもっとも密接な層 |
| `--text` | 本文・見出し | 純白を避け温かさを保つ。DESIGN.md: "Warm white—never cold." |
| `--text-dim` | Signal断片・日付 | 「かすれた痕跡」の表現に適合 |
| `--accent` | Gate CTA・強調 | IP固有の招待色。テンプレート状態では中性的な青灰色で構造を保つ |

---

## 2. タイポグラフィ定義

DESIGN.md Section 3「三層システム」に準拠。

### フォント定義

```css
:root {
  --font-serif:   Georgia, "Yu Mincho", "Hiragino Mincho ProN",
                  "Noto Serif JP", "Times New Roman", serif;
  --font-sans:    -apple-system, "Helvetica Neue",
                  "Hiragino Kaku Gothic ProN", sans-serif;
  --font-mono:    "Courier New", Courier, monospace;
}
```

### フォント層の割り当て

| テキスト要素 | 層 | フォント変数 | 理由 |
|---|---|---|---|
| Hero 問いかけ文 | 物語声 | `--font-serif` | 世界が語りかける言葉。物語の声で発される |
| Signal 断片テキスト | 物語声 | `--font-serif` | 「誰かがここにいた証跡」は物語言語で残す |
| Echo 本文 | 物語声 | `--font-serif` | 読ませる文章。DESIGN.md: "Serif for any text meant to be experienced as narrative" |
| Gate CTAテキスト | 機能声 | `--font-sans` | 行動への招待。UIとしての明確さが必要 |
| 日付・タグ・座標風テキスト | 技術声 | `--font-mono` | メタデータ。記号的な「証跡」表現 |

### サイズ・字間・行間

```css
/* Hero 問いかけ文 */
.hero-question {
  font-size: clamp(1.6rem, 4vw, 3.2rem);
  letter-spacing: 0.05em;
  line-height: 1.6;
}

/* Signal 断片テキスト */
.signal-fragment {
  font-size: clamp(0.9rem, 1.5vw, 1.1rem);
  letter-spacing: 0.35em;   /* 「彫られた言葉」印象 — director指定 */
  line-height: 2.4;
  text-transform: none;     /* 大文字化は断片感を壊す */
}

/* Echo 本文 */
.echo-body {
  font-size: 16px;
  letter-spacing: 0.02em;
  line-height: 2.2;         /* director指定: 2.2以上 */
}

/* Gate CTA */
.gate-cta-text {
  font-size: clamp(0.8rem, 1.2vw, 1rem);
  letter-spacing: 0.25em;
  text-transform: uppercase;
}

/* Mono メタ情報 */
.meta-mono {
  font-size: 10px;
  letter-spacing: 0.4em;
  color: var(--text-dim);
  text-transform: uppercase;
}
```

---

## 3. グリッド・レイアウト定義

### ページ全体

```css
:root {
  --max-content:  1100px;
  --max-text:     600px;    /* director指定: Echo は 600px */
  --side-pad:     clamp(1.5rem, 5vw, 4rem);
}

.section-wrap {
  max-width: var(--max-content);
  margin: 0 auto;
  padding: 0 var(--side-pad);
}

.text-wrap {
  max-width: var(--max-text);
  margin: 0 auto;
}
```

### セクション別レイアウト

| セクション | レイアウト | 理由 |
|---|---|---|
| Hero | `display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh` | 単一の問いかけを空間の中心に置く |
| Signal | シングルカラム中央寄せ。テキスト断片を縦に散在させる | 「極疎」密度設計。断片が浮かぶような印象 |
| Echo | `max-width: 600px` シングルカラム。左右に大きな余白 | director指定。「左右に空気を作る」 |
| Gate | `display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh` | 「扉の前に立つ」対称的な構造 |

---

## 4. アニメーション仕様

DESIGN.md Section 6 準拠。void-invitation の「重さ・静けさ」に特化。

### 基本フェードイン（全セクション共通）

```css
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.9s ease, transform 0.9s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

**duration: 0.9s を基本** — director指定: 速さで「軽さ」を出さない

### セクション別アニメーション詳細

**Hero:**
```
問いかけ文: delay 0.3s, duration 0.9s, ease
下部スクロール誘導点: delay 1.5s, duration 0.7s, ease
  → その後 opacity: 0.4 と 1.0 の間で pulse (2s ease-in-out infinite)
  → DESIGN.md禁止のループは「誘導専用の微細な点」のみ例外適用
```

**Signal:**
```
断片テキスト1: delay 0s
断片テキスト2: delay 0.4s
断片テキスト3: delay 0.8s
mono メタ: delay 1.1s
```

**Echo（フォーカスブロック3点）:**
```
各ブロック: delay 0s / 0.3s / 0.6s
duration: 0.9s
```

**Gate:**
```
背景グロー: opacity 0→0.6, duration 1.2s, delay 0.2s
CTA容器: delay 0.4s, duration 0.9s
CTA文字: delay 0.7s, duration 0.7s
```

### ホバー効果

```css
/* Gate CTAボタン */
.gate-cta {
  transition: box-shadow 0.3s ease, background 0.2s ease;
}
.gate-cta:hover {
  box-shadow: 0 0 20px var(--accent-glow);
}

/* Echo フォーカスブロック */
.echo-focus:hover {
  background: var(--surface-cont);
  transition: background 0.3s ease;
}
```

---

## 5. 余白設計

DESIGN.md Section 7「Silence & Negative Space」準拠。

```css
/* セクション間 — 「沈黙の間」 */
.section + .section {
  margin-top: 120px;   /* director指定: 100px以上。ここでは120pxを採用 */
}

/* Hero 内部余白 */
.hero-inner {
  padding: 0 var(--side-pad);
  gap: 48px;            /* 問いかけ文と誘導点の間 */
}

/* Signal 断片間 */
.signal-fragment + .signal-fragment {
  margin-top: 80px;    /* 断片が「孤立」して見えるための距離 */
}

/* Echo フォーカスブロック間 */
.echo-focus + .echo-focus {
  margin-top: 80px;
}

/* Gate CTA上部 */
.gate-cta-wrap {
  margin-top: 60px;
}
```

---

## 6. モバイル対応方針

```css
@media (max-width: 768px) {
  /* フォントスケール: clamp で自動対応済み */

  /* Signal 断片テキスト: letter-spacingを少し詰める */
  .signal-fragment {
    letter-spacing: 0.2em;
  }

  /* Echo: 余白を縮小するが空気感を維持 */
  .text-wrap {
    max-width: 100%;
    padding: 0 var(--side-pad);
  }

  /* セクション間余白を縮小 */
  .section + .section {
    margin-top: 80px;
  }

  /* Gate: ボタンを横幅いっぱいにしない（孤立感を維持） */
  .gate-cta {
    min-width: 200px;
    width: auto;
  }
}
```

---

## 7. 区切り・境界の処理

DESIGN.md「No-Line Rule」準拠。

```css
/* セクション間の背景切り替えで分離（区切り線不使用） */
#hero    { background: var(--bg); }
#signal  { background: var(--surface); }
#echo    { background: var(--bg); }
#gate    { background: var(--surface); }

/* Echoフォーカスブロックの境界（必要な場合のみ） */
.echo-focus {
  border: 1px solid rgba(255, 255, 255, 0.08); /* Ghost border fallback */
  padding: 40px;
}
```

---

## 8. 装飾要素仕様

### Hero 背景処理

```css
#hero {
  background: var(--bg);
  /* 純粋な暗闇から始める — director指定 */
  /* グラデーション許容: 中央から外縁に向けて微細に明るくする */
  background-image: radial-gradient(
    ellipse at 50% 60%,
    rgba(160, 160, 176, 0.04) 0%,
    transparent 70%
  );
}
```

### Gate 背景グロー

```css
#gate::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(
    ellipse at 50% 50%,
    var(--accent-glow) 0%,
    transparent 60%
  );
  opacity: 0;
  /* アニメーションでopacity: 0.6まで上昇 */
  pointer-events: none;
}
```

### スクロール誘導点（Hero下部）

```css
.scroll-hint {
  width: 1px;
  height: 40px;
  background: linear-gradient(to bottom, transparent, var(--accent));
  margin: 0 auto;
  animation: pulse-line 2s ease-in-out infinite;
}

@keyframes pulse-line {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 1; }
}
```

注: ループアニメーションはDESIGN.md禁止事項に該当するが、ナビなし構造では「スクロール可能であること」を示す唯一の合図として例外適用。対象は線1本のみ（視覚的ノイズ極小）。

---

## 9. コンポーネント仕様

### Gate CTAボタン

```css
.gate-cta {
  display: inline-block;
  padding: 14px 48px;
  border-radius: 0;              /* DESIGN.md: シャープエッジ */
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.15);  /* Secondary ghost border */
  color: var(--accent);
  font-family: var(--font-sans);
  font-size: clamp(0.8rem, 1.2vw, 1rem);
  letter-spacing: 0.25em;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
  transition: box-shadow 0.3s ease, border-color 0.2s ease;
}

.gate-cta:hover {
  box-shadow: 0 0 20px var(--accent-glow);
  border-color: var(--accent);
}
```

注: director指定「CTAは命令ではなく招待」に対応し、Secondary ghost borderを採用。Primary（accent背景塗り）は命令的に見えるため不採用。

### Echoフォーカスブロック

```css
.echo-focus {
  padding: 48px;
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.08);
  transition: background 0.3s ease;
}

.echo-focus:hover {
  background: var(--surface-cont);
}

.echo-focus-label {
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: 0.4em;
  color: var(--text-dim);
  text-transform: uppercase;
  margin-bottom: 24px;
}

.echo-focus-title {
  font-family: var(--font-serif);
  font-size: clamp(1.2rem, 2.5vw, 1.8rem);
  color: var(--text);
  margin-bottom: 20px;
}

.echo-focus-body {
  font-family: var(--font-serif);
  font-size: 15px;
  line-height: 2.2;
  color: var(--text-dim);
}
```

---

## 10. 構築人（web-coder）への注意事項

1. `<nav>` 要素は生成しない。director設計でナビなし確定
2. IntersectionObserverの `rootMargin` は `"-10% 0px"` を推奨（画面中央付近でreveal）
3. スクロール誘導点（`.scroll-hint`）のループアニメーションは意図的例外。削除しないこと
4. Echoセクションのフォーカスブロックは3つを縦並びで実装。横並びにしない
5. `--accent` は必ず変数で参照する。直値 `#a0a0b0` をソースに埋め込まない
6. Gate の `::before` 疑似要素によるグローは `position: relative` が親に必要
7. HTMLのセクションIDは `hero` / `signal` / `echo` / `gate` で統一する
8. `<title>` タグは `pattern-AA: void-invitation | Seep Logos` とする
9. プレースホルダー画像は本テンプレートでは使用しない（画像なし設計）
10. セクション間の余白は `margin` ではなく各セクションの `padding-top/bottom` で実装する（スクロール位置の計算ズレを防ぐため）

---

*Webデザイナー（web-designer） | pattern-AA void-invitation | 2026-04-04*
