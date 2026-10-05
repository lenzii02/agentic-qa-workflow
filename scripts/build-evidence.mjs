#!/usr/bin/env node
/**
 * Generic Evidence Builder
 * Maps Playwright JSON reporter output to structured evidence.json for Laya classification.
 */

import fs from 'fs';
import path from 'path';

const RESULTS_PATH = process.env.RESULTS_PATH || './test-results/results.json';
const OUTPUT_PATH = process.env.OUTPUT_PATH || './evidence/evidence.json';

function collectTests(node, out) {
  if (!node) return;
  if (node.suites) for (const s of node.suites) collectTests(s, out);
  if (node.specs) {
    for (const spec of node.specs) {
      const specTitle = spec.title || '';
      for (const t of (spec.tests || [])) {
        for (const r of (t.results || [])) {
          out.push({
            title: specTitle,
            status: r.status,
            duration: r.duration,
            error: (r.errors || []).map(e => e.message || '').join('\n'),
            stdout: (r.stdout || []).map(s => s.text || '').join('\n'),
            stderr: (r.stderr || []).map(s => s.text || '').join('\n'),
          });
        }
      }
    }
  }
}

function main() {
  if (!fs.existsSync(RESULTS_PATH)) {
    console.error(`[error] Results file not found: ${RESULTS_PATH}`);
    process.exit(1);
  }

  const rawData = JSON.parse(fs.readFileSync(RESULTS_PATH, 'utf8'));
  const flatTests = [];
  if (rawData.suites) collectTests(rawData, flatTests);

  console.log(`[evidence] Parsed ${flatTests.length} tests from ${RESULTS_PATH}`);

  const evidence = flatTests.map((t, index) => {
    const combined = [t.stdout, t.error].filter(Boolean).join('\n');
    const urlMatches = [...combined.matchAll(/https?:\/\/[^\s"']+/g)].map(m => m[0]).slice(0, 5);
    const urls = {};
    urlMatches.forEach((u, i) => { urls[`url_${i + 1}`] = u; });

    const tcMatch = t.title.match(/TC[-_]?\d+/i);
    const tcId = tcMatch ? tcMatch[0].toUpperCase() : `TC_${String(index + 1).padStart(3, '0')}`;

    return {
      test_id: tcId,
      title: t.title,
      actors: ["system"],
      module: "General",
      expected_result: t.title,
      playwright_status: t.status === 'passed' ? 'passed' : 'failed',
      actual: {
        urls,
        logs: combined.split('\n').filter(Boolean).slice(0, 15),
        snippets: combined.split('\n').filter(s => s.trim().length > 15).slice(0, 5),
        error: (t.error || '').slice(0, 1000),
        duration_ms: t.duration || 0,
      },
      laya_state_hint: `TC ${tcId} | Title:${t.title} | Status:${t.status}`,
    };
  });

  fs.mkdirSync(path.dirname(OUTPUT_PATH), { recursive: true });
  fs.writeFileSync(OUTPUT_PATH, JSON.stringify(evidence, null, 2), 'utf8');
  console.log(`[done] Wrote ${evidence.length} evidence items to ${OUTPUT_PATH}`);
}

main();
