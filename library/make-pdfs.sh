#!/bin/sh
# Makes the flyer and poster kit PDFs for one ride.
#   ./library/make-pdfs.sh 2026-11-04
# Needs WeasyPrint: brew install weasyprint
set -e
cd "$(dirname "$0")"
date="${1:?Give the ride date, like 2026-11-04}"
out="rides/$date"
mkdir -p "$out"
weasyprint flyer.html "$out/flyer.pdf" 2>/dev/null
weasyprint poster-kit.html "$out/poster-kit.pdf" 2>/dev/null
weasyprint handlebar-tag.html "$out/handlebar-tag.pdf" 2>/dev/null
echo "Made the flyer, poster kit and handlebar tags in $out"
echo "Look at every page before printing, and scan the QR code with your phone."
