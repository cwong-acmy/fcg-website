# Design System: FCG Group - Travel Infrastructure

> Extracted from [https://hostmyclaudehtml.com/p/_Y67ztwQOo](https://hostmyclaudehtml.com/p/_Y67ztwQOo) by brandmd

## 1. Visual Theme & Atmosphere

**Overall mood:** Balanced and professional

**Density:** Moderate. The layout uses a varied spacing scale.

**Shape language:** Rounded, friendly aesthetic with generous corner radii.

**Depth:** Uses 5 shadow styles for layering and elevation.

## 2. Color Palette & Roles

- **White** (`#FFFFFF`) — Page background
- **Dark Blue** (`#111827`) — Dark background / footer
- **Orange** (`#F97316`) — Accent background
- **Muted Blue** (`#9CA3AF`) — Secondary background
- **Dark gray** (`#71717A`) — Secondary background
- **Black** (`#000000`) — Primary text
- **Dark Muted Blue** (`#6B7280`) — Secondary text
- **Light Muted Blue** (`#E5E7EB`) — Divider / border
- **Black** (`#0000001F`) — Divider / border

## 3. Typography Rules

**Primary font:** Inter
**Secondary font:** SFMono-Regular

**Fonts by role:**
- Headings: Inter, SFMono-Regular
- Body: Inter

**All detected fonts:** Inter (780), SFMono-Regular (162), JetBrains Mono (32)

**Type scale:**
- Headings: 24px, 30px, 48px, 60px, 72px, 144px
- Body / UI: 14px, 16px, 18px, 20px
- Captions / Small: 8px, 9px, 10px, 11.52px, 12px

**Weights in use:** 300, 400, 500, 600, 700

**Line heights:** 24px, 16px, 15px, 28px, 20px, 17.28px, 12px, 22.75px, 72px, 13.5px

**Letter spacing:** 0.8px, -1.8px, -3px, -0.5px, -0.6px, -0.75px

## 4. Component Stylings

### Buttons
- Background: `rgb(17, 24, 39)`
- Text color: `rgb(255, 255, 255)`
- Corner radius: 9999px
- Padding: 16px 32px 16px 32px
- Font: 14px, weight 500

### Cards
- Background: `rgba(0, 0, 0, 0.05)`
- Corner radius: 16px
- Padding: 16px 16px 16px 16px

### Inputs
- Border color: `#E5E7EB`

## 5. Layout Principles

**Spacing scale:** 1px, 4px, 8px, 12px, 16px, 24px, 32px, 40px

**Base unit:** 4px grid (values are mostly multiples of 4).

**Border radii:** 2px, 4px, 8px, 12px, 16px, 24px, 32px, 9999px

## 6. Guidelines

### Do
- Use 4px grid for all spacing
- Use `#F97316` for primary actions and CTAs
- Use `Inter` as the primary typeface

### Don't
- Don't introduce colors outside the palette above
- Don't mix fonts beyond Inter and SFMono-Regular
- Don't use inline styles when the design system covers the pattern
- Don't use border-radius values outside: 2px, 4px, 8px, 12px, 16px, 24px, 32px, 9999px
