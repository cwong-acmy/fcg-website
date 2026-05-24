# Design Language: FCG Group - Travel Infrastructure

> Extracted from `https://hostmyclaudehtml.com/p/_Y67ztwQOo` on May 23, 2026
> 1220 elements analyzed

This document describes the complete design language of the website. It is structured for AI/LLM consumption — use it to faithfully recreate the visual design in any framework.

## Color Palette

### Primary Colors

| Role | Hex | RGB | HSL | Usage Count |
|------|-----|-----|-----|-------------|
| Primary | `#111827` | rgb(17, 24, 39) | hsl(221, 39%, 11%) | 204 |
| Secondary | `#f97316` | rgb(249, 115, 22) | hsl(25, 95%, 53%) | 60 |

### Neutral Colors

| Hex | HSL | Usage Count |
|-----|-----|-------------|
| `#e5e7eb` | hsl(220, 13%, 91%) | 881 |
| `#0f1114` | hsl(216, 14%, 7%) | 711 |
| `#6b7280` | hsl(220, 9%, 46%) | 204 |
| `#000000` | hsl(0, 0%, 0%) | 163 |
| `#4b5563` | hsl(215, 14%, 34%) | 155 |
| `#ffffff` | hsl(0, 0%, 100%) | 134 |
| `#d1d5db` | hsl(216, 12%, 84%) | 130 |
| `#f3f4f6` | hsl(220, 14%, 96%) | 17 |
| `#888888` | hsl(0, 0%, 53%) | 14 |
| `#9ca3af` | hsl(218, 11%, 65%) | 14 |
| `#2a2a2a` | hsl(0, 0%, 16%) | 7 |
| `#374151` | hsl(217, 19%, 27%) | 5 |

### Background Colors

Used on large-area elements: `#ffffff`, `#050505`, `#f97316`, `#121212`, `#000000`, `#f3f4f6`

### Text Colors

Text color palette: `#000000`, `#0f1114`, `#111827`, `#f97316`, `#6b7280`, `#ffffff`, `#374151`, `#18181b`, `#e4e4e7`, `#888888`

### Gradients

```css
background-image: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.9));
```

```css
background-image: linear-gradient(to top, rgb(255, 255, 255) 30%, rgba(0, 0, 0, 0) 70%);
```

```css
background-image: linear-gradient(to right, rgb(249, 250, 251), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to left, rgb(249, 250, 251), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to right, rgba(0, 0, 0, 0.08) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(rgba(0, 0, 0, 0.08) 1px, rgba(0, 0, 0, 0) 1px);
```

```css
background-image: radial-gradient(circle at 100% 0%, rgba(0, 0, 0, 0.03), rgba(0, 0, 0, 0) 50%);
```

```css
background-image: linear-gradient(to right, rgba(0, 0, 0, 0.05) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(rgba(0, 0, 0, 0.05) 1px, rgba(0, 0, 0, 0) 1px);
```

```css
background-image: linear-gradient(to left, rgba(0, 0, 0, 0.02), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(rgb(255, 255, 255), rgb(255, 255, 255)), linear-gradient(to right bottom, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.06));
```

```css
background-image: radial-gradient(circle, rgba(255, 255, 255, 0.03), rgba(0, 0, 0, 0) 70%);
```

```css
background-image: radial-gradient(circle, rgba(255, 255, 255, 0) 30%, rgba(255, 255, 255, 0.18) 58%, rgba(255, 255, 255, 0.42) 80%, rgba(255, 255, 255, 0.72) 100%);
```

```css
background-image: linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0));
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0));
```

```css
background-image: radial-gradient(rgba(0, 0, 0, 0.15) 1px, rgba(0, 0, 0, 0) 1px);
```

```css
background-image: radial-gradient(circle, rgba(255, 255, 255, 0.024), rgba(0, 0, 0, 0) 72%);
```

```css
background-image: linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(255, 255, 255, 0));
```

```css
background-image: linear-gradient(to right top, rgba(255, 255, 255, 0.016), rgba(0, 0, 0, 0));
```

```css
background-image: radial-gradient(circle, rgba(255, 255, 255, 0.03), rgba(0, 0, 0, 0) 74%);
```

```css
background-image: linear-gradient(to right bottom, rgba(255, 255, 255, 0.02), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to top, rgb(255, 255, 255), rgba(255, 255, 255, 0.4), rgba(0, 0, 0, 0));
```

