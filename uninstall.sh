#!/bin/bash
# Mimiq — Uninstaller

GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${CYAN}Uninstalling Mimiq skills...${NC}"
echo ""

SKILLS_DIR="$HOME/.claude/skills"

for skill in social-suite voice-capture content-audit post-strategist; do
    if [ -d "$SKILLS_DIR/$skill" ]; then
        rm -rf "$SKILLS_DIR/$skill"
        echo -e "  ${GREEN}✓${NC} Removed $skill"
    fi
done

echo ""
echo -e "${GREEN}Mimiq uninstalled.${NC}"
echo ""
