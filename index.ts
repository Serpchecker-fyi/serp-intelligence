#!/usr/bin/env node

interface SERPIntelligenceInput {
  keyword: string;
  searchIntent: string;
  serpVisibility: number;
  searchIntent_score: number;
  rankingPattern: number;
  competitorVisibility: number;
  serpFeature: number;
  contentOpportunity: number;
}

interface SERPIntelligenceOutput {
  keyword: string;
  searchIntent: string;
  serpVisibilityScore: number;
  searchIntentScore: number;
  rankingPatternScore: number;
  competitorVisibilityScore: number;
  serpFeatureScore: number;
  contentOpportunityScore: number;
  overallSERPIntelligenceIndex: number;
  priorityAction: string;
  serpChannels: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    serpVisibility: "SERP Visibility",
    searchIntent: "Search Intent",
    rankingPattern: "Ranking Pattern",
    competitorVisibility: "Competitor Visibility",
    serpFeature: "SERP Feature",
    contentOpportunity: "Content Opportunity",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getSERPChannels(visibility: number, feature: number, intent: number, competitor: number): Record<string, number> {
  return {
    "Organic Results": Math.min(100, Math.round(visibility * 1.0)),
    "Featured Snippets": Math.min(100, Math.round(feature * 1.0)),
    "People Also Ask": Math.min(100, Math.round(intent * 1.0)),
    "Local Pack": Math.min(100, Math.round(competitor * 1.0)),
  };
}

export function analyzeSERPIntelligence(input: SERPIntelligenceInput): SERPIntelligenceOutput {
  const scores = {
    serpVisibility: input.serpVisibility,
    searchIntent: input.searchIntent_score,
    rankingPattern: input.rankingPattern,
    competitorVisibility: input.competitorVisibility,
    serpFeature: input.serpFeature,
    contentOpportunity: input.contentOpportunity,
  };
  const overallSERPIntelligenceIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    keyword: input.keyword,
    searchIntent: input.searchIntent.charAt(0).toUpperCase() + input.searchIntent.slice(1),
    serpVisibilityScore: input.serpVisibility,
    searchIntentScore: input.searchIntent_score,
    rankingPatternScore: input.rankingPattern,
    competitorVisibilityScore: input.competitorVisibility,
    serpFeatureScore: input.serpFeature,
    contentOpportunityScore: input.contentOpportunity,
    overallSERPIntelligenceIndex,
    priorityAction: getPriorityAction(scores),
    serpChannels: getSERPChannels(input.serpVisibility, input.serpFeature, input.searchIntent_score, input.competitorVisibility),
  };
}

const args = process.argv.slice(2);
const keyword = args[0] || "target-keyword";
const searchIntent = args[1] || "informational";
const serpVisibility = parseInt(args[2]) || 88;
const searchIntent_score = parseInt(args[3]) || 82;
const rankingPattern = parseInt(args[4]) || 85;
const competitorVisibility = parseInt(args[5]) || 78;
const serpFeature = parseInt(args[6]) || 90;
const contentOpportunity = parseInt(args[7]) || 84;

const result = analyzeSERPIntelligence({
  keyword, searchIntent, serpVisibility, searchIntent_score,
  rankingPattern, competitorVisibility, serpFeature, contentOpportunity,
});

console.log(`Keyword: ${result.keyword}`);
console.log(`Search Intent: ${result.searchIntent}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`SERP Visibility Score:         ${result.serpVisibilityScore}/100  [${getStatus(result.serpVisibilityScore)}]`);
console.log(`Search Intent Score:           ${result.searchIntentScore}/100  [${getStatus(result.searchIntentScore)}]`);
console.log(`Ranking Pattern Score:         ${result.rankingPatternScore}/100  [${getStatus(result.rankingPatternScore)}]`);
console.log(`Competitor Visibility Score:   ${result.competitorVisibilityScore}/100  [${getStatus(result.competitorVisibilityScore)}]`);
console.log(`SERP Feature Score:            ${result.serpFeatureScore}/100  [${getStatus(result.serpFeatureScore)}]`);
console.log(`Content Opportunity Score:     ${result.contentOpportunityScore}/100  [${getStatus(result.contentOpportunityScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall SERP Intelligence Index: ${result.overallSERPIntelligenceIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nSERP Channels:");
Object.entries(result.serpChannels).forEach(([channel, score]) => {
  console.log(`  ${channel.padEnd(22)} ${score}/100`);
});