```css
background-image: radial-gradient(circle, rgba(0, 0, 0, 0.03), rgba(0, 0, 0, 0) 42%);
```

```css
background-image: linear-gradient(rgba(255, 255, 255, 0.03), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to right top, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.05));
```

```css
background-image: linear-gradient(rgba(82, 82, 82, 0.6), rgba(38, 38, 38, 0.3), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(rgb(64, 64, 64), rgb(38, 38, 38));
```

```css
background-image: linear-gradient(to right bottom, rgba(64, 64, 64, 0.5), rgba(38, 38, 38, 0.2), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to left bottom, rgba(64, 64, 64, 0.5), rgba(38, 38, 38, 0.2), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(rgb(38, 38, 38), rgba(38, 38, 38, 0.5));
```

```css
background-image: linear-gradient(rgba(64, 64, 64, 0.3), rgba(0, 0, 0, 0));
```

```css
background-image: linear-gradient(to top, rgba(255, 255, 255, 0.8), rgba(0, 0, 0, 0));
```

### Full Color Inventory

| Hex | Contexts | Count |
|-----|----------|-------|
| `#e5e7eb` | border, background, text | 881 |
| `#0f1114` | text, border, background | 711 |
| `#111827` | text, background, border | 204 |
| `#6b7280` | text, border, background | 204 |
| `#000000` | text, border, background | 163 |
| `#4b5563` | text, border | 155 |
| `#ffffff` | background, text, border | 134 |
| `#d1d5db` | border, background, text | 130 |
| `#f97316` | text, border, background | 60 |
| `#f3f4f6` | background | 17 |
| `#888888` | text | 14 |
| `#9ca3af` | background, text | 14 |
| `#2a2a2a` | border, background | 7 |
| `#374151` | text, background | 5 |

## Typography

### Font Families

- **Inter** — used for all (1015 elements)
- **JetBrains Mono** — used for body (38 elements)

### Type Scale

| Size (px) | Size (rem) | Weight | Line Height | Letter Spacing | Used On |
|-----------|------------|--------|-------------|----------------|---------|
| 128px | 8rem | 700 | 192px | -6.4px | h2 |
| 96px | 6rem | 500 | 96px | -4.8px | h1 |
| 72px | 4.5rem | 500 | 72px | -3.6px | h1, br, span |
| 60px | 3.75rem | 300 | 60px | -3px | span |
| 48px | 3rem | 500 | 48px | -1.2px | h2, span |
| 30px | 1.875rem | 500 | 36px | -0.75px | h3, div |
| 24px | 1.5rem | 400 | 32px | normal | iconify-icon, style, svg, path |
| 20px | 1.25rem | 500 | 28px | -0.5px | h3, iconify-icon, style, svg |
| 18px | 1.125rem | 300 | 28px | normal | p, a, span, div |
| 16px | 1rem | 400 | 24px | normal | html, head, meta, title |
| 14px | 0.875rem | 500 | 20px | -0.35px | button, iconify-icon, style, svg |
| 12px | 0.75rem | 400 | 16px | -0.6px | div, span, iconify-icon, style |
| 10.4px | 0.65rem | 400 | 15.6px | normal | footer, div, svg, path |
| 10px | 0.625rem | 400 | 15px | normal | span, div |
| 9px | 0.5625rem | 400 | 13.5px | normal | div, span |

### Heading Scale

```css
h2 { font-size: 128px; font-weight: 700; line-height: 192px; }
h1 { font-size: 96px; font-weight: 500; line-height: 96px; }
h1 { font-size: 72px; font-weight: 500; line-height: 72px; }
h2 { font-size: 48px; font-weight: 500; line-height: 48px; }
h3 { font-size: 30px; font-weight: 500; line-height: 36px; }
h3 { font-size: 24px; font-weight: 400; line-height: 32px; }
h3 { font-size: 20px; font-weight: 500; line-height: 28px; }
h3 { font-size: 18px; font-weight: 300; line-height: 28px; }
h3 { font-size: 16px; font-weight: 400; line-height: 24px; }
h3 { font-size: 14px; font-weight: 500; line-height: 20px; }
h2 { font-size: 12px; font-weight: 400; line-height: 16px; }
```

### Body Text

```css
body { font-size: 12px; font-weight: 400; line-height: 16px; }
```

### Font Weights in Use

`400` (954x), `300` (170x), `500` (68x), `600` (20x), `700` (8x)

## Spacing

**Base unit:** 2px

