# Horizon Log Report Generator

A lightweight and practical tool to generate structured, easy-to-read reports from Omnissa / VMware Horizon log bundles.


## Overview

Reviewing Horizon logs can be time-consuming and fragmented across multiple files and components. This tool simplifies the process by extracting key information and consolidating it into a single, readable report.

The Horizon Log Report Generator parses valid Horizon log bundles and produces a comprehensive report that helps identify issues faster and more efficiently.


## Features

The generated report includes:

- Machine Information
- Additional Server Roles
- Running Services (Horizon)
- Open Ports (Horizon)
- Installed Applications
- Certificates
- locked.properties File Analysis


## Purpose

The goal of this tool is to:

- Simplify log analysis for Horizon log bundles
- Centralize relevant diagnostic information
- Reduce troubleshooting time
- Improve readability and accessibility of log data


## Installation

1. Download the installer `HorizonReportGeneratorInstaller.zip` from this repository.

2. Extract and run the installer.

3. Once installed, a new option will be added to the Windows context menu.


## How to Use

1. Locate any valid Horizon log bundle (`.zip` file)

2. Right-click the file

3. Select `Horizon Report → Horizon Report Generator`

4. The tool will generate a report in the same directory as the original log bundle


## Built With

- Python — Core scripting logic
- PyInstaller — Packaging the script into a standalone `.exe`
- Inno Setup — Creating the installer and integrating with Windows context menu


## Output

The generated report is a single, structured file designed for:

- Quick scanning
- Easy sharing
- Efficient troubleshooting


## Use Cases

- Troubleshooting Horizon environments
- Support and diagnostic workflows
- System health reviews
- Log analysis automation


## Requirements

- Windows (Only OS supported)
- Valid Omnissa / VMware Horizon log bundle


## Notes

- The tool is designed to work with properly generated Horizon log bundles
- Ensure Horizon logs are complete for accurate report generation


## Author

- [@Maiker260](https://github.com/Maiker260)
