try:
    from app.text_processor import extract_keywords

    texts = [
        "Dependency management is extremely important in real projects.",
        "Old libraries cause production issues."
    ]

    print(extract_keywords(texts))
except ImportError as e:
    print(f"Test failed due to missing dependency: {e}")
except Exception as e:
    print(f"Test failed: {e}")
