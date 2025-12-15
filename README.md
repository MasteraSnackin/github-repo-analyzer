# github-repo-analyzer

A GitHub API integration tool that analyzes repository statistics, contributions, and provides insights

## Features

- 📊 Fetch detailed repository information (stars, forks, issues)
- 👥 Analyze contributor statistics and rankings
- 💻 Programming language breakdown with percentages
- 🔍 Comprehensive repository insights
- 🚀 Easy to use command-line interface

## Installation

```bash
# Clone the repository
git clone https://github.com/MasteraSnackin/github-repo-analyzer.git
cd github-repo-analyzer

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from analyzer import GitHubRepoAnalyzer

# Initialize analyzer
analyzer = GitHubRepoAnalyzer()

# Analyze a repository
analyzer.analyze_repository("torvalds", "linux")
```

### With Authentication Token

For better rate limits, use a GitHub personal access token:

```python
analyzer = GitHubRepoAnalyzer(token="your_github_token")
analyzer.analyze_repository("owner", "repo")
```

## Example Output

```
=== Analyzing torvalds/linux ===

Repository: linux
Description: Linux kernel source tree
Stars: 150000
Forks: 50000
Open Issues: 1000
Created: 2011-09-04T22:48:12Z
Last Updated: 2025-12-15T10:00:00Z

Top Contributors:
1. torvalds - 25000 contributions
2. contributor2 - 15000 contributions
3. contributor3 - 10000 contributions

Languages:
  C: 95.5%
  Assembly: 2.1%
  Shell: 1.2%
  Python: 1.2%
```

## Requirements

- Python 3.7+
- requests library (>=2.28.0)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
