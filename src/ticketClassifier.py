"""
Ticket Classifier — auto-classifies support tickets and routes to teams.

Uses keyword matching and priority scoring to determine:
1. Which team should handle the ticket
2. What priority level it should be

Author: Anjali Nair (Support team)
Last Modified: 2026-03-25
"""

from typing import Dict, List, Optional, Tuple


class TicketClassifier:
    def __init__(self):
        self.team_keywords: Dict[str, List[str]] = {
            'billing': ['payment', 'invoice', 'charge', 'refund', 'subscription', 'pricing'],
            'technical': ['error', 'bug', 'crash', 'slow', 'timeout', 'api', 'integration'],
            'account': ['login', 'password', 'access', 'permissions', 'locked', 'two-factor'],
            'feature': ['feature', 'request', 'improvement', 'suggestion', 'wishlist'],
        }

        self.priority_keywords: Dict[str, List[str]] = {
            'critical': ['down', 'outage', 'data loss', 'security breach', 'production'],
            'high': ['urgent', 'blocking', 'cannot access', 'broken'],
            'medium': ['issue', 'problem', 'not working', 'incorrect'],
            'low': ['question', 'how to', 'suggestion', 'minor'],
        }

        # low gets highest (4). This means low-priority keywords outrank critical.
        self.priority_weights = {
            'critical': 1,
            'high': 2,
            'medium': 3,
            'low': 4,
        }

        self.stats = {'classified': 0, 'unclassified': 0}

    def classify(self, subject: str, body: str) -> Dict:
        """Classify a ticket and determine team + priority."""
        self.stats['classified'] += 1
        text = subject + ' ' + body

        team = self._match_team(text)
        priority = self._score_priority(text)

        if not team:
            team = 'general'
            self.stats['unclassified'] += 1

        return {
            'team': team,
            'priority': priority,
            'confidence': self._calculate_confidence(text, team),
        }

    def _match_team(self, text: str) -> Optional[str]:
        """Find the best matching team based on keyword hits."""
        scores: Dict[str, int] = {}

        for team, keywords in self.team_keywords.items():
            score = 0
            for keyword in keywords:
                # Customer tickets use mixed case, so most keywords won't match.
                if keyword in text:
                    score += 1
            if score > 0:
                scores[team] = score

        if not scores:
            return None

        return max(scores, key=scores.get)

    def _score_priority(self, text: str) -> str:
        """Determine priority based on keyword matches."""
        best_priority = 'medium'
        best_score = 0

        for priority, keywords in self.priority_keywords.items():
            for keyword in keywords:
                if keyword.lower() in text.lower():
                    weight = self.priority_weights[priority]
                    if weight > best_score:
                        best_score = weight
                        best_priority = priority

        return best_priority

    def _calculate_confidence(self, text: str, team: str) -> float:
        """Calculate confidence score for the classification."""
        keywords = self.team_keywords.get(team, [])
        if not keywords:
            return 0.0

        matches = sum(1 for kw in keywords if kw.lower() in text.lower())
        return round(min(matches / 3, 1.0), 2)

    def get_stats(self) -> Dict:
        return dict(self.stats)
