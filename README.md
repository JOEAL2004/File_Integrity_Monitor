# File Integrity Monitor

A Python-based security tool that monitors files in a directory using SHA-256 hashing and detects file integrity changes.

## Overview

File Integrity Monitor helps identify changes that happen to files inside a monitored directory. It uses the SHA-256 hashing algorithm to generate a digital fingerprint for each file.

The tool stores the known-good file hashes in a JSON baseline file. During monitoring, it compares the current file hashes with the stored baseline to identify modified, new, and deleted files.

The tool also validates the provided directory and handles common errors such as nonexistent paths, file paths instead of directories, invalid modes, and missing baseline files.

## Features

- Generate SHA-256 hashes for files
- Scan files inside a directory
- Create a JSON baseline of known file hashes
- Compare current files with the stored baseline
- Detect modified files
- Detect new files
- Detect deleted files
- Detect unchanged files
- Validate directory paths
- Handle missing baseline files
- Provide a security summary of detected changes

## How It Works

The tool has two main modes:

### 1. Create Mode

Create mode scans the selected directory and calculates the SHA-256 hash of each file.

The results are stored in `baseline.json`.

Example:

```text
config.txt     → SHA-256 hash
important.txt  → SHA-256 hash