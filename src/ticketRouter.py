"""
Ticket Router — routes classified tickets to team queues.

Author: Anjali Nair (Support team)
Last Modified: 2026-03-25
"""

from typing import Dict, List, Optional
from collections import defaultdict


class TicketRouter:
    """Routes tickets to team queues based on classification."""

    def __init__(self):
        self.queues: Dict[str, List[Dict]] = defaultdict(list)
        self.routing_log: List[Dict] = []

    def route(self, ticket_id: str, classification: Dict, metadata: Optional[Dict] = None) -> Dict:
        """Route a ticket to the appropriate team queue."""
        team = classification.get('team', 'general')
        priority = classification.get('priority', 'medium')

        entry = {
            'ticket_id': ticket_id,
            'team': team,
            'priority': priority,
            'confidence': classification.get('confidence', 0),
            'metadata': metadata or {},
        }

        self.queues[team].append(entry)
        self.routing_log.append(entry)

        return {'routed': True, 'team': team, 'queue_position': len(self.queues[team])}

    def get_queue(self, team: str) -> List[Dict]:
        """Get all tickets in a team's queue, sorted by priority."""
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        queue = self.queues.get(team, [])
        return sorted(queue, key=lambda t: priority_order.get(t['priority'], 2))

    def get_queue_stats(self) -> Dict:
        return {
            team: len(tickets)
            for team, tickets in self.queues.items()
        }
