from tools.search import DuckDuckGoSearchTool


def test_search():
    tool = DuckDuckGoSearchTool(max_results=3)

    results = tool.search("latest research in transformers AI")

    assert len(results) > 0
    assert "title" in results[0]
    assert "href" in results[0]