| Token | Value | Rem |
|-------|-------|-----|
| spacing-1 | 1px | 0.0625rem |
| spacing-32 | 32px | 2rem |
| spacing-40 | 40px | 2.5rem |
| spacing-46 | 46px | 2.875rem |
| spacing-57 | 57px | 3.5625rem |
| spacing-64 | 64px | 4rem |
| spacing-80 | 80px | 5rem |
| spacing-96 | 96px | 6rem |
| spacing-128 | 128px | 8rem |
| spacing-136 | 136px | 8.5rem |
| spacing-141 | 141px | 8.8125rem |
| spacing-160 | 160px | 10rem |
| spacing-192 | 192px | 12rem |
| spacing-256 | 256px | 16rem |

## Border Radii

| Label | Value | Count |
|-------|-------|-------|
| xs | 2px | 9 |
| md | 8px | 5 |
| lg | 11px | 3 |
| lg | 15px | 3 |
| xl | 24px | 12 |
| full | 32px | 21 |
| full | 50px | 2 |
| full | 9999px | 92 |

## Box Shadows

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(249, 115, 22, 0.4) 0px 0px 8px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.6) 0px 0px 10px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(249, 115, 22, 0.5) 0px 0px 8px 0px;
```

**sm (inset)** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.9) 0px 0px 60px 0px, rgba(0, 0, 0, 0.2) 0px 0px 20px 0px inset;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.8) 0px 0px 10px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(249, 115, 22, 0.5) 0px 0px 10px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.4) 0px 0px 8px 0px;
```

**sm** — blur: 0px
```css
box-shadow: rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.6) 0px 0px 8px 0px;
```

**xs (inset)** — blur: 0px
```css
box-shadow: rgba(255, 255, 255, 0.8) 0px 1px 0px 0px inset, rgba(0, 0, 0, 0.12) 0px 20px 40px -15px;
```

**sm** — blur: 4.40716px
```css
box-shadow: rgba(255, 255, 255, 0.235) 0px 0px 4.40716px 0px;
```

**sm** — blur: 5.26937px
```css
box-shadow: rgba(255, 255, 255, 0.263) 0px 0px 5.26937px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.553) 0px 0px 7.36532px 0px;
```

**sm** — blur: 5.26937px
```css
box-shadow: rgba(255, 255, 255, 0.263) 0px 0px 5.26937px 0px;
```

**sm (inset)** — blur: 4px
```css
box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;
```

**md** — blur: 10px
```css
box-shadow: rgba(0, 0, 0, 0.15) 0px 0px 10px 0px;
```

**md** — blur: 12.621px
```css
box-shadow: rgba(255, 255, 255, 0.675) 0px 0px 12.621px 0px;
```

**md** — blur: 13.9866px
```css
box-shadow: rgba(255, 255, 255, 0.75) 0px 0px 13.9866px 0px;
```

**lg** — blur: 20px
```css
box-shadow: rgba(0, 0, 0, 0.15) 0px 0px 20px 0px;
```

**lg** — blur: 30px
```css
box-shadow: rgba(0, 0, 0, 0.15) 0px 0px 30px 0px;
```

**lg** — blur: 32px
```css
box-shadow: rgba(0, 0, 0, 0.12) 0px 0px 32px 0px;
```

