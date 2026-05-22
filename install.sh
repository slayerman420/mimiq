#!/bin/bash
# Mimiq — Claude Skills Installer
# Installs voice-capture, content-audit, post-strategist, and social-suite
# into the global ~/.claude/skills/ directory

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║         🪞 Mimiq — Claude Skills             ║${NC}"
echo -e "${CYAN}║   Voice · Audit · Ghostwrite · Strategy      ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════╝${NC}"
echo ""

# Detect if running via curl | bash (remote) or from cloned repo
if [ -n "$BASH_SOURCE" ] && [ "$BASH_SOURCE" != "bash" ] && [ -f "$BASH_SOURCE" ]; then
    SCRIPT_DIR="$(cd "$(dirname "$BASH_SOURCE")" && pwd)"
else
    echo -e "${YELLOW}Running remote install — cloning repository...${NC}"
    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 https://github.com/slayerman420/mimiq.git "$TEMP_DIR/mimiq" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo -e "${RED}Failed to clone repository. Check your internet connection.${NC}"
        exit 1
    fi
    SCRIPT_DIR="$TEMP_DIR/mimiq"
fi

# Global install target
SKILLS_DIR="$HOME/.claude/skills"

echo -e "${BLUE}Source:${NC}  $SCRIPT_DIR/skills"
echo -e "${BLUE}Target:${NC}  $SKILLS_DIR"
echo ""

# Check if Claude Code is available
if command -v claude &>/dev/null; then
    echo -e "${GREEN}✓ Claude Code detected${NC}"
else
    echo -e "${YELLOW}⚠ Claude Code not found in PATH${NC}"
    if [ -t 0 ]; then
        read -p "  Continue anyway? (y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Installation cancelled."
            exit 0
        fi
    else
        echo "  Continuing (non-interactive mode)..."
    fi
fi

# Create global skills directory
mkdir -p "$SKILLS_DIR"

# Skills to install
SKILLS=(
    "social-suite"
    "voice-capture"
    "content-audit"
    "post-strategist"
)

echo -e "${BLUE}Installing Mimiq skills...${NC}"

SKILL_COUNT=0
for skill in "${SKILLS[@]}"; do
    if [ -f "$SCRIPT_DIR/skills/$skill/SKILL.md" ]; then
        mkdir -p "$SKILLS_DIR/$skill"
        cp "$SCRIPT_DIR/skills/$skill/SKILL.md" "$SKILLS_DIR/$skill/SKILL.md"
        echo -e "  ${GREEN}✓${NC} $skill"
        SKILL_COUNT=$((SKILL_COUNT + 1))
    else
        echo -e "  ${RED}✗${NC} $skill (not found — install may be incomplete)"
    fi
done

# Cleanup temp directory if used
if [ -n "$TEMP_DIR" ] && [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi

# Summary
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║         Installation Complete! 🪞            ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  Skills installed: ${GREEN}$SKILL_COUNT / 4${NC}"
echo -e "  Location:         ${CYAN}$SKILLS_DIR${NC}"
echo ""
echo -e "${CYAN}Available Commands (Claude Code):${NC}"
echo "  /social-suite       Full setup — start here"
echo "  /voice-capture      Capture your writing style"
echo "  /content-audit      Analyze your best content"
echo "  /post-strategist    Ghostwrite posts in your voice"
echo ""
echo -e "${CYAN}Claude.ai Chat / Cowork:${NC}"
echo "  Skills trigger automatically. Just say:"
echo "  \"Help me with my social media\" or \"Write a post for me\""
echo ""
echo -e "  ${YELLOW}Start a new Claude session to activate the skills.${NC}"
echo ""
