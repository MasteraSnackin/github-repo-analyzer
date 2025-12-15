#!/usr/bin/env python3
"""
GitHub Repository Analyzer
A tool that uses the GitHub API to analyze repository statistics and contributions.
"""

import requests
import json
from datetime import datetime

class GitHubRepoAnalyzer:
    def __init__(self, token=None):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"
    
    def get_repo_info(self, owner, repo):
        """Get basic repository information"""
        url = f"{self.base_url}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch repo: {response.status_code}"}
    
    def get_contributors(self, owner, repo):
        """Get list of contributors"""
        url = f"{self.base_url}/repos/{owner}/{repo}/contributors"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch contributors: {response.status_code}"}
    
    def get_languages(self, owner, repo):
        """Get programming languages used"""
        url = f"{self.base_url}/repos/{owner}/{repo}/languages"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch languages: {response.status_code}"}
    
    def analyze_repository(self, owner, repo):
        """Full repository analysis"""
        print(f"\n=== Analyzing {owner}/{repo} ===")
        
        # Get repo info
        repo_info = self.get_repo_info(owner, repo)
        if "error" not in repo_info:
            print(f"\nRepository: {repo_info['name']}")
            print(f"Description: {repo_info['description']}")
            print(f"Stars: {repo_info['stargazers_count']}")
            print(f"Forks: {repo_info['forks_count']}")
            print(f"Open Issues: {repo_info['open_issues_count']}")
            print(f"Created: {repo_info['created_at']}")
            print(f"Last Updated: {repo_info['updated_at']}")
        
        # Get contributors
        contributors = self.get_contributors(owner, repo)
        if isinstance(contributors, list):
            print(f"\nTop Contributors:")
            for i, contrib in enumerate(contributors[:5], 1):
                print(f"{i}. {contrib['login']} - {contrib['contributions']} contributions")
        
        # Get languages
        languages = self.get_languages(owner, repo)
        if isinstance(languages, dict) and "error" not in languages:
            print(f"\nLanguages:")
            total = sum(languages.values())
            for lang, bytes in languages.items():
                percentage = (bytes / total) * 100
                print(f"  {lang}: {percentage:.1f}%")

def main():
    # Example usage
    analyzer = GitHubRepoAnalyzer()
    
    # Analyze a popular repository
    analyzer.analyze_repository("torvalds", "linux")
    
    print("\n\nTo use this tool with your own token:")
    print("analyzer = GitHubRepoAnalyzer(token='your_github_token')")
    print("analyzer.analyze_repository('owner', 'repo')")

if __name__ == "__main__":
    main()
