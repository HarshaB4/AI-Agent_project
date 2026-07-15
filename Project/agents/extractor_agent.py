from rag.retriever import retrieve_context
from services.gemini_service import generate_response


def extract_profile(name, context):

    query = f"{name} {context}"

    print("\n" + "=" * 50)
    print("PROFILE EXTRACTION STARTED")
    print("=" * 50)

    # Retrieve relevant documents
    retrieved_data = retrieve_context(query)

    documents = retrieved_data.get("documents", [[]])[0]

    print(f"Documents Retrieved: {len(documents)}")

    if not documents:
        return {
            "error": "No documents retrieved from vector database"
        }

    print(f"First Document Length: {len(documents[0])}")

    # Use top 5 retrieved documents
    combined_context = "\n\n".join(documents[:5])

    # Limit prompt size
    combined_context = combined_context[:15000]

    print(f"Context Length: {len(combined_context)}")

    prompt = f"""
You are an expert AI researcher and profile generation assistant.

Your task is to generate a structured profile using ONLY the information available in the provided context.

Instructions:
1. Do NOT hallucinate or invent information.
2. Use only facts found in the context.
3. If information is unavailable, return "Not Found".
4. Extract as much information as possible.
5. Pay special attention to:
   - Executive Summary
   - Biography
   - Career Timeline
   - Education
   - Interests and Hobbies
   - Estimated Net Worth
   - Recent News
   - References
6. Return ONLY valid JSON.

CONTEXT:
{combined_context}

OUTPUT FORMAT:

{{
    "executive_summary": "",
    "basic_details": {{
        "full_name": "",
        "nationality": "",
        "current_role": "",
        "industry": "",
        "current_city": "",
        "current_country": ""
    }},
    "biography": "",
    "career_timeline": [
        {{
            "year": "",
            "role": ""
        }}
    ],
    "education": [
        {{
            "degree": "",
            "institution": ""
        }}
    ],
    "interests": [],
    "estimated_net_worth": "",
    "recent_news": [],
    "references": []
}}
"""

    try:

        print("\nSending Request To Gemini...")

        response = generate_response(prompt)

        print("Profile Generated Successfully")

        print("\n===== RAW GEMINI RESPONSE =====")
        print(response)
        print("==============================\n")

        return response

    except Exception as e:

        print("Gemini Error:", str(e))

        return {
            "error": str(e)
        }