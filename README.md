# Visual Chinese Character Learning

A minimalist, distraction-free flashcard application designed beautifully for augmented reality (AR) glasses. It features a high-contrast layout displaying large Chinese characters with English translations directly in your field of view.

## Quick Start

The easiest way to initialize and start the program is via the included launch script, which will automatically create a Python virtual environment to keep your system dependencies clean before launching.

```bash
# Provide execute permissions (first time only)
chmod +x run.sh

# Run the launch script
./run.sh
```

## Features
- **AR Optimized**: Full-screen, borderless display using pure black backgrounds which are completely transparent when projected onto AR lenses.
- **Visual Focus**: Characters are massive while English text is small and dim, focusing purely on visual shape recognition without pinyin or pronunciation distractions.
- **Easy Vocabulary Management**: Simply edit the `data/vocabulary.json` file to add your desired vocabulary.

## Controls
- **Right Arrow** or **Spacebar**: Next random card.
- **Left Arrow**: Previous card.
- **Escape**: Exit application completely.