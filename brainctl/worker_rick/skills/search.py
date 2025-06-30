# brainctl/worker_rick/skills/search.py

from duckduckgo_search import DDGS

def handle(query: str) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)
        if not results:
            return "⚠️ No results found."

        response_lines = [f"- {item.get('title', 'No title')}: {item.get('href')}" 
                           for item in results]
        return "\n".join(response_lines)