**xl** — blur: 30px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 30px 0px;
```

**xl** — blur: 25px
```css
box-shadow: rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.08) 0px 8px 10px -6px;
```

**xl (inset)** — blur: 63.4443px
```css
box-shadow: rgba(255, 255, 255, 0.475) 0px 0px 63.4443px 0px, rgba(255, 255, 255, 0.22) 0px 0px 31.7222px 0px inset;
```

**xl** — blur: 50px
```css
box-shadow: rgba(0, 0, 0, 0.15) 0px 25px 50px -12px;
```

## CSS Custom Properties

### Colors

```css
--color-bg: #080805;
--color-fg: #ffffff;
--color-card: #121212;
--color-border: #2A2A2A;
--color-muted: #888888;
--tw-ring-offset-shadow: 0 0 #0000;
--tw-ring-shadow: 0 0 #0000;
--color-accent: #F97316;
--tw-ring-offset-width: 0px;
--tw-ring-inset: ;
--tw-border-spacing-x: 0;
--tw-shadow-colored: 0 0 #0000;
--tw-border-spacing-y: 0;
--tw-ring-color: rgb(59 130 246 / 0.5);
--tw-ring-offset-color: #fff;
```

### Spacing

```css
--tw-contain-size: ;
--tw-numeric-spacing: ;
```

### Shadows

```css
--tw-shadow: 0 0 #0000;
--tw-drop-shadow: ;
```

### Other

```css
--tw-contrast: ;
--tw-backdrop-sepia: ;
--tw-sepia: ;
--tw-skew-x: 0;
--tw-ordinal: ;
--tw-backdrop-saturate: ;
--tw-backdrop-blur: ;
--tw-contain-style: ;
--tw-translate-x: 0;
--tw-gradient-via-position: ;
--tw-backdrop-invert: ;
--tw-saturate: ;
--tw-scroll-snap-strictness: proximity;
--tw-grayscale: ;
--tw-scale-x: 1;
--tw-backdrop-hue-rotate: ;
--tw-gradient-to-position: ;
--tw-brightness: ;
--tw-numeric-fraction: ;
--tw-backdrop-grayscale: ;
--tw-hue-rotate: ;
--tw-scale-y: 1;
--tw-pan-y: ;
--tw-backdrop-contrast: ;
--tw-skew-y: 0;
--tw-backdrop-brightness: ;
--tw-slashed-zero: ;
--tw-blur: ;
--tw-invert: ;
--tw-pan-x: ;
--tw-translate-y: 0;
--tw-backdrop-opacity: ;
--tw-gradient-from-position: ;
--tw-numeric-figure: ;
--tw-rotate: 0;
--tw-pinch-zoom: ;
--tw-contain-paint: ;
--tw-contain-layout: ;
```

### Semantic

```css
success: [object Object];
warning: [object Object];
error: [object Object];
info: [object Object];
```

## Breakpoints

| Name | Value | Type |
|------|-------|------|
| sm | 640px | min-width |
| md | 768px | min-width |
| lg | 1024px | min-width |

## Transitions & Animations

**Easing functions:** `[object Object]`, `[object Object]`, `[object Object]`, `[object Object]`

**Durations:** `0.3s`, `0.15s`, `1.2s`, `0.5s`, `0.7s`, `1s`, `0.1s`, `0.075s`, `0.2s`, `2s`

### Common Transitions

```css
transition: all;
transition: background-color 0.3s, color 0.3s;
transition: 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 1.2s;
transition: opacity 0.5s, filter 0.5s;
transition: color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: transform 0.7s cubic-bezier(0, 0, 0.2, 1);
transition: opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1);
transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1), transform 1s cubic-bezier(0.16, 1, 0.3, 1);
```

### Keyframe Animations

**gridMove**
```css
@keyframes gridMove {
  0% { transform: translateY(0px); }
  100% { transform: translateY(40px); }
}
```

**float**
```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}
```

**marquee**
```css
@keyframes marquee {
  0% { transform: translateX(0px); }
  100% { transform: translateX(-50%); }
}
```

**shimmer**
```css
@keyframes shimmer {
  100% { background-position: 200% center; }
}
```

**barPulse1**
```css
@keyframes barPulse1 {
  0% { height: 30%; }
  100% { height: 70%; }
}
```

**barPulse2**
```css
@keyframes barPulse2 {
  0% { height: 60%; }
  100% { height: 95%; }
}
```

**barPulse3**
```css
@keyframes barPulse3 {
  0% { height: 40%; }
  100% { height: 80%; }
}
```

**barPulse4**
```css
@keyframes barPulse4 {
  0% { height: 75%; }
  100% { height: 45%; }
}
```

**barPulse5**
```css
@keyframes barPulse5 {
  0% { height: 50%; }
  100% { height: 85%; }
}
```

**floatLayer**
```css
@keyframes floatLayer {
  0%, 100% { transform: translateY(0px) rotateX(45deg) rotateZ(-45deg); }
  50% { transform: translateY(-10px) rotateX(45deg) rotateZ(-45deg); }
}
```

## Component Patterns

Detected UI component patterns and their most common styles:

### Buttons (3 instances)

```css
.button {
  background-color: rgb(17, 24, 39);
  color: rgb(255, 255, 255);
  font-size: 14px;
  font-weight: 500;
  padding-top: 14px;
  padding-right: 32px;
  border-radius: 9999px;
}
```

### Cards (75 instances)

```css
.card {
  background-color: rgb(255, 255, 255);
  border-radius: 9999px;
  box-shadow: rgba(0, 0, 0, 0.15) 0px 0px 10px 0px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Inputs (1 instances)

```css
.input {
  color: rgb(15, 17, 20);
  border-color: rgb(15, 17, 20);
  border-radius: 0px;
  font-size: 16px;
  padding-top: 0px;
  padding-right: 0px;
}
```

### Links (25 instances)

```css
.link {
  color: rgb(107, 114, 128);
  font-size: 10.4px;
  font-weight: 400;
}
```

### Navigation (2 instances)

```css
.navigatio {
  background-color: rgb(255, 255, 255);
  color: rgb(15, 17, 20);
  padding-top: 0px;
  padding-bottom: 0px;
  padding-left: 32px;
  padding-right: 32px;
  position: absolute;
}
```

### Footer (2 instances)

```css
.foote {
  background-color: rgb(255, 255, 255);
  color: rgb(15, 17, 20);
  padding-top: 0px;
  padding-bottom: 0px;
  font-size: 16px;
}
```

## Component Clusters

Reusable component instances grouped by DOM structure and style similarity:

### Button — 1 instance, 1 variant

**Variant 1** (1 instance)

```css
  background: rgb(17, 24, 39);
  color: rgb(255, 255, 255);
  padding: 16px 32px 16px 32px;
  border-radius: 9999px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 14px;
  font-weight: 500;
```

### Card — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgba(0, 0, 0, 0.05);
  color: rgb(15, 17, 20);
  padding: 16px 16px 16px 16px;
  border-radius: 16px;
  border: 1px solid rgba(0, 0, 0, 0.12);
  font-size: 16px;
  font-weight: 400;
```

### Card — 3 instances, 1 variant

**Variant 1** (3 instances)

```css
  background: rgb(18, 18, 18);
  color: rgb(15, 17, 20);
  padding: 40px 40px 40px 40px;
  border-radius: 32px;
  border: 1px solid rgb(42, 42, 42);
  font-size: 16px;
  font-weight: 400;
```

### Card — 5 instances, 1 variant

**Variant 1** (5 instances)

```css
  background: rgb(255, 255, 255);
  color: rgb(15, 17, 20);
  padding: 40px 40px 40px 40px;
  border-radius: 32px;
  border: 1px solid rgba(0, 0, 0, 0);
  font-size: 16px;
  font-weight: 400;
```

### Button — 2 instances, 1 variant

**Variant 1** (2 instances)

```css
  background: rgb(17, 24, 39);
  color: rgb(255, 255, 255);
  padding: 14px 32px 14px 32px;
  border-radius: 9999px;
  border: 0px solid rgb(229, 231, 235);
  font-size: 14px;
  font-weight: 500;
```

## Layout System

**9 grid containers** and **225 flex containers** detected.

### Container Widths

| Max Width | Padding |
|-----------|---------|
| 1600px | 0px |
| 600px | 0px |
| 100% | 0px |
| 672px | 0px |
| 1440px | 48px |
| 1280px | 0px |
| 1152px | 24px |
| 1203.2px | 0px |
| 1100px | 0px |
| 1024px | 0px |
| 896px | 24px |

### Grid Column Patterns

| Columns | Usage Count |
|---------|-------------|
| 3-column | 3x |
| 12-column | 2x |
| 2-column | 2x |
| 4-column | 2x |

### Grid Templates

```css
grid-template-columns: 296px 296px 296px 296px;
gap: 16px;
grid-template-columns: 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px 69.3281px;
gap: 32px;
grid-template-columns: 394.656px 394.672px 394.656px;
gap: 24px;
grid-template-columns: 536px 536px;
gap: 32px;
grid-template-columns: 378.656px 378.672px 378.656px;
gap: 24px;
```

### Flex Patterns

| Direction/Wrap | Count |
|----------------|-------|
| column/nowrap | 63x |
| row/nowrap | 162x |

**Gap values:** `128px`, `12px`, `16px`, `24px`, `32px`, `48px`, `48px 32px`, `4px`, `64px`, `6px`, `8px`, `96px`

## Responsive Design

### Viewport Snapshots

| Viewport | Body Font | Nav Visible | Max Columns | Hamburger | Page Height |
|----------|-----------|-------------|-------------|-----------|-------------|
| mobile (375px) | 16px | Yes | 4 | No | 18071px |
| tablet (768px) | 16px | Yes | 12 | No | 15801px |
| desktop (1280px) | 16px | Yes | 12 | No | 13980px |
| wide (1920px) | 16px | Yes | 12 | No | 14338px |

### Breakpoint Changes

**375px → 768px** (mobile → tablet):
- H1 size: `48px` → `72px`
- Max grid columns: `4` → `12`
- Page height: `18071px` → `15801px`

**768px → 1280px** (tablet → desktop):
- H1 size: `72px` → `96px`
- Page height: `15801px` → `13980px`

**1280px → 1920px** (desktop → wide):
- Page height: `13980px` → `14338px`

## Interaction States

### Button States

**"Book a demo"**
```css
/* Focus */
background-color: rgb(17, 24, 39) → rgb(55, 65, 81);
outline: rgb(255, 255, 255) none 3px → rgb(255, 255, 255) auto 3px;
```

**"Book a demo"**
```css
/* Hover */
background-color: rgb(17, 24, 39) → rgb(20, 27, 43);
transform: none → matrix(1.00427, 0, 0, 1.00427, 0, 0);
```
```css
/* Focus */
background-color: rgb(17, 24, 39) → rgb(46, 56, 72);
transform: none → matrix(1.03877, 0, 0, 1.03877, 0, 0);
outline: rgb(255, 255, 255) none 3px → rgb(233, 241, 251) auto 2px;
```

**"Schedule a Call"**
```css
/* Focus */
background-color: rgba(0, 0, 0, 0.06) → rgba(0, 0, 0, 0.055);
outline: rgb(17, 24, 39) none 3px → rgb(16, 30, 53) auto 2px;
```

### Link Hover

```css
color: rgb(15, 17, 20) → rgb(249, 115, 22);
outline: rgb(15, 17, 20) none 3px → rgb(249, 115, 22) none 3px;
```

## Accessibility (WCAG 2.1)

**Overall Score: 25%** — 1 passing, 3 failing color pairs

### Failing Color Pairs

| Foreground | Background | Ratio | Level | Used On |
|------------|------------|-------|-------|---------|
| `#6b7280` | `#f3f4f6` | 4.39:1 | FAIL | span (3x) |

### Passing Color Pairs

| Foreground | Background | Ratio | Level |
|------------|------------|-------|-------|
| `#ffffff` | `#111827` | 17.74:1 | AAA |

## Design System Score

**Overall: 72/100 (Grade: C)**

| Category | Score |
|----------|-------|
| Color Discipline | 92/100 |
| Typography Consistency | 82/100 |
| Spacing System | 85/100 |
| Shadow Consistency | 62/100 |
| Border Radius Consistency | 80/100 |
| Accessibility | 25/100 |
| CSS Tokenization | 100/100 |

**Strengths:** Tight, disciplined color palette, Well-defined spacing scale, Good CSS variable tokenization

**Issues:**
- 3 WCAG contrast failures
- 121 !important rules — prefer specificity over overrides
- 58% of CSS is unused — consider purging
- 334 duplicate CSS declarations

## Gradients

**34 unique gradients** detected.

| Type | Direction | Stops | Classification |
|------|-----------|-------|----------------|
| linear | — | 3 | bold |
| linear | to top | 2 | brand |
| linear | to right | 2 | brand |
| linear | to left | 2 | brand |
| linear | to right | 2 | brand |
| linear | — | 2 | brand |
| radial | circle at 100% 0% | 2 | brand |
| linear | to right | 2 | brand |
| linear | — | 2 | brand |
| linear | to left | 2 | brand |
| linear | — | 2 | brand |
| linear | to right bottom | 2 | brand |
| radial | circle | 2 | brand |
| radial | circle | 4 | bold |
| linear | to right | 3 | bold |

```css
background: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.9));
background: linear-gradient(to top, rgb(255, 255, 255) 30%, rgba(0, 0, 0, 0) 70%);
background: linear-gradient(to right, rgb(249, 250, 251), rgba(0, 0, 0, 0));
background: linear-gradient(to left, rgb(249, 250, 251), rgba(0, 0, 0, 0));
background: linear-gradient(to right, rgba(0, 0, 0, 0.08) 1px, rgba(0, 0, 0, 0) 1px);
```

## Z-Index Map

**12 unique z-index values** across 2 layers.

| Layer | Range | Elements |
|-------|-------|----------|
| sticky | 10,50 | section.r.e.l.a.t.i.v.e. .z.-.1.0. .m.i.n.-.h.-.[.1.0.0.d.v.h.]. .p.t.-.3.2. .p.b.-.1.6. .p.x.-.6. .m.d.:.p.x.-.1.2. .f.l.e.x. .f.l.e.x.-.c.o.l. .j.u.s.t.i.f.y.-.c.e.n.t.e.r. .w.-.f.u.l.l, div.a.b.s.o.l.u.t.e. .b.o.t.t.o.m.-.1.0. .-.l.e.f.t.-.1.0. .f.l.e.x. .f.l.e.x.-.c.o.l. .g.a.p.-.1. .s.u.r.f.a.c.e.-.g.l.a.s.s. .p.-.4. .r.o.u.n.d.e.d.-.x.l. .b.o.r.d.e.r. .t.e.x.t.-.x.s. .f.o.n.t.-.m.o.n.o. .t.e.x.t.-.z.i.n.c.-.5.0.0. .z.-.1.0. .s.h.a.d.o.w.-.2.x.l. .b.o.r.d.e.r.-.w.h.i.t.e./.1.0, div |
| base | -10,7 | div.a.b.s.o.l.u.t.e. .t.o.p.-.1./.2. .l.e.f.t.-.1./.2. .-.t.r.a.n.s.l.a.t.e.-.x.-.1./.2. .-.t.r.a.n.s.l.a.t.e.-.y.-.1./.2. .w.-.[.6.0.0.p.x.]. .h.-.[.6.0.0.p.x.]. .b.g.-.a.c.c.e.n.t./.5. .r.o.u.n.d.e.d.-.f.u.l.l. .b.l.u.r.-.[.1.0.0.p.x.]. .-.z.-.1.0, div, div |

## SVG Icons

**17 unique SVG icons** detected. Dominant style: **outlined**.

| Size Class | Count |
|------------|-------|
| xs | 2 |
| sm | 3 |
| md | 8 |
| lg | 1 |
| xl | 3 |

**Icon colors:** `currentColor`, `black`, `rgba(255,255,255,0.6)`, `rgb(0, 0, 0)`, `white`

## Font Files

| Family | Source | Weights | Styles |
|--------|--------|---------|--------|
| Inter | google-fonts | 300, 400, 500, 600 | normal |
| Sora | google-fonts | 300, 400, 500, 600 | normal |
| JetBrains Mono | google-fonts | 400, 500 | normal |

**Google Fonts URL:** `https://fonts.googleapis.com/`

## Image Style Patterns

| Pattern | Count | Key Styles |
|---------|-------|------------|
| general | 2 | objectFit: cover, borderRadius: 0px, shape: square |
| hero | 1 | objectFit: cover, borderRadius: 0px, shape: square |
| thumbnail | 1 | objectFit: fill, borderRadius: 0px, shape: square |

**Aspect ratios:** 4:3 (2x), 16:9 (1x), 21:9 (1x)

## Motion Language

**Feel:** mixed · **Scroll-linked:** yes

### Duration Tokens

| name | value | ms |
|---|---|---|
| `instant` | `75ms` | 75 |
| `xs` | `100ms` | 100 |
| `sm` | `200ms` | 200 |
| `md` | `300ms` | 300 |
| `lg` | `500ms` | 500 |
| `xl` | `1s` | 1000 |

### Easing Families

- **custom** (94 uses) — `cubic-bezier(0.4, 0, 0.2, 1)`
- **ease-out** (25 uses) — `cubic-bezier(0, 0, 0.2, 1)`, `cubic-bezier(0.16, 1, 0.3, 1)`, `cubic-bezier(0.23, 1, 0.32, 1)`

### Keyframes In Use

| name | kind | properties | uses |
|---|---|---|---|
| `gridMove` | slide-y | transform | 8 |
| `marquee` | slide-x | transform | 2 |
| `barPulse1` | custom | height | 3 |
| `barPulse2` | custom | height | 3 |
| `barPulse3` | custom | height | 2 |
| `barPulse4` | custom | height | 2 |
| `barPulse5` | custom | height | 2 |
| `floatLayer` | slide-y | transform | 3 |
| `pulse` | fade | opacity | 11 |
| `schemaNodePulse` | slide | transform, opacity, box-shadow | 11 |
| `schemaRingSpin` | slide | transform | 5 |
| `schemaRingSpinInset` | rotate | transform | 7 |
| `schemaBoxSpin` | slide | transform | 1 |
| `schemaLineHCenter` | reveal | transform, opacity | 8 |
| `schemaLineVCenter` | reveal | transform, opacity | 6 |
| `schemaFlash` | fade | opacity, background, box-shadow | 16 |
| `schemaPulseDot` | reveal | transform, opacity, box-shadow | 2 |
| `schemaPulseDotPos` | slide | transform, opacity, box-shadow | 2 |
| `core-pulse-anim` | slide | transform, box-shadow | 1 |
| `radar-pull-anim` | slide | transform, opacity, border-width | 3 |

## Component Anatomy

### card — 13 instances

**Slots:** description
**Sizes:** md

### button — 3 instances

**Slots:** label
**Sizes:** sm

## Brand Voice

**Tone:** neutral · **Pronoun:** you-only · **Headings:** Title Case (tight)

### Top CTA Verbs

- **book** (2)
- **schedule** (1)

### Button Copy Patterns

- "book a demo" (2×)
- "schedule a call" (1×)

### Sample Headings

> The travel operating system for modern operators.
> The systems, the team, and the volume are already in place with unbeatable inventory depth.
> One Platform. Five Integrated Solutions.
> AgreeEase
> Atlas
> Advisory Services
> Travakey
> Supply. Book. Settle. Done.
> Asia-native. Globally ready.
> Operate at scale.

## Page Intent

**Type:** `legal` (confidence 0.26)

Alternates: blog-post (0.35)

## Section Roles

Reading order (top→bottom): hero → nav → pricing-table → content → feature-grid → testimonials → pricing-table → content → content → pricing-table → pricing-table → nav → footer → nav → footer

| # | Role | Heading | Confidence |
|---|------|---------|------------|
| 0 | hero | The travel operating system for modern operators. | 0.85 |
| 1 | nav | — | 0.9 |
| 2 | pricing-table | The systems, the team, and the volume are already in place with unbeatable inven | 0.9 |
| 3 | content | One Platform. Five Integrated Solutions. | 0.3 |
| 4 | feature-grid | Supply. Book. Settle. Done. | 0.8 |
| 5 | nav | — | 0.9 |
| 6 | testimonials | 360° COVERAGE | 0.4 |
| 7 | pricing-table | The Network at a Glance | 0.9 |
| 8 | content | BOOKING TOOLS | 0.3 |
| 9 | content | Travel infrastructure, end to end. | 0.3 |
| 10 | pricing-table | Infrastructure that scales across borders and markets. | 0.9 |
| 11 | pricing-table | Infrastructure that scales across borders and markets. | 0.9 |
| 12 | nav | Infrastructure that scales across borders and markets. | 0.4 |
| 13 | footer | > Ready to modernize? | 0.95 |
| 14 | footer | — | 0.95 |

## Material Language

**Label:** `flat` (confidence 0)

| Metric | Value |
|--------|-------|
| Avg saturation | 0.189 |
| Shadow profile | soft |
| Avg shadow blur | 0px |
| Max radius | 9999px |
| backdrop-filter in use | no |
| Gradients | 34 |

## Imagery Style

**Label:** `mixed` (confidence 0.167)
**Counts:** total 4, svg 2, icon 1, screenshot-like 0, photo-like 1
**Dominant aspect:** square-ish
**Radius profile on images:** square

## Component Library

**Detected:** `shadcn/ui` (confidence 0.65)

Evidence:
- shadcn css tokens

Also considered: vuetify (0.4), tailwindcss (0.3)

## Component Screenshots

9 retina crops written to `screenshots/`. Index: `*-screenshots.json`.

| Cluster | Variant | Size (px) | File |
|---------|---------|-----------|------|
| button--default--sm | 0 | 173 × 52 | `screenshots/button-default-sm-0.png` |
| button--default--sm | 1 | 175 × 48 | `screenshots/button-default-sm-1.png` |
| button--default--sm | 2 | 193 × 50 | `screenshots/button-default-sm-2.png` |
| card--default | 0 | 333 × 98 | `screenshots/card-default-0.png` |
| card--default | 1 | 333 × 98 | `screenshots/card-default-1.png` |
| card--default | 2 | 333 × 113 | `screenshots/card-default-2.png` |
| card--default--md | 0 | 450 × 450 | `screenshots/card-default-md-0.png` |
| card--default--md | 1 | 450 × 450 | `screenshots/card-default-md-1.png` |
| card--default--md | 2 | 450 × 450 | `screenshots/card-default-md-2.png` |

Full-page: `screenshots/full-page.png`

## Quick Start

To recreate this design in a new project:

1. **Install fonts:** Add `Inter` from Google Fonts or your font provider
2. **Import CSS variables:** Copy `variables.css` into your project
3. **Tailwind users:** Use the generated `tailwind.config.js` to extend your theme
4. **Design tokens:** Import `design-tokens.json` for tooling integration
