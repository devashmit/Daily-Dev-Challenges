# 🐍 Automated File Organizer — Day 21 Python Challenge

**Issue:** [#391](https://github.com/abhishek-goswami1/Daily-Dev-Challenges/issues/391) | Week 3 | Beginner

## 📋 Description

CLI tool that scans a folder and sorts files into subfolders by extension. Logs every move. `--dry-run` flag previews without moving anything.

## ✨ Features
- Sorts into images/, documents/, videos/, audio/, code/, others/
- `--dry-run` preview mode
- `--source` flag for target folder
- Logs to `organizer.log`
- Safe duplicate handling

## 🚀 How to Run
```bash
python organizer.py --source /path/to/folder --dry-run
python organizer.py --source /path/to/folder
```
