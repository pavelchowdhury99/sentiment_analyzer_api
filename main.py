from nltk.sentiment import SentimentIntensityAnalyzer
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()


class Text(BaseModel):
    text: str


def get_sentiment_and_polarity_score(text: str) -> dict:
    """Return a dict of polarity_score and final Sentiment"""
    sentiment_intensity_analyzer = SentimentIntensityAnalyzer()
    scores = sentiment_intensity_analyzer.polarity_scores(text)
    senti = "Positive" if scores.get("compound") >= 0.05 else "Negative" \
        if scores.get("compound") <= -0.05 else "Neutral"
    return {"text": text, "polarity_scores": scores, "sentiment": senti}


@app.post("/get-sentiment")
def predict_sentiment(text: Text):
    # text = request.json.get("text")
    return get_sentiment_and_polarity_score(text.text)["sentiment"]


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')


if __name__ == "__main__":
    # test run
    print(get_sentiment_and_polarity_score('Did not understand a bit of what he taught, but enjoyed the class'))
