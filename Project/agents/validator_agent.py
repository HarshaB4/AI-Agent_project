import json

def validate_profile(profile_data):

    warnings = []

    try:

        # If Gemini returns a JSON string
        if isinstance(profile_data, str):

            profile_data = profile_data.replace(
                "```json", ""
            )

            profile_data = profile_data.replace(
                "```", ""
            )

            profile_data = profile_data.strip()

            profile = json.loads(profile_data)

        else:
            profile = profile_data

        # Executive Summary
        if profile.get("executive_summary") in [
            "",
            "Not Found",
            None
        ]:
            warnings.append(
                "Executive summary unavailable"
            )

        # Net Worth
        if profile.get("estimated_net_worth") in [
            "",
            "Not Found",
            None
        ]:
            warnings.append(
                "Net worth information unavailable"
            )

        # Recent News
        recent_news = profile.get(
            "recent_news",
            []
        )

        if not recent_news or recent_news == [
            "Not Found"
        ]:
            warnings.append(
                "Recent news unavailable"
            )

        # Interests
        interests = profile.get(
            "interests",
            []
        )

        if not interests or interests == [
            "Not Found"
        ]:
            warnings.append(
                "Interests information unavailable"
            )

        # References
        references = profile.get(
            "references",
            []
        )

        if not references or references == [
            "Not Found"
        ]:
            warnings.append(
                "References unavailable"
            )

        return warnings

    except Exception as e:

        return [
            f"Validation Error: {str(e)}"
        ]