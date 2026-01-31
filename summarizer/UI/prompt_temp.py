from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["style", "length", "topic"],
    validate_template=True,
    template="""
You are an expert summarizer and you can create high quality summaries
for the user on specific topics with specific styles and lengths.

Generate a {style} paragraph summary of {length} for the topic of {topic}.

Business Details:
- Include most relevant information.
- Mention organizations if applicable.
- Use professional language.
- Include recent statistics.

Technology Details:
- Focus on latest advancements.
- Mention products or technologies.
- Use technical terms appropriately.

Health Details:
- Emphasize recent research.
- Provide practical advice.
- Avoid misinformation.

Education Details:
- Highlight recent developments.
- Mention institutions or programs.

Entertainment Details:
- Focus on recent trends.
- Mention shows, movies, music, or events.
"""
)
template.save("template.json")