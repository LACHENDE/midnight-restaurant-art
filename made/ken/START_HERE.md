# Ken animation handoff for Claude

This package contains 20 Ken motion variants for Midnight Restaurant, a beginner Japanese-learning restaurant game. Read manifest.json before integration. Files are assets and previews, not an integrated game implementation.

## User requirements
- Preserve Ken: navy beanie, brown hair, olive jacket, cream shirt, clay/low-poly toy style.
- Keep his face BLANK. Facial features, if needed, belong to the game layer.
- Character poses and motion only: no captions, labels, dialogue, or baked backgrounds in game assets.
- Expressive motion, coherent inbetween poses, transparent backgrounds.
- Do NOT use Higgsfield or spend Higgsfield credits.
- Menus/props must remain consistent across frames; reuse a fixed graphic instead of regenerating its contents.

## What to use
current/: latest five redone clips (idle, confused/listening, order confirmation, paying, arrival/departure). These supersede the earlier eight-pose/white-background versions, which are intentionally omitted. Each has a 4x4 PNG sheet, transparent GIF, and lossless animated WebP. 16 drawn poses each. Movement frames are 80ms (12.5fps), idle 100ms (10fps), with longer holds. The arrival/departure GIF adds horizontal screen translation; its PNG sheet contains centered directional poses. Do not apply translation twice.

earlier/: 15 other selected motion variants with their source PNG sheets and GIF previews. Most earlier GIFs have baked dark backgrounds and some have title labels. They are reference previews, NOT transparent game sprites. Source sheet alpha ranges are listed in manifest.json, but edge quality/anchoring still needs visual QA. This package does NOT claim these older clips have received the v2 polish pass.

## Menu exception
The selected choosing-order preview is the FIXED version. Its primary sheet is a blank-menu clean plate. Composite ken-fixed-menu-art.png onto the card consistently; preserve overlapping fingers. The portable rebuild_fixed_menu_preview.py documents the existing placement/masking approach and requires Pillow/numpy. menu-original-sheet.png is only a source/reference; its changing icons must NOT be used as the final menu artwork. The script recreates the old labeled dark-background preview, so adapt its output step for transparent game exports.

## Integration guidance
1. Inspect the actual repository and its renderer before changing game code. No repo is included here. Previously discussed repositories: LACHENDE/midnight-restaurant and LACHENDE/midnight-restaurant-art; verify current structure.
2. Prefer source PNG sheets + an animation player for a canvas/game renderer. WebP is useful for direct animated-image display. GIF has binary transparency and coarser edges; PNG/WebP preserve soft alpha.
3. Grid dimensions and actual per-GIF-frame timing are in manifest.json. GIF preview frame sequences can repeat/reorder sheet poses; do not assume frame count equals cell count. Especially anger and entrance/exit.
4. Align torso/waist anchor and character scale across clips. AI-generated poses still have some shape/position variation; transparent export is not a guarantee of production-perfect registration.
5. Use idle as default, action clips once then return to idle. Hold listening/waiting/anger only as game state requires. Existing files loop for preview purposes.
6. Suggested flow: arrive -> idle -> call/choose -> confirmed -> wait -> itadakimasu -> eat -> delicious -> bill -> pay -> leave. Wrong-order, spicy, anger, confusion, and forgot-wallet are optional state branches.
7. Keep the older source artwork; improve transparent exports and timing without replacing approved design unnecessarily. Check on light and dark backgrounds, verify clipping and transitions.

## Complete motion inventory
- idle (latest_transparent_v2)
- confused (latest_transparent_v2)
- confirmed (latest_transparent_v2)
- paying (latest_transparent_v2)
- arrival-departure (latest_transparent_v2)
- hand-raise (earlier_preview_requires_export_polish)
- excited-hand-raise (earlier_preview_requires_export_polish)
- itadakimasu (earlier_preview_requires_export_polish)
- eating-ramen (earlier_preview_requires_export_polish)
- delicious (earlier_preview_requires_export_polish)
- goodbye (earlier_preview_requires_export_polish)
- wrong-order (earlier_preview_requires_export_polish)
- angry-annoyed (earlier_preview_requires_export_polish)
- angry-complaining (earlier_preview_requires_export_polish)
- angry-furious (earlier_preview_requires_export_polish)
- choosing-order (earlier_preview_requires_export_polish)
- waiting (earlier_preview_requires_export_polish)
- bill-request (earlier_preview_requires_export_polish)
- too-spicy (earlier_preview_requires_export_polish)
- forgot-wallet (earlier_preview_requires_export_polish)
