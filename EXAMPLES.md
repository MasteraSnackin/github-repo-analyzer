# Usage Examples

## Basic Analysis
```python
from analyzer import GitHubRepoAnalyzer
analyzer = GitHubRepoAnalyzer()
analyzer.analyze_repository("github", "docs")
```

## With Authentication
```python
analyzer = GitHubRepoAnalyzer(token="ghp_xxx")
analyzer.analyze_repository("microsoft", "vscode")
```
