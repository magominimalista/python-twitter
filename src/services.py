from typing import Any, Dict, List
import tweepy
from fastapi import Depends, HTTPException
from pymongo.errors import PyMongoError

from src.constants import BRAZIL_WOE_ID
from src.connection import trends_collection
from src.dependencies import get_tweepy_api


def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    """Get trending topics.

    Args:
        woe_id (int): Identifier of location.
    Returns:
        List[Dict[str, Any]]: Trending list.
    """
    try:
        trends = api.get_place_trends(woe_id)
        return trends[0]["trends"]
    except tweepy.TweepyException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching trends: {str(e)}")


def get_trends_from_mongo() -> List[Dict[str, Any]]:
    try:
        trend = trends_collection.find({})
        return list(trend)
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Error fetching trends from MongoDB: {str(e)}")


def save_trends(api: tweepy.API = Depends(get_tweepy_api)) -> Dict[str, str]:
    try:
        trends = _get_trends(BRAZIL_WOE_ID, api)
        trends_collection.insert_many(trends)
        return {"status": "success"}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Error saving trends to MongoDB: {str(e)}")
