from datetime import datetime
from dotenv import load_dotenv
from microagent import Microagent, Agent
from duckduckgo_search import DDGS

load_dotenv()
client = Microagent(llm_type='groq')
ddgs = DDGS()

def search_web(query):
    current_date = datetime.now().strftime("%Y-%m")
    results = ddgs.text(f"{query} {current_date}", max_results=10)
    if results:
        news_results = "\n\n".join(
            f"Title: {result['title']}\nURL: {result['href']}\nDescription: {result['body']}" for result in results
        )
        return news_results.strip()
    else:
        return f"Could not find news results for {query}."

def analyze_research(raw_news):
    researcher_agent = Agent(
        name="Research Assistant",
        instructions="""Your role is to analyze and synthesize the raw search results. You should:
        1. Remove duplicate information and redundant content
        2. Identify and merge related topics and themes
        3. Verify information consistency across sources
        4. Prioritize recent and relevant information
        5. Extract key facts, statistics, and quotes
        6. Identify primary sources when available
        7. Flag any contradictory information
        8. Maintain proper attribution for important claims
        9. Organize information in a logical sequence
        10. Preserve important context and relationships between topics""",
        model="llama3-groq-70b-8192-tool-use-preview"
    )
    research_analysis_response = client.run(
        agent=researcher_agent,
        messages=[{"role": "user", "content": raw_news}],
    )
    deduplicated_news = research_analysis_response.messages[-1]["content"]
    return deduplicated_news

def write_article(deduplicated_news):
    writer_agent = Agent(
        name="Writer Assistant",
        instructions="""Your role is to transform the deduplicated research results into a polished, publication-ready article. You should:
        1. Organize content into clear, thematic sections
        2. Write in a professional yet engaging tone, that is genuine and informative
        3. Ensure proper flow between topics
        4. Add relevant context where needed
        5. Maintain factual accuracy while making complex topics accessible
        6. Include a brief summary at the beginning
        7. Format with clear headlines and subheadings
        8. Preserve all key information from the source material""",
        model="llama3-groq-70b-8192-tool-use-preview"
    )
    article_response = client.run(
        agent=writer_agent,
        messages=[{"role": "user", "content": deduplicated_news}],
    )
    full_article = article_response.messages[-1]["content"]
    return full_article

def generate_article(query):
    raw_news = search_web(query)
    deduplicated_news = analyze_research(raw_news)
    return write_article(deduplicated_news)