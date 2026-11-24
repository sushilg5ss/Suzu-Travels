#!/usr/bin/env bash
# Cab Kit measurement: Lighthouse mobile x N runs per URL, prints the MEDIAN
# score / FCP / LCP / TBT / CLS / transfer KiB + benchmarkIndex.
# Use the median for the "> 3 pt drop = revert" speed rule (ENHANCEMENTS row 32).
# Build-time/agent tool only - never shipped to WordPress, no page writes.
#
# Usage:  bash measure.sh [-n RUNS] [-o OUTDIR] URL [URL ...]
#   default URLs = hub + delhi-to-manali-taxi, RUNS = 3
# Needs: node >= 18; lighthouse@12.6.1 (installed on first use into $LH_DIR,
# default ~/lh); the Playwright Chromium (auto-found under /opt/pw-browsers or
# ~/.cache/ms-playwright, or set CHROME_PATH). Uses HTTPS_PROXY if set.
set -u
RUNS=3
OUT="${TMPDIR:-/tmp}/szc-measure"
while getopts "n:o:" opt; do
  case $opt in
    n) RUNS="$OPTARG" ;;
    o) OUT="$OPTARG" ;;
    *) echo "usage: $0 [-n RUNS] [-o OUTDIR] URL..."; exit 2 ;;
  esac
done
shift $((OPTIND-1))
if [ $# -eq 0 ]; then
  set -- "https://suzutravels.com/cabs/" "https://suzutravels.com/cabs/delhi-to-manali-taxi/"
fi
LH_VER="12.6.1"
LH_DIR="${LH_DIR:-$HOME/lh}"
if [ ! -x "$LH_DIR/node_modules/.bin/lighthouse" ]; then
  mkdir -p "$LH_DIR"
  (cd "$LH_DIR" && { [ -f package.json ] || npm init -y >/dev/null; } && npm i "lighthouse@$LH_VER" --no-audit --no-fund >/dev/null 2>&1) || { echo "lighthouse install failed"; exit 1; }
fi
LH="$LH_DIR/node_modules/.bin/lighthouse"
if [ -z "${CHROME_PATH:-}" ]; then
  CHROME_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux*/chrome "$HOME"/.cache/ms-playwright/chromium-*/chrome-linux*/chrome 2>/dev/null | sort -V | tail -1)
fi
[ -x "${CHROME_PATH:-}" ] || { echo "no Chromium found - set CHROME_PATH"; exit 1; }
export CHROME_PATH
FLAGS="--headless=new --no-sandbox --disable-gpu --ignore-certificate-errors"
if [ -n "${HTTPS_PROXY:-}" ]; then FLAGS="$FLAGS --proxy-server=$HTTPS_PROXY"; fi
mkdir -p "$OUT"
echo "Lighthouse $LH_VER mobile, $RUNS runs per URL, Chromium: $CHROME_PATH"
for URL in "$@"; do
  TAG=$(echo "$URL" | sed -e 's#https\?://##' -e 's#[^A-Za-z0-9]#_#g')
  FILES=""
  for i in $(seq 1 "$RUNS"); do
    F="$OUT/$TAG.$i.json"
    "$LH" "$URL" --quiet --output=json --output-path="$F" \
      --only-categories=performance --form-factor=mobile \
      --chrome-flags="$FLAGS" --max-wait-for-load=60000 >/dev/null 2>"$OUT/$TAG.$i.err" \
      || { echo "  run $i failed (see $OUT/$TAG.$i.err)"; continue; }
    FILES="$FILES $F"
  done
  [ -n "$FILES" ] || { echo "$URL: no successful run"; continue; }
  node -e '
    var fs=require("fs");var url=process.argv[1];var files=process.argv.slice(2);
    var rows=[];
    files.forEach(function(f){try{var j=JSON.parse(fs.readFileSync(f,"utf8"));var a=j.audits;
      if(j.runtimeError){console.log("  "+f+": "+j.runtimeError.code);return;}
      rows.push({s:j.categories.performance.score,fcp:a["first-contentful-paint"].numericValue,
        lcp:a["largest-contentful-paint"].numericValue,tbt:a["total-blocking-time"].numericValue,
        cls:a["cumulative-layout-shift"].numericValue,kib:a["total-byte-weight"].numericValue/1024,
        bi:j.environment.benchmarkIndex});}catch(e){console.log("  bad json "+f);}});
    if(!rows.length){console.log(url+": no valid run");process.exit(0);}
    function med(k){var v=rows.map(function(r){return r[k];}).sort(function(x,y){return x-y;});
      var m=Math.floor(v.length/2);return v.length%2?v[m]:(v[m-1]+v[m])/2;}
    console.log(url);
    console.log("  runs   : "+rows.map(function(r){return Math.round(r.s*100)+" (TBT "+Math.round(r.tbt)+" ms)";}).join(" / "));
    console.log("  MEDIAN : score "+Math.round(med("s")*100)+" | FCP "+(med("fcp")/1000).toFixed(1)+" s | LCP "+(med("lcp")/1000).toFixed(1)+" s | TBT "+Math.round(med("tbt"))+" ms | CLS "+med("cls").toFixed(3)+" | "+Math.round(med("kib"))+" KiB | benchmarkIndex "+Math.round(med("bi")));
  ' "$URL" $FILES
done
