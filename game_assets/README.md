# AI Engineer Assessment: Smart Game Asset Pipeline

## Objective
Build a Python tool that analyzes game assets and identifies optimization opportunities to reduce game size, improve loading times, and enhance performance across different platforms.

## Problem Statement

Game developers often struggle with asset management as projects grow. Assets accumulate over time, leading to:
- **Bloated game sizes** due to unused or oversized assets
- **Poor performance** from unoptimized textures and models
- **Platform-specific issues** when assets aren't optimized for target devices
- **Manual inefficiencies** in identifying which assets need attention

Your task is to build an intelligent asset analysis system that helps developers optimize their game assets automatically.

## What You Need to Build

### Core Requirements (Take-home: 45-60 minutes)

1. **Asset Analyzer**: Parse the provided JSON file containing game asset metadata
2. **Inefficiency Detection**: Identify assets that need optimization based on defined criteria
3. **Optimization Suggestions**: Recommend specific actions for each problematic asset
4. **CLI Interface**: Provide a command-line tool for developers to use

### Asset Inefficiency Definitions

An asset is considered inefficient if it meets any of these criteria:

- **Oversized Textures**: Texture files > 2MB that are used < 10 times in the game
- **Wrong Format**: Using uncompressed formats (PNG, BMP) for textures when compressed formats (DXT, ASTC) would work
- **Unused Assets**: Assets with usage_count = 0 (never referenced in game)
- **Platform Mismatch**: High-resolution assets (> 1024x1024) used on mobile platforms
- **Redundant Audio**: Audio files > 1MB in uncompressed WAV format
- **Oversized Models**: 3D models with > 10,000 polygons used for background/minor objects

### CLI Interface Requirements

Your CLI should support these commands:
```bash
# Analyze all assets and show summary
python asset_analyzer.py analyze

# Show only inefficient assets
python asset_analyzer.py analyze --inefficient-only

# Filter by asset type
python asset_analyzer.py analyze --type texture

# Export results to file
python asset_analyzer.py analyze --output report.json

# Show optimization suggestions
python asset_analyzer.py suggest --asset-id "texture_001"
```

Choose the approach that best demonstrates your problem-solving style.

## Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Files Provided
- `game_assets.json` - Sample asset database (150+ assets)
- `requirements.txt` - Python dependencies (you can chose to add anything else that you need to)
- `sample_output.txt` - Expected output examples
- `README.md` - This document

### API Keys (Optional)
If needed, do set up a limited use API key in an .env file for:
- OpenAI GPT-4
- Anthropic Claude

### Evaluation Criteria
- **Code Quality**: Clean, readable, well-structured Python
- **Problem Solving**: How you break down and tackle the requirements
- **AI Integration**: Thoughtful use of AI where appropriate (or solid rule-based logic)
- **User Experience**: Intuitive CLI design and clear output
- **Extensibility**: How easy it is to add new features during live session

### Submission
- Complete Python solution with all required features
- Brief documentation explaining your approach
- Any additional files needed to run your solution

Good luck! Focus on creating a tool that a game developer would actually want to use.