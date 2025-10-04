#!/bin/bash
#
# Check for upstream updates
# This script helps maintainers check if there are new updates from upstream
#

set -e

echo "🔍 Checking for upstream updates..."
echo ""

# Add upstream remote if it doesn't exist
if ! git remote | grep -q "^upstream$"; then
    echo "Adding upstream remote..."
    git remote add upstream https://github.com/mrlt8/docker-wyze-bridge.git
fi

# Fetch upstream
echo "Fetching upstream..."
git fetch upstream --tags

# Get current version
CURRENT_VERSION=$(grep "^VERSION=" app/.env | cut -d'=' -f2)
echo "📦 Current fork version: v$CURRENT_VERSION"

# Get latest upstream tag
LATEST_TAG=$(git ls-remote --tags upstream | grep -v '\^{}' | grep 'v[0-9]' | awk '{print $2}' | sed 's/refs\/tags\///' | sort -V | tail -1)
echo "📦 Latest upstream tag: $LATEST_TAG"

# Check commits behind
BEHIND=$(git rev-list --count HEAD..upstream/main 2>/dev/null || echo "0")
echo "📊 Commits behind upstream: $BEHIND"

echo ""

if [ "$BEHIND" -gt 0 ]; then
    echo "⚠️  Updates available!"
    echo ""
    echo "To view changes:"
    echo "  git log HEAD..upstream/main --oneline"
    echo ""
    echo "To view detailed diff:"
    echo "  git log HEAD..upstream/main --graph --decorate"
    echo ""
    echo "To merge updates:"
    echo "  git checkout main"
    echo "  git merge upstream/main"
    echo ""
    echo "See MAINTENANCE.md for complete sync procedures."
else
    echo "✅ Fork is up to date with upstream!"
fi

echo ""
echo "Useful commands:"
echo "  View upstream releases: git tag -l 'v*' | sort -V | tail -10"
echo "  View recent upstream commits: git log upstream/main --oneline -10"
echo "  Compare versions: git log v$CURRENT_VERSION..$LATEST_TAG --oneline"
